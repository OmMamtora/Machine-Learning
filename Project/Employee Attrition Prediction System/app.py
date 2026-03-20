import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model_data = pickle.load(open("Employee Attrition Status.pkl", "rb"))
process = model_data["process"]
model = model_data["model"]

# ---------------- TITLE ----------------
st.title("📊 Employee Attrition Prediction System")
st.write("Predict whether an employee is likely to leave the company.")

st.divider()


# ---------------- INPUT FORM ----------------
with st.form("prediction_form"):

    st.subheader("Employee Information")

    col1, col2, col3 = st.columns(3)

    # ---------- COLUMN 1 ----------
    with col1:
        Age = st.number_input("Age", min_value=18, max_value=60, value=30)

        BusinessTravel = st.selectbox(
            "Business Travel",
            ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
        )

        DailyRate = st.number_input("Daily Rate", 100, 2000, 500)

        Department = st.selectbox(
            "Department",
            ["Sales", "Research & Development", "Human Resources"]
        )

        DistanceFromHome = st.number_input("Distance From Home", 1, 50, 10)

        Education = st.selectbox("Education Level", [1,2,3,4,5])

        EducationField = st.selectbox(
            "Education Field",
            ["Life Sciences","Medical","Marketing",
             "Technical Degree","Other","Human Resources"]
        )

    # ---------- COLUMN 2 ----------
    with col2:
        EnvironmentSatisfaction = st.slider("Environment Satisfaction",1,4,3)

        Gender = st.selectbox("Gender",["Male","Female"])

        HourlyRate = st.number_input("Hourly Rate",30,100,60)

        JobInvolvement = st.slider("Job Involvement",1,4,3)

        JobLevel = st.selectbox("Job Level",[1,2,3,4,5])

        JobRole = st.selectbox(
            "Job Role",
            ["Sales Executive","Research Scientist","Laboratory Technician",
             "Manufacturing Director","Healthcare Representative",
             "Manager","Sales Representative","Research Director",
             "Human Resources"]
        )

        JobSatisfaction = st.slider("Job Satisfaction",1,4,3)

    # ---------- COLUMN 3 ----------
    with col3:
        MaritalStatus = st.selectbox(
            "Marital Status",
            ["Single","Married","Divorced"]
        )

        MonthlyIncome = st.number_input("Monthly Income",1000,20000,5000)

        MonthlyRate = st.number_input("Monthly Rate",2000,30000,10000)

        NumCompaniesWorked = st.number_input("Companies Worked",0,10,2)

        OverTime = st.selectbox("Over Time",["Yes","No"])

        PercentSalaryHike = st.number_input("Percent Salary Hike",10,25,15)

        PerformanceRating = st.selectbox("Performance Rating",[1,2,3,4])

    st.divider()

    st.subheader("Career History")

    col4, col5 = st.columns(2)

    with col4:
        RelationshipSatisfaction = st.slider("Relationship Satisfaction",1,4,3)

        StockOptionLevel = st.selectbox("Stock Option Level",[0,1,2,3])

        TotalWorkingYears = st.number_input("Total Working Years",0,40,10)

        TrainingTimesLastYear = st.number_input("Training Times Last Year",0,10,3)

        WorkLifeBalance = st.slider("Work Life Balance",1,4,3)

    with col5:
        YearsAtCompany = st.number_input("Years At Company",0,40,5)

        YearsInCurrentRole = st.number_input("Years In Current Role",0,20,3)

        YearsSinceLastPromotion = st.number_input("Years Since Last Promotion",0,15,1)

        YearsWithCurrManager = st.number_input("Years With Current Manager",0,20,3)

    predict = st.form_submit_button("🔍 Predict Attrition")


# ---------------- DATAFRAME ----------------
input_data = pd.DataFrame({
    
    "Age":[Age],
    "BusinessTravel":[BusinessTravel],
    "DailyRate":[DailyRate],
    "Department":[Department],
    "DistanceFromHome":[DistanceFromHome],
    "Education":[Education],
    "EducationField":[EducationField],
    "EnvironmentSatisfaction":[EnvironmentSatisfaction],
    "Gender":[Gender],
    "HourlyRate":[HourlyRate],
    "JobInvolvement":[JobInvolvement],
    "JobLevel":[JobLevel],
    "JobRole":[JobRole],
    "JobSatisfaction":[JobSatisfaction],
    "MaritalStatus":[MaritalStatus],
    "MonthlyIncome":[MonthlyIncome],
    "MonthlyRate":[MonthlyRate],
    "NumCompaniesWorked":[NumCompaniesWorked],
    "OverTime":[OverTime],
    "PercentSalaryHike":[PercentSalaryHike],
    "PerformanceRating":[PerformanceRating],
    "RelationshipSatisfaction":[RelationshipSatisfaction],
    "StockOptionLevel":[StockOptionLevel],
    "TotalWorkingYears":[TotalWorkingYears],
    "TrainingTimesLastYear":[TrainingTimesLastYear],
    "WorkLifeBalance":[WorkLifeBalance],
    "YearsAtCompany":[YearsAtCompany],
    "YearsInCurrentRole":[YearsInCurrentRole],
    "YearsSinceLastPromotion":[YearsSinceLastPromotion],
    "YearsWithCurrManager":[YearsWithCurrManager]
})

# ---------------- PREDICTION ----------------
if predict:

    processed = process.transform(input_data)

    prediction = model.predict(processed)
    probability = model.predict_proba(processed)[0][1]

    st.divider()
    st.subheader("Prediction Result")

    st.metric("Attrition Probability", f"{probability*100:.2f}%")

    st.progress(probability)

    if probability > 0.7:
        st.error("⚠️ High Attrition Risk (Employee Likely to Leave)")

    elif probability > 0.4:
        st.warning("⚠️ Medium Attrition Risk")

    else:
        st.success("✅ Low Attrition Risk (Employee Likely to Stay)")