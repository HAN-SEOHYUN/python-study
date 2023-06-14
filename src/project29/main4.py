import streamlit as st
import time

st.title("streamlit 웹앱 만들기!")
st.header("python_study : project29")
st.write("streamlit 라이브러리는 빠르고 쉽게 웹앱을 만들기 위한 라이브러리입니다. 앱을 만드는 미니멀한 프레임워크로, Python 을 사용해서 빠르게 프로토타입을 만들고 싶을 때 사용할 수 있습니다.")

if st.button("버튼"):
  st.write("Button Clicked !")

if st.button("등록"):
  st.success("등록되었습니다.")

if st.button("로딩"):
  with st.spinner('Loading...'):
        time.sleep(3)
  st.error('오류가 발생했습니다. 관리자에게 문의하세요.')

checkbox_btn = st.checkbox('Checktbox Button')
if checkbox_btn:
  st.write('뿅')
  
checkbox_btn2 = st.checkbox('Checktbox Button2', value=True) # default 값을 true 로 줘서 선택상태
if checkbox_btn2:
  st.write('clicked !')

selected_item = st.radio("Radio 버튼", ("A", "B", "C"))

if selected_item == "A":
    st.write("A가 선택되었습니다")
elif selected_item == "B":
    st.write("B가 선택되었습니다")
elif selected_item == "C":
    st.write("C가 선택되었습니다")
    
option = st.selectbox('SelectBox',
                      ('모나', '로사', '우기', '융'))

st.write('선택된 멤버 :', option)

multi_select = st.multiselect('Multi SelectBox',
                              ['봄', '여름', '가을', '겨울'])

st.write('선택된 계절 :', multi_select)

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

