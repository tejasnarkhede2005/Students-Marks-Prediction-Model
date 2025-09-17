import streamlit as st
import pickle

# Load the trained model
@st.cache_resource
def load_model():
    with open('students_marks.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# App title
st.title("Student Marks Prediction")

# Input fields
number_courses = st.number_input("Number of Courses", min_value=1, max_value=10, value=3)
time_study = st.number_input("Study Time (hours)", min_value=0.0, max_value=20.0, value=5.0)

# Prediction
if st.button("Predict Marks"):
    features = [[number_courses, time_study]]
    prediction = model.predict(features)[0]
    st.success(f"Predicted Marks: {prediction:.2f}")
