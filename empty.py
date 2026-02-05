import streamlit as st
import time 

st.header("TIME TO LEARN EMPTY TAG ")
with st.empty():

    for i in range(1,6):
        st.write(f"processing....{i}")
        time.sleep(1)

st.header("time to learn expander tag")

with st.expander("click to see details"):
    st.write("Here we are learning the expander and empty tag")