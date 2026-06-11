import streamlit as st
import pandas as pd

st.title("🔋 Energy Calculator")

df = pd.read_csv("data/appliances.csv")

appliance = st.selectbox(
    "Select Appliance",
    df["Appliance"]
)

power = df[df["Appliance"] == appliance]["Power"].values[0]

hours = st.slider(
    "Hours Used Per Day",
    1,
    24,
    5
)

rate = st.number_input(
    "Electricity Rate (₹/kWh)",
    min_value=1.0,
    value=6.0
)

if st.button("Calculate"):

    units = (power * hours) / 1000

    daily_cost = units * rate

    monthly_cost = daily_cost * 30

    st.success("Calculation Completed")

    st.metric("Power Rating", f"{power} W")
    st.metric("Daily Consumption", f"{units:.2f} kWh")
    st.metric("Daily Cost", f"₹{daily_cost:.2f}")
    st.metric("Monthly Cost", f"₹{monthly_cost:.2f}")
