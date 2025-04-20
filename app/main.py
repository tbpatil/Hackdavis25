import streamlit as st
from pages import home, upload, result
from dotenv import load_dotenv
import os

# ✅ Load Gemini API key from .env file at startup
load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
    st.error("🚨 Missing GEMINI_API_KEY in your .env file!")
    st.stop()

# 🔁 Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# 🚦 Page Router
if st.session_state.page == "home":
    home.render()
elif st.session_state.page == "upload":
    upload.render()
elif st.session_state.page == "result":
    result.render()
