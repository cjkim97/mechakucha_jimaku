# 현재 작업이 완료된 자막 목록이 보이는 곳
import streamlit as st
import base64
from glob import glob

from utils import set_background_main, set_sidebar, setting_session_state

# 기본 배경 설정
set_background_main()

# # sidebar 설정
set_sidebar()

# 초기값 설정
setting_session_state()

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
                    justify-content : center;
                    margin-top : 3vw;
                    padding-left : 3vw;
                    padding-right : 3vw;
                    gap : 40px 40px;                 
                }}
                .offair_content > a {{
                    text-decoration: none;
                    display : flex;
                    flex-direction : column;
                    justify-content : space-between;
                }}
                .offair_content > a > img {{
                    width : 14vw;
                    border-radius: 1vw;
                    height : 9vw;
                }}
                .offair_content > a > p{{
                    text-align : center;
                    font-family : 'Nanumsquare';
                    color : #000000;
                    font-weight: 600;
                    font-size : 0.6vw;
                     z-index : 99999;
                }}
                .offair_content > a:hover {{
                    transform : scale(1.05);
                    transition : .5s;
                }}
                /* 정렬 버튼 디자인 */
                [data-testid="stHorizontalBlock"] {{
                    gap : 0;
                    padding-left : 32vw;
                    padding-right : 32vw;
                    display : flex;
                    align-items : flex-end;
                    justify-content : center;
                    flex-basis: min-content;
                }}
                [class='row-widget stButton']{{
                    display : flex;
                    justify-content : center;
                }}
                [class='row-widget stButton'] > button{{
                    border-radius: 50px;
                    background : #FFFFFF;
                    border : hidden;
                    display : flex;
                    align-items : flex-end;
                }}
                [class='row-widget stButton'] > button > div {{
                    color : #989898;
                    font-family : 'Nanumsquare';
                }}
                [class='row-widget stButton'] > button > div > p {{
                    font-size : 1.5rem;
                }}
                [class='row-widget stButton'] > button > div:hover {{
                    color : #000000;
                    font-family : 'Nanumsquare';
                }}
                [class='row-widget stButton'] > button:hover {{
                    transform : scale(1.1);
                    transition : .5s;
                }}
                [class='row-widget stButton'] > button:active {{
                    background : #FFFFFF;
                }}
                .css-1np2sqp{{
                    width : 10px !important;
                }}
            
            </style>''',unsafe_allow_html=True)

# 요소 노출

## 최신순/과거순 정렬
## 페이지 타이틀
st.markdown(f'''
            <div class="page_title">
                <p> 🎉작업 종료된 작품들 </p> 
            </div>''', unsafe_allow_html=True)
sort1, sort2 = st.columns([1,1])
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
    # 10 update_date
    # 11 url
    content_id = content[0]
    content_kr = content[1]
    content_release_date = content[3]
    content_hashtag = content[4]
    content_url = content[11]

    # cache 가 더 오래 걸리는 이유는..?
    # try :
    #     thumbnail = get_image_base64(f'./static/images/{content_id}.jpg')
    # except : # 이미지가 없을경우
    #     thumbnail = get_image_base64(f'./static/images/basic.png')

    try : 
        with open(f'./static/images/{content_id}.jpg', 'rb') as f:
            thumbnail = f.read()
            thumbnail = (base64.b64encode(thumbnail).decode("utf-8"))
    except : # 이미지가 없으면 그냥 favicon 으로? 
         with open(f'./static/images/basic.png', 'rb') as f:
            thumbnail = f.read()
            thumbnail = (base64.b64encode(thumbnail).decode("utf-8"))
    
    content_list_html.append(f"""<a id = {content_id} href='{content_url}' title={content_kr} target="_blank"><img src="data:image/gif;base64,{thumbnail}"> <p> {content_kr} </p> </a>""")

ONAIR_HTML = f'''
            <div class = "offair_content"> 
                {''.join(content_list_html)}
            </div>'''
st.markdown(ONAIR_HTML, unsafe_allow_html=True)