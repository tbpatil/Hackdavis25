import streamlit as st
from PIL import Image

def render():
    image_path = "app/assets/landingpic.png"
    image = Image.open(image_path)
    rotated_image = image.rotate(-90, expand=True)

    # Show retina image rotated
    st.image(rotated_image, use_container_width=True)

    # Styled text block
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

       # Inject style for button
    st.markdown("""
        <style>
        .center-container {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
        .stButton>button {
            background-color: #FFD700 !important;
            color: black !important;
            font-weight: 700 !important;
            font-size: 1.1em !important;
            padding: 0.75em 2em !important;
            border-radius: 12px !important;
            border: none !important;
            box-shadow: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Button inside centered div
    col1, col2, col3 = st.columns([2, 2, 1])
    with col2:
        if st.button("Get Started", key="start_button"):
            st.session_state.page = "profile"
            st.rerun()
