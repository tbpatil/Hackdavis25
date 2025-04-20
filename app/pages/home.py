import streamlit as st
import base64
import os
from PIL import Image
import io

# Helper to convert and rotate image to base64
def get_base64_image(image_path, rotate_angle=-90):
    image = Image.open(image_path)
    rotated_image = image.rotate(rotate_angle, expand=True)
    buffered = io.BytesIO()
    rotated_image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    return base64.b64encode(img_bytes).decode()

def render():
    image_path = os.path.join("app", "assets", "landingpic.png")
    img_base64 = get_base64_image(image_path)

    st.markdown(
        f"""
        <style>
        html, body {{
            background-color: #000000;
            font-family: Arial, sans-serif;
        }}

        .container {{
            text-align: center;
            color: white;
            padding: 40px 20px;
        }}

        .hero-img {{
            width: 100%;
            max-width: 400px;
            border-radius: 0px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }}

        .title {{
            font-size: 36px;
            font-weight: 800;
            color: white;
            margin-top: 20px;
            margin-bottom: 10px;
        }}

        .highlight {{
            color: #FFD700;
        }}

        .subtitle {{
            font-size: 16px;
            font-weight: 400;
            color: #cccccc;
            margin-top: 10px;
            max-width: 380px;
            margin-left: auto;
            margin-right: auto;
        }}

        .start-button {{
            font-size: 18px;
            background-color: #FFD700;
            border: none;
            border-radius: 18px;
            padding: 14px 32px;
            color: black;
            cursor: pointer;
            transition: 0.3s ease;
            margin-top: 40px;
            font-weight: 600;
        }}

        .start-button:hover {{
            background-color: #ffc800;
        }}
        </style>

        <div class="container">
            <img src="data:image/png;base64,{img_base64}" class="hero-img"/>
            <div class="title"><span class="highlight">Visinex</span> detect<br>retinopathy in time</div>
            <div class="subtitle">Visinex uses machine learning to detect early signs of diabetic retinopathy from retinal images, enabling faster, more accurate screening.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col = st.columns([0.33, 0.34, 0.33])[1]
    with col:
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <button class="start-button" onclick="window.location.reload()">Get Started</button>
            </div>
            <script>
            const button = window.parent.document.querySelector('.start-button');
            if (button) {{
                button.onclick = function() {{
                    fetch('/', {{
                        method: 'POST',
                        headers: {{
                            'Content-Type': 'application/x-www-form-urlencoded'
                        }},
                        body: 'streamlit_switch_page=upload'
                    }}).then(() => window.location.reload());
                }}
            }}
            </script>
            """,
            unsafe_allow_html=True
        )

    if st.button("Hidden Start", key="start", help="Hidden button to trigger session state"):
        st.session_state.page = "upload"
