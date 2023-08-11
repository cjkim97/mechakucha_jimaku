# 현재 작업 중인 자막 목록이 보이는 곳
import streamlit as st
import base64
import pandas as pd
from datetime import datetime
import os

from utils import set_background_main

# 기본 배경 설정
set_background_main()

# # sidebar 설정
# set_sidebar()

# 초기값 설정
DATA_PATH = './static/data/'
if 'CONTENT_INFO' not in st.session_state: # 자막 챌린지 기록 불러오기
    st.session_state['CONTENT_INFO'] = pd.read_csv(DATA_PATH + os.listdir(DATA_PATH)[0])

# 요소 디자인
st.markdown(f'''
            <style>
                /* 페이지 타이틀 */
                .page_title p {{
                    font-family: 'InkLipquid';
                    font-size : 72px;
                    white-space : nowrap;
                    font-weight : 700;
                }}
            </style>''',unsafe_allow_html=True)

# 요소 노출
## 페이지 타이틀
st.markdown(f'''
            <div class="page_title">
                <p> 🎈잡동사니 </p> 
            </div>''', unsafe_allow_html=True)

## 현재 작업 중인 작품 정보
ONAIR_DATA = st.session_state.CONTENT_INFO[st.session_state['CONTENT_INFO']['onair']=='Y'].copy()

### 이미지 리스트 html화 하기
