# 현재 작업 중인 자막 목록이 보이는 곳
import streamlit as st

from utils import set_background_playground, set_sidebar, setting_session_state
from playground_pages import MAIN, KEI_RECSYS, CLEAN_LYRIC

# 기본 배경 설정
set_background_playground()

# sidebar 설정
set_sidebar()

# 초기값 설정
setting_session_state()

if st.session_state.playground_page == 'playground_main':
    MAIN()
elif st.session_state.playground_page == 'KEI_RECSYS':
    KEI_RECSYS()
elif st.session_state.playground_page == 'CLEAN_LYRIC':
    CLEAN_LYRIC()
