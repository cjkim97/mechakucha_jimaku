# 현재 작업이 완료된 자막 목록이 보이는 곳
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
                /*현재 작업 완료된 작품 리스트 */
                .offair_content {{
                    display : flex;
                    flex-wrap : wrap;
                    justify-content : space-start;
                    margin-bottom : 3vw;
                    # margin-top : 3vw;
                    padding-left : 5vw;
                    padding-right : 5vw;
                    gap : 20px 10px;
                    
                }}
                .offair_content > a {{
                    text-decoration: none;
                    display : flex;
                    flex-direction : column;
                    justify-content : space-between;
                }}
                .offair_content > a > img {{
                    width : 400px;
                    border-radius: 20px;
                }}
                .offair_content > a > p{{
                    text-align : center;
                    font-family : 'Nanumsquare';
                    color : #000000;
                    font-weight: 600;
                    font-size : 1rem;

                }}
                .offair_content > a:hover {{
                    transform : scale(1.05);
                    transition : .5s;
                }}
                /* 정렬 버튼 디자인 */
                [data-testid="stHorizontalBlock"] {{
                    gap : 0;
                }}
                [class='row-widget stButton'] > button{{
                    border-radius: 50px;
                    background : #D9D9D9;
                    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
                    border : hidden;
                }}
                [class='row-widget stButton'] > button > div {{
                    color : #FFFFFF;
                }}
                [class='row-widget stButton'] > button:hover {{
                    background : #2D5AF0;
                    transform : scale(1.1);
                    transition : .5s;
                }}
            </style>''',unsafe_allow_html=True)

# 요소 노출
## 페이지 타이틀
st.markdown(f'''
            <div class="page_title">
                <p> 🎉작업 종료된 작품들 </p> 
            </div>''', unsafe_allow_html=True)

## 최신순/과거순 정렬
sort1, sort2 = st.columns([1,25])
NEW = sort1.button('최신순')
OLD = sort2.button('과거순')
## 현재 작업 중인 작품 정보
OFFAIR_DATA = st.session_state.CONTENT_INFO[st.session_state['CONTENT_INFO']['onair']=='N'].copy()
values = OFFAIR_DATA.values

### 이미지 리스트 html화 하기
content_list_html = []
if NEW : 
    values = OFFAIR_DATA.values[::-1]
if OLD : 
    values = OFFAIR_DATA.values

for content in values:
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

    try : 
        with open(f'./static/images/{content_id}.jpg', 'rb') as f:
            thumbnail = f.read()
            thumbnail = (base64.b64encode(thumbnail).decode("utf-8"))
    except : # 이미지가 없으면 그냥 favicon 으로? 
         with open(f'./static/images/basic.png', 'rb') as f:
            thumbnail = f.read()
            thumbnail = (base64.b64encode(thumbnail).decode("utf-8"))
    
    content_list_html.append(f"""<a id = {content_id} href='#' title={content_kr}><img src="data:image/gif;base64,{thumbnail}"> <p> {content_kr} </p> </a>""")

ONAIR_HTML = f'''
            <div class = "offair_content"> 
                {''.join(content_list_html)}
            </div>'''
st.markdown(ONAIR_HTML, unsafe_allow_html=True)