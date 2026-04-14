import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

# -------------------- LOAD DATA --------------------
df = pd.read_csv("traffic_data.csv")

# Fix column name
df = df.rename(columns={"passengers": "Traffic_Demand"})

# Create Slice column
slices = ["eMBB", "URLLC", "mMTC"]
df["Slice"] = np.random.choice(slices, size=len(df))

# Create Weight column
df["Weight"] = df["Slice"].map({
    "eMBB": 1,
    "URLLC": 2,
    "mMTC": 1
})

# Create Allocated Bandwidth
total_bandwidth = 100
df["Allocated_Bandwidth"] = (
    df["Traffic_Demand"] * df["Weight"]
) / (df["Traffic_Demand"] * df["Weight"]).sum() * total_bandwidth

# -------------------- TITLE --------------------
st.title(" Network Traffic Analysis Dashboard")
st.markdown("### Overview of Traffic and Resource Allocation")

# -------------------- KPI CARDS --------------------
col1, col2, col3 = st.columns(3)

col1.metric(" Avg Traffic", f"{round(df['Traffic_Demand'].mean(),2)} Mbps")
col2.metric(" Max Traffic", f"{df['Traffic_Demand'].max()} Mbps")
col3.metric(" Total Allocation", f"{round(df['Allocated_Bandwidth'].sum(),2)} Mbps")

# -------------------- SIDEBAR FILTERS --------------------
st.sidebar.title("Filters")
st.sidebar.markdown("Filter data dynamically")
st.sidebar.markdown("---")

# Slice filter
slice_option = st.sidebar.selectbox(
    "Select Slice",
    df["Slice"].unique()
)

# Traffic range filter
min_val = int(df["Traffic_Demand"].min())
max_val = int(df["Traffic_Demand"].max())

traffic_range = st.sidebar.slider(
    "Select Traffic Range",
    min_val,
    max_val,
    (min_val, max_val)
)

# Apply filters
filtered_df = df[
    (df["Slice"] == slice_option) &
    (df["Traffic_Demand"] >= traffic_range[0]) &
    (df["Traffic_Demand"] <= traffic_range[1])
]

# -------------------- DATASET VIEW --------------------
with st.expander(" View Dataset"):
    st.write(df.head(50))

# -------------------- TABS --------------------
tab1, tab2, tab3 = st.tabs([" Analysis", " Trends", " Prediction"])

# -------------------- TAB 1: ANALYSIS --------------------
with tab1:
    st.subheader("Slice-wise Traffic Analysis")

    # Use full dataset for comparison
    slice_avg = df.groupby("Slice")["Traffic_Demand"].mean()
    st.bar_chart(slice_avg)

    st.subheader("Filtered Allocation")
    st.bar_chart(filtered_df["Allocated_Bandwidth"])

# -------------------- TAB 2: TRENDS --------------------
with tab2:
    st.subheader("Traffic Trend Over Time")
    st.line_chart(df["Traffic_Demand"])

# -------------------- TAB 3: ML PREDICTION --------------------
model = DecisionTreeRegressor()
model.fit(df[["Traffic_Demand"]], df["Allocated_Bandwidth"])

with tab3:
    st.subheader("Predict Resource Allocation")

    input_val = st.number_input("Enter Traffic Demand", min_value=1, max_value=500)

    prediction = model.predict([[input_val]])

    st.success(f"Predicted Allocation: {round(prediction[0],2)} Mbps")
