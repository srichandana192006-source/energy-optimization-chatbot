import streamlit as st

st.title("Carbon Footprint Calculator")

units = st.number_input(
    "Monthly Units Consumed",
    min_value=0.0
)

if st.button("Calculate Footprint"):

    carbon = units * 0.82

    st.metric(
        "CO₂ Emission",
        f"{carbon:.2f} kg"
    )
