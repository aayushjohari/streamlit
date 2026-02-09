import streamlit as st
from PIL import Image

st.title("File uploading")

img = st.file_uploader('Upload files' , type=['png' , 'jpg', 'png'])

if img is not None:
    file_details = {'file_name': img.name , 'file.type': img.type , 'file.size':img.size}
    st.write(file_details)
    st.image(Image.open(img))