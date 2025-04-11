import streamlit as st

def set_page_config():
    st.set_page_config(page_title="Data Entry App", layout="centered")

def apply_custom_styles():
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
