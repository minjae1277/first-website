import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

# 버튼 클릭
button = st.button('버튼을 눌러보세요')
if button:
  st.write(':blue[버튼]이 눌렸습니다 :sparkles:')







#파일 다운로드 버튼
#샘플 데이터 생성
# Dateeframe이란, pandas라이브러리에서 제공하는 2차원 데이터  구조(액셀과 유사)
dateframe = pd.Dateframe({
  'first column': ['kor''eng''math''science'],
  'second column': [10,20,30,40]
})

#다운로드 버튼 연결
st.download_button(
    label='CSV로 성적표 다운로드',
    data=dataframe.to_csv(),   # dataframe을 csv 형태로 변환
    file_name_='sample.csv',
    mime='text/csv'            #데이터 유형
)