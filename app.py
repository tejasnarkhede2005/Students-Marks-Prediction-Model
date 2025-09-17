import streamlit as st
import pickle

# Professional CSS styling
st.markdown("""
<style>
    /* Import professional fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Global styling */
    .stApp {
        background: linear-gradient(135deg, #2d3748 0%, #1a202c 50%, #000000 100%);
        min-height: 100vh;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 900px;
        background: rgba(45, 55, 72, 0.15);
        backdrop-filter: blur(15px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4), 0 10px 10px -5px rgba(0, 0, 0, 0.2);
        margin: 2rem auto;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    
    /* Title styling */
    h1 {
        text-align: center !important;
        font-weight: 700 !important;
        font-size: 2.25rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.025em !important;
        background: linear-gradient(135deg, #f7fafc, #cbd5e0, #a0aec0) !important;
        background-size: 200% 200% !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        animation: gradientShift 4s ease infinite !important;
        filter: drop-shadow(0 2px 8px rgba(255, 255, 255, 0.1)) !important;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Subtitle styling */
    .subtitle {
        text-align: center;
        color: #cbd5e0;
        font-size: 1.125rem;
        font-weight: 400;
        margin-bottom: 3rem;
        line-height: 1.5;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
        opacity: 0.9;
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(135deg, #f7fafc, #e2e8f0, #cbd5e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        margin-top: 2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(203, 213, 224, 0.3);
        filter: drop-shadow(0 1px 2px rgba(255, 255, 255, 0.1));
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input {
        background: rgba(45, 55, 72, 0.6) !important;
        border: 1.5px solid rgba(203, 213, 224, 0.2) !important;
        border-radius: 8px !important;
        color: #f7fafc !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(5px) !important;
    }
    
    .stNumberInput > div > div > input:focus {
        outline: none !important;
        border-color: #cbd5e0 !important;
        box-shadow: 0 0 0 3px rgba(203, 213, 224, 0.2), 0 0 15px rgba(203, 213, 224, 0.3) !important;
        background: rgba(45, 55, 72, 0.8) !important;
        color: #ffffff !important;
    }
    
    .stNumberInput > div > div > input:hover {
        border-color: rgba(203, 213, 224, 0.3) !important;
        background: rgba(45, 55, 72, 0.7) !important;
    }
    
    /* Label styling */
    .stNumberInput > label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        margin-bottom: 8px !important;
        display: block !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5) !important;
        opacity: 0.95 !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #4a5568, #2d3748, #1a202c) !important;
        border: 1px solid rgba(203, 213, 224, 0.2) !important;
        border-radius: 10px !important;
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 14px 32px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin-top: 2rem !important;
        cursor: pointer !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4) !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2d3748, #4a5568, #2d3748) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6) !important;
        border-color: rgba(203, 213, 224, 0.4) !important;
        color: #f7fafc !important;
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
        background: rgba(45, 55, 72, 0.3);
        border: 1px solid rgba(203, 213, 224, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    
    .info-card h3 {
        color: #f7fafc;
        font-size: 1.125rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
    }
    
    .info-card p {
        color: #cbd5e0;
        font-size: 0.95rem;
        line-height: 1.5;
        margin: 0;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
        opacity: 0.9;
    }
    
    /* Results card */
    .result-card {
        background: linear-gradient(135deg, #4a5568 0%, #2d3748 50%, #1a202c 100%);
        border-radius: 16px;
        padding: 2.5rem;
        text-align: center;
        margin-top: 2rem;
        color: #f7fafc;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 10px 10px -5px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(203, 213, 224, 0.1);
    }
    
    .result-card h2 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
        background: linear-gradient(135deg, #f7fafc, #e2e8f0, #cbd5e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
    }
    
    .result-card p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin: 0;
        font-weight: 500;
        color: #e2e8f0;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(203, 213, 224, 0.2);
        color: #cbd5e0;
        font-size: 0.875rem;
        font-weight: 400;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
    }
    
    .footer p {
        margin: 0.25rem 0;
        opacity: 0.8;
    }
    
    .footer strong {
        color: #e2e8f0;
        opacity: 1;
    }
    
    /* Loading spinner customization */
    .stSpinner {
        text-align: center !important;
        color: #3b82f6 !important;
    }
    
    /* Metrics styling */
    [data-testid="metric-container"] {
        background: rgba(45, 55, 72, 0.3) !important;
        border: 1px solid rgba(203, 213, 224, 0.1) !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3) !important;
        backdrop-filter: blur(15px) !important;
    }
    
    [data-testid="metric-container"] > div {
        color: #f7fafc !important;
    }
    
    [data-testid="metric-container"] [data-testid="metric-container"] div[data-testid="metric-container"] {
        font-weight: 600 !important;
    }
    
    /* Metric labels and values */
    [data-testid="metric-container"] div[data-testid="metric-container"] > div {
        color: #e2e8f0 !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.4) !important;
    }
    
    /* Metric value styling */
    [data-testid="metric-container"] [data-testid="metric-container"] > div:first-child {
        color: #f7fafc !important;
        font-weight: 700 !important;
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
    <p>Powered by Machine Learning • Built By Tejas</p>
</div>
""", unsafe_allow_html=True)

