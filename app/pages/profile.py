import streamlit as st

def render():
    st.title("👤 My Profile")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    sex = st.radio("Sex", ["Male", "Female", "Other"])
    has_diabetes = st.radio("Do you have diabetes?", ["Yes", "No"])
    diabetes_years = st.number_input("If yes, how many years?", min_value=0, step=1)
    treatments = st.multiselect("Current treatments", ["Insulin", "Oral medication", "Diet"])
    symptoms = st.multiselect("Choose your vision symptoms", ["Blurred vision", "Floaters", "Flashes of light", "Difficulty seeing at night"])

    if st.button("Save and Continue"):
        st.session_state.user_info = {
            "name": name,
            "age": age,
            "sex": sex,
            "has_diabetes": has_diabetes,
            "diabetes_years": diabetes_years,
            "treatments": treatments,
            "symptoms": symptoms,
        }
        st.session_state.user_name = name  
        st.session_state.page = "dashboard"
        st.rerun()
