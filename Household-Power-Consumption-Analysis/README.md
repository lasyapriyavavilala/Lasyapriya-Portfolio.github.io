# Household Electricity Consumption Analysis & Classification

## Overview
This project analyzes household electricity consumption data to identify usage patterns and classify power consumption levels (Low / Medium / High). The goal is to extract meaningful insights from time-series energy data and build machine learning models that can support demand forecasting and energy optimization use cases.

## Dataset
- Household electricity consumption dataset
- Time-series data containing active power usage and related electrical measurements
- Data preprocessing includes handling missing values, normalization, and feature extraction

## Objectives
- Perform exploratory data analysis (EDA) on electricity usage patterns
- Engineer relevant statistical and time-based features
- Classify electricity consumption levels using machine learning models
- Evaluate and compare model performance

## Methodology
### 1. Data Preprocessing
- Data cleaning and missing value handling
- Feature scaling and normalization
- Time-based aggregation

### 2. Exploratory Data Analysis
- Consumption trends over time
- Distribution of power usage
- Correlation analysis between electrical variables

### 3. Feature Engineering
- Statistical features (mean, variance, peak usage)
- Temporal features (hourly/daily patterns)
- Consumption category labeling (Low / Medium / High)

### 4. Modeling
Models implemented:
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree Classifier

### 5. Evaluation
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix

## Results
- Tree-based models captured non-linear consumption patterns effectively
- SVM performed well after feature scaling
- Clear separation observed between low and high consumption classes

## Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Google Colab

## Applications
- Energy demand forecasting
- Smart grid analytics
- Household energy optimization
- Sustainability and energy efficiency studies

## Future Work
- Time-series forecasting using LSTM or ARIMA
- Integration with real-time smart meter data
- Hyperparameter tuning and model ensembling

## Author
**Jahnavi Lasyapriya Vavilala**  
MS in Data Science, Analytics & Engineering  
