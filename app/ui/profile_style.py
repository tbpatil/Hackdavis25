def inject_profile_styles():
    import streamlit as st

    st.markdown("""
        <style>
        /* Style the main dropdown box */
        .stMultiSelect > div, .stSelectbox > div {
            background-color: #333 !important;
            color: white !important;
            border-radius: 8px;
            padding: 0.5em;
        }
        
        .stButton>button {
            background-color: #FFD700 !important;
            color: black !important;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 2em;
        }

        /* Placeholder (default text like "Choose an option") */
        .css-1wa3eu0-placeholder {
            color: #ccc !important;
        }

        /* Selected item */
        .css-1n76uvr {
            color:black !important;
        }

        /* Actual dropdown options (in open menu) */
        div[data-baseweb="select"] span {
            color: black !important;
        }

        div[data-baseweb="select"] {
            background-color: #222 !important;
        }

        /* Fix the arrow dropdown */
        .stMultiSelect [data-baseweb="select"] svg {
            fill: black !important;
        }

        /* Optional: radio/checkbox label */
        label, .stRadio > label, .stCheckbox > label {
            color: black !important;
        }
        </style>
    """, unsafe_allow_html=True)
