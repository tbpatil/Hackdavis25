import streamlit as st
import os
from model.predict import predict_image
from gemini_principal.gemini.summary_generator import generate_short_summary, generate_detailed_summary

def render():
    st.title("📤 Upload Retina Image")

    uploaded_file = st.file_uploader("Upload a retina image", type=["jpg", "jpeg", "png"], key="file_uploader")

    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        temp_path = "temp.jpg"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        if st.button("🔍 Analyze"):
            with st.spinner("Running prediction..."):
                stage, probs = predict_image(temp_path)
                confidence = max(probs)
                
                # Gather user info from session
                user_info = {
                    "name": st.session_state.get("name", "The Patient"),
                    "years_with_diabetes": st.session_state.get("diabetes_years", "N/A"),
                    "treatments": st.session_state.get("treatments", []),
                    "symptoms": st.session_state.get("symptoms", [])
}

                short_summary, _ = generate_short_summary(stage, confidence, user_info=user_info)
                from datetime import datetime

                # Store summary in history
                scan_entry = {
                    "summary": short_summary,
                    "stage": stage,
                    "image": temp_path,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
                }

                if "scan_history" not in st.session_state:
                    st.session_state.scan_history = []

                st.session_state.scan_history.append(scan_entry)
                detailed_summary, _ = generate_detailed_summary(stage, confidence, user_info)

                st.session_state.predicted_stage = stage
                st.session_state.confidence = confidence
                st.session_state.short_summary = short_summary
                st.session_state.detailed_summary = detailed_summary
                if "scan_count" not in st.session_state:
                    st.session_state.scan_count = 0
                st.session_state.scan_count += 1

                # Go to result
                st.session_state.page = "result"
                st.rerun()

