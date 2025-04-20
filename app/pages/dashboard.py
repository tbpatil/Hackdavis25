# app/pages/dashboard.py

import streamlit as st
import base64
from ui.dashboard_style import inject_dashboard_styles

def _encode_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def render():
    inject_dashboard_styles()

    user = st.session_state.get("user_name", "User")
    scans = st.session_state.get("scan_history", [])

    # Centered welcome message
    st.markdown(f"""
        <div style="text-align:center; padding-top: 10px;">
            <h2 style="color:white;">👋 Welcome, {user}!</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="text-align:center; padding: 20px;">
            <h1 style="font-size: 48px; color: #FFD700;">📸 {len(scans)}</h1>
            <p style="color:white;">Scans completed</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🗂️ Scans History")

    if not scans:
        st.markdown(
            "<p style='text-align:center; font-size:1.2em; color:#bbb;'>No scans yet.</p>",
            unsafe_allow_html=True
        )

        # Single grey placeholder card
        st.markdown("""
            <div style="background-color: #444; padding: 16px; margin-bottom: 15px; border-radius: 20px; color: #ccc;">
                <p><b>Stage:</b> –</p>
                <p><b>Summary:</b> Scan summary will appear here after analysis.</p>
                <p style="font-size: 0.8em;">🕒 –</p>
            </div>
        """, unsafe_allow_html=True)

    for entry in reversed(scans):
        st.markdown(f"""
        <div class="scan-card">
            <img src="data:image/jpg;base64,{_encode_image(entry['image'])}" width="100%" />
            <p><b>Stage:</b> {entry['stage']}</p>
            <p><b>Summary:</b> {entry['summary'][:150]}{'...' if len(entry['summary']) > 150 else ''}</p>
            <p style="font-size: 0.8em;">🕒 {entry['timestamp']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Centered "New Scan" button (no emoji)
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("New Scan"):
            st.session_state.page = "upload"
            st.rerun()
