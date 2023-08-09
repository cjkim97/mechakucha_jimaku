import streamlit as st

# 기본 배경 만들기
def set_background_main():
    # FAV = Image.open('./img/favicon.png')
    st.set_page_config(
        page_title="Mecha_Jimaku",
        # page_icon=FAV,
        layout="wide",
        initial_sidebar_state="collapsed"
    )