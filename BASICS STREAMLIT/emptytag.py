import streamlit as st
import time 

st.set_page_config(page_title="Doing Stremlit")
# empty tag
st.header("TIME TO LEARN EMPTY TAG ")
with st.empty():

    for i in range(1,6):
        st.write(f"processing....{i}")
        time.sleep(1)


# expander tag

st.header("time to learn expander tag")

with st.expander("click to see details"):
    st.write("Here we are learning the expander and empty tag")

# # spinner tag

with st.spinner("wait for it "):
    time.sleep(5)

# prgogress bar
with st.empty():
    for i in range(100):
        time.sleep(.1)
        st.progress(i+1, text="completed")
