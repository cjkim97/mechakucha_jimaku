# 현재 작업 중인 자막 목록이 보이는 곳
import streamlit as st
import base64
import pandas as pd
from datetime import datetime
import os

from utils import set_background_main, set_sidebar

# 기본 배경 설정
set_background_main()

# # sidebar 설정
set_sidebar()

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
                /* 놀이터 버튼 디자인 */
                [class='row-widget stButton'] > button{{
                    border-radius: 50px;
                    background : #FFFFFF;
                    border : hidden;
                    display : flex;
                    align-items : flex-end;
                }}
                [class='row-widget stButton'] > button > div {{
                    color : #000000;
                    font-family : 'InkLipquid';
                }}
                [class='row-widget stButton'] > button > div > p {{
                    font-size : 1.5rem;
                }}
                [class='row-widget stButton'] > button > div:hover {{
                    color : #8181F7;
                    font-family : 'InkLipquid';
                }}
                [class='row-widget stButton'] > button:hover {{
                    transform : scale(1.1);
                    transition : .5s;
                }}
                [class='row-widget stButton'] > button:active {{
                    background : #FFFFFF;
                }}
                /* 페이지 설명 */
                .info p {{
                    color : #989898;
                    font-family : 'Nanumsquare'
                }}
            </style>''',unsafe_allow_html=True)

# 요소 노출
## 페이지 타이틀
st.markdown(f'''
            <div class="page_title">
                <p> 🎈잡동사니(추후 기능 업데이트 예정) </p> 
            </div>''', unsafe_allow_html=True)

## 필모추천기
content_recsys = st.button('#다나카 케이 필모 추천기')
## 부연 설명
st.markdown(f'''
            <div class="info">
                <p> 분기마다 한 작품 이상 꼭 나오는 또나카 케이의 필모그래피를 추천해드립니다!</p> 
            </div>''', unsafe_allow_html=True)

### 이미지 리스트 html화 하기
