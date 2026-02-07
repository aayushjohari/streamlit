import streamlit as st
from PIL import Image 

# image from path 
st.title("1. Image from path")
img = Image.open('E:\streamlit\9exs4f49l1x71.webp')
st.image(img)

# image from link
st.title("2. Image from link")
st.image('https://www.pixelstalk.net/wp-content/uploads/2016/07/Download-Free-Pictures-3840x2160.jpg')

# video from source
st.title("3. video from source ")
st.video("https://www.youtube.com/watch?v=HiIdiZfWskg")
