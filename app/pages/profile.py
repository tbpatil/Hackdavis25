import streamlit as st
from ui.profile_style import inject_profile_styles

def render():
    inject_profile_styles()

    st.title("👤 My Profile")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    sex = st.radio("Sex", ["Male", "Female", "Other"])
    has_diabetes = st.radio("Do you have diabetes?", ["Yes", "No"])
    diabetes_years = st.number_input("If yes, how many years?", min_value=0, step=1)
    treatments = st.text_input("Current treatments (comma separated)")
    symptoms = st.text_input("Vision symptoms (comma separated)")
    
    col1, col2, col3 = st.columns([3,1,2])
    with col1:
        if st.button("Update"):
            st.session_state.user_info = {
                "name": name,
                "age": age,
                "sex": sex,
                "has_diabetes": has_diabetes,
                "years_with_diabetes": diabetes_years,
                "treatments": [t.strip() for t in treatments.split(",") if t],
                "symptoms": [s.strip() for s in symptoms.split(",") if s],
            }
            st.session_state.user_name = name
            st.session_state.page = "dashboard"
            st.rerun()
