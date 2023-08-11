import streamlit as st
from PIL import Image
from io import BytesIO
import pandas as pd
import base64

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
        # initial_sidebar_state='expanded'
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
                    background: #2D5AF0;
                    font-family : "Nanumsquare";
                    color : #2D5AF0 !important;
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
                    color: #FFFFFF;
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
                    # [data-testid="stSidebar"] {{
                    #     display : none;
                    # }}
                    # [data-testid="stSidebar"] > div {{
                    #     display : none;
                    # }}
                    [data-testid="stSidebar"] {{
                        z-index : 1 !important;
                    }}
                </style>''', unsafe_allow_html=True)