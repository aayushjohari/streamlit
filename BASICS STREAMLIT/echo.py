import streamlit as st
import time

with st.echo():
    x = 10
    y = 20
    st.write("Sum is:", x + y)


with st.echo():
    name = "Aayush"
    age = 21
    st.write(f"My name is {name} and I am {age} years old")



age = st.number_input("Enter your age", min_value=0)

if age < 18:
    st.warning("You are not eligible")
    st.stop()

st.success("You are eligible")
