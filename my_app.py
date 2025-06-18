import streamlit as st

st.title("안녕하세요, Streamlit!")
st.write("이것은 제가 만든 첫 번째 Streamlit 앱입니다.")

user_input = st.text_input("당신의 이름을 입력해주세요:", "이름")
st.write(f"안녕하세요, {user_input}님!")

if st.button("클릭해보세요!"):
    st.write("버튼이 클릭되었습니다!")

