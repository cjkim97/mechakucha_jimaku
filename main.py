import streamlit as st
import pandas as pd
from datetime import datetime

from utils import set_background_main

# 기본 배경 설정
set_background_main()

# 초기값 설정
TODAY_DATE = str(datetime.today().year) + str(datetime.today().month).zfill(2) + str(datetime.today().day).zfill(2)
if 'CONTENT_INFO' not in st.session_state: # 자막 챌린지 기록 불러오기
    st.session_state['CONTENT_INFO'] = pd.read_csv(f'./static/data/content_info_{TODAY_DATE}.csv')

