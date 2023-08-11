import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import pandas as pd
import numpy as np
from glob import glob

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
        page_title="Mecha_Jimaku",
        page_icon=FAV,
        layout="wide",
        initial_sidebar_state='expanded'
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
                        max-height : 50vh !important;
                        # border : hidden;
                        border-bottom-style : none;
                    }}
                    [data-testid="stSidebar"] svg{{
                        display : none;
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
    if 'CONTENT_INFO' not in st.session_state: # 자막 챌린지 기록 불러오기
        st.session_state['CONTENT_INFO'] = pd.read_csv(glob(r'./static/data/content_info_*')[0])

# 예측 함수
def recommend(target, user_size = 1, film_size = 122, hidden_size = 5, steps = 1000, learning_rate = 0.01, r_lambda = 0.01):
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