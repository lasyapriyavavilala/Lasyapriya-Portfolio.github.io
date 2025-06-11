# 📊 Time Series Forecasting of Hotel Bookings to Optimize Resource Allocation and Pricing Strategies
This project focuses on **forecasting hotel booking demand** using time series analysis. By analyzing past hotel booking data, we aim to help hotel managers make informed decisions regarding **resource allocation**, **pricing strategies**, and **seasonal planning**.



---

## 🧾 Project Overview

Hotel booking patterns are influenced by a range of factors like holidays, weather, and customer behavior. Using a dataset with over 30 features about guest details, booking timelines, cancellations, and pricing, this project builds forecasting models to predict **monthly demand**.

We address:
- Missing values and inconsistent formats
- Feature engineering for time series
- Seasonal decomposition and correlation
- Forecasting using ARIMA, SARIMA, and Holt-Winters

---

## 📁 Dataset Description

The dataset contains reservations from **resort and city hotels**, including:
- Booking date, length of stay
- Number of guests (adults, children, babies)
- Cancellation status
- Financial metrics (daily rate, deposits)
- Special requests, parking needs, and more

Source: Uploaded in this folder

---

## 📉 Exploratory Data Analysis (EDA)

- Lead time distribution analysis
- Cancellation correlation with advance bookings
- Monthly demand trends (2015–2017)
- Seasonal box plots highlighting demand variability



---

## 🏗 Feature Engineering

- Target variable: `monthly demand`
- Lag features: demand at t−1, t−2, t−3 months
- Seasonal flag for holidays
- `year_month` converted to datetime index

---

## 🔍 Forecasting Models

### 1. ARIMA
- Captures trend and noise
- Conservative, less responsive to seasonal effects

### 2. SARIMA
- Best performance on test data
- Captures both seasonality and trends

### 3. Holt-Winters
- Captures trends effectively
- Performs well but may overreact to recent values



| Model        | Seasonality Handling | Trend Capture | Confidence Interval | Notes          |
|--------------|----------------------|---------------|----------------------|----------------|
| **SARIMA**   | ✅ Excellent         | ✅ Good       | ✅ Narrow            | Most balanced  |
| **ARIMA**    | ❌ Limited           | ✅ Moderate   | ❌ Wide              | Conservative   |
| **Holt-Winters** | ✅ Good          | ✅ Excellent   | ❌ Very Wide         | High variance  |

---

## 📊 Hypothesis Testing

- **Null Hypothesis (H₀)**: No significant seasonality
- **Alternative Hypothesis (H₁)**: There is significant seasonality

Statistical tests (T-test, ANOVA, Ljung-Box) were performed. Results support **rejecting H₀** — indicating **strong seasonal trends** in hotel bookings.

---

## 🏁 Conclusion

- Seasonality exists in hotel demand.
- SARIMA model is the most effective for real-world forecasting.
- Forecasting can significantly enhance hotel strategy planning.

---

## 🧠 Technologies Used

- Python (pandas, matplotlib, seaborn)
- Statsmodels (ARIMA, SARIMA)
- Scikit-learn
- Jupyter Notebooks
- Tableau for EDA



