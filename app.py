import streamlit as st

st.set_page_config(page_title="Energy Optimization Chatbot")

st.title("⚡ Energy Optimization Chatbot")

st.write("Calculate electricity consumption and get energy-saving tips.")

appliance = st.selectbox(
    "Select Appliance",
    ["Air Conditioner", "Fan", "Refrigerator", "Computer", "Washing Machine"]
)

power = st.number_input(
    "Power Rating (Watts)",
    min_value=1,
    value=100
)

hours = st.slider(
    "Usage Hours Per Day",
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

    st.subheader("Results")

    st.metric("Daily Consumption", f"{units:.2f} kWh")
    st.metric("Daily Cost", f"₹{daily_cost:.2f}")
    st.metric("Monthly Cost", f"₹{monthly_cost:.2f}")

    if units > 10:
        st.warning("High energy consumption detected.")
    else:
        st.success("Energy usage is efficient.")

st.subheader("Energy Saving Tips")

tips = [
    "Switch off unused appliances.",
    "Use LED bulbs.",
    "Unplug chargers when not in use.",
    "Use energy-efficient appliances.",
    "Reduce peak-hour electricity usage."
]

for tip in tips:
    st.write("✅", tip)
