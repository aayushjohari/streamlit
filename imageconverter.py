import streamlit as st
from PIL import Image
import os

def convert_image(img_path , new_format):
    with Image.open(img_path) as img:
        
        file_name = os.path.splitext(img_path.name)[0]
        new_name  = f"{file_name}.{new_format}"

        save_path = os.path.join(os.getcwd() , new_name)

        img = img.convert("RGB")
        img.save(save_path)
        st.success(f"✅ Image saved at: {save_path}")

st.header("Image converter")

img_path= st.file_uploader("Upload the image" , type=['png','jpeg','jpg'])

new_format= st.selectbox("output format", ['png','jpeg','jpg'])

if st.button('Convert'):
    if img_path is not None:
        convert_image(img_path , new_format)
    else:
        st.error("please upload the image")

