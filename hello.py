from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st


st.title("인사말 앱")

name = st.text_input("이름을 입력하세요")

if name:
    st.write(f"안녕하세요, {name}님! 만나서 반가워요.")

if st.button("현재 시간 보기"):
    local_time = datetime.now(ZoneInfo("Asia/Seoul"))
    current_time = local_time.strftime("%Y년 %m월 %d일 %H:%M:%S")
    st.write(f"현재 로컬 시간은 {current_time}입니다.")