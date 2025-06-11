
🛠️ Project Summary: Predictive Maintenance using Signal Processing & ML
===============================

This project explores Predictive Maintenance (PdM) on NASA’s IMS bearing dataset using a combination of signal processing, classical machine learning models, and deep learning (CNN, LSTM, CNN-LSTM).

PdM anticipates machinery failures before they occur, minimizing downtime and reducing maintenance costs. The dataset includes time-series vibration signals captured by sensors, which are transformed using FFT, bandpass filtering, and wavelet decomposition.

📊 Key Features:
- Z-score & boxplot analysis for anomaly detection
- FFT + Wavelet for frequency and time-domain features
- Statistical features like Energy, Entropy, Skewness, Kurtosis
- Labeling bearings as Healthy or Faulty using IQR-based thresholds

🧠 Classical ML Models Evaluated:
- Logistic Regression, Random Forest, Decision Tree, Naive Bayes
- KNN, SVM, XGBoost

📈 Deep Learning Models:
- CNN: 100% training accuracy, 99.28% validation accuracy
- LSTM: 99.94% training accuracy
- CNN-LSTM Hybrid: Best RUL prediction performance (R² ≈ 0.89)

🧪 RUL Prediction:
- Performed using LSTM, Random Forest, and CNN-LSTM
- RF yielded most accurate Remaining Useful Life (RUL) estimates


This project showcases the end-to-end process of signal-based predictive maintenance — from raw sensor data to actionable predictions.
