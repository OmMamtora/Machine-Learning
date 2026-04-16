# import streamlit as st
# import pickle
# import pandas as pd


# # Load model
# model_load = pickle.load(open('credit-risk-prediction.pkl', 'rb'))

# # App title
# st.title("💳 Credit Risk Prediction")
# st.write("Fill in the applicant details to predict loan approval.")

# # Input fields
# col1, col2 = st.columns(2)

# with col1:
#     age = st.number_input("Age", min_value=18, max_value=100, value=30)
#     income = st.number_input("Income ($)", min_value=0, value=50000)
#     loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=20000)
#     credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
#     years_experience = st.number_input("Years Experience", min_value=0, max_value=50, value=5)

# with col2:
#     gender = st.selectbox("Gender", ["Male", "Female"])
#     education = st.selectbox("Education", ["High School", "Bachelors", "Masters", "PhD"])
#     city = st.selectbox("City", ["Chicago", "New York", "Houston", "San Francisco"])
#     employment_type = st.selectbox("Employment Type", ["Salaried", "Self-Employed", "Unemployed"])

# # Predict button
# if st.button("Predict"):
#     input_data = pd.DataFrame([{
#         'Age': age,
#         'Income': income,
#         'LoanAmount': loan_amount,
#         'CreditScore': credit_score,
#         'YearsExperience': years_experience,
#         'Gender': gender,
#         'Education': education,
#         'City': city,
#         'EmploymentType': employment_type
#     }])

#     predict = model_load.predict(input_data)
#     prob = model_load.predict_proba(input_data)

#     approval_prob = prob[0][1]
#     rejection_prob = prob[0][0]

#     st.divider()

#     # Decision
#     if predict[0] == 1:
#         st.success("✅ Loan Approved")
#     else:
#         st.error("❌ Loan Rejected")

#     # Probabilities
#     col3, col4 = st.columns(2)
#     with col3:
#         st.metric("Approval Probability", f"{approval_prob:.2%}")
#     with col4:
#         st.metric("Rejection Probability", f"{rejection_prob:.2%}")

#     # Risk level
#     st.divider()
#     if approval_prob >= 0.75:
#         st.info("🟢 Risk Level : LOW")
#     elif approval_prob >= 0.40:
#         st.warning("🟡 Risk Level : MEDIUM")
#     else:
#         st.error("🔴 Risk Level : HIGH")

#     # Progress bar
#     st.write("Approval Probability")
#     st.progress(approval_prob)



import streamlit as st
import pickle
import pandas as pd
import time

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="CreditLens AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# LOAD MODEL
# ─────────────────────────────────────────────
@st.cache_resource
def load_model():
    return pickle.load(open('credit-risk-prediction.pkl', 'rb'))

model_load = load_model()

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

* { font-family: 'Syne', sans-serif; }
code, .mono { font-family: 'DM Mono', monospace; }

/* Background */
.stApp {
    background: #0a0a0f;
    background-image:
        radial-gradient(ellipse at 20% 50%, rgba(99, 50, 255, 0.08) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 20%, rgba(0, 200, 150, 0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 60% 80%, rgba(255, 80, 120, 0.05) 0%, transparent 50%);
    min-height: 100vh;
}

/* Hide default streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem; max-width: 1200px; }

/* Hero Section */
.hero {
    text-align: center;
    padding: 3rem 0 2rem 0;
    position: relative;
}
.hero-badge {
    display: inline-block;
    background: rgba(99, 50, 255, 0.15);
    border: 1px solid rgba(99, 50, 255, 0.4);
    color: #a78bfa;
    padding: 0.3rem 1rem;
    border-radius: 100px;
    font-size: 0.75rem;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}
.hero-title {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 800;
    line-height: 1.05;
    margin: 0 0 1rem 0;
    background: linear-gradient(135deg, #ffffff 0%, #a78bfa 50%, #34d399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.02em;
}
.hero-sub {
    color: #6b7280;
    font-size: 1.05rem;
    font-weight: 400;
    max-width: 500px;
    margin: 0 auto 2.5rem auto;
    line-height: 1.6;
}

/* Divider */
.gradient-line {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,50,255,0.5), rgba(52,211,153,0.5), transparent);
    margin: 2rem 0;
}

/* Cards */
.glass-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 1.8rem;
    backdrop-filter: blur(10px);
    margin-bottom: 1rem;
    transition: border-color 0.3s ease;
}
.glass-card:hover { border-color: rgba(99,50,255,0.3); }

.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #6b7280;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.06);
}

/* Result Cards */
.result-approved {
    background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(52,211,153,0.06));
    border: 1px solid rgba(52,211,153,0.3);
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    animation: fadeInUp 0.6s ease;
}
.result-rejected {
    background: linear-gradient(135deg, rgba(239,68,68,0.12), rgba(255,80,120,0.06));
    border: 1px solid rgba(239,68,68,0.3);
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    animation: fadeInUp 0.6s ease;
}

.result-icon { font-size: 3.5rem; margin-bottom: 0.5rem; }
.result-title {
    font-size: 2rem;
    font-weight: 800;
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.02em;
}
.result-approved .result-title { color: #34d399; }
.result-rejected .result-title { color: #f87171; }
.result-subtitle { color: #9ca3af; font-size: 0.9rem; }

/* Stat boxes */
.stat-box {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
}
.stat-value {
    font-size: 1.8rem;
    font-weight: 800;
    font-family: 'DM Mono', monospace;
    letter-spacing: -0.02em;
}
.stat-label {
    font-size: 0.75rem;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-family: 'DM Mono', monospace;
    margin-top: 0.2rem;
}

/* Risk badge */
.risk-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.6rem 1.4rem;
    border-radius: 100px;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.05em;
    margin-top: 1rem;
}
.risk-low { background: rgba(52,211,153,0.15); color: #34d399; border: 1px solid rgba(52,211,153,0.3); }
.risk-medium { background: rgba(251,191,36,0.15); color: #fbbf24; border: 1px solid rgba(251,191,36,0.3); }
.risk-high { background: rgba(239,68,68,0.15); color: #f87171; border: 1px solid rgba(239,68,68,0.3); }

/* Progress bar custom */
.prob-bar-wrap {
    background: rgba(255,255,255,0.05);
    border-radius: 100px;
    height: 8px;
    overflow: hidden;
    margin-top: 0.5rem;
}
.prob-bar-fill {
    height: 100%;
    border-radius: 100px;
    transition: width 1s ease;
}

/* Factor row */
.factor-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.6rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    font-size: 0.875rem;
}
.factor-row:last-child { border-bottom: none; }
.factor-name { color: #9ca3af; }
.factor-val { font-family: 'DM Mono', monospace; color: #e5e7eb; font-weight: 500; }

/* Predict button */
.stButton > button {
    background: linear-gradient(135deg, #6332ff, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.02em !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 24px rgba(99,50,255,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(99,50,255,0.5) !important;
}

/* Force dark background + white text on ALL inputs */
div[data-baseweb="base-input"],
div[data-baseweb="input"],
div[data-baseweb="select"] > div,
.stNumberInput > div > div,
div[data-testid="stNumberInput"] > div {
    background-color: #1c1c2e !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
}

/* +/- buttons */
button[data-testid="stNumberInputStepDown"],
button[data-testid="stNumberInputStepUp"] {
    background-color: #2d2d44 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    border-radius: 8px !important;
}
button[data-testid="stNumberInputStepDown"]:hover,
button[data-testid="stNumberInputStepUp"]:hover {
    background-color: rgba(99,50,255,0.4) !important;
    border-color: rgba(99,50,255,0.6) !important;
}
button[data-testid="stNumberInputStepDown"] svg,
button[data-testid="stNumberInputStepUp"] svg {
    fill: #ffffff !important;
    stroke: #ffffff !important;
}

input, input[type="number"],
input:focus, input:active, input:hover,
div[data-baseweb="input"] input,
div[data-baseweb="input"] input:focus,
.stNumberInput input,
.stNumberInput input:focus,
div[data-testid="stNumberInput"] input {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    caret-color: #a78bfa !important;
    background-color: #1c1c2e !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Mono', monospace !important;
    opacity: 1 !important;
}

/* Selectbox container */
div[data-baseweb="select"] > div,
div[data-baseweb="select"] > div:hover {
    background-color: #1c1c2e !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
}

/* Selectbox text */
div[data-baseweb="select"] div,
div[data-baseweb="select"] span,
div[data-baseweb="select"] input,
div[data-baseweb="select"] * {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    background-color: transparent !important;
}

/* Dropdown menu */
ul[role="listbox"],
div[data-baseweb="popover"] {
    background-color: #1c1c2e !important;
    border: 1px solid rgba(99,50,255,0.3) !important;
    border-radius: 10px !important;
}

/* Dropdown options */
li[role="option"], div[role="option"] {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    background-color: #1c1c2e !important;
}
li[role="option"]:hover, li[role="option"][aria-selected="true"] {
    background-color: rgba(99,50,255,0.25) !important;
}

/* Metric value */
div[data-testid="metric-container"] * {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* Labels */
.stNumberInput label, .stSelectbox label,
div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] label {
    color: #9ca3af !important;
    -webkit-text-fill-color: #9ca3af !important;
    font-size: 0.8rem !important;
    font-family: 'DM Mono', monospace !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
}

/* Placeholder */
input::placeholder {
    color: #4b5563 !important;
    -webkit-text-fill-color: #4b5563 !important;
}

/* Animations */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 20px rgba(99,50,255,0.2); }
    50% { box-shadow: 0 0 40px rgba(99,50,255,0.4); }
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(99,50,255,0.4); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">⚡ Powered by Stacking Classifier · XGBoost · Random Forest</div>
    <h1 class="hero-title">CreditLens AI</h1>
    <p class="hero-sub">Instant credit risk assessment using machine learning. Fill in applicant details and get a decision in seconds.</p>
</div>
<div class="gradient-line"></div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LAYOUT
# ─────────────────────────────────────────────
left, right = st.columns([1.1, 0.9], gap="large")

with left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">👤 Personal Info</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        education = st.selectbox("Education", ["High School", "Bachelors", "Masters", "PhD"])
    with c2:
        years_exp = st.number_input("Years Experience", min_value=0, max_value=50, value=5)
        city = st.selectbox("City", ["Chicago", "New York", "Houston", "San Francisco"])
        employment = st.selectbox("Employment", ["Salaried", "Self-Employed", "Unemployed"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">💰 Financial Info</div>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3:
        income = st.number_input("Annual Income ($)", min_value=0, value=50000, step=1000)
        loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=20000, step=1000)
    with c4:
        credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
        loan_income_ratio = loan_amount / income if income > 0 else 0
        st.metric("Loan/Income Ratio", f"{loan_income_ratio:.2f}x",
                  delta="Low ✓" if loan_income_ratio < 1 else "High ✗",
                  delta_color="normal" if loan_income_ratio < 1 else "inverse")
    st.markdown('</div>', unsafe_allow_html=True)

    if employment == "Unemployed" and credit_score > 700:
        st.warning("⚠️ Unusual: Unemployed applicant with very high credit score.")
    if education == "High School" and age < 22 and credit_score > 700:
        st.warning("⚠️ Unusual: High School student with credit score above 700.")
    if age < 22 and credit_score > 750:
        st.warning("⚠️ Unusual: Applicant under 22 with credit score above 750.")

    predict_btn = st.button("🔍 Analyze Credit Risk", use_container_width=True)

with right:
    if predict_btn:
        with st.spinner("Analyzing applicant profile..."):
            time.sleep(0.8)

        input_data = pd.DataFrame([{
            'Age': age,
            'Income': income,
            'LoanAmount': loan_amount,
            'CreditScore': credit_score,
            'YearsExperience': years_exp,
            'Gender': gender,
            'Education': education,
            'City': city,
            'EmploymentType': employment
        }])

        predict = model_load.predict(input_data)
        prob = model_load.predict_proba(input_data)
        approval_prob = prob[0][1]
        rejection_prob = prob[0][0]

        # Result card
        if predict[0] == 1:
            st.markdown(f"""
            <div class="result-approved">
                <div class="result-icon">✅</div>
                <div class="result-title">Loan Approved</div>
                <div class="result-subtitle">Applicant meets the credit criteria</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-rejected">
                <div class="result-icon">❌</div>
                <div class="result-title">Loan Rejected</div>
                <div class="result-subtitle">Applicant does not meet credit criteria</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Stats
        c5, c6 = st.columns(2)
        with c5:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-value" style="color:#34d399">{approval_prob:.1%}</div>
                <div class="stat-label">Approval Prob</div>
            </div>""", unsafe_allow_html=True)
        with c6:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-value" style="color:#f87171">{rejection_prob:.1%}</div>
                <div class="stat-label">Rejection Prob</div>
            </div>""", unsafe_allow_html=True)

        # Risk level
        if approval_prob >= 0.75:
            risk_class, risk_label, risk_icon = "risk-low", "LOW RISK", "🟢"
        elif approval_prob >= 0.40:
            risk_class, risk_label, risk_icon = "risk-medium", "MEDIUM RISK", "🟡"
        else:
            risk_class, risk_label, risk_icon = "risk-high", "HIGH RISK", "🔴"

        st.markdown(f"""
        <div style="text-align:center; margin: 1rem 0;">
            <span class="risk-badge {risk_class}">{risk_icon} {risk_label}</span>
        </div>""", unsafe_allow_html=True)

        # Progress bar
        bar_color = "#34d399" if approval_prob >= 0.75 else "#fbbf24" if approval_prob >= 0.40 else "#f87171"
        st.markdown(f"""
        <div style="margin: 1rem 0;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#6b7280; font-family:'DM Mono',monospace; margin-bottom:0.3rem;">
                <span>Approval Probability</span><span>{approval_prob:.1%}</span>
            </div>
            <div class="prob-bar-wrap">
                <div class="prob-bar-fill" style="width:{approval_prob*100}%; background:{bar_color};"></div>
            </div>
        </div>""", unsafe_allow_html=True)

        # Key factors
        st.markdown('<div class="glass-card" style="margin-top:1rem;">', unsafe_allow_html=True)
        st.markdown('<div class="section-label">📊 Key Factors</div>', unsafe_allow_html=True)

        credit_signal = "✅ Good" if credit_score >= 650 else "⚠️ Fair" if credit_score >= 500 else "❌ Poor"
        emp_signal = "✅ Stable" if employment == "Salaried" else "⚠️ Variable" if employment == "Self-Employed" else "❌ Unemployed"
        ratio_signal = "✅ Low" if loan_income_ratio < 0.5 else "⚠️ Moderate" if loan_income_ratio < 1.5 else "❌ High"
        exp_signal = "✅ Experienced" if years_exp >= 5 else "⚠️ Moderate" if years_exp >= 2 else "❌ Low"

        st.markdown(f"""
        <div class="factor-row"><span class="factor-name">Credit Score</span><span class="factor-val">{credit_score} · {credit_signal}</span></div>
        <div class="factor-row"><span class="factor-name">Employment</span><span class="factor-val">{employment} · {emp_signal}</span></div>
        <div class="factor-row"><span class="factor-name">Loan/Income Ratio</span><span class="factor-val">{loan_income_ratio:.2f}x · {ratio_signal}</span></div>
        <div class="factor-row"><span class="factor-name">Experience</span><span class="factor-val">{years_exp} yrs · {exp_signal}</span></div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        # Placeholder state
        st.markdown("""
        <div style="
            height: 100%;
            min-height: 400px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            border: 1px dashed rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 3rem;
            background: rgba(255,255,255,0.01);
        ">
            <div style="font-size:3rem; margin-bottom:1rem; opacity:0.4;">🔍</div>
            <div style="color:#4b5563; font-size:0.95rem; line-height:1.7;">
                Fill in the applicant details<br>on the left and click<br>
                <strong style="color:#6b7280;">Analyze Credit Risk</strong><br>to see the prediction.
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown('<div class="gradient-line" style="margin-top:3rem;"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding: 1rem 0 2rem; color:#374151; font-family:'DM Mono',monospace; font-size:0.75rem;">
    CreditLens AI · Stacking Classifier · 96% Accuracy on Test Data
</div>
""", unsafe_allow_html=True)
