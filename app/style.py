import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #0d0d0d;
            color: white;
        }

        .stApp {
            background-color: #0d0d0d;
            color: white;
        }

        h1, h2, h3, h4, h5, h6, p, div {
            color: white !important;
        }

        .stButton>button {
            background-color: #FFD700;
            color: black;
            border-radius: 8px;
        }

        .stButton>button:hover {
            background-color: #e6c200;
        }
        </style>
    """, unsafe_allow_html=True)
