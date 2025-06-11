

# 🔧 Predictive Maintenance using Signal Processing & Machine Learning

This repository presents a complete pipeline for **predictive maintenance (PdM)** using **signal processing** and **machine learning** techniques. The project is based on the **NASA IMS Bearing Dataset** and demonstrates both classical ML and deep learning models to predict the health and Remaining Useful Life (RUL) of bearings.

---


## 📊 Project Overview

Predictive Maintenance (PdM) aims to anticipate equipment failures before they happen. This project uses signal snapshots of bearing vibrations to:
- Detect anomalies
- Classify healthy vs faulty bearings
- Predict Remaining Useful Life (RUL)

**Signal processing** techniques (FFT, filtering, wavelet transform) are used to extract meaningful features from raw time-series data. These are used to train ML/DL models.

---

## 📂 Dataset

- **Source:** NASA IMS Bearing Dataset
- **Used:** Set 2 with 984 ASCII files
- **Collected with:** NI DAQCard 6062E
- **Frequency:** 20 kHz sampling rate
- **Dataset Link**: https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/

---

## 🧠 Feature Engineering

- 🧮 **Time-domain Features:** RMS, Skewness, Kurtosis, Entropy, Energy
- 🌐 **Frequency-domain:** FFT, Bandpass Filter (100–9500 Hz), High-pass Filter (cutoff: 50 Hz)
- 🌊 **Wavelet Features:** Using DWT via `PyWavelets`

---

## ⚙️ Models Implemented

### 🔁 Classical ML Models
- Logistic Regression
- Random Forest
- Decision Tree
- Naive Bayes
- K-Nearest Neighbors (KNN)
- SVM
- XGBoost

### 🧠 Deep Learning
- Convolutional Neural Network (CNN)
- Long Short-Term Memory (LSTM)
- Hybrid CNN-LSTM

---

## ⏳ RUL Prediction

We estimated Remaining Useful Life (RUL) using:
- LSTM
- Random Forest
- CNN-LSTM

Each model was evaluated on test loss and MAE. CNN-LSTM achieved the highest R² score (~0.88).

