def inject_dashboard_styles():
    import streamlit as st

    st.markdown("""
    <style>
    /* Page background and text color */
    .stApp {
        background-color: #0d0d0d;
        color: white;
    }

    /* Header and subheader styling */
    h1, h2, h3, h4, .stMarkdown > div > p {
        color: white;
    }

    /* Scan history box */
    .scan-card {
        background-color: #b89f2c;
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 20px;
        color: white;
    }

    /* Scan thumbnail */
    .scan-card img {
        border-radius: 10px;
    }

    /* Floating camera button */
    .floating-button {
        position: fixed;
        bottom: 70px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 10;
        background-color: #FFD700;
        border-radius: 50%;
        width: 75px;
        height: 75px;
        border: none;
        font-size: 28px;
        cursor: pointer;
    }

    /* Bottom navigation bar */
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #eeeeee;
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 12px 0;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
        z-index: 5;
    }

    .bottom-nav div {
        text-align: center;
        cursor: pointer;
        color: black;
    }

    .bottom-nav img {
        width: 24px;
    }

    .bottom-nav p {
        margin: 4px 0 0;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)
