import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("antenna_model.pkl")

st.title("AI Patch Antenna Designer")

freq = st.number_input(
    "Enter Frequency (GHz)",
    min_value=1.0,
    max_value=10.0,
    value=2.4
)

if st.button("Generate Dimensions"):

    prediction = model.predict(
        pd.DataFrame({
            "Frequency_GHz": [freq]
        })
    )[0]

    st.subheader("Generated Dimensions")

    st.write(
        f"Patch Width: {prediction[0]:.2f} mm"
    )

    st.write(
        f"Patch Length: {prediction[1]:.2f} mm"
    )

    st.write(
        f"Ground Width: {prediction[2]:.2f} mm"
    )

    st.write(
        f"Ground Length: {prediction[3]:.2f} mm"
    )