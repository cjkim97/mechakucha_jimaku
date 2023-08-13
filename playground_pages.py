import streamlit as st
import re
import time
import pandas as pd
from utils import initialize_playground_session, recommend

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
                    /* vertical block */
                    [data-testid="stVerticalBlock"] {{
                        gap : 0;
                    }}
                    /*header 수정하기 */
                    header {{
                        display : none !important;
                    }} 
                </style>''',unsafe_allow_html=True)

    # 요소 노출
    ## 페이지 타이틀
    st.title('🎈잡동사니')

    ## 필모추천기
    kei_recsys = st.button('#다나카 케이 필모 추천기 v1.0')
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
    #요소 스타일링
    st.markdown(f'''
                <style>
                    /* header 고정 */
                    header {{
                        # background : #000000 !important;
                        height : 6rem !important;
                    }}
                    [data-testid="stToolbar"] {{
                        display : none;
                    }}
                    /* chat_input 관련 */
                    textarea::placeholder {{
                        font-family : 'Nanumsquare';
                    }}
                     /* 사용자 채팅 배경 */
                    [class="stChatMessage css-1c7y2kd eeusbqq4"] {{
                        background-color: rgba(240, 242, 246, 0.5)
                    }}
                    [class="css-bz34a4 eeusbqq2"] {{
                        border-radius: 1rem;
                    }}
                    /* 면접관 채팅 배경 */
                    [class="stChatMessage css-4oy321 eeusbqq4"] {{
                        background-color: rgba(130, 130, 247, 0.11)
                    }}
                    [data-testid="stChatMessageContent"] p {{
                        margin-right : 1rem;
                        font-family : "Nanumsquare";
                        text-wrap : wrap;
                    }}
                    [data-testid="stText"] {{
                        font-family : "Nanumsquare";
                        text-wrap : wrap;
                        word-break : keep-all;
                        margin-right : 1rem;
                    }}
                    p {{
                        font-family : "Nanumsquare";
                        font-weight : 500;
                        text-wrap : nowrap;
                    }}
                    /* 버튼 관련 */
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
                </style>''',unsafe_allow_html=True)
    
    # 타이틀
    st.markdown(f"<div class='page_title'>📽️오늘 뭐 볼까?</div>", unsafe_allow_html=True)

    # check=0 인 것만
    try :
        rec_content = st.session_state.kei_filmo_info[st.session_state.kei_filmo_info['check']==0].sample(n=1)
        st.session_state.kei_filmo_info.loc[rec_content.index[0], 'check'] = 1 # 점수를 물어본 작품은 패스하기 위해
    except : 
        with st.chat_message("assistant", avatar=st.session_state.kei_icon):
            st.markdown(f'준비된 모든 작품에 대한 입력을 마쳤어요! 이제 추천해드릴까요?')
            st.session_state.input_over = True

    if not st.session_state.messages: 
        st.session_state.messages=[
                            {
                            "role":"assistant" # 인사
                            ,"content": f"안녕하세요! 저의 많고 많은 필모들, 뭐 볼지 어려우셨죠? 간단하게 몇 작품에 별점을 매겨주신다면 제가 무슨 작품을 보면 좋을지 추천드릴게요 :) 실제로 제가 뽑은 작품이 BEST 라고 확신할 순 없으니, 재미로만 확인해주세요! "
                            },
                            {
                            "role":"assistant" # 하는 방법
                            ,"content": f"최소한 작품 5개에 점수를 매겨주셔야 추천드릴 수 있답니다! 점수는 5점 이하로(3.141592..도 좋아요!) 지유롭게 적어주세요! 단, 작품이 별로라도 0점보다는 높게 주셔야해요..😢 준비 되셨다면 저에게 하고 싶은 말 하나 남겨주시면 시작할게요!"
                            }]

    # 점수만 걸러내기 위한 정규식!
    p = re.compile("\d*\.?\d+")
    
    # 메시지 히스토리 보여주는 곳
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar= st.session_state.kei_icon if message["role"]=='assistant' else st.session_state.user_icon):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("봤던 작품에 점수를 매겨보세요!"):
        # 입력하면 history에 등록하고
        st.session_state.messages.append({"role": "user", "content": prompt})

        # 화면에 띄운다
        with st.chat_message("user", avatar= st.session_state.user_icon):
            st.markdown(prompt)
        
        # 점수를 매겼다면 cnt+1, 추천 후보에서 제외
        try :
            score = p.findall(prompt)[0] # 일반 문자면 튕겨나감
            # 정상 범위일 경우
            if eval(score) <=5 and eval(score) >0 and len(st.session_state.messages)>3 : # 정상범위 내 숫자가 아니면 튕겨나감, 첫 답변은 제외
                st.session_state.input_score_cnt +=1
                st.session_state.kei_filmo_info.loc[rec_content.index[0], 'score'] = eval(score) # 점수 입력
        except :
            pass

        # Display assistant response in chat message container
        with st.chat_message("assistant",avatar= st.session_state.kei_icon):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = f"<{rec_content['title'].values[0]}> 어땠어요? 본 작품이라면 점수(0<점수≤5)를, 아직 안 본 작품이라면 0을 입력해주세요"
    
            # 글자 입력 애니메이션 설정
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    # 필모 추천받기 버튼
    if st.session_state.input_score_cnt >=5:
        if st.button('😙이제 작품 추천해주세요!'): 
            with st.spinner('잠시만 기다려주세요! 출연한 작품이 많아서 고민되네요..🤗'): # 필모 추천
                # target_data 제작
                train_data = pd.DataFrame(st.session_state.kei_filmo_info['score'].values, index = st.session_state.kei_filmo_info['title'].values).T
                train = train_data.values
                pred = recommend(train,len(st.session_state.kei_filmo_info['score'].values) )
                # 결과
                pred_df = pd.DataFrame(pred, columns = train_data.columns)
                pred_df = pred_df.T.sort_values(by=0,ascending=False).reset_index()

                # 아직 보지 않은 작품들
                no_watch = train_data.T[(train_data.T[0].isna()) |(train_data.T[0]==0)].index

                time.sleep(4.2)
            with st.chat_message("assistant", avatar=st.session_state.kei_icon):
                st.markdown(f'짜잔🎉 BEST 5를 골라봤어요!')
    
            with st.chat_message("assistant", avatar=st.session_state.kei_icon):
                message_placeholder = st.empty()
                full_response = ''
                response = ''
                ind = 1
                for title, pred_score in pred_df[pred_df['index'].isin(no_watch)].values[:5]:
                    if pred_score > 5:
                        set_score = 5
                    elif pred_score <0:
                        set_score = 0.0
                    else :
                        set_score = pred_score
                    response += f'BEST {ind}. {title}/예상 점수:{round(set_score,2)}점' + '\n\n'
                    ind+=1

                # 글자 입력 애니메이션 설정
                for i, chunk in enumerate(response.split()):
                    if chunk =='BEST' and i>0:
                        full_response += "\n\n" + chunk + " "
                    else :
                        full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                st.session_state.recsys_over = True

        if st.session_state.recsys_over:
            if st.button('🤔 다시 추천받을래요') :
                initialize_playground_session()
                st.session_state.playground_page = 'KEI_RECSYS'
                st.experimental_rerun()
            if not st.session_state.input_over :
                if st.button('☺️ 더 입력해보고 추천받을래요') :
                    st.session_state.recsys_over = False
                    st.experimental_rerun()
            if st.button('🎈 목록으로 돌아가기'):
                initialize_playground_session()
                st.experimental_rerun()

def CLEAN_LYRIC():
    back_to_main = st.button('목록으로 돌아가기')
    if back_to_main:
        st.session_state.playground_page = 'playground_main'
        st.experimental_rerun()
