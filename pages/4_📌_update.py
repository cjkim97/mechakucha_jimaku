import streamlit as st

from utils import set_background_main, set_sidebar, setting_session_state,initialize_playground_session

set_background_main()
set_sidebar()
setting_session_state()
initialize_playground_session()

# 요소 스타일링
st.markdown(f"""
            <style> 
                h3 {{
                    font-family : 'NanumBarunGothic' !important;
                    font-size : 1.2rem;
                }}
                [data-testid="stText"] {{
                    font-family : 'NanumBarunGothic' !important;
                }}
            </style>""", unsafe_allow_html=True)


st.title('🛠️ 엉터리 자막 보관소 Update Log')

st.subheader('📌 v2.3.1 release 2023.08.14')
st.text('⚡offair) 전체보기/완결작 보기 필터링 기능 추가')
st.text('💄offair) 필터링/정렬 기능 UI 선택형으로 변경')
st.text('📃update 메뉴 생성')
st.text('ㅤ')


st.subheader('📌 v1.2 release 2023.08.13')
st.text('⚡playground) 다나카케이 필모 추천기 활성화')
st.text('ㅤ')

st.subheader('📌 v0.2 release 2023.08.12')
st.text('⚡onair) 최근 업데이트 기록 반영')
st.text('ㅤ')

st.subheader('📌 v0.1 release 2023.08.11')
st.text('📃onair/offair/playground 메뉴 생성')
st.text('⚡offair) 과거순/최신순 정렬 기능 추가')