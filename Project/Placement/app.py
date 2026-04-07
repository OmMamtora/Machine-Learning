import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Placement Predictor", layout="centered")

st.title("🎓 Placement Prediction System")
st.write("Enter student details to predict placement status")

# Input fields
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("IQ", min_value=0, max_value=200, step=1)

# Prediction button
if st.button("Predict"):
    input_data = pd.DataFrame([[cgpa, iq]], columns=["cgpa", "iq"])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("✅ Student will be Placed")
    else:
        st.error("❌ Student will NOT be Placed")