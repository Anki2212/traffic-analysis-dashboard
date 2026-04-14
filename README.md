# Network Traffic Analysis and Resource Allocation

This project presents a data-driven approach to analyzing network traffic patterns and optimizing resource allocation using data analytics and machine learning techniques. It includes both exploratory analysis and an interactive dashboard developed using Streamlit.

---

## Business Requirement

To perform a comprehensive analysis of network traffic data in order to understand traffic patterns, optimize resource allocation, and improve overall network efficiency. The project aims to generate actionable insights using data analytics techniques and predictive modeling.

---

## Project Architecture

- Data Collection and Loading
- Data Preprocessing and Cleaning
- Feature Engineering (Slice, Weight, Allocation)
- Exploratory Data Analysis (EDA)
- Machine Learning Model (Decision Tree Regressor)
- Dashboard Development (Streamlit)
- Insights and Conclusion

---

## Dataset Information

The dataset used in this project contains traffic-related information. The original column "passengers" is transformed into "Traffic_Demand" for analysis. Additional features such as Slice type, Weight, and Allocated Bandwidth are generated during preprocessing.

---

## Key Performance Indicators (KPIs)

* **Total Traffic Demand**: Total traffic generated across all slices
* **Average Traffic Demand**: Mean traffic across observations
* **Maximum Traffic Demand**: Peak traffic value observed
* **Total Allocated Bandwidth**: Total bandwidth distributed across slices
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
## Limitations

- The dataset is simplified and does not represent real-world telecom complexity
- The model uses limited features for prediction
- Allocation strategy is based on assumptions and simulated weights

---

## Future Improvements

- Use real-world telecom datasets
- Implement advanced machine learning models
- Add real-time data processing
- Integrate Power BI for business-level visualization

---

## Conclusion

This project demonstrates the application of data analytics and machine learning techniques in analyzing network traffic and optimizing resource allocation. It highlights the importance of data-driven approaches in improving system performance and decision-making.
