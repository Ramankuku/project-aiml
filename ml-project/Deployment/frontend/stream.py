import streamlit as st
import requests

# API_URL = "http://127.0.0.1:5000/predict"

API_URL = "http://backend:5000/predict"

st.title("Flight Satisfaction Prediction")

with st.form("prediction_form"):
    customer_type = st.selectbox("Customer Type", [1, 0])
    age = st.number_input("Age", min_value=0, max_value=120)
    travel_type = st.selectbox("Type of Travel", [1, 0])
    flight_class = st.selectbox("Class", [0, 2, 1])
    distance = st.number_input("Flight Distance", min_value=0, max_value=5000)
    flight_service = st.number_input("Flight Service", min_value=0, max_value=5)
    total_delayed = st.number_input("Total Delayed (minutes)", min_value=0, max_value=300)
    online_services = st.number_input("Online Services (rating 0-5)", min_value=0, max_value=5)

    submit_button = st.form_submit_button("Predict")

    if submit_button:
        payload = {
            "Customer Type": customer_type,
            "Age": age,
            "Type of Travel": travel_type,
            "Class": flight_class,
            "Flight Distance": distance,
            "Flight Service": flight_service,
            "Total_delayed": total_delayed,
            "Online Services": online_services
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Satisfaction: {result['prediction']} with probability {result['probability']:.2f}")
        else:
            st.error(f"Error: {response.json()['error']}")
