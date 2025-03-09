import streamlit as st
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

# Load the trained model and scaler
model = load_model("hackathon_attendance_model.h5")
scaler = joblib.load("scaler.pkl")

# Set Streamlit page config
st.set_page_config(page_title="Hackathon Attendance Predictor", layout="wide")
st.markdown("<h1 style='text-align: center; color: white;margin-top:0'>🎯 Hackathon Attendance Predictor 🚀</h1>", unsafe_allow_html=True)

# Custom CSS for better layout
st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            font-size: 18px;
            padding: 10px;
        }
        .result-box {
            padding: 20px;
            border-radius: 10px;
            background-color: #f9f9f9;
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            color: white;
            background-color: darkorchid;
}
        }
    </style>
""", unsafe_allow_html=True)

# Creating columns for layout
col1, col2 = st.columns([1, 1])  # 1:1 ratio for left and right sections

# Left Column - User Input
with col1:
    st.header("📝 Enter Candidate Details")

    # Dropdowns for user inputs
    registered = st.selectbox("Registered?", ["Yes", "No"])
    engagement_level = st.selectbox("Engagement Level", [0, 1, 2, 3])
    interested_in_job = st.selectbox("Interested in Job Opportunities?", ["Yes", "No"])
    long_distance = st.selectbox("Lives Far Away?", ["Yes", "No"])
    questionnaire = st.selectbox("Completed Questionnaire?", ["Yes", "No"])
    prev_hack = st.selectbox("Attended Previous Hackathon?", ["Yes", "No"])

    # Convert selections to numerical values
    data_dict = {
        "Registered": 1 if registered == "Yes" else 0,
        "Engagement_Level": int(engagement_level),
        "Interested_In_Job_Opp": 1 if interested_in_job == "Yes" else 0,
        "Long_Distance": 1 if long_distance == "Yes" else 0,
        "Questionnaire": 1 if questionnaire == "Yes" else 0,
        "Prev_Hack": 1 if prev_hack == "Yes" else 0
    }

    # Convert to DataFrame
    new_data = pd.DataFrame([data_dict])

    # Predict Button
    if st.button("🔍 Predict Attendance"):
        # Scale input
        new_data_scaled = scaler.transform(new_data)

        # Get prediction probability
        prediction_prob = model.predict(new_data_scaled)[0][0]
        predicted_class = "🎉 Yes, Will Attend!" if prediction_prob > 0.5 else "❌ No, Won't Attend"

        # Save the result in session state
        st.session_state["predicted_class"] = predicted_class
        st.session_state["prediction_prob"] = prediction_prob



# Right Column - Display Prediction & Model Details
with col2:
    # Toggle Model Details
    if "show_model_details" not in st.session_state:
        st.session_state["show_model_details"] = False

    if st.button("ℹ️ Show Model Details", key="toggle_model_details", help="Click to show/hide model details"):
        st.session_state["show_model_details"] = not st.session_state["show_model_details"]

    if st.session_state["show_model_details"]:
        st.markdown("""
        <div class='model-details'>
            <h4>📌 Model Information</h4>
            <ul>
                <li><b>Dataset:</b> Synthetic dataset of size 5000</li>
                <li><b>Model Type:</b> Sequential Dense Neural Network</li>
                <li><b>Total params:</b> 16,993</li>
                <li><b>Trainable params:</b> 16,737</li>
                <li><b>Non-trainable params:</b> 256</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.header("🎯 Prediction Result")

    # Check if prediction exists in session state
    if "predicted_class" in st.session_state:
        # Show result inside a styled box
        st.markdown(f"""
        <div class='result-box'>
            <p>📢 Prediction: {st.session_state["predicted_class"]}</p>
            <p>📊 Confidence Level: {st.session_state["prediction_prob"] * 100:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)

        # Display success or error message
        if st.session_state["prediction_prob"] > 0.5:
            st.success("Great! The candidate is likely to attend! 🎉")
        else:
            st.error("This candidate is unlikely to attend. ❌")
