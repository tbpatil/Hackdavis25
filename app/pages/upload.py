import streamlit as st
import os
from model.predict import predict_image
from gemini_principal.gemini.summary_generator import generate_short_summary, generate_detailed_summary
from datetime import datetime

def render():
    # 📤 Centered title
    st.markdown("<h1 style='color: white; text-align: center;'>📤 Upload a retina image</h1>", unsafe_allow_html=True)

    # ⬇️ Centered instruction text
    st.markdown("""
        <p style="font-size: 1.2em; text-align: center; color: #ccc; margin-top: 10px;">
            Please take a high resolution picture of your eye
        </p>
    """, unsafe_allow_html=True)

    # ⬛ Custom uploader styling
    st.markdown("""
        <style>
        section[data-testid="stFileUploader"] {
            background-color: #A9A9A9;
            padding: 1em;
            border-radius: 12px;
            margin: 1.5em auto;
            max-width: 600px;
        }

        section[data-testid="stFileUploader"] label {
            color: black !important;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload", type=["jpg", "jpeg", "png"], key="file_uploader")

    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        temp_path = "temp.jpg"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        # ⬛ Centered analyze button
        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            if st.button("Analyze"):
                with st.spinner("Running prediction..."):
                    stage, probs = predict_image(temp_path)
                    confidence = max(probs)

                    # Gather user info from session
                    user_info = {
                        "name": st.session_state.get("user_name", "The Patient"),
                        "years_with_diabetes": st.session_state.get("diabetes_years", "N/A"),
                        "treatments": st.session_state.get("treatments", []),
                        "symptoms": st.session_state.get("symptoms", [])
                    }

                    short_summary, _ = generate_short_summary(stage, confidence, user_info=user_info)
                    detailed_summary, _ = generate_detailed_summary(stage, confidence, user_info)

                    scan_entry = {
                        "summary": short_summary,
                        "stage": stage,
                        "image": temp_path,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }

                    # Update scan history
                    if "scan_history" not in st.session_state:
                        st.session_state.scan_history = []
                    st.session_state.scan_history.append(scan_entry)

                    st.session_state.predicted_stage = stage
                    st.session_state.confidence = confidence
                    st.session_state.short_summary = short_summary
                    st.session_state.detailed_summary = detailed_summary
                    st.session_state.scan_count = st.session_state.get("scan_count", 0) + 1

                    st.session_state.page = "result"
                    st.rerun()
