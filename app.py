import streamlit as st
import pickle

# Professional CSS styling
st.markdown("""
<style>
    /* Import professional fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Global styling */
    .stApp {
        background-color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 900px;
        background: #ffffff;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin: 2rem auto;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    
    /* Title styling */
    h1 {
        color: #1e293b !important;
        text-align: center !important;
        font-weight: 700 !important;
        font-size: 2.25rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.025em !important;
    }
    
    /* Subtitle styling */
    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 1.125rem;
        font-weight: 400;
        margin-bottom: 3rem;
        line-height: 1.5;
    }
    
    /* Section headers */
    .section-header {
        color: #374151;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        margin-top: 2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e5e7eb;
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input {
        background-color: #ffffff !important;
        border: 1.5px solid #d1d5db !important;
        border-radius: 6px !important;
        color: #374151 !important;
        font-weight: 400 !important;
        font-size: 1rem !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        outline: none !important;
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
    }
    
    .stNumberInput > div > div > input:hover {
        border-color: #9ca3af !important;
    }
    
    /* Label styling */
    .stNumberInput > label {
        color: #374151 !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 6px !important;
        display: block !important;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #3b82f6 !important;
        border: none !important;
        border-radius: 6px !important;
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        padding: 12px 32px !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        margin-top: 2rem !important;
        cursor: pointer !important;
    }
    
    .stButton > button:hover {
        background-color: #2563eb !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
        background-color: #1d4ed8 !important;
    }
    
    /* Success message styling */
    .stSuccess {
        background-color: #f0f9f4 !important;
        border: 1px solid #bbf7d0 !important;
        border-left: 4px solid #10b981 !important;
        border-radius: 6px !important;
        color: #065f46 !important;
        font-weight: 500 !important;
        padding: 16px 20px !important;
        margin-top: 2rem !important;
    }
    
    .stSuccess > div {
        font-size: 1.1rem !important;
    }
    
    /* Warning/Info messages */
    .stWarning {
        background-color: #fffbeb !important;
        border: 1px solid #fed7aa !important;
        border-left: 4px solid #f59e0b !important;
        border-radius: 6px !important;
        color: #92400e !important;
        padding: 16px 20px !important;
    }
    
    .stInfo {
        background-color: #eff6ff !important;
        border: 1px solid #bfdbfe !important;
        border-left: 4px solid #3b82f6 !important;
        border-radius: 6px !important;
        color: #1e40af !important;
        padding: 16px 20px !important;
    }
    
    /* Columns spacing */
    .element-container {
        margin-bottom: 1rem;
    }
    
    /* Custom card styling */
    .info-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .info-card h3 {
        color: #1e293b;
        font-size: 1.125rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .info-card p {
        color: #64748b;
        font-size: 0.95rem;
        line-height: 1.5;
        margin: 0;
    }
    
    /* Results card */
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 8px;
        padding: 2rem;
        text-align: center;
        margin-top: 2rem;
        color: white;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .result-card h2 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
    }
    
    .result-card p {
        font-size: 1.1rem;
        opacity: 0.9;
        margin: 0;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid #e5e7eb;
        color: #6b7280;
        font-size: 0.875rem;
    }
    
    /* Loading spinner customization */
    .stSpinner {
        text-align: center !important;
        color: #3b82f6 !important;
    }
    
    /* Metrics styling */
    [data-testid="metric-container"] {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
    }
    
    [data-testid="metric-container"] > div {
        color: #374151;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main .block-container {
            margin: 1rem;
            padding: 2rem 1.5rem;
        }
        
        h1 {
            font-size: 1.875rem !important;
        }
        
        .result-card h2 {
            font-size: 2rem;
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

# App header
st.title("Student Performance Analytics")

st.markdown("""
<div class="subtitle">
    Advanced machine learning model for academic performance prediction
</div>
""", unsafe_allow_html=True)

# Information card
st.markdown("""
<div class="info-card">
    <h3>How it works</h3>
    <p>Our predictive model analyzes course load and study time patterns to forecast academic performance. 
    Input your current academic parameters below to receive an evidence-based performance prediction.</p>
</div>
""", unsafe_allow_html=True)

# Input section
st.markdown("""<div class="section-header">Input Parameters</div>""", unsafe_allow_html=True)

# Create columns for professional layout
col1, col2 = st.columns(2, gap="large")

with col1:
    number_courses = st.number_input(
        "Number of Courses",
        min_value=1,
        max_value=10,
        value=3,
        help="Total number of courses you are currently enrolled in"
    )

with col2:
    time_study = st.number_input(
        "Weekly Study Hours",
        min_value=0.0,
        max_value=80.0,
        value=20.0,
        step=0.5,
        help="Average number of hours you study per week"
    )

# Analysis section
st.markdown("""<div class="section-header">Performance Analysis</div>""", unsafe_allow_html=True)

# Prediction button
if st.button("Generate Performance Prediction", type="primary"):
    with st.spinner('Analyzing academic parameters...'):
        import time
        time.sleep(1)  # Professional loading experience
        
        features = [[number_courses, time_study]]
        prediction = model.predict(features)[0]
        
        # Display result in professional card format
        st.markdown(f"""
        <div class="result-card">
            <h2>{prediction:.1f}%</h2>
            <p>Predicted Academic Performance</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Professional metrics display
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="Course Load",
                value=f"{number_courses} courses",
                delta=f"{number_courses - 3} vs average" if number_courses != 3 else "Average load"
            )
        
        with col2:
            st.metric(
                label="Study Commitment",
                value=f"{time_study} hrs/week",
                delta=f"{time_study - 20:.1f} vs recommended" if time_study != 20 else "Optimal"
            )
        
        with col3:
            performance_level = "Excellent" if prediction >= 85 else "Good" if prediction >= 75 else "Average" if prediction >= 65 else "Below Average"
            st.metric(
                label="Performance Level",
                value=performance_level,
                delta=None
            )
        
        # Professional recommendations
        st.markdown("""<div class="section-header">Recommendations</div>""", unsafe_allow_html=True)
        
        if prediction >= 85:
            st.success("🎯 **Excellent trajectory** - Your current study pattern indicates strong academic performance. Consider challenging yourself with advanced coursework.")
        elif prediction >= 75:
            st.success("✅ **Solid performance** - You're on track for good results. Maintain consistent study habits.")
        elif prediction >= 65:
            st.warning("⚠️ **Room for improvement** - Consider optimizing your study schedule or reducing course load for better outcomes.")
        else:
            st.error("📈 **Action required** - Your current parameters suggest academic challenges. We recommend academic counseling or study strategy adjustment.")

# Additional insights section
if st.session_state.get('show_insights', False) or st.button("Show Detailed Insights", type="secondary"):
    st.session_state.show_insights = True
    
    st.markdown("""<div class="section-header">Academic Insights</div>""", unsafe_allow_html=True)
    
    # Professional analysis cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>Study-Performance Correlation</h3>
            <p>Research indicates optimal study time ranges between 15-25 hours per week for undergraduate students, 
            with diminishing returns beyond 30 hours due to fatigue and reduced retention.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>Course Load Impact</h3>
            <p>Students taking 3-4 courses typically achieve higher individual course performance compared to 
            those with 5+ courses, due to improved focus and time allocation per subject.</p>
        </div>
        """, unsafe_allow_html=True)

# Professional footer
st.markdown("""
<div class="footer">
    <p><strong>Student Performance Analytics</strong> | Advanced Predictive Modeling</p>
    <p>Powered by Machine Learning • Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
