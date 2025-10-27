# -*- coding: utf-8 -*-
"""MyChatBot.ipynb


I am using the Dataset DSTC8 SGD to develop the Chatbot
"""

!git clone https://github.com/google-research-datasets/dstc8-schema-guided-dialogue.git

"""I am extracting the utterance-intent pairs from the dataset"""

import json
import os

def extract_user_intents(path):
    data = []
    for file in os.listdir(path):
        if file.startswith("dialogues_") and file.endswith(".json"):
            with open(os.path.join(path, file), "r") as f:
                dialogs = json.load(f)
                for dialog in dialogs:
                    if "turns" not in dialog:
                        continue  # Skip malformed entries
                    for turn in dialog["turns"]:
                        if turn.get("speaker") == "USER":
                            utterance = turn.get("utterance", "")
                            for frame in turn.get("frames", []):
                                intent = frame.get("state", {}).get("active_intent", "NONE")
                                if intent != "NONE":
                                    data.append((utterance, intent))
    return data

# ✅ Run the fixed version
train_data = extract_user_intents("/content/dstc8-schema-guided-dialogue/train")
print(f"Extracted {len(train_data)} utterance-intent pairs")
train_data[:5]

"""✅ Step 1: Convert to DataFrame & Explore"""

import pandas as pd

# Convert to DataFrame
df = pd.DataFrame(train_data, columns=["text", "label"])

# Remove duplicates and "NONE" labels (if any remain)
df = df.drop_duplicates()
df = df[df["label"] != "NONE"]
df = df.reset_index(drop=True)

# Inspect
print(f"Total samples: {len(df)}")
df["label"].value_counts().head(10)

df.to_csv("dstc8_intent_dataset.csv", index=False)

from google.colab import files
files.download("dstc8_intent_dataset.csv")

"""Now I'm going to train a BERT-based intent classifier using DSTC8 data.

🔧 Step 0: Install Hugging Face Libraries
"""

!pip install transformers datasets scikit-learn

"""📊 Step 1: Prepare Dataset (Tokenization + Encoding Labels)

"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.preprocessing import LabelEncoder
from datasets import Dataset

# Encode labels into integers
label_encoder = LabelEncoder()
df["label_id"] = label_encoder.fit_transform(df["label"])

# Save label encoder mappings
id2label = {i: label for i, label in enumerate(label_encoder.classes_)}
label2id = {label: i for i, label in enumerate(label_encoder.classes_)}

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Convert pandas DataFrame to Hugging Face Dataset
dataset = Dataset.from_pandas(df[["text", "label_id"]])

# Tokenize the text
def tokenize(batch):
    return tokenizer(batch["text"], padding="max_length", truncation=True)

dataset = dataset.map(tokenize, batched=True)

# Load DistilBERT model for sequence classification
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=len(label_encoder.classes_),
    id2label=id2label,
    label2id=label2id
)

🧪 Step 2: Train-Test Split

dataset = dataset.train_test_split(test_size=0.1)
train_dataset = dataset["train"]
test_dataset = dataset["test"]

train_dataset = train_dataset.rename_columns({"label_id": "labels"})
test_dataset = test_dataset.rename_columns({"label_id": "labels"})

from sklearn.preprocessing import LabelEncoder

# Combine all intents from train and test data
all_intents = [label for _, label in train_data]


# Fit LabelEncoder to convert intent strings to numeric IDs
label_encoder = LabelEncoder()
label_encoder.fit(all_intents)

# Create mappings
id2label = {i: label for i, label in enumerate(label_encoder.classes_)}
label2id = {label: i for i, label in enumerate(label_encoder.classes_)}

"""🧠 Step 3: Load BERT Model

⚙️ Step 4: Set Training Arguments
"""

!pip install transformers==4.28.1

"""📈 Step 5: Define Evaluation Metrics"""

import numpy as np
from sklearn.metrics import accuracy_score, f1_score

def compute_metrics(pred):
    labels = pred.label_ids
    preds = np.argmax(pred.predictions, axis=1)
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average='weighted')
    return {"accuracy": acc, "f1": f1}

"""🏋️ Step 6: Train the Model"""

# 4. Define training arguments
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    fp16=True,  # mixed precision for speed
    gradient_accumulation_steps=2
)

# 5. Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

"""Training the model"""

trainer.train()

import torch

def predict_intent(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(model.device)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    return id2label[prediction]

# Example
predict_intent("I'd like to reset my password")

# Save model and tokenizer
model.save_pretrained("./intent_model")
tokenizer.save_pretrained("./intent_model")

# Later you can reload
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("./intent_model")
tokenizer = AutoTokenizer.from_pretrained("./intent_model")

from huggingface_hub import notebook_login

notebook_login()

model.push_to_hub("lasyapriyav/intent-classifier-bert")
tokenizer.push_to_hub("lasyapriyav/intent-classifier-bert")

from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "lasyapriyav/intent-classifier-bert"

# Download and save locally
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save to local directory
save_directory = "./intent_classifier_model"
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)

pip install gradio

import gradio as gr
from transformers import pipeline

# Load model from Hugging Face Hub (your model repo)
model_name = "lasyapriyav/intent-classifier-bert"
classifier = pipeline("text-classification", model=model_name)

# Inference function
def predict_intent(text):
    result = classifier(text)[0]
    return f"Intent: {result['label']} (Confidence: {round(result['score'], 2)})"

# Launch Gradio interface
gr.Interface(
    fn=predict_intent,
    inputs=gr.Textbox(lines=2, placeholder="Enter a support query..."),
    outputs="text",
    title="Intent Classifier Chatbot",
    description="This chatbot predicts the intent of user queries using a fine-tuned DistilBERT model."
).launch()
