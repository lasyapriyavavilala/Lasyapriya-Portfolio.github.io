%%writefile app.py
import streamlit as st
from PIL import Image
import torch
from transformers import AutoModelForImageClassification, AutoImageProcessor
from huggingface_hub import InferenceClient
import io, os

# ------------------------------
# Load classifier model once
# ------------------------------
@st.cache_resource
def load_model():
    model_id = "dima806/deepfake_vs_real_image_detection"
    processor = AutoImageProcessor.from_pretrained(model_id)
    model = AutoModelForImageClassification.from_pretrained(model_id)
    return processor, model

processor, model = load_model()

# ------------------------------
# Load Hugging Face reasoning model (Mistral)
# ------------------------------
HF_TOKEN = os.getenv("HF_TOKEN", "")  # token should be set in environment
reasoning_client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2", token=HF_TOKEN)

st.title("🕵️ Deepfake Detection App with Reasoning")
st.write("Upload an image to check if it's **real or fake** and get reasoning behind it.")

# ------------------------------
# File upload
# ------------------------------
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Step 1: Classification
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        preds = torch.nn.functional.softmax(outputs.logits, dim=-1)
        score, label = torch.max(preds, dim=1)

    label_str = model.config.id2label[label.item()]
    st.subheader(f"Prediction: **{label_str}**")
    st.write(f"Confidence: {score.item():.2%}")

    # Step 2: Reasoning with Mistral (text-only)
    with st.spinner("Generating reasoning..."):
        try:
            response = reasoning_client.text_generation(
                prompt=(
                    f"The image classifier predicted this image as {label_str} "
                    f"with confidence {score.item():.2%}. "
                    f"Give 2 short reasons why this image might look {label_str}, "
                    f"considering possible visual cues like texture, lighting, or facial symmetry."
                ),
                max_new_tokens=120,
                temperature=0.4,
            )
            reasoning = response.strip()
        except Exception as e:
            reasoning = f"(Fallback) Predicted as {label_str} mainly due to typical {label_str}-like visual features."

    st.subheader("🔍 Reasoning")
    st.write(reasoning)
