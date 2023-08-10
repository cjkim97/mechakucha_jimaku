import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# 이미지 불러오기
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
        layout="wide"
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
                /* app_view 컨테이너 수정하기 */
                [data-testid="stAppViewContainer"] > section:nth-child(2) > div:nth-child(1) {{
                    padding-top : 3rem !important;
                }}

                /* sidebar 수정하기 */
                [data-testid="stSidebar"] {{
                    width : 10% !important;
                }}

                /*header 수정하기 */
                header {{
                    visibility : hidden;
                }} 

                /* footer 꾸미기 */
                footer {{
                    visibility: visible;
                    background: #2D5AF0;
                    font-family : "Nanumsquare";
                    color : #2D5AF0 !important;
                }}
            
                footer a {{
                    visibility: hidden;
                }}
                footer:after {{
                    visibility: visible; 
                    content:"ⓒ 2023. UgwayK All rights reserved";
                    font-weight: 700;
                    font-size: 15px;
                    color: #FFFFFF;
                    align-self : center;
                }}
            </style>''',unsafe_allow_html=True)