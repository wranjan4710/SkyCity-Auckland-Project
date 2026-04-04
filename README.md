# 📊 SkyCity Channel Intelligence Dashboard

A Streamlit-based analytics dashboard built for SkyCity Auckland Restaurants & Bars to analyze restaurant performance, delivery channels, market share, and dependency risks.

---

## 🚀 Project Overview

The SkyCity Channel Intelligence Dashboard helps restaurant businesses understand customer ordering patterns across multiple channels such as In-Store, Uber Eats, DoorDash, and Self Delivery.

This project provides interactive visualizations, KPI tracking, and risk analysis to support better business decisions.

---

## ✨ Features

* Interactive Streamlit Dashboard
* Global Filters for Subregion, Cuisine Type, and Business Segment
* Channel Market Share Analysis
* Delivery vs In-Store Comparison
* Net Profit Analysis by Channel
* Subregion-wise Channel Dominance
* Cuisine and Segment Insights
* Aggregator Dependency Risk Analysis
* High-Risk Restaurant Identification
* Executive KPI Summary
* Interactive Charts and Graphs
* Filtered Dataset Preview

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Matplotlib
* Seaborn

---

## 📂 Project Structure

```text
SkyCity_Channel_Intelligence/
│
├── app.py
├── requirements.txt
├── data/
│   └── SkyCity Auckland Restaurants & Bars.csv
│
├── utils/
│   ├── data_loader.py
│   ├── kpi_calculator.py
│   └── validation.py
│
├── pages/
│   ├── 1_Channel_Overview.py
│   ├── 2_Subregion_Analysis.py
│   ├── 3_Cuisine_Segment_Analysis.py
│   └── 4_Dependency_Risk_Analysis.py
```

---

## 📊 Dashboard Pages

### 1. Main Dashboard

* Executive KPI Summary
* Channel Share Metrics
* Orders Breakdown
* Dependency & Diversification Insights
* Dataset Preview

### 2. Channel Overview

* Channel Market Share
* Delivery vs In-Store Orders
* Net Profit by Channel

### 3. Subregion Analysis

* Regional Channel Dominance
* Heatmap Analysis by Subregion

### 4. Cuisine & Segment Analysis

* Delivery Usage by Cuisine
* Business Segment Channel Mix

### 5. Dependency Risk Analysis

* Diversification Score Distribution
* Risk Category Classification
* High-Risk Restaurant Table

---

## 📈 Key Insights

* Identify the most popular ordering channel
* Compare online delivery platforms with in-store performance
* Understand which subregions depend more on delivery platforms
* Discover cuisine types with the highest delivery demand
* Detect restaurants with high aggregator dependency risk
* Measure diversification across channels

---

## ⚙️ Installation Guide

1. Clone the repository

```bash
git clone https://github.com/your-username/skycity-channel-intelligence.git
```

2. Move into the project folder

```bash
cd skycity-channel-intelligence
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📋 Requirements

```text
streamlit
pandas
numpy
plotly
matplotlib
seaborn
```

---

## 🔮 Future Improvements

* Add Machine Learning Forecasting
* Add PDF Report Export
* Add Revenue Prediction
* Add Restaurant Ranking System
* Add Dark Mode
* Deploy on Streamlit Cloud
* Add Real-Time API Integration

---

## 👨‍💻 Author

Dablu Ranjan
AI & ML Student
