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
st.text('우진이 팬들을 위한 팬클럽을 만들어 보았습니다.')
           
# 마크다운 문법 지원
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
# 컬러코드: blue, green, orange, red, violet
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")

#LaTex 수식 지원
#복잡한 수학공식, 기호 등을 웹 페이지에서 깔끔한 수식으로 변환
st.latex(r'\sqrt{x^2+y^2}=1')
