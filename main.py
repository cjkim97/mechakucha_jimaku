import streamlit as st
import pandas as pd
import os
from datetime import datetime

from utils import set_background_main, set_sidebar
from utils import get_image_base64

# 기본 배경 설정
set_background_main()

# sidebar 설정
set_sidebar()

# 초기값 설정
# TODAY_DATE = str(datetime.today().year) + str(datetime.today().month).zfill(2) + str(datetime.today().day).zfill(2)
DATA_PATH = './static/data/'
if 'CONTENT_INFO' not in st.session_state: # 자막 챌린지 기록 불러오기
    st.session_state['CONTENT_INFO'] = pd.read_csv(DATA_PATH + os.listdir(DATA_PATH)[0])

# 요소 디자인
st.markdown(f'''
            <style> 
                /* 메인 타이틀 관련 */
                .Main_title {{
                    display : flex;
                    justify-content : center;
                    align-items : center;
                }}
                #title_name{{
                    font-family: "InkLipquid";
                    font-size : 5vw;
                    white-space : nowrap;
                    margin-bottom : -1.5vw;
                    font-weight : 700;
                }}
                /* 메인 메뉴 관련 */
                .Main_menu {{
                    display : flex;
                    justify-content : center;
                    align-items : center;
                    gap : 2rem;
                }}
                .Main_menu > a > img {{
                    width : 10vw;
                    margin-bottom : -1vw;
                    margin-top : -2vw;
                }}
                .Main_menu > a > img:hover {{
                    transform : scale(1.1);
                    transition : .5s;
                }}
            
                /* 메인 공지 텍스트 */
                .Main_notice {{
                    display : flex;
                    flex-direction : column;
                    justify-content : center;
                    align-items : center;
                }}
                .Main_notice p {{
                    white-space : nowrap;
                    text-align : center;
                    margin-bottom : 0;
                    margin-top : 0;
                    font-weight : 700;
                    color : #808080;
                    font-size : 1.25vw;
                    font-family : 'Nanumsquare';
                }}
                /* 메인 링크관련 */
                .Main_link_menu_name p {{
                    white-space : nowrap;
                    text-align : center;
                    margin-bottom : 0;
                    margin-top : 0;
                    font-family : 'Nanumsquare';
                    font-weight : 700;
                    color : #000000;
                    font-size : 1.5vw;
                    margin-top : 2vw;
                }}
                .Main_link {{
                    display : flex;
                    justify-content : center;
                    gap : 1rem;
                }}
                .Main_link > a > img{{
                    width : 3vw ;
                    height : 3vw;
                }}
            </style>''', unsafe_allow_html=True)

# 요소 노출
# Maintitle
st.markdown('''
            <div class = "Main_title">
                <p id = "title_name"> 엉터리 자막 보관소 </p>
            </div>''', unsafe_allow_html=True)

# 자막 메뉴로 이동
onair_icon = get_image_base64('./static/icons/onair.png')
offair_icon = get_image_base64('./static/icons/offair.png')
st.markdown(f'''
            <div class = "Main_menu">
                <a id = "onair_menu_icon" href="/onair" target="_self">
                    <img src="data:img\logo_char.jpg;base64,{onair_icon}" title="현재 작업 중인 자막들"/>
                </a>
                <a id = "offair_menu_icon" href="/offair" target="_self">
                    <img src="data:img\logo_char.jpg;base64,{offair_icon}" title = "작업 완료/미완 자막들"/>
                </a>
            </div>''', unsafe_allow_html=True )

# 주요 공지사항
# st.markdown(f'''
#             <div class = "Main_notice">
#                 <p> 📌 상업적 이용 금지 📌 </p>
#                 <p> 📌 출처 삭제 금지 및 배포 지양 📌 </p>
#                 <p> 📌 의역/오역/맞춤법 오류 겁나 많음 📌 </p>
#                 <p> 📌 자막 싱크는 대부분 TVER(추출) 기준 📌 </p>
#                 <p> 📌 그저 공부용이니 허접해도 양해부탁드립니다 :) 📌 </p>
#             </div>''', unsafe_allow_html=True)
st.markdown(f'''
            <div class = "Main_notice"> 
                <p> 🤗 뭐든 재밌게 공부하는 거 좋아하는 편 🤗</p>
                <p style='font-size : 0.75vw;'> ※ PC 사용을 권장합니다 ※</p>
                
            </div>''', unsafe_allow_html=True)

# 주요 링크 아이콘
naver_blog_icon = get_image_base64('./static/icons/naver_blog.png')
github_icon = get_image_base64('./static/icons/github.png')
youtube_icon = get_image_base64('./static/icons/youtube.png')

st.markdown(f'''
            <div class = "Main_link_menu_name"> 
                <p style='font-family: "InkLipquid";'> UgwayK's Info </p>
            </div>
            <div class = "Main_link"> 
                <a id = "blog_link" href="https://blog.naver.com/PostList.naver?blogId=nuang0530_2&categoryNo=32&skinType=&skinId=&from=menu" target="_blank">
                    <img src="data:img\logo_char.jpg;base64,{naver_blog_icon}" title="잡덕의 세계♪"/>
                </a>
                <a id = "git_link" href="https://github.com/cjkim97/mechakucha_jimaku" target="_blank">
                    <img src="data:img\logo_char.jpg;base64,{github_icon}" title="Github"/>
                </a>
                <a id = "youtube_link" href="https://www.youtube.com/playlist?list=PLXITT4dvFV6euVuyJ9-6rljAA2dTzIO-W" target="_blank">
                    <img src="data:img\logo_char.jpg;base64,{youtube_icon}"; title = "일본어 조금 알아먹는 거북이"/>
                </a>
            </div>''', unsafe_allow_html=True)
    

