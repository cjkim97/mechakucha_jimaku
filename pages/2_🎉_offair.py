# 현재 작업이 완료된 자막 목록이 보이는 곳
import streamlit as st
import base64
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
                /*현재 작업 완료된 작품 리스트 */
                .offair_content {{
                    display : flex;
                    flex-wrap : wrap;
                    justify-content : center;
                    margin-top : 3vw;
                    padding-left : 3vw;
                    padding-right : 3vw;
                    gap : 20px 20px;                 
                }}
                .offair_content > a {{
                    text-decoration: none;
                    display : flex;
                    flex-direction : column;
                    justify-content : space-between;
                    white-space : nowrap;
                }}
                .offair_content > a > img {{
                    width : 15rem;
                    border-radius: 1rem;
                    height : 10rem;
                }}
                .offair_content > a > p{{
                    text-align : center;
                    font-family : 'Nanumsquare';
                    color : #000000;
                    font-weight: 600;
                    font-size : 1rem;
                     z-index : 99999;
                }}
                .offair_content > a:hover {{
                    transform : scale(1.05);
                    transition : .5s;
                }}
                /* 정렬 버튼 디자인 */
                # [data-testid="stHorizontalBlock"] {{
                #     gap : 0;
                #     padding-left : 10vw;
                #     padding-right : 10vw;
                #     display : flex;
                #     align-items : flex-end;
                #     justify-content : center;
                #     flex-basis: min-content;
                # }}
                # [class='row-widget stButton']{{
                #     display : flex;
                #     justify-content : center;
                # }}
                # [class='row-widget stButton'] > button{{
                #     background : #FFFFFF;
                #     border : hidden;
                #     display : flex;
                #     align-items : flex-end;
                # }}
                # [class='row-widget stButton'] > button > div {{
                #     color : #989898;
                #     font-family : 'Nanumsquare';
                # }}
                # [class='row-widget stButton'] > button > div > p {{
                #     font-size : 1rem;
                # }}
                # [class='row-widget stButton'] > button > div:hover {{
                #     color : #000000;
                #     font-family : 'Nanumsquare';
                # }}
                # [class='row-widget stButton'] > button:hover {{
                #     transform : scale(1.1);
                #     transition : .5s;
                # }}
                # [class='row-widget stButton'] > button:active {{
                #     background : #FFFFFF;
                # }}
                # .css-1np2sqp{{
                #     width : 10px !important;
                # }}
                /* 필터링 및 정렬 선택 버튼 */
                [data-baseweb="radio"] div {{
                    font-family : 'Nanumsquare';
                }}
                [class="row-widget stRadio"] p {{
                    font-family : 'Nanumsquare';
                    font-weight : 700;
                }}
                [class="row-widget stRadio"] > label {{
                    padding-top : 10px;
                }}
            
            </style>''',unsafe_allow_html=True)

# 요소 노출

## 최신순/과거순 정렬
## 페이지 타이틀
st.title('🎉작업 종료된 작품들')
# st.markdown(f'''
#             <div class="page_title">
#                 <p> 🎉작업 종료된 작품들 </p> 
#             </div>''', unsafe_allow_html=True)
## 현재 작업 중인 작품 정보
OFFAIR_DATA = st.session_state.CONTENT_INFO[st.session_state['CONTENT_INFO']['onair']=='N'].copy()
filtering = st.radio('📌필터링', options=['전체보기', '완결작만보기'],label_visibility='visible', horizontal=True)
sorting = st.radio('📌정렬', options=['최신순', '과거순'],label_visibility='visible', horizontal=True)

if filtering == '완결작만보기':
    SORTED_DATA = OFFAIR_DATA[OFFAIR_DATA['is_full']=='Y']
else : 
    SORTED_DATA = OFFAIR_DATA

# sort1, sort2 = st.columns([1,1])
# NEW = sort1.button('최신순')
# OLD = sort2.button('과거순') #default
### 이미지 리스트 html화 하기
content_list_html = []
# if NEW : 
if sorting == '최신순':
    SORTED_DATA = SORTED_DATA.iloc[::-1,:]

for content in SORTED_DATA[['content_id', 'content_kr', 'url']].values:
    content_id, content_kr, content_url = content

    content_name = content_kr.split('~')[0]
    try : 
        with open(f'./static/images/{content_id}.jpg', 'rb') as f:
            thumbnail = f.read()
            thumbnail = (base64.b64encode(thumbnail).decode("utf-8"))
    except : # 이미지가 없으면 그냥 favicon 으로? 
         with open(f'./static/images/basic.png', 'rb') as f:
            thumbnail = f.read()
            thumbnail = (base64.b64encode(thumbnail).decode("utf-8"))
    
    content_list_html.append(f"""<a id = {content_id} href='{content_url}' title={content_kr} target="_blank"><img src="data:image/gif;base64,{thumbnail}"> <p> {content_name} </p> </a>""")

ONAIR_HTML = f'''
            <div class = "offair_content"> 
                {''.join(content_list_html)}
            </div>'''
st.markdown(ONAIR_HTML, unsafe_allow_html=True)