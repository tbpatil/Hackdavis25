# app/pages/landing.py
import streamlit as st
from PIL import Image

def render():
    image_path = "app/assets/landingpic.png"
    image = Image.open(image_path)
    rotated_image = image.rotate(-90, expand=True)

    # Show retina image rotated
    st.image(rotated_image, use_column_width=True)

    # Styled content block
    st.markdown("""
        <div style="padding: 30px 20px;">
            <h1 style="font-size: 2.8em; font-weight: 900;">
                <span style="color: #FFD700;">Visinex</span> detect<br>
                rethinopathy<br>in time
            </h1>
            <p style="font-size: 1.1em; color: #CCCCCC; margin-top: 20px;">
                Visinex uses machine learning to detect early signs of diabetic retinopathy from retinal images,
                enabling faster, more accurate screening.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Streamlit-native button (handled by st.button)
    if st.button("Get Started", key="start_button"):
        st.session_state.page = "profile"
        st.rerun()
