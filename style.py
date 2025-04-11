import streamlit as st

def set_page_config():
    st.set_page_config(page_title="Data Entry App", layout="centered")

def apply_custom_styles(theme="light"):
    if theme == "dark":
        st.markdown(
            """
            <style>
            body {
                background-color: #0e1117;
                color: #fafafa;
            }
            .stButton>button {
                background-color: #1f77b4;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    elif theme == "blue":
        st.markdown(
            """
            <style>
            body {
                background-color: #e6f0ff;
                color: #000000;
            }
            .stButton>button {
                background-color: #0052cc;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        # light
        st.markdown(
            """
            <style>
            .stButton>button {
                background-color: #4CAF50;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
