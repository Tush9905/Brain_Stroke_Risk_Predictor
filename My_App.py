import streamlit as st
import pandas as pd
import joblib

st.write("# Brain Stroke Risk Predictor")
Map = {"Male" : 1, "Female" : 0, "Yes" : 1, "No" : 0, True : 1, False : 0, "never smoked" : 0, "formerly smoked" : 1, "smokes" : 2}
model = joblib.load(filename="Model.pkl")
with st.form("The Form"):
    st.write("Plese fill in your details.")
    gender = Map[st.radio(label="Gender", options=["Male", "Female"])]
    age	= st.number_input(label="Age")
    hypertension = Map[st.toggle(label="Hypertension")]
    heart_disease = Map[st.toggle(label="Heart Disease")]
    ever_married = Map[st.radio(label="Did you ever marry?", options=["Yes", "No"])]	
    avg_glucose_level = st.number_input(label="Average Glucose Level")
    Height_cm = st.number_input(label="Height in cm")
    Weight_kg = st.number_input(label="Weight in kg")
    smoking_status = Map[st.selectbox(label="Smoking Status", options=["never smoked", "formerly smoked", "smokes"])]
    Residence_type = st.selectbox(label="Residence Type", options=["Rural", "Urban"])
    Residence_type_Rural = True if Residence_type == "Rural" else False
    Residence_type_Urban = True if Residence_type == "Urban" else False
    Work = st.selectbox(label="Work", options=["Government Job", "Private Job", "Self Employed", "Never Worked", "House Wife / House Husband"])
    work_type_Govt_job	= True if Work == "Government Job" else False
    work_type_Never_worked = True if Work == "Never Worked" else False
    work_type_Private = True if Work == "Private Job" else False
    work_type_Self_employed = True if Work == "Self Employed" else False
    work_type_children = True if Work == "House Wife / House Husband" else False
    submitted = st.form_submit_button("Submit")
    if submitted == True:    
        bmi = int()
        try:   
            bmi	= Weight_kg / ((Height_cm * Height_cm)/100)
        except Exception:
            st.write("Are you sure that's your Height / Weight?")    

        pred = model.predict([[gender, age, hypertension, heart_disease, ever_married, avg_glucose_level, bmi, smoking_status, Residence_type_Rural,	Residence_type_Urban,	work_type_Govt_job,	work_type_Never_worked,	work_type_Private,	work_type_Self_employed,	work_type_children]])
        if pred == 1:
            st.write("You may be at risk of having Brain Stroke.")
        else:
            st.write("You have no risk of Brain Stroke.")
