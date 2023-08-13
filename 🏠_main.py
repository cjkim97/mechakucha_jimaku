import streamlit as st

from utils import set_background_main, set_sidebar
from utils import get_image_base64
from utils import setting_session_state
from utils import initialize_playground_session

# 기본 배경 설정
set_background_main()

# sidebar 설정
set_sidebar()

# 초기값 설정
setting_session_state()

# playground 벗어났을 경우를 대비하여 초기화
initialize_playground_session()

# 요소 디자인
st.markdown(f'''
            <style> 
                /* 메인 타이틀 관련 */
                # .Main_title {{
                #     display : flex;
                #     justify-content : center;
                #     align-items : center;
                #     padding-top : 0;
                # }}
                # .Main_title span {{
                #     font-family : 'Nanumsquare';
                #     font-size : 2vw;
                #     font-weight : 700;
                #     white-space : nowrap;
                #     color : #808080;
                # }}
                # #title_name{{
                #     font-family: "InkLipquid";
                #     font-size : 10vw;
                #     white-space : nowrap;
                #     font-weight : 700;
                #     line-height : 1.2;
                # }}
                [class="css-10trblm e1nzilvr0"] {{
                    display : flex;
                    justify-content : center;
                    font-size : 8vw;
                }}
                h1 > div > a {{
                    display : none !important;
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
                    padding-top : 4vw;
                }}
                .Main_notice p {{
                    white-space : nowrap;
                    text-align : center;
                    font-weight : 400;
                    color : #808080;
                    font-size : 3vw;
                    font-family : 'Nanum Pen Script';
                    line-height : 1.2;
                    margin-bottom : 0;
                }}
                /* 메인 링크관련 */
                .Main_link_menu_name {{
                    margin-top : 5vw;
                }}
                .Main_link_menu_name p {{
                    white-space : nowrap;
                    text-align : center;
                    margin-bottom : 0;
                    font-family : 'Nanumsquare';
                    font-weight : 700;
                    color : #000000;
                    font-size : 1.5vw;
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
st.title('엉터리 자막 보관소 v1.2')
# st.markdown('''
#             <div class = "Main_title">
#                 <p id = "title_name"> 엉터리 자막 보관소 </p><span>v0.2</span>
#             </div>''', unsafe_allow_html=True)

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
st.markdown(f'''
            <div class = "Main_notice"> 
                <p style='font-size : 0.75vw; font-family : "Nanumsquare"; '> ※ PC 사용을 권장합니다 ※</p>
                <p> <br>공부용으로 만들었던 자막을 기록하는 장소이자,<br>끄적대며 만든 것도 남겨두는 곳</p>
                
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
    

