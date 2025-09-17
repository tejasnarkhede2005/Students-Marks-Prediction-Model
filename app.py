import streamlit as st
import pickle

# Custom CSS for modern, fashionable styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 800px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        margin: 2rem auto;
    }
    
    /* Title styling */
    h1 {
        color: #ffffff !important;
        text-align: center !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        margin-bottom: 2rem !important;
        text-shadow: 0 4px 8px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 3s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.2) !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #ffffff !important;
        font-weight: 500 !important;
        padding: 12px 16px !important;
        backdrop-filter: blur(5px) !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #4ecdc4 !important;
        box-shadow: 0 0 20px rgba(78, 205, 196, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Label styling */
    .stNumberInput > label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        margin-bottom: 8px !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4) !important;
        border: none !important;
        border-radius: 25px !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        padding: 12px 30px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-top: 20px !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3) !important;
        background: linear-gradient(45deg, #4ecdc4, #ff6b6b) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(135deg, #4ecdc4, #44a08d) !important;
        border: none !important;
        border-radius: 15px !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
        padding: 20px !important;
        box-shadow: 0 4px 20px rgba(78, 205, 196, 0.4) !important;
        text-align: center !important;
        margin-top: 20px !important;
    }
    
    /* Add some floating particles effect */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 200, 255, 0.3) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #4ecdc4, #ff6b6b);
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main .block-container {
            margin: 1rem;
            padding: 2rem 1rem;
        }
        
        h1 {
            font-size: 2rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Load the trained model
@st.cache_resource
def load_model():
    with open('students_marks.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# App title with emoji
st.title("🎓 Student Marks Prediction")

# Add some spacing and description
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <p style="color: rgba(255, 255, 255, 0.8); font-size: 1.1rem; font-weight: 300;">
        Predict your academic performance with our AI-powered tool
    </p>
</div>
""", unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Input fields
    number_courses = st.number_input("📚 Number of Courses", min_value=1, max_value=10, value=3)

with col2:
    time_study = st.number_input("⏰ Study Time (hours)", min_value=0.0, max_value=20.0, value=5.0)

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Prediction
if st.button("🚀 Predict My Marks"):
    features = [[number_courses, time_study]]
    prediction = model.predict(features)[0]
    
    # Add a slight delay for dramatic effect (optional)
    import time
    with st.spinner('🔮 Calculating your predicted marks...'):
        time.sleep(1)
    
    st.success(f"🎯 Predicted Marks: {prediction:.2f}%")
    
    # Add motivational message based on prediction
    if prediction >= 80:
        st.balloons()
        st.markdown("🌟 **Excellent performance expected! Keep up the great work!**")
    elif prediction >= 70:
        st.markdown("👍 **Good job! You're on the right track!**")
    elif prediction >= 60:
        st.markdown("💪 **You can do better! Consider increasing your study time.**")
    else:
        st.markdown("📈 **There's room for improvement! Try taking fewer courses or studying more.**")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.2);">
    <p style="color: rgba(255, 255, 255, 0.6); font-size: 0.9rem;">
        Made with ❤️ using Streamlit | Powered by Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)
