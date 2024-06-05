import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import myfunc as my

st.session_state.id = "김관우"
st.write(st.session_state.id, "님 반갑습니다.")
        
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
        my.bmi_range(bmi)
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
    
    
    df = pd.read_csv("gapminder.csv")
    #st.write(df)
    
    country = df['country'].unique()
    #st.write(country)
    
    options = st.multiselect(
    "국가를 선택하세요.",
    country,
    ["Korea, Rep."])

    st.write("You selected:", options[0])
    
    #x = options[0]
    
    #st.write(df[ df["country"] == x ]) 
    
    fig, ax = plt.subplots()
    for x in options:
        ax.plot(range(len(df[ df["country"] == x] ["year"])),df[ df["country"] == x] ["gdpPercap"],label=x)
        ax.legend()
        ax.set_xticks(range(len(df[df['country']==x]["pop"])),df[df['country']==x]['year'])
        ax.set_title('Population Growth')
    st.pyplot(fig)
    
    fig1, ax1 = plt.subplots()
    for x in options:
        ax1.plot(range(len(df[ df["country"] == x] ["lifeExp"])),df[ df["country"] == x] ["lifeExp"],label=x)
        ax1.legend()
        ax1.set_xticks(range(len(df[df['country']==x]['pop'])),df[df['country']==x]["year"])
        ax1.set_title('Life Expectancy')
    st.pyplot(fig1)