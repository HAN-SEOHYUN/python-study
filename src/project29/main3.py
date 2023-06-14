# Stremalit 를 사용해 선택한 날짜에 해당하는 비트코인 1일 차트를 보여주는 웹앱
import streamlit as st
import datetime
import pyupbit

d = st.date_input(
  "날짜를 선택하세요",
  datetime.date.today())
# 사용자로부터 날짜를 입력받는 date_input 위젯생성

st.write('비트코인 1일 차트')
# 제목출력

ticker = 'KRW-BTC'
#  조회할 가상화폐의 티커 심볼('KRW-BTC')을 변수 ticker에 저장

interval = 'minute60'
# 차트의 시간 간격을 지정 - 1시간 간격의 데이터

to = str(d + datetime.timedelta(days=1))
# 선택한 날짜에 하루를 더한 날짜를 문자열로 저장
# datetime.timedelta() : 특정 날짜와 시간을 계산하거나 시간 간격을 조작할 수 있다
# now = datetime.datetime.now()
# two_days_later = now + datetime.timedelta(days=2)

count = 24
# 조회할 데이터의 개수 지정 : 1일동안의 데이터를 조회하기 위해 24로 설정함

price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval, to=to, count=count)
# get_ohlcv(지정한 티커, 시간간격, 조회기간, 데이터개수)
# ohlcv (시가, 고가, 저가, 종가, 거래량) 데이터를 가져와서 price_now 변수에 저장

st.line_chart(price_now.close)
# line_chart 함수를 사용하여 종가 데이터를 시각화하여 출력