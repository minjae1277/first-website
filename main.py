import streamlit as st

#타이틀 적용 예시
st.title('정우진 팬클럽 Offecil site')

#특수 이모티콘 삽입 예시
#emogi: https://streamlit-emogi-shortcodes-streamlit-app-gwck.streamlit.app/
st.title('해피 :sunglasses:')

# header 적용
st.header(' 공식 팬클럽 사이트:sparkles:')

#subheader 적용
st.subheader('정우진에 진심인 분들만 오세요!')



# 캡션 적용
st.caption('            ')

# 코드 표시
sample_code = '''
def function():
    print('hello, world')
    '''
st.code(sample_code, language="python")

 # 일반 텍스트
st.text('일반적인 텍스트를 입력해 보았습니다.')
           
