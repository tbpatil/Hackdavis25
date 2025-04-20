import streamlit as st
import os

def render():
    st.header("📤 Upload Retina Image")
    uploaded_file = st.file_uploader("Choose a retina image...", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.read())
        st.session_state.image_path = "temp.jpg"
        st.image("temp.jpg", caption="Uploaded Image", use_column_width=True)
        if st.button("Analyze"):
            st.session_state.page = "result"
