import streamlit as st

st.subheader('1. Radio button')
gender=  st.radio('select your gender:  ', options=['Male' , 'Female', 'Other'], help='choose one' , horizontal=True)

st.subheader('2. Selct box')
st.selectbox('select the option:  ', options = ['ML', 'DA', 'ANN'] , help= 'choose one')

st.subheader('4. Multi-selectbox')
st.multiselect('select the option:  ', options = ['ML', 'DA', 'ANN'] , help= 'choose one')

st.subheader('4. Checkbox')
st.checkbox('I agree to the terms and conditons')

st.button('submit your response')             