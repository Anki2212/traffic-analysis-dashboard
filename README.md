# Network Traffic Analysis and Resource Allocation

This repository contains a data analysis and machine learning project focused on network traffic analysis and resource allocation. The project includes both a Python-based analysis and an interactive dashboard developed using Streamlit.

---

## Business Requirement

To perform a comprehensive analysis of network traffic data in order to understand traffic patterns, optimize resource allocation, and improve overall network efficiency. The project aims to generate actionable insights using data analytics techniques and predictive modeling.

---

## Key Performance Indicators (KPIs)

* **Total Traffic Demand**: The overall network traffic generated
* **Average Traffic Demand**: The average traffic across all observations
* **Maximum Traffic Demand**: The peak traffic value observed
* **Total Allocated Bandwidth**: The total bandwidth distributed across slices
* **Allocation Efficiency**: Measure of how effectively resources are allocated

---

## Analysis Requirements

### Traffic Distribution Analysis

**Objective**: Analyze the distribution of traffic demand across the dataset
**Chart Type**: Histogram

---

### Slice-wise Traffic Analysis

**Objective**: Compare traffic demand across different network slices (eMBB, URLLC, mMTC)
**Chart Type**: Bar Chart

---

### Traffic Trend Over Time

**Objective**: Analyze how traffic demand changes over time
**Chart Type**: Line Chart

---

### Resource Allocation Analysis

**Objective**: Evaluate how bandwidth is allocated based on traffic demand and priority weights
**Chart Type**: Bar Chart

---

### Prediction of Resource Allocation

**Objective**: Predict optimal bandwidth allocation based on input traffic demand using a machine learning model
**Model Used**: Decision Tree Regressor

---

## Project Steps

* Requirement Analysis
* Data Collection and Loading
* Data Cleaning and Preprocessing
* Feature Engineering (Slice, Weight, Allocation)
* Exploratory Data Analysis (EDA)
* Data Visualization
* Machine Learning Model Development
* Dashboard Development using Streamlit
* Insights Generation

---

## Dashboard Features

* Display of key metrics such as average traffic and total allocation
* Interactive filtering based on slice type and traffic range
* Visualization of traffic distribution and slice-wise comparison
* Trend analysis of traffic demand
* Real-time prediction of resource allocation

---

## Project Contents

* `traffic_analysis.ipynb`: Jupyter Notebook containing data analysis and machine learning
* `dashboard.py`: Streamlit dashboard for interactive visualization
* `traffic_data.csv`: Dataset used for analysis
* `requirements.txt`: List of required Python libraries

---

## Getting Started

1. Clone this repository
2. Install the required dependencies using:

   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit dashboard:

   ```
   streamlit run dashboard.py
   ```

---

## Requirements

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## Insights

* Traffic demand varies across different network slices
* eMBB shows higher traffic demand compared to other slices
* URLLC requires priority allocation due to low-latency requirements
* Traffic patterns are dynamic and fluctuate over time
* Weighted allocation improves resource efficiency
* Machine learning enables predictive resource allocation

---

## Conclusion

This project demonstrates the application of data analytics and machine learning techniques in analyzing network traffic and optimizing resource allocation. It highlights the importance of data-driven approaches in improving system performance and decision-making.
