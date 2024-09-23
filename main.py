import streamlit as st

#타이틀 적용 예시
st.title('정우진 공식사이트')

#특수 이모티콘 삽입 예시
#emogi: https://streamlit-emogi-shortcodes-streamlit-app-gwck.streamlit.app/
st.title('스마일 :sunglasses:')

# header 적용
st.header('헤더는 섹션의 제목 :sparkles:')

#subheader 적용
st.subheader('subheader는 섹션의 부제목')



# 캡션 적용
st.caption('            )

# 코드 표시
sample_code = '''
def function():
    print('hello, world')
    '''
st.code(sample_code, language="python")

 # 일반 텍스트
st.text('일반적인 텍스트를 입력해 보았습니다.')
           
