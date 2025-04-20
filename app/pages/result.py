import streamlit as st

def render():
    st.title(f"Stage: {st.session_state.predicted_stage}")

    if "show_details" not in st.session_state:
        st.session_state.show_details = False

    st.markdown(
        """
        <div style="background-color:#1c1c1c; padding: 20px; border-radius: 10px; color:white;">
            <h3 style="color:#FFD700;">Summary</h3>
            <p>{}</p>
        </div>
        """.format(st.session_state.short_summary),
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Learn More"):
            st.session_state.show_details = True

    with col2:
        if st.button("🔙 Back to Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()

    if st.session_state.show_details:
        st.markdown(
            """
            <div style="background-color:#1c1c1c; padding: 20px; border-radius: 10px; color:white; margin-top: 20px;">
                <h3 style="color:#FFD700;">Details</h3>
                <p>{}</p>
            </div>
            """.format(st.session_state.detailed_summary),
            unsafe_allow_html=True
        )
