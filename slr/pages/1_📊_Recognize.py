import streamlit as st
from streamlit_navigation_bar import st_navbar
from uuid_extensions import uuid7str
import os
from datetime import datetime
from slr.libs import extract_frames, inference
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
                 selected="Rekognisi", styles=styles, options=options)

if page == "Beranda":
    st.switch_page("0_🏠_Home.py")
if page == "Riwayat":
    st.switch_page("pages/2_🔢_History.py")

st.title(":bar_chart: Rekognisi")

uploaded_file = st.file_uploader("Pilih Video", type=["mp4"])

frames = []

if uploaded_file is not None:
    st.video(uploaded_file)

    if st.button("Proses", type="primary"):
        file_id = uuid7str()
        file_path = os.path.join("slr", "data", "video", f"{file_id}.mp4")

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        frames = extract_frames(file_path)

        with st.spinner('Merekognisi...'):
            result = inference(frames)

        df = pd.DataFrame([{
            "id": file_id,
            "video_path": file_path,
            "result": result,
            "created_at": str(datetime.now())
        }])

        df.to_csv(os.path.join("slr", "data", "histories",
                  "histories.csv"), mode='a', index=False, header=False)

        st.write(f"Hasil: {result}")
