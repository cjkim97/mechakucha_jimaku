import streamlit as st

def MAIN():
    # 요소 디자인
    st.markdown(f'''
                <style>
                    /* 놀이터 버튼 디자인 */
                    [class='row-widget stButton'] > button{{
                        border-radius: 50px;
                        background : #FFFFFF;
                        border : hidden;
                        display : flex;
                        align-items : flex-end;
                    }}
                    [class='row-widget stButton'] > button > div {{
                        color : #000000;
                        font-family : 'InkLipquid';
                    }}
                    [class='row-widget stButton'] > button > div > p {{
                        font-size : 1.5rem;
                    }}
                    [class='row-widget stButton'] > button > div:hover {{
                        color : #8181F7;
                        font-family : 'InkLipquid';
                    }}
                    [class='row-widget stButton'] > button:hover {{
                        transform : scale(1.1);
                        transition : .5s;
                    }}
                    [class='row-widget stButton'] > button:active {{
                        background : #FFFFFF;
                    }}
                    /* 페이지 설명 */
                    .info p {{
                        color : #989898;
                        font-family : 'Nanumsquare'
                    }}
                </style>''',unsafe_allow_html=True)

    # 요소 노출
    ## 페이지 타이틀
    st.markdown(f'''
                <div class="page_title">
                    <p> 🎈잡동사니 </p> 
                </div>''', unsafe_allow_html=True)

    ## 필모추천기
    kei_recsys = st.button('#다나카 케이 필모 추천기(v1.2 예정)')
    if kei_recsys : 
        st.session_state['playground_page'] =  'KEI_RECSYS'
        st.experimental_rerun()
    ## 부연 설명
    st.markdown(f'''
                <div class="info">
                    <p> 분기마다 한 작품 이상 꼭 나오는 또나카 케이의 필모그래피를 추천해드립니다!</p><br> 
                </div>''', unsafe_allow_html=True)

    ## 필모추천기
    clean_tver_lyric = st.button('#TVER 일자막 정리하기(v2.2예정)')
    if clean_tver_lyric : 
        st.session_state['playground_page'] =  'CLEAN_LYRIC'
        st.experimental_rerun()
    ## 부연 설명
    st.markdown(f'''
                <div class="info">
                    <p> TVER에서 자막 추출하면 가끔 뒤집어서 나오는 경우 있지 않나요!? 그 부분, 해결해드립니다!(싱크는 안 맞을 수 있음)</p> 
                </div>''', unsafe_allow_html=True)

def KEI_RECSYS():
    back_to_main = st.button('목록으로 돌아가기')
    if back_to_main:
        st.session_state.playground_page = 'playground_main'
        st.experimental_rerun()

def CLEAN_LYRIC():
    back_to_main = st.button('목록으로 돌아가기')
    if back_to_main:
        st.session_state.playground_page = 'playground_main'
        st.experimental_rerun()
