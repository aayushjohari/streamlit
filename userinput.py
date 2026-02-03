import streamlit as st

# to take the text input

st.header('Text input')
name  = st.text_input('Enter your name: ')
st.write('Hello' , name )

