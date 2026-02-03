import streamlit as st
from datetime import datetime
# to take the text input

st.subheader('Text input')
name  = st.text_input('Enter your name: ')
st.write('Hello' , name )

# tot ake the text area

st.subheader('2. Text area')
st.text_area('Tell me something about yourself ', height=100 , max_chars=500 , help = 'max 500 words allowed')

# to take the password
st.subheader('3. Text password')
st.text_input("enter your password: " , type='password')

# to take the numeric data 

st.subheader('4. Numeric input')
st.number_input('enter your age: ', min_value=0 , max_value=120)

# to take the date 
st.subheader('5. Date input')
today = datetime.now().date()
date = st.date_input('enter the date : ')