# 🛰️ Overparameterization in Deep Learning: Satellite Image Classification

This project investigates how overparameterization impacts **generalization**, **optimization**, and **model redundancy** in deep neural networks using satellite image classification as a case study.


> **Dataset**: EuroSAT (RGB satellite images)  
> **Models**: SmallNet, MediumNet, LargeNet  
> **Optimizers**: SGD, Adam, RMSprop  
> **Extras**: Pruning, Generalization Gap, Double Descent Analysis

---

## 📌 Project Objectives

- Understand how **model capacity** influences convergence and generalization.
- Compare **optimizers** in the context of overparameterization.
- Analyze **parameter pruning** effects on accuracy and model size.
- Support findings through metrics: training loss, test accuracy, generalization gap.

---

## 🧪 Key Experiments

1. **Model Scaling**:  
   - SmallNet (~307K params)  
   - MediumNet (~809K params)  
   - LargeNet (~5.1M params)

2. **Optimizer Comparison**:  
   - Adam showed best convergence and test accuracy  
   - SGD generalized better on smaller models  
   - RMSprop was unstable on larger models

3. **Generalization Gap**:  
   - LargeNet had low training loss and high test accuracy  
   - Gap widened with RMSprop, minimal with Adam

4. **Pruning Analysis**:  
   - MediumNet & LargeNet retain accuracy after pruning  
   - Confirms redundancy in overparameterized nets

---

## 📊 Results Tabulation

| Model      | Optimizer | Train Acc | Test Acc | Gap  |
|------------|-----------|-----------|----------|------|
| SmallNet   | Adam      | 0.75      | 0.65     | 0.10 |
| MediumNet  | Adam      | 0.85      | 0.82     | 0.03 |
| LargeNet   | Adam      | 0.88      | 0.81     | 0.07 |
| LargeNet   | RMSprop   | 0.59      | 0.54     | 0.05 |
| MediumNet  | SGD       | 0.90      | 0.76     | 0.14 |

---

## 📈 Pruning Results

- **Pruning Method**: L1-norm filter pruning  
- **Effect**:  
  - Accuracy drop < 1% for MediumNet  
  - ~3% drop for LargeNet  
  - Confirms overparameterized networks are **robust to compression**

---

## 🚀 Technologies Used

- Python
- PyTorch
- EuroSAT dataset
- TorchPruning / custom pruning logic
- Matplotlib, Seaborn for visualization

---

## 📄 Summary

This project provides empirical support for the theory that:
- **Overparameterization accelerates convergence**
- **Larger networks generalize well despite capacity**
- **Optimizers interact differently with model size**
- **Redundant parameters can be removed without hurting accuracy**


