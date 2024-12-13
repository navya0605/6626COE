#take salary from user
#take 3 shopping bills
#display total shopping amount
#% of amount spent on shopping feom salary
import streamlit as st
st.title("shopping percentage")
salary=st.number_input("give the salary",min_value=500,step=100)
bill1=st.number_input("give bill 1",min_value=100,step=10)
bill2=st.number_input("give bill 2",min_value=100,step=10)
bill3=st.number_input("give bill 3",min_value=100,step=10)
total_shopping_amount = bill1 + bill2 + bill3
percentage = total_shopping_amount / salary * 100
if st.button("total salary"):
    st.text(f"total shopping amount is {total_shopping_amount}")
if st.button("shopping percentage"):
    st.text(f" total shopping percentage is {percentage}%")