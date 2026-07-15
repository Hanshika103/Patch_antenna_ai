


import streamlit as st
import joblib
import pandas as pd
st.set_page_config(
    page_title="AI Patch Antenna Designer",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

.stApp{
    background:#f5f6fa;
}

/* Remove Streamlit header */
header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Main container */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

/* Title */
h1{
    text-align:center;
    color:#2d3748;
    font-size:42px;
    font-weight:800;
}

h2,h3{
    color:#374151;
}

/* Input Labels */
label{
    font-weight:600 !important;
    color:#374151 !important;
}

/* Input Boxes */
.stNumberInput input{
    border-radius:12px;
    border:2px solid #d1d5db;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:12px;
}

/* Button */
.stButton>button{

    width:100%;
    height:55px;

    border:none;
    border-radius:12px;

    background:linear-gradient(
    90deg,
    #d4af37,
    #f4d03f
    );

    color:black;

    font-size:18px;
    font-weight:bold;

    transition:0.3s;
}

.stButton>button:hover{

    transform:scale(1.02);

    box-shadow:0 8px 25px rgba(212,175,55,.35);

}

/* Success */
.stSuccess{

    border-radius:12px;

}

/* Horizontal Line */
hr{

    border:1px solid #e5e7eb;

}

/* Metric Style */
.metric-card{

background:white;

padding:20px;

border-radius:15px;

text-align:center;

border:1px solid #ececec;

box-shadow:0 5px 20px rgba(0,0,0,.05);

margin-bottom:15px;

}

.metric-title{

font-size:18px;

color:#6b7280;

}

.metric-value{

font-size:28px;

font-weight:700;

color:#d4af37;

}

/* Summary Card */

.summary{

background:white;

padding:20px;

border-radius:15px;

box-shadow:0 5px 18px rgba(0,0,0,.05);

border:1px solid #ececec;

margin-top:10px;

}

</style>
""", unsafe_allow_html=True)

model = joblib.load("antenna_model.pkl")

st.markdown("""
<h1>📡 AI Patch Antenna Designer</h1>
<p style='text-align:center;
color:gray;
font-size:18px;'>

Intelligent Microstrip Patch Antenna Design using Machine Learning

</p>
""", unsafe_allow_html=True)

frequency = st.number_input(
    "Center Frequency (GHz)",
    min_value=1.0,
    max_value=20.0,
    value=9.5
)

material = st.selectbox(
    "Substrate Material",
    [
        "FR4",
        "Rogers 4003C",
        "Rogers RT5880",
        "Custom"
    ]
)

er = st.number_input(
    "Dielectric Constant (εr)",
    value=4.4
)

height = st.number_input(
    "Substrate Height (mm)",
    value=1.6
)

loss = st.number_input(
    "Loss Tangent",
    value=0.02,
    format="%.4f"
)

copper = st.number_input(
    "Copper Thickness (mm)",
    value=0.035,
    format="%.3f"
)

if st.button("Generate Dimensions"):

    input_df = pd.DataFrame({
        "Frequency_GHz":[frequency],
        "Dielectric_Constant":[er],
        "Height_mm":[height],
        "Loss_Tangent":[loss],
        "Copper_Thickness_mm":[copper]
    })

    prediction = model.predict(input_df)[0]

    st.success("Design Generated Successfully")

    st.markdown("<div class='summary'>", unsafe_allow_html=True)

    st.subheader("📋 Design Summary")

    st.write(f"Center Frequency : {frequency:.2f} GHz")
    st.write(f"Substrate : {material}")
    st.write(f"Dielectric Constant (εr) : {er}")
    st.write(f"Height : {height} mm")
    st.write(f"Loss Tangent : {loss}")
    st.write(f"Copper Thickness : {copper} mm")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Predicted Dimensions")

    st.write(f"Patch Width : {prediction[0]:.2f} mm")
    st.write(f"Patch Length : {prediction[1]:.2f} mm")
    st.write(f"Ground Width : {prediction[2]:.2f} mm")
    st.write(f"Ground Length : {prediction[3]:.2f} mm")