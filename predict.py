import pickle
import pandas as pd
import numpy as np
import os
from glob import glob
from utils import recommend

np.random.seed(55)

# 케이데이터 가져옴
with open(glob(r'./static/data/*watcha')[0], 'rb') as fr:
    kei_filmo = pickle.load(fr)

train_file = 'input/train_data.pkl'

# 입력 받는 부분
if not os.path.isfile(train_file):
    # 개인 스코어 테이블 제작(기존 파일이 없을 경우)
    your_score = kei_filmo[['title']].copy()
    your_score['score'] = np.nan
    your_score.index = your_score.title
    your_score = your_score[['score']]

    # 정보 받아들이는 부분
    score_ct = 0
    your_score_dict = {
        'title': [],
        'score': []
    }

    print('\n최근 작품 최소 5개에 대한 기록이 필요해요!')
    # 입력 받는 곳
    for ind,info in enumerate(kei_filmo.values):
        print(f'\n===={info[1]} - {info[0]}====')
        score = input(f'봤다면 평가(0<n<=5)를, 아직 보지 않았다면 그냥 enter, 그만두려면 n >> ')
        try:
            your_score_dict['score'].append(float(score))
            your_score_dict['title'].append(info[0])
            score_ct +=1
        except:
            if 'n' in score : 
                break
            else:
                continue

    print('\n잠시만 기다려주세요!')
    # 예측 하는 곳
    your_score_df = pd.DataFrame(your_score_dict)
    for_predict = pd.merge(kei_filmo[['title','year']], your_score_df, on='title', how='left')

    # for_predict 파일 저장
    with open(train_file, 'wb') as fw:
        pickle.dump(for_predict, fw)
else: # 파일이 있으면
    # 파일 부르기
    with open(train_file, 'rb') as fr:
        for_predict = pickle.load(fr)
        for_predict['score'] = for_predict['score'].fillna(0)
    #print(for_predict)
    input_count = len(for_predict[for_predict['score']>0])
    start = input(f"\n기존에 입력한 파일({input_count}/{len(for_predict)} 기록)이 있어요! 추가로 입력하시겠어요? y/n >> ")
    if 'n' in start.lower():
        print('\n잠시만 기다려주세요!')
    else:
        for ind,info in enumerate(for_predict.values):
            if info[-1] == 0:
                print(f'\n===={info[1]} - {info[0]}====')
                score = input(f'봤다면 평가(0<n<=5)를, 아직 보지 않았다면 그냥 enter, 그만두려면 n >> ')
                try:
                    for_predict.iloc[ind,-1] = float(score)
                except:
                    if 'n' in score.lower():
                        print('\n잠시만 기다려주세요!')
                        break
                    else:
                        continue
# 파일 저장
with open(train_file, 'wb') as fw:
    pickle.dump(for_predict, fw)
# 예측 하는 부분
# target_data 제작
train_data = pd.DataFrame(for_predict['score'].values, index = for_predict['title'].values).T
train = train_data.values
pred = recommend(train)

# 결과
pred_df = pd.DataFrame(pred, columns = train_data.columns)
pred_df = pred_df.T.sort_values(by=0,ascending=False).reset_index()

# 아직 보지 않은 작품들
no_watch = train_data.T[(train_data.T[0].isna()) |(train_data.T[0]==0)  ].index

# 5개 추천
print(f'\n아직 기록되지 않은 {len(no_watch)}개 작품 중에서 추천작 5선')
for ind,result in enumerate(pred_df[pred_df['index'].isin(no_watch)].values):
    print(f'{ind+1}) {result[0]}')
    if ind==4:
        break