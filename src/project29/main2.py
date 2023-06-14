import streamlit as st
import datetime

d = st.date_input(
  "날짜를 선택하세요",
  datetime.date.today())

st.write('선택한 날짜:', d)

# streamlit 라이브러리
# 빠르고 쉽게 웹앱을 만들기 위한 라이브러리
# 앱을 만드는 미니멀한 프레임워크
# Python 을 사용해서 빠르게 프로토타입을 만들고 싶을 때 사용할 수 있다