# Deepfake Sentinel: AI-Powered Safety Shield

[![Streamlit](https://img.shields.io/badge/Streamlit-FF6B35?style=for-the-badge&logo=streamlit)](https://streamlit.io/) [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/) [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF4B4B?style=for-the-badge&logo=huggingface)](https://huggingface.co/)

# Deepfake Sentinel: AI-Powered Safety Shield
  
# Built for SunHacks 2025 – Targeting Best Hack for Safety and Best AI Agent.

# 🎯 Inspiration & Impact
Deepfakes fuel misinformation. Deepfake Sentinel detects fake images, highlights faces, and explains classifications with AI agents, promoting safer digital spaces.

# 🚀 What It Does

Upload Image: Streamlit UI.
Face Detection: MTCNN highlights faces (>90% confidence).
Deepfake Classification: Hugging Face model labels “real” or “fake”.
AI Analysis: CrewAI agents or Mistral-7B reasoning (e.g., “Fake due to texture artifacts”).
Output: Visuals + insights.

# 🛠 Tech Stack

Languages: Python
Frameworks: Streamlit, Transformers (Hugging Face), CrewAI, LangChain-HuggingFace, PyTorch, OpenCV, PIL
Platforms: Hugging Face, GitHub, Ngrok
Cloud Services: Hugging Face Inference API (Mistral-7B), Ngrok Cloud
APIs: Hugging Face Inference API, Ngrok API
Other: MTCNN (face detection), NumPy, Torchvision

# 📋 Setup & Run Locally

Clone:git clone https://github.com/lasyapriyavavilala/Lasyapriya-Portfolio.github.io.git
cd Lasyapriya-Portfolio.github.io/Sunhack-Deepfake-Sentinel


Install:pip install -r requirements.txt


Set environment:export HF_TOKEN="hf_your_token"
export NGROK_TOKEN="your_ngrok_token"


Run:
CrewAI + Face Detection: streamlit run deepfake_sentinel.py
Classifier + Mistral: streamlit run app.py



# 🌐 Public Demo

Install ngrok: pip install pyngrok
Start Streamlit: streamlit run app.py --server.port 8501
Run ngrok: ngrok http 8501
Use public URL ([Streamlit Link](https://nonhallucinatory-renae-unlauded.ngrok-free.dev/)).

# 📸 Screenshots
Please find them in the folder

# 🏆 Accomplishments & Challenges

# Accomplishments:
Two versions with >90% accuracy.
Clear reasoning via CrewAI/Mistral.
Reliable demos with fallbacks.


# Challenges:
Model Selection: Tested multiple models; chose dima806. Switched to Mistral-7B for API stability.
Deployment: Resolved Streamlit/ngrok issues with environment variables and fallbacks.



# 🔮 Future Work

Video detection.
X integration.
Mobile optimization.

# 📂 Files

deepfake_sentinel.py: CrewAI + MTCNN
app.py: Classifier + Mistral
requirements.txt
screenshots/

# 📹 Demo Video
YouTube Demo (unlisted; we consent to SunHacks playlist if we win).
Built with 💪 at SunHacks 2025 by Lasyapriya Vavilala.
Devpost | GitHub
