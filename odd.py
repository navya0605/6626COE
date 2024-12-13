import streamlit as st
st.title("even or odd")
num=st.number_input("enter number",min_value=1,step=1)
if st.button("even/odd"):
    if num%2==0:
        st.success("even number")
    else:
        st.error("odd number")