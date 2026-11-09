
import streamlit as st
import pandas as pd
import joblib

# ================= LOAD MODEL =================

model = joblib.load("student_performance_model.pkl")
features = joblib.load("student_features.pkl")

# ================= PAGE CONFIGURATION =================

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ================= CUSTOM DESIGN =================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --purple: #a78bfa;
    --light-purple: #c4b5fd;
    --text: #f5f3ff;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 0%, #302052 0%, transparent 35%),
        radial-gradient(ellipse at 95% 100%, #172b50 0%, transparent 35%),
        #080b18;
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

#MainMenu, footer {
    visibility: hidden;
}

/* ================= HEADER ================= */

.hero {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 25px;
    background:
        radial-gradient(circle at 85% 45%, rgba(139,92,246,0.22), transparent 32%),
        linear-gradient(115deg, #15142b, #201a3e 55%, #292052);
    border: 1px solid rgba(196,181,253,0.24);
    border-radius: 26px;
    padding: 42px 45px;
    margin-bottom: 32px;
    overflow: hidden;
    box-shadow: 0 18px 55px rgba(0,0,0,0.28);
}

.hero::before {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    right: -100px;
    top: -150px;
    border-radius: 50%;
    border: 1px solid rgba(196,181,253,0.12);
}

.hero::after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    right: -55px;
    bottom: -155px;
    border-radius: 50%;
    border: 1px solid rgba(196,181,253,0.15);
}

.hero-left {
    position: relative;
    z-index: 2;
    flex: 1;
}

.hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #d8caff;
    background: rgba(167,139,250,0.13);
    border: 1px solid rgba(196,181,253,0.28);
    border-radius: 30px;
    padding: 8px 15px;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.7px;
    margin-bottom: 22px;
}

.hero h1 {
    color: white !important;
    font-size: 39px;
    line-height: 1.2;
    font-weight: 900;
    letter-spacing: -1.5px;
    margin: 0 0 14px 0;
}

.hero h1 span {
    background: linear-gradient(90deg, #c4b5fd, #9b8cff, #e0c8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #c4c1dc !important;
    font-size: 14px;
    line-height: 1.9;
    max-width: 590px;
    margin: 0;
}

.hero-right {
    position: relative;
    z-index: 2;
    width: 205px;
    min-width: 205px;
    height: 190px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-orbit {
    width: 165px;
    height: 165px;
    border: 1px solid rgba(196,181,253,0.3);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    box-shadow: 0 0 45px rgba(167,139,250,0.12);
}

.hero-orbit::before {
    content: "";
    position: absolute;
    inset: 14px;
    border: 1px dashed rgba(196,181,253,0.35);
    border-radius: 50%;
}

.hero-icon {
    width: 105px;
    height: 105px;
    border-radius: 30px;
    background: linear-gradient(145deg, #7754d9, #39286c);
    border: 1px solid rgba(255,255,255,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.3);
}

.hero-dot {
    position: absolute;
    width: 11px;
    height: 11px;
    background: #c4b5fd;
    border-radius: 50%;
    box-shadow: 0 0 15px #a78bfa;
}

.dot-one {
    top: 15px;
    right: 35px;
}

.dot-two {
    bottom: 22px;
    left: 10px;
}

/* ================= SECTION HEADINGS ================= */

.section-heading {
    color: #e3d9ff;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.2px;
    margin: 25px 0 18px 0;
    padding: 14px 18px;
    background: linear-gradient(
        90deg,
        rgba(124,91,255,0.16),
        rgba(124,91,255,0.02)
    );
    border-left: 4px solid #a78bfa;
    border-bottom: 1px solid rgba(167,139,250,0.18);
    border-radius: 8px;
}

/* ================= FORM BACKGROUND ================= */

div[data-testid="stForm"] {
    background: rgba(19,26,48,0.58);
    border: 1px solid rgba(167,139,250,0.22);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.16);
}

/* ================= LABELS ================= */

label {
    color: #e0daf5 !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}

div[data-testid="stWidgetLabel"] p {
    color: #e0daf5 !important;
}

/* ================= DROPDOWNS ================= */

div[data-baseweb="select"] > div {
    background: linear-gradient(135deg, #191f39, #202543) !important;
    border: 1px solid #514477 !important;
    border-radius: 12px !important;
    min-height: 43px;
    transition: all 0.2s ease;
}

div[data-baseweb="select"] > div:hover {
    border-color: #a78bfa !important;
    box-shadow: 0 0 12px rgba(167,139,250,0.12);
}

div[data-baseweb="select"] span {
    color: #f5f3ff !important;
}

div[data-baseweb="popover"] {
    background: #171d35 !important;
}

ul[role="listbox"] {
    background: #171d35 !important;
    border: 1px solid #514477 !important;
    border-radius: 10px !important;
}

li[role="option"] {
    color: white !important;
}

li[role="option"]:hover {
    background: #34275b !important;
}

/* ================= NUMBER INPUT ================= */

div[data-testid="stNumberInput"] input {
    background: linear-gradient(135deg, #191f39, #202543) !important;
    color: white !important;
    border: 1px solid #514477 !important;
    border-radius: 12px !important;
    min-height: 43px;
}

div[data-testid="stNumberInput"] input:focus {
    border-color: #a78bfa !important;
    box-shadow: 0 0 12px rgba(167,139,250,0.15);
}

/* ================= SLIDERS ================= */

div[data-testid="stSlider"] {
    padding-top: 5px;
    padding-bottom: 8px;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    color: #a78bfa !important;
}

div[data-testid="stSlider"] [role="slider"] {
    background: #a78bfa !important;
    border: 2px solid white !important;
    box-shadow: 0 0 10px rgba(167,139,250,0.4);
}

div[data-testid="stSlider"] [data-testid="stTickBar"] {
    background: #514477 !important;
}

div[data-testid="stSlider"] [data-testid="stTickBarMin"],
div[data-testid="stSlider"] [data-testid="stTickBarMax"] {
    color: #aeb2cc !important;
}

/* ================= SUBMIT BUTTON ================= */

.stFormSubmitButton button {
    width: 100%;
    height: 56px;
    border-radius: 14px;
    border: 1px solid #c4b5fd;
    background: linear-gradient(100deg, #7048e8, #a078ff);
    color: white !important;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 0.7px;
    box-shadow: 0 6px 25px rgba(124,91,255,0.3);
    transition: all 0.25s ease;
}

.stFormSubmitButton button:hover {
    background: linear-gradient(100deg, #805fff, #b18cff);
    box-shadow: 0 8px 30px rgba(124,91,255,0.5);
    transform: translateY(-2px);
    border: 1px solid white;
}

/* ================= RESULT CARD ================= */

.result-card {
    background:
        radial-gradient(circle at 50% 0%, rgba(167,139,250,0.18), transparent 60%),
        linear-gradient(135deg, #201a42, #30245d);
    border: 1px solid rgba(196,181,253,0.4);
    border-radius: 24px;
    padding: 42px 25px;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0 12px 35px rgba(93,65,190,0.2);
}

.result-label {
    color: #c4b5fd;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.result-value {
    font-size: 46px;
    font-weight: 800;
    margin-top: 12px;
}

/* ================= ALERTS ================= */

div[data-testid="stAlert"] {
    background: rgba(83,65,142,0.18);
    border: 1px solid rgba(167,139,250,0.3);
    border-radius: 12px;
}

/* ================= CAPTIONS ================= */

.stCaption {
    color: #a5abc5 !important;
}

/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #858ba9;
    font-size: 11px;
    letter-spacing: 1px;
    line-height: 2;
    padding: 30px 0 5px;
}

hr {
    border-color: rgba(167,139,250,0.2);
}

/* ================= MOBILE DESIGN ================= */

@media (max-width: 768px) {
    .hero {
        padding: 27px;
    }

    .hero-right {
        display: none;
    }

    .hero h1 {
        font-size: 29px;
    }

    div[data-testid="stForm"] {
        padding: 15px;
    }

    .result-value {
        font-size: 36px;
    }
}

</style>
""", unsafe_allow_html=True)


# ================= HERO HEADER =================

st.markdown("""
<div class="hero">
<div class="hero-left">
<div class="hero-tag">✦ &nbsp; AI / ML PROJECT</div>
<h1>Student Performance<br><span>Predictor.</span></h1>
<p>
Discover insights into student academic performance
through Machine Learning. Enter student information
and explore the predicted performance category.
</p>
</div>
<div class="hero-right">
<div class="hero-orbit">
<div class="hero-icon">🎓</div>
<div class="hero-dot dot-one"></div>
<div class="hero-dot dot-two"></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)


# ================= STUDENT FORM =================

st.markdown(
    '<div class="section-heading">01 &nbsp; Academic Information</div>',
    unsafe_allow_html=True
)

with st.form("student_form"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 15, 22, 17)

        studytime = st.selectbox(
            "Weekly Study Time",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "Less than 2 hours",
                2: "2 to 5 hours",
                3: "5 to 10 hours",
                4: "More than 10 hours"
            }[x]
        )

        failures = st.selectbox(
            "Past Class Failures", [0, 1, 2, 3]
        )

        absences = st.number_input(
            "Number of Absences",
            min_value=0,
            max_value=100,
            value=0
        )

    with col2:
        schoolsup = st.selectbox(
            "Extra Educational Support", ["yes", "no"]
        )

        higher = st.selectbox(
            "Wants Higher Education", ["yes", "no"]
        )

        activities = st.selectbox(
            "Extra-curricular Activities", ["yes", "no"]
        )

    st.markdown(
        '<div class="section-heading">02 &nbsp; Family Information</div>',
        unsafe_allow_html=True
    )

    col3, col4 = st.columns(2)

    with col3:
        Medu = st.selectbox(
            "Mother's Education (0-4)", [0, 1, 2, 3, 4]
        )

        Fedu = st.selectbox(
            "Father's Education (0-4)", [0, 1, 2, 3, 4]
        )

        famsize = st.selectbox(
            "Family Size", ["GT3", "LE3"]
        )

    with col4:
        famrel = st.slider(
            "Family Relationship Quality", 1, 5, 4
        )

        internet = st.selectbox(
            "Internet Access", ["yes", "no"]
        )

    st.markdown(
        '<div class="section-heading">03 &nbsp; Lifestyle Information</div>',
        unsafe_allow_html=True
    )

    col5, col6 = st.columns(2)

    with col5:
        goout = st.slider(
            "Going Out With Friends", 1, 5, 3
        )

        Dalc = st.slider(
            "Workday Alcohol Consumption", 1, 5, 1
        )

        Walc = st.slider(
            "Weekend Alcohol Consumption", 1, 5, 1
        )

    with col6:
        health = st.slider(
            "Current Health", 1, 5, 3
        )

        address = st.selectbox(
            "Home Address",
            ["U", "R"],
            format_func=lambda x: {
                "U": "Urban",
                "R": "Rural"
            }[x]
        )

        sex = st.selectbox(
            "Gender", ["F", "M"]
        )

    st.markdown(
        '<div class="section-heading">04 &nbsp; School Information</div>',
        unsafe_allow_html=True
    )

    school = st.selectbox(
        "School", ["GP", "MS"]
    )

    predict_button = st.form_submit_button(
        "✦  PREDICT STUDENT PERFORMANCE  ✦"
    )


# ================= PREDICTION =================

if predict_button:

    input_data = {
        'age': age,
        'studytime': studytime,
        'failures': failures,
        'absences': absences,
        'goout': goout,
        'Dalc': Dalc,
        'Walc': Walc,
        'health': health,
        'famrel': famrel,
        'sex': sex,
        'school': school,
        'address': address,
        'famsize': famsize,
        'Medu': Medu,
        'Fedu': Fedu,
        'internet': internet,
        'higher': higher,
        'activities': activities,
        'schoolsup': schoolsup
    }

    input_df = pd.DataFrame([input_data])

    input_df = pd.get_dummies(input_df)

    input_df = input_df.reindex(
        columns=features,
        fill_value=0
    )

    prediction = model.predict(input_df)[0]

    result_colors = {
        "Low": "#ff8c9b",
        "Average": "#ffd580",
        "High": "#78e6b0"
    }

    st.markdown(
        '<div class="section-heading">✦ Prediction Result</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">
            Predicted Performance Category
        </div>
        <div class="result-value"
             style="color: {result_colors[prediction]};">
            {prediction}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "Educational demonstration only. This prediction is not "
        "a definitive assessment of a student's abilities."
    )


# ================= FOOTER =================

st.markdown("""
<div class="footer">
    BUILT WITH PYTHON &nbsp; • &nbsp; STREAMLIT &nbsp; • &nbsp;
    SCIKIT-LEARN
    <br><br>
    STUDENT PERFORMANCE PREDICTOR | AI & ML PROJECT
</div>
""", unsafe_allow_html=True)
