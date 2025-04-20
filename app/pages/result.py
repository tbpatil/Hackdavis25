import streamlit as st
import sys
import os

# Add the parent 'app' directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','gemini_principal')))
from model.predict import predict_image

def render():
    st.title("🔍 Prediction Result")

    if "image_path" not in st.session_state:
        st.warning("No image uploaded. Please go back.")
        return

    # Predict DR stage and get confidence scores
    predicted_stage, probs = predict_image(st.session_state.image_path)
    confidence = max(probs)

    st.success(f"✅ Predicted DR Level: {predicted_stage}")
    st.write(f"🧠 Model Confidence: {confidence * 100:.2f}%")

    # Option to go back to home
    st.markdown("---")
    st.button("🔄 Start Over", on_click=lambda: st.session_state.update({"page": "home"}))
