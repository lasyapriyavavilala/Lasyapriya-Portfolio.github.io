# deepfake_sentinel.py
import streamlit as st
from mtcnn import MTCNN
from PIL import Image, ImageDraw
import numpy as np
from transformers import pipeline
from crewai import Agent, Task, Crew
from langchain_huggingface import HuggingFaceEndpoint
import os

# ------------------------------
# Face detection + highlight
# ------------------------------
def detect_and_highlight_faces(image: Image.Image):
    img = np.array(image.convert("RGB"))
    detector = MTCNN()
    faces = detector.detect_faces(img)

    pil_img = image.copy()
    draw = ImageDraw.Draw(pil_img)
    for face in faces:
        x, y, w, h = face['box']
        confidence = face['confidence']
        if confidence > 0.9:
            draw.rectangle([x, y, x+w, y+h], outline="red", width=3)
            draw.text((x, y-10), f"{confidence:.2f}", fill="red")
    return pil_img, faces

# ------------------------------
# Deepfake detection model
# ------------------------------
classifier = pipeline(
    "image-classification",
    model="dima806/deepfake_vs_real_image_detection"
)

def detect_deepfake(image: Image.Image):
    results = classifier(image)
    top_result = max(results, key=lambda x: x['score'])
    label = "fake" if top_result['label'] == "fake" else "real"
    score = top_result['score']
    return {"label": label, "confidence": score, "risk_level": "high" if label == "fake" and score > 0.8 else "low"}

# ------------------------------
# Crew AI Setup (Mistral instead of Qwen)
# ------------------------------
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HF_TOKEN", "")

llm = None
try:
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.1",
        temperature=0.2,
        max_new_tokens=60
    )
except Exception as e:
    st.error(f"Mistral LLM failed: {str(e)}. Using fallback reasoning.")

# Define agents
detector_agent = Agent(
    role="Deepfake Analyst",
    goal="Analyze images for authenticity",
    backstory="Forensic AI expert detecting manipulations.",
    llm=llm
)
notifier_agent = Agent(
    role="Safety Alert Coordinator",
    goal="Log alerts for suspicious deepfakes",
    backstory="Ensures user safety.",
    llm=llm
)
summarizer_agent = Agent(
    role="Risk Assessor",
    goal="Summarize detection results",
    backstory="Synthesizes analysis.",
    llm=llm
)
reasoning_agent = Agent(
    role="Explainability Specialist",
    goal="Explain why image is real or fake",
    backstory="Expert in identifying artifacts like lighting, asymmetry, or texture mismatches.",
    llm=llm
)

def create_crew(image_name, detection_result, faces):
    fallback_reasoning = {
        "fake": f"Flagged as fake likely due to artifacts or lighting inconsistencies. Confidence {detection_result['confidence']:.2f}.",
        "real": f"Flagged as real due to natural facial features and consistent lighting. Confidence {detection_result['confidence']:.2f}."
    }

    face_info = ", ".join([f"box {face['box']} (conf: {face['confidence']:.2f})" for face in faces]) if faces else "No faces detected."

    detect_task = Task(description=f"Analyze {image_name}: {detection_result['label']} (confidence {detection_result['confidence']:.2f}).",
                       agent=detector_agent)
    notify_task = Task(description=f"Log alert if fake: {detection_result['label']} (risk {detection_result['risk_level']}).",
                       agent=notifier_agent)
    summarize_task = Task(description=f"Summarize detection results.",
                          agent=summarizer_agent,
                          context=[detect_task, notify_task])
    reasoning_task = Task(description=f"Explain in 1-2 short sentences why {image_name} was classified as {detection_result['label']} "
                                      f"(confidence {detection_result['confidence']:.2f}). Face info: {face_info}.",
                          agent=reasoning_agent,
                          context=[summarize_task])

    crew = Crew(
        agents=[detector_agent, notifier_agent, summarizer_agent, reasoning_agent],
        tasks=[detect_task, notify_task, summarize_task, reasoning_task],
        verbose=False
    )

    try:
        return crew.kickoff()
    except Exception:
        return {
            "detector": f"Analyzed {image_name}: {detection_result['label']}.",
            "notifier": f"{'Alert logged' if detection_result['label']=='fake' else 'No alert needed'}.",
            "summarizer": f"Image is {detection_result['label']} (confidence {detection_result['confidence']:.2f}).",
            "reasoning": fallback_reasoning[detection_result['label']]
        }

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🔍 Deepfake Sentinel (Mistral Edition)")
st.write("Upload → Highlight faces → Detect deepfake → CrewAI summary + Mistral reasoning")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)

    highlighted, faces = detect_and_highlight_faces(image)
    st.image(highlighted, caption="Detected Faces", use_column_width=True)

    if faces:
        x, y, w, h = faces[0]['box']
        face_img = image.crop((x, y, x+w, y+h))
        detection = detect_deepfake(face_img)
    else:
        detection = detect_deepfake(image)

    st.subheader("Detection Results")
    st.write(f"**Label:** {detection['label']}")
    st.write(f"**Confidence:** {detection['confidence']:.2f}")
    st.write(f"**Risk Level:** {detection['risk_level']}")

    crew_summary = create_crew(uploaded_file.name, detection, faces)

    st.subheader("Crew AI Results")
    st.info(crew_summary.get("detector", ""))
    st.warning(crew_summary.get("notifier", ""))
    st.success(crew_summary.get("summarizer", ""))
    st.info(crew_summary.get("reasoning", ""))
