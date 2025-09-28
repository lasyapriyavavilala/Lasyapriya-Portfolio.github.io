# app.py
import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
from mtcnn import MTCNN
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
    model="dima806/deepfake_vs_real_image_detection",
    device=-1  # CPU, change to 0 if GPU is available
)

def detect_deepfake(image: Image.Image):
    results = classifier(image)
    top_result = max(results, key=lambda x: x['score'])
    label = "fake" if top_result['label'] == "fake" else "real"
    score = top_result['score']
    return {
        "label": label,
        "confidence": score,
        "risk_level": "high" if label == "fake" and score > 0.8 else "low"
    }

# ------------------------------
# CrewAI Setup
# ------------------------------
# Replace with your Hugging Face API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "YOUR_HF_API_KEY"

llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3-8b", temperature=0.2)

detector_agent = Agent(role="Deepfake Analyst",
                       goal="Analyze images for deepfakes",
                       backstory="Forensic AI expert",
                       llm=llm)

notifier_agent = Agent(role="Safety Alert Coordinator",
                       goal="Log suspicious deepfakes",
                       backstory="Vigilant sentinel",
                       llm=llm)

summarizer_agent = Agent(role="Risk Assessor",
                         goal="Summarize detection results",
                         backstory="Strategic advisor",
                         llm=llm)

def create_crew(image_name, detection_result):
    detect_task = Task(
        description=f"Analyze {image_name}. Result: {detection_result}.",
        agent=detector_agent
    )
    notify_task = Task(
        description=f"If fake, log alert: {detection_result}",
        agent=notifier_agent
    )
    summarize_task = Task(
        description=f"Summarize result: {detection_result}",
        agent=summarizer_agent,
        context=[detect_task, notify_task]
    )
    crew = Crew(
        agents=[detector_agent, notifier_agent, summarizer_agent],
        tasks=[detect_task, notify_task, summarize_task]
    )
    return crew.kickoff()

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🔍 Deepfake Sentinel")
st.write("Upload an image → Highlight faces → Detect deepfake → Crew AI summary")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    # Step 1: Highlight faces
    highlighted, faces = detect_and_highlight_faces(image)
    st.image(highlighted, caption="Detected Faces", use_column_width=True)

    # Step 2: Deepfake detection
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

    # Step 3: Crew AI
    crew_summary = create_crew(uploaded_file.name, detection)
    st.subheader("Crew AI Summary")
    st.write(crew_summary)
