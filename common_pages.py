import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

# playground - 필모추천기
# 점수를 챗 형식으로 입력받다가, 이제는 추천 좀 해주세요! 하면 추천 결과 뜨게끔 하게 하려고 함~

# def kei_recommendation():
#     # 케이데이터 가져옴
#     with open('/static/data/211103_watcha', 'rb') as fr:
#         kei_filmo = pickle.load(fr)
#     train_file = '/input/train_data.pkl' #저장되는 곳~

