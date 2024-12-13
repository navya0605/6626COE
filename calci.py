import streamlit as st
st.title("basic calculator")
num1=st.number_input("enter one number",min_value=0,step=1)
num2=st.number_input('enter another number',min_value=0,step=1)
if st.button("add"):
    c=num1+num2
    st.success(c)
if st.button("minus"):
    c=num1-num2
    st.success(c)
if st.button("mul"):
    c=num1*num2
    st.success(c)
if st.button("/"):
    c=num1/num2
    st.success(c)
    if num1/0:
        st.error("cannot divide by 0")
if st.button("%"):
    c=num1%num2
    st.success(c)