# ✅ FIRST Streamlit command
import streamlit as st
st.set_page_config(page_title="VISNIEX", layout="centered")

# ✅ Imports
from pages import home, upload, result, profile, dashboard, landing
from dotenv import load_dotenv
import os
from style import inject_custom_css

# ✅ Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("🚨 Missing GEMINI_API_KEY in your .env file!")
    st.stop()
else:
    print("LOADED API KEY:", API_KEY)

# ✅ Apply custom CSS
inject_custom_css()

# ✅ Initialize session state
if st.session_state.page == "main":
    landing.render()

# ✅ Navigation logic
def render_page(page):
    if page == "main":
        st.title("👁️ VISNIEX")
        st.markdown("Welcome to AI-powered Retina Diagnostics!")
        if st.button("Get Started"):
            st.session_state.page = "profile"
            st.rerun()

    elif page == "profile":
        profile.render()

    elif page == "dashboard":
        dashboard.render()

    elif page == "upload":
        upload.render()

    elif page == "result":
        result.render()

# ✅ Render selected page
render_page(st.session_state.page)
