# 🧠 GenAI Chatbot – Intent Classification using BERT

This project builds a **Generative AI chatbot** that classifies **user intents** from natural language queries.  
It uses the **DSTC8 Schema-Guided Dialogue** dataset and a **fine-tuned BERT model** to predict user intent in real time.

---

## 🚀 Features
- Extracts user utterances and active intents from DSTC8 JSON files  
- Creates a labeled dataset for intent classification  
- Fine-tunes **BERT (bert-base-uncased)** using Hugging Face Transformers  
- Evaluates model performance using **accuracy** and **F1-score**  
- Deploys the model on **Hugging Face Hub** and builds a **Gradio chatbot interface**  
- Predicts user intent with confidence scores

---

## 🧩 Tech Stack
- **Python**, **PyTorch**, **Transformers**, **Hugging Face Datasets**
- **Scikit-learn**, **Pandas**, **Gradio**, **Google Colab**
- **Hugging Face Hub** for model hosting and inference

---

## 📊 Dataset
- [DSTC8 Schema-Guided Dialogue Dataset](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue)
- Extracted utterance–intent pairs for supervised fine-tuning

---

## 🏋️‍♀️ Training
The model was fine-tuned using the Hugging Face `Trainer` API with:
- Learning rate: `2e-5`
- Epochs: `3`
- Batch size: `2`
- Evaluation metric: Weighted F1-score

---

## 💬 Deployment
The fine-tuned model was uploaded to [Hugging Face Hub](https://huggingface.co/lasyapriyav/intent-classifier-bert)  
and integrated with **Gradio** for interactive inference.

Run locally:
```bash
pip install gradio transformers
python app/app.py

Input: "I'd like to reset my password"
→ Predicted Intent: Reset_Password  (Confidence: 0.94)
