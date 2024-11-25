import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd

if 'histories' not in st.session_state:
    st.session_state['histories'] = []

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

page = st_navbar(["Beranda", "Rekognisi", "Riwayat"],
                 selected="Riwayat", styles=styles, options=options)

if page == "Beranda":
    st.switch_page("0_🏠_Home.py")
if page == "Rekognisi":
    st.switch_page("pages/1_📊_Recognize.py")

histories = pd.read_csv('slr/data/histories/histories.csv').to_dict('records')

for history in histories:
    st.markdown(f"## ID: {history['id']}")
    st.write(f"**Waktu:** {history['created_at']}")
    st.video(history['video_path'])
    st.write(f"**Hasil rekognisi:** {history['result']}")
