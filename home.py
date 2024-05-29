import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def bmi_range(bmi):
    if bmi >25: 
        st.warning("비만입니다.")
    elif 18.5 < bmi < 23:
        st.info("정상입니다.")
    elif 23 < bmi <25:
        st.warning("과체중입니다.")
    else:
        st.warning("저체중입니다.")
        
selected = st.sidebar.selectbox("목차", ("체질량계산기","갭마인더","국가별통계"))

if selected == "체질량계산기":    
        
    st.title("체질량지수 계산기")

    st.info("체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.")

    height = st.number_input("신장 (cm)", value = 160, step = 3)
    st.write(f"당신의 신장은 : {height} cm")

    weight = st.number_input("체중 (kg)", value = 60, step = 1)
    st.write(f"당신의 체중은 : {weight} kg")

    bmi = weight / ((height/100)**2)

    if st.button("계산하기"):
        st.write(f"당신의 체질량지수는 {round(bmi,2)} 입니다.")
        bmi_range(bmi)
        st.balloons()
        
        st.image('ss.jpeg', caption='균형있는 식단이 필요합니다.')

if selected == "갭마인더":
    st.title("갭마인더")
    
    st.write("파일 불러오기")
    data = pd.read_csv("gapminder.csv")
    
    year = st.slider("Select a Year",1952,2007,1952,step =5)
    st.write(f"{year} 년도")
    
    data = data[data["year"] == year]
    
    st.write(data)
    
    fig, ax = plt.subplots()
    ax.scatter(data["gdpPercap"],data["lifeExp"], s = data['pop']*0.000002)
    
    st.pyplot(fig)
    
if selected == "국가별통계":
    st.title("국가별통계")    