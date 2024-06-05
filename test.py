import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time

st.write("hello world!")

st.warning('This is a warning', icon="⚠️")

st.success('This is a success message!', icon="✅")

#with st.spinner('Wait for it...'):
#    time.sleep(5)
#st.success('Done!')

#st.balloons()
#st.snow()

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')
    
st.image('vege.jpg', caption='균형있는 식단을 추천합니다!')    

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
