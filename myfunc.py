import streamlit as st

def bmi_range(bmi):
    if bmi >25: 
        st.warning("비만입니다.")
    elif 18.5 < bmi < 23:
        st.info("정상입니다.")
    elif 23 < bmi <25:
        st.warning("과체중입니다.")
    else:
        st.warning("저체중입니다.")