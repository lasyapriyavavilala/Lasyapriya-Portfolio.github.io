# Deepfake Sentinel: AI-Powered Safety Shield

[![Streamlit](https://img.shields.io/badge/Streamlit-FF6B35?style=for-the-badge&logo=streamlit)](https://streamlit.io/) [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/) [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF4B4B?style=for-the-badge&logo=huggingface)](https://huggingface.co/)

Built for **SunHacks 2025** – Targeting **Best Hack for Safety** (deepfake detection for online protection) and **Best AI Agent** (CrewAI multi-agent analysis).

## 🎯 Inspiration & Impact
Deepfakes spread misinformation and harm—our app detects them in real-time to promote safer digital spaces. It highlights faces, classifies authenticity, and uses AI agents for smart summaries/alerts. Scalable for social media verification.

## 🚀 What It Does
1. **Upload Image**: Via Streamlit UI.
2. **Face Detection**: MTCNN highlights faces (>90% confidence).
3. **Deepfake Check**: Hugging Face model labels "real/fake" with confidence & risk level.
4. **AI Agent Analysis**: CrewAI team (Analyst, Coordinator, Assessor) powered by Llama-3 summarizes results and logs alerts.
5. **Output**: Visuals + insights in a clean dashboard.

## 🛠 Tech Stack
- **UI**: Streamlit
- **Face Detection**: MTCNN + OpenCV/PIL
- **Classification**: Hugging Face Transformers (dima806/deepfake_vs_real_image_detection) + PyTorch
- **AI Agents**: CrewAI + LangChain-HuggingFace (Llama-3 endpoint)
- **Deployment**: Ngrok for public demos

