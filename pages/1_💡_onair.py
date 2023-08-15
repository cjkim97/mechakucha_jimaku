# 현재 작업 중인 자막 목록이 보이는 곳
import streamlit as st
import base64
from datetime import datetime, timedelta
from glob import glob

from utils import set_background_main, set_sidebar, setting_session_state, initialize_playground_session

# 기본 배경 설정
set_background_main()

# # sidebar 설정
set_sidebar()

# 초기값 설정
setting_session_state()
# playground 벗어났을 경우를 대비하여 초기화
initialize_playground_session()

# 요소 디자인
st.markdown(f'''
            <style>
                /*현재 작업 중인 작품 리스트 */
                .onair_content {{
                    display : flex;
                    margin-top : 1vw;
                    margin-bottom : 3vw;
                    padding-left : 5vw;
                    padding-right : 5vw;
                }}
                .onair_content > a {{
                    text-decoration: none;
                }}
                .onair_content > a > img {{
                    width : 15rem;
                    border-radius: 20px;
                }}
                .onair_content > a > figcaption{{
                    text-align : center;
                    font-family : 'Nanumsquare';
                    color : #000000;
                    font-weight: 600;
                    font-size : 1rem;
                }}
                .onair_content > a:hover {{
                    transform : scale(1.05);
                    transition : .5s;
                }}
                /* 최근 업데이트 내역 */
                # .update_log {{              
                #     background : #F2F2F2;
                #     border-radius : 10px;
                #     margin-left : 5vw;
                #     padding-right : 2vw;
                #     margin-top : 1vw;
                #     height : 20vw;
                #     width : 80vw;
                # }}
                .update_log p{{
                    font-size : 1rem;
                    font-family : 'NanumBarunGothic';
                }}

            </style>''',unsafe_allow_html=True)

# 요소 노출
## 페이지 타이틀
st.title("💡현재 작업 중인 작품들")
# st.markdown(f'''
#             <div class="page_title">
#                 <p> 💡현재 작업 중인 작품들 </p> 
#             </div>''', unsafe_allow_html=True)

## 현재 작업 중인 작품 정보
ONAIR_DATA = st.session_state.CONTENT_INFO[st.session_state['CONTENT_INFO']['onair']=='Y'].copy()
RECENT_UPDATE = []

### 이미지 리스트 html화 하기
content_list_html = ''
for content in ONAIR_DATA[['content_id', 'content_kr', 'release_date', 'hashtag', 'url','update_date', 'last_episode']].values:
    content_id, content_kr, content_release_date, content_hashtag, content_url, update_date, last_episode = content
    y,m,d = update_date.split('.')
    # 최근 1주일 내 업데이트인 경우 가져오기~
    if datetime.today() - datetime(int(y), int(m), int(d)) < timedelta(days=7):
        RECENT_UPDATE.append([content_kr, update_date, last_episode])
        content_kr = '🆕' + content_kr
    
    with open(f'./static/images/{content_id}.gif', 'rb') as f:
        thumbnail = f.read()
        thumbnail = (base64.b64encode(thumbnail).decode("utf-8"))
    
    content_list_html += f"""<a id = {content_id} href='{content_url}' title={content_kr} target="_blank"> 
    <img src="data:image/gif;base64,{thumbnail}"> <figcaption> {content_kr}/{content_release_date} </figcaption> </a>"""

ONAIR_HTML = f'''
            <div class = "onair_content"> 
                {content_list_html}
            </div>'''
st.markdown(ONAIR_HTML, unsafe_allow_html=True)

## 최근 업데이트 내역
### 최근 1주일 내 업데이트 내역만 반영하려고 함
st.title("📌최근 업데이트 내역")
# st.markdown(f'''
#             <div class="page_title">
#                 <p> 📌최근 업데이트 내역</p> 
#             </div>''', unsafe_allow_html=True)

update_log_html = ''
for log in RECENT_UPDATE:
    update_log_html += f'<p>{log[0]}  ·······  {log[1]} {int(log[2])}화 🆕</p>'

if update_log_html : 
    recent_log = f'''<div class="update_log">{update_log_html}</div>'''
else : 
    recent_log = f'''<div class="update_log"></div>'''

st.markdown(f'{recent_log}',unsafe_allow_html=True)