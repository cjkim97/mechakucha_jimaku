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
                /*현재 작업 중인 작품 리스트 */
                .onair_content {{
                    display : flex;
                    margin-bottom : 3vw;
                    margin-top : 3vw;
                    padding-left : 5vw;
                    padding-right : 5vw;
                }}
                .onair_content > a {{
                    text-decoration: none;
                }}
                .onair_content > a > img {{
                    width : 400px;
                    border-radius: 20px;
                }}
                .onair_content > a > figcaption{{
                    text-align : center;
                    font-family : 'Nanumsquare';
                    color : #808080;
                    font-weight: 600;
                }}
                .onair_content > a:hover {{
                    transform : scale(1.05);
                    transition : .5s;
                }}
                /* 최근 업데이트 내역 */
                .update_log {{
                    background : #F2F2F2;
                    border-radius : 10px;
                    padding-left : 2vw;
                    padding-top : 1vw;
                    height : 10vw;
                }}
                .update_log p{{
                    font-size : 1.5vw;
                }}

            </style>''',unsafe_allow_html=True)

# 요소 노출
## 페이지 타이틀
st.markdown(f'''
            <div class="page_title">
                <p> 💡현재 작업 중인 작품들 </p> 
            </div>''', unsafe_allow_html=True)

## 현재 작업 중인 작품 정보
ONAIR_DATA = st.session_state.CONTENT_INFO[st.session_state['CONTENT_INFO']['onair']=='Y'].copy()

### 이미지 리스트 html화 하기
content_list_html = ''
for content in ONAIR_DATA.values:
    # 0 content_id
    # 1 content_kr
    # 2 content_jp
    # 3 release_date
    # 4 hashtag
    # 5 onair
    # 6 is_full
    # 7 detail
    # 8 OTT
    # 9 maker
    content_id = content[0]
    content_kr = content[1]
    content_release_date = content[3]
    content_hashtag = content[4]

    with open(f'./static/images/{content_id}.gif', 'rb') as f:
        thumbnail = f.read()
        thumbnail = (base64.b64encode(thumbnail).decode("utf-8"))
    
    content_list_html += f"""<a id = {content_id} href='#' title={content_kr}> 
    <img src="data:image/gif;base64,{thumbnail}"> <figcaption> {content_kr}/{content_release_date} </figcaption> </a>"""

ONAIR_HTML = f'''
            <div class = "onair_content"> 
                {content_list_html}
            </div>'''
st.markdown(ONAIR_HTML, unsafe_allow_html=True)

## 최근 업데이트 내역
### 최근 1주일 내 업데이트 내역만 반영하려고 함
st.markdown(f'''
            <div class="page_title">
                <p> 📌최근 업데이트 내역 </p> 
            </div>''', unsafe_allow_html=True)
TODAY_DATE = str(datetime.today().year) + str(datetime.today().month).zfill(2) + str(datetime.today().day).zfill(2)
st.markdown(f'''<div class="update_log">
                <p>230810  ·······  Unknown </p>
            </div>''',unsafe_allow_html=True)