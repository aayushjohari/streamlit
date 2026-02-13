import streamlit as st
import pandas as pd
import numpy as np 

st.title("1. line chart")
chrt_data = pd.DataFrame(np.random.randn(20,4), columns=['L-1' , 'L-2', 'L-3','L-4'])
st.line_chart(chrt_data)

st.title("1.Area chart")
chrt_data = pd.DataFrame(np.random.randn(20,4), columns=['L-1' , 'L-2', 'L-3','L-4'])
st.area_chart(chrt_data)

st.title("1. BAR chart")
chrt_data = pd.DataFrame(np.random.randn(20,4), columns=['L-1' , 'L-2', 'L-3','L-4'])
st.bar_chart(chrt_data)
