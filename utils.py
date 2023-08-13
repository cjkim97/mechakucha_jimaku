import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import pandas as pd
import numpy as np
from glob import glob
from google.oauth2 import service_account
from gsheetsdb import connect

import pickle

# 이미지 불러오기
@st.cache_data
def get_image_base64(img_path):
    image = Image.open(img_path)
    buffered = BytesIO()
    image.save(buffered, format="png")
    image_str = base64.b64encode(buffered.getvalue()).decode()
    return image_str

# 기본 배경 만들기
def set_background_main():
    FAV = Image.open('./static/icons/favicon.png')
    st.set_page_config(
        page_title="엉터리 자막 보관소",
        page_icon=FAV,
        layout="wide",
        initial_sidebar_state='auto'
    )
    st.markdown(f'''
            <style>
                /* 웹폰트 불러오기 */
                @import url('http://www.openhiun.com/hangul/nanumbarungothic.css');
                @import url('https://cdn.rawgit.com/moonspam/NanumSquare/master/nanumsquare.css');
                @import url(//fonts.googleapis.com/earlyaccess/nanumpenscript.css);
                .nanumpenscript * {{
                font-family: 'Nanum Pen Script', cursive;
                }}
                @font-face{{
                    font-family: 'InkLipquid';
                    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/InkLipquid.woff') format('woff');
                    font-weight: normal;
                    font-style: normal;
                }}
                /* 페이지 타이틀 */
                .page_title p {{
                    font-family: 'InkLipquid';
                    font-size : 5vw;
                    white-space : nowrap;
                    font-weight : 700;
                }}
                /* 페이지 타이틀 */
                h1 {{
                    font-family: 'InkLipquid' !important;
                    margin-bottom : 10px;
                }}
                /* vertical block */
                [data-testid="stVerticalBlock"] {{
                    gap : 0;
                }}

                /* app_view 컨테이너 수정하기 */
                [data-testid="stAppViewContainer"] > section:nth-child(2) > div:nth-child(1) {{
                    padding-top : 5vw !important;
                    padding-bottom : 5vw !important;
                }}

                /*header 수정하기 */
                header {{
                    display : none !important;
                }} 

                /* footer 꾸미기 */
                footer {{
                    visibility: visible;
                    background: #FFFFFF;
                    font-family : "Nanumsquare";
                    color : #FFFFFF !important;
                    padding-left : 0 !important;
                    z-index : 9999;
                }}
            
                footer a {{
                    display : none;
                }}
                footer:after {{
                    visibility: visible; 
                    content:"ⓒ 2023. UgwayK All rights reserved";
                    font-weight: 700;
                    font-size: 15px;
                    color: #2D5AF0;
                    align-self : center;
                    height : 2vw !important;
                }}
                body {{
                    font-family : 'Nanumsquare';
                }}
            </style>''',unsafe_allow_html=True)
    
# playground 세팅 만들기
def set_background_playground():
    FAV = Image.open('./static/icons/favicon.png')
    st.set_page_config(
        page_title="엉터리 자막 보관소",
        page_icon=FAV,
        layout="wide",
        initial_sidebar_state='auto'
    )
    st.markdown(f'''
                <style>
                    /* 웹폰트 불러오기 */
                    @import url('http://www.openhiun.com/hangul/nanumbarungothic.css');
                    @import url('https://cdn.rawgit.com/moonspam/NanumSquare/master/nanumsquare.css');
                    @import url(//fonts.googleapis.com/earlyaccess/nanumpenscript.css);
                    .nanumpenscript * {{
                        font-family: 'Nanum Pen Script', cursive;
                    }}
                    @font-face{{
                        font-family: 'InkLipquid';
                        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/InkLipquid.woff') format('woff');
                        font-weight: normal;
                        font-style: normal;
                    }}
                    /* 페이지 타이틀 */
                    h1 {{
                        font-family: 'InkLipquid' !important;
                        margin-bottom : 10px;
                    }}
                    .page_title {{
                        font-family: 'InkLipquid';
                        font-size : 2rem;
                        white-space : nowrap;
                        font-weight : 700;
                        background : #FFFFFF;
                        position : fixed;
                        margin-top : -2rem;
                        z-index : 999999;
                        width : 100%;
                    }}
                    /* footer 꾸미기 */
                    footer {{
                        visibility: visible;
                        background: #FFFFFF;
                        font-family : "Nanumsquare";
                        color : #FFFFFF !important;
                        padding-left : 0 !important;
                        z-index : 9999;
                    }}
                
                    footer a {{
                        display : none;
                    }}
                    footer:after {{
                        visibility: visible; 
                        content:"ⓒ 2023. UgwayK All rights reserved";
                        font-weight: 700;
                        font-size: 15px;
                        color: #2D5AF0;
                        align-self : center;
                        height : 2vw !important;
                    }}
                    body {{
                        font-family : 'Nanumsquare';
                    }}
                </style>''',unsafe_allow_html=True)

@st.cache_resource
def set_sidebar():
    st.markdown(f'''
                <style> 
                    /* sidebar 수정하기 */
                    [data-testid="stSidebar"] {{
                        width : 0.5vw !important;
                        background : #FFFFFF;
                        border-right-style : groove;
                        position : fixed;
                    }}
                    [data-testid="stSidebar"] ul {{
                        padding-top : 15rem;
                        max-height : 100vh !important;
                        height : 90vh !important;
                        # border : hidden;
                        border-bottom-style : none;
                    }}
                    [data-testid="stSidebar"] span{{
                        font-size : 20px;

                    }}
                    [data-testid="stSidebarNav"] a:visited {{
                        background-color: #8181F7
                    }}
                    /* sidebar 내부요소 설정하기 */
                    .main_img img{{
                        width : 200px !important;
                        border-radius: 1vw;
                        position : fixed;
                        left : 1.5rem;
                        top : 6rem;
                        z-index : 99999999999;
                    }}
                </style>''', unsafe_allow_html=True)
    thumbnail = get_image_base64('./static/images/basic.png')
    side =st.sidebar
    with side:
        side.markdown(f'''
                    <div class = "main_img"> 
                        <a href='/main' target="_self"><img id = "thumbnail" src="data:image/gif;base64,{thumbnail}"></a>
                    </div>''', unsafe_allow_html=True)

# 초기값 설정
def setting_session_state():
    # 구글시트연동 불러오기 
    credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    conn = connect(credentials=credentials)
    @st.cache_resource(ttl=600)
    def run_query(query):
        rows = conn.execute(query, headers=1)
        rows = rows.fetchall()
        return rows
    
    if 'CONTENT_INFO' not in st.session_state:
        # 챌린지 기록 불러오기
        sheet_url = st.secrets["content_info_url"]
        rows = run_query(f'SELECT * FROM "{sheet_url}"')
        st.session_state['CONTENT_INFO'] = pd.DataFrame(rows)

    if 'kei_filmo_info' not in st.session_state:
        # 케이 필모 불러오기
        sheet_url = st.secrets["kei_filmo_url"]
        rows = run_query(f'SELECT * FROM "{sheet_url}"')
        st.session_state['kei_filmo_info'] = pd.DataFrame(rows)
        st.session_state['kei_filmo_info']['score'] = 0 #input 점수 받는 것으로 채워질 예정
        st.session_state['kei_filmo_info']['check'] = 0 #check 시 1로 변경
    

    if 'input_score_cnt' not in st.session_state:
        # 작품 점수 입력 개수 카운트용
        st.session_state.input_score_cnt = 0
    
    if 'recsys_over' not in st.session_state:
        # 추천완료 여부
        st.session_state.recsys_over = False
    
    if 'input_over' not in st.session_state:
        # 입력 완료 여부
        st.session_state.input_over = False

    # playground session state
    if 'playground_page' not in st.session_state:
        st.session_state['playground_page'] = 'playground_main'
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if 'kei_icon' not in st.session_state:
        st.session_state.kei_icon = Image.open('./static/icons/kei_recsys_icon.png')
    
    if 'user_icon' not in st.session_state:
        st.session_state.user_icon = '💙'

# playground session 초기화 함수
def initialize_playground_session():
    st.session_state['playground_page'] = 'playground_main'
    st.session_state.messages = []
    st.session_state.kei_filmo_info['score']=0
    st.session_state['kei_filmo_info']['check'] = 0
    st.session_state.input_score_cnt = 0
    st.session_state.recsys_over = False
    st.session_state.input_over = False

# 예측 함수
def recommend(target, user_size = 1, film_size = 122, hidden_size = 5, steps = 1000, learning_rate = 0.01, r_lambda = 0.1):
    # random score, kei hidden
    score_hidden = np.random.normal(scale=1, size=(user_size, hidden_size))
    kei_hidden = np.random.normal(scale=1, size = (film_size, hidden_size))
    non_zeros = [(i, j, target[i, j]) for i in range(1) for j in range(122) if target[i, j] > 0]

    for step in range(steps):
        for i, j, r in non_zeros:
            # 실제 값과 예측 값의 오차
            err = r - np.matmul(score_hidden[i, :], kei_hidden[j, :].T)

            # 최적화
            score_hidden[i, :] += learning_rate * (err * kei_hidden[j, :] - r_lambda * score_hidden[i, :])
            kei_hidden[j, :] += learning_rate * (err * score_hidden[i, :] - r_lambda * kei_hidden[j, :])

    pred = np.matmul(score_hidden, kei_hidden.T)
    return pred