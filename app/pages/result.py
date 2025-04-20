import streamlit as st

def render():
    # Top Back Button
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if st.button("⬅ Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()

    # Title
    st.title(f"Stage: {st.session_state.predicted_stage}")

    if "show_details" not in st.session_state:
        st.session_state.show_details = False

    # Summary Box
    st.markdown(
        f"""
        <div style="background-color:#1c1c1c; padding: 20px; border-radius: 10px; color:white;">
            <h3 style="color:#FFD700;">Summary</h3>
            <p>{st.session_state.short_summary}</p>
        </div>
        """, unsafe_allow_html=True
    )

    # ✅ Correct indentation here
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("🔍 Learn More"):
            st.session_state.show_details = True

    # Details Section (Conditional)
    if st.session_state.show_details:
        st.markdown(
            f"""
            <div style="background-color:#1c1c1c; padding: 20px; border-radius: 10px; color:white; margin-top: 20px;">
                <h3 style="color:#FFD700;">Details</h3>
                <p>{st.session_state.detailed_summary}</p>
            </div>
            """, unsafe_allow_html=True
        )
