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
