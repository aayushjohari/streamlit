import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

st.title("DATA VISUALIZATION WITH MATPLOTLIB AND SEABORN")

st.text("displaying the dataset")
df = pd.read_csv('iris_dataset.csv')
st.dataframe(df)

st.text("BAR PLOT USING MATPLOTLIB")
FIG = plt.figure(figsize=(15,8))
df['target'].value_counts().plot(kind='bar')
st.pyplot(FIG)

st.text("distplot using seaborn")
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal length (cm)'])
st.pyplot(fig)

st.text("Multiple graphs")
col1 , col2 = st.columns(2)

with col1:
    st.write("KDE - FALSE")
    fig1 = plt.figure()
    sns.distplot(df["sepal length (cm)"], kde=False)
    st.pyplot(fig1)

with col2:
    st.write("HIST - FALSE")
    fig2 = plt.figure()
    sns.distplot(df["sepal length (cm)"], hist=False)
    st.pyplot(fig2)

st.text("Chnanging the styles of the graphs")
col1 , col2 = st.columns(2)

with col1:
    # st.write("KDE - FALSE")
    fig1 = plt.figure()
    sns.set_theme(style="darkgrid", context='poster')
    g =sns.displot(df["petal length (cm)"], kind="kde")
    st.pyplot(g.figure)

with col2:
    # st.write("HIST - FALSE")
    fig2 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context("notebook")
    g =sns.displot(df["petal length (cm)"], kind="hist")
    st.pyplot(g.figure)

st.text("Count plot")
fig = plt.figure(figsize=(15,8))
sns.countplot(data=df , x ='target')
st.pyplot(fig)


st.text("Box Plot")
fig = plt.figure(figsize=(15,8))
sns.boxplot(data=df , x='target' , y = 'petal length (cm)', palette='coolwarm')
st.pyplot(fig)