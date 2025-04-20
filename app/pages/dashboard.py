import streamlit as st
import base64

def _encode_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def render():
    user = st.session_state.get("user_name", "User")
    scans = st.session_state.get("scan_history", [])

    st.title(f"👋 Welcome, {user}!")
    
    st.markdown(
        f"""
        <div style="text-align:center; padding: 20px;">
            <h1 style="font-size: 48px; color: #FFD700;">📸 {len(scans)}</h1>
            <p style="color:white;">Scans completed</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.subheader("🗂️ Scans History")

    for entry in reversed(scans):
        st.markdown(f"""
        <div style="background-color: #b89f2c; padding: 16px; margin-bottom: 15px; border-radius: 20px; color: white;">
            <img src="data:image/jpg;base64,{_encode_image(entry['image'])}" width="100%" style="border-radius: 10px;" />
            <p><b>Stage:</b> {entry['stage']}</p>
            <p><b>Summary:</b> {entry['summary'][:150]}{'...' if len(entry['summary']) > 150 else ''}</p>
            <p style="font-size: 0.8em;">🕒 {entry['timestamp']}</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("📤 New Scan"):
        st.session_state.page = "upload"
        st.rerun()
