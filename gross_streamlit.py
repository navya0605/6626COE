import streamlit as st
st.title("gross salary calculation")
salary=st.number_input('enter salary',min_value=1000,step=10)
if st.button("get gross salary"):
    if salary<=10000:
        HRA=salary*67/100
        DA=salary*73/100
    elif 10000<salary<=20000:
        HRA = salary * 69 / 100
        DA = salary * 76 / 100
    else:
        HRA = salary * 73 / 100
        DA = salary * 89 / 100
GS = HRA + DA + salary
if st.button("calculate gs"):
    st.text(f'gross salary is {GS}')