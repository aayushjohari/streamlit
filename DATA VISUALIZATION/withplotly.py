import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

st.title('Visualizations with Plotly')
df = pd.read_csv('tips.csv')
st.dataframe(df.head())

st.text('1. Pie Chart')
fig = px.pie(df , values = 'total_bill', names = 'day')
st.plotly_chart(fig)