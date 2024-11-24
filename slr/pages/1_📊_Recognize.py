import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(
    page_title="Recogize - Sign Language Recognizer",
    page_icon="👀",
    initial_sidebar_state="collapsed",
)

styles = {
    "nav": {
        "background-color": "var(--background-color)"
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "var(--text-color)",
        "border-radius": "0.5rem",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "var(--secondary-background-color)",
    },
    "hover": {
        "background-color": "var(--secondary-background-color)",
    },
}
options = {
    "show_sidebar": False,
}

page = st_navbar(["Home", "Recognize", "History"], selected="Recognize", styles=styles, options=options)

if page == "Home":
    st.switch_page("0_🏠_Home.py")
if page == "History":
    st.switch_page("pages/2_🔢_History.py")

