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

if selected == "국가별통계":
    st.title("국가별통계")    