import streamlit as st
import random
import datetime

st.title(':sparkles:우진이 배구팀 및 경기 일정 생성기:sparkles:')

# 로또 번호 생성 함수
def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 27)
        lotto.add(number)
    lotto = list(lotto)
    lotto.sort()
    return lotto

# 경기 일정 생성 함수
def generate_schedule(teams, start_date):
    schedule = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            match_date = start_date + datetime.timedelta(days=random.randint(1, 30))  # 1~30일 랜덤
            schedule.append((teams[i], teams[j], match_date))
    return schedule

# 세션 상태 초기화
if 'teams' not in st.session_state:
    st.session_state.teams = []
if 'schedule' not in st.session_state:
    st.session_state.schedule = []
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.date.today()

# 팀 생성 버튼
button = st.button('팀 번호를 생성해 주세요!')

if button:
    st.session_state.teams = [f'팀 {i + 1}: {generate_lotto()}' for i in range(5)]
    
    st.subheader("생성된 팀:")
    for team in st.session_state.teams:
        st.write(team)

# 경기 일정 생성을 위한 시작 날짜 입력
st.session_state.start_date = st.date_input("경기 시작일 선택:", st.session_state.start_date)

# 경기 일정 생성 버튼
if st.button('경기 일정을 생성해 주세요!'):
    st.session_state.schedule = generate_schedule(st.session_state.teams, st.session_state.start_date)
    
    st.subheader("생성된 경기 일정:")
    for match in st.session_state.schedule:
        st.write(f"{match[0]} vs {match[1]} - 날짜: {match[2].strftime('%Y-%m-%d')}")

# 생성된 시각 표시
st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
