import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="AutoData-Refiner", layout="wide")

st.title("🚗 AutoData-Refiner: On-Demand Dataset Customization Service")
st.subheader("Turn raw autonomous vehicle sensory logs into high-value training subsets.")

def load_or_generate_data():
    filename = 'raw_vehicle_logs.csv'
    if not os.path.exists(filename):
        n_rows = 1000000
        data = {
            'timestamp': pd.date_range(start='2026-01-01', periods=n_rows, freq='s'),
            'scene_id': np.random.randint(1000, 1050, size=n_rows),
            'weather': np.random.choice(['Sunny', 'Rainy', 'Foggy', 'Snowy'], size=n_rows, p=[0.6, 0.2, 0.1, 0.1]),
            'time_of_day': np.random.choice(['Day', 'Night'], size=n_rows, p=[0.7, 0.3]),
            'pedestrian_detected': np.random.choice([0, 1], size=n_rows, p=[0.8, 0.2]),
            'gps_latitude': np.random.uniform(25.0, 25.2, size=n_rows),
            'gps_longitude': np.random.uniform(121.5, 121.6, size=n_rows),
            'lidar_file_size_mb': np.random.uniform(15.0, 50.0, size=n_rows)
        }
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        return df
    return pd.read_csv(filename)

df = load_or_generate_data()

st.sidebar.header("Filter Criteria (Target Subsets)")
selected_weather = st.sidebar.multiselect("Weather Condition", options=df['weather'].unique(), default=['Rainy', 'Foggy'])
selected_time = st.sidebar.selectbox("Time of Day", options=df['time_of_day'].unique(), index=1) # Night
pedestrian_only = st.sidebar.checkbox("Only include scenes with pedestrians", value=True)

filtered_df = df[(df['weather'].isin(selected_weather)) & (df['time_of_day'] == selected_time)]
if pedestrian_only:
    filtered_df = filtered_df[filtered_df['pedestrian_detected'] == 1]

total_raw_size_gb = (df['lidar_file_size_mb'].sum()) / 1024
filtered_size_gb = (filtered_df['lidar_file_size_mb'].sum()) / 1024
time_saved_hours = len(filtered_df) * 0.005 

col1, col2, col3 = st.columns(3)
col1.metric("Original Dataset Size", f"{total_raw_size_gb:.2f} GB")
col2.metric("Refined Subset Size", f"{filtered_size_gb:.2f} GB", delta=f"-{(total_raw_size_gb - filtered_size_gb):.2f} GB")
col3.metric("Estimated Labor Saved", f"{time_saved_hours:.1f} Hours")

st.write(f"### 📊 Previewing Refined Subset ({len(filtered_df):,} rows found)")
st.dataframe(filtered_df.head(100))

st.divider()
st.write("### 💰 Monetization & Data Delivery")
estimated_price = max(5.0, filtered_size_gb * 12.5) 

st.info(f"💡 **Value Proposition:** Downloading this tailored dataset saves your lab **{time_saved_hours:.1f} hours** of manual data sorting and **{total_raw_size_gb - filtered_size_gb:.2f} GB** of local storage.")

if st.button(f"Purchase & Export This Subset (Price: ${estimated_price:.2f} USD)"):
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Purchased Dataset",
        data=csv_data,
        file_name="refined_av_dataset.csv",
        mime="text/csv"
    )
    st.success("Transaction Simulated Successfully! Your downsized data is ready.")