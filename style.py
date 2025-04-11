import streamlit as st

def set_page_config():
    # Setting the page title and layout
    st.set_page_config(page_title="Data Entry App", layout="centered")

def apply_custom_styles(theme_choice):
    if theme_choice == "light":
        st.markdown("""
            <style>
                body {
                    background-color: white;
                    color: black;
                }
                .stButton>button {
                    background-color: #4CAF50;
                    color: white;
                }
                .stTextInput input {
                    background-color: white;
                    color: black;
                }
                .stTextArea textarea {
                    background-color: white;
                    color: black;
                }
            </style>
        """, unsafe_allow_html=True)
    
    elif theme_choice == "dark":
        st.markdown("""
            <style>
                body {
                    background-color: #2b2b2b;
                    color: white;
                }
                .stButton>button {
                    background-color: #0066cc;
                    color: white;
                }
                .stTextInput input {
                    background-color: #3c3c3c;
                    color: white;
                }
                .stTextArea textarea {
                    background-color: #3c3c3c;
                    color: white;
                }
            </style>
        """, unsafe_allow_html=True)

    elif theme_choice == "blue":
        st.markdown("""
            <style>
                body {
                    background-color: #e0f7fa;
                    color: #006064;
                }
                .stButton>button {
                    background-color: #00838f;
                    color: white;
                }
                .stTextInput input {
                    background-color: #b2ebf2;
                    color: #006064;
                }
                .stTextArea textarea {
                    background-color: #b2ebf2;
                    color: #006064;
                }
            </style>
        """, unsafe_allow_html=True)
