import streamlit as st
from PIL import Image
import cv2 as cv
import numpy as np 


def rotate_img(image , angle):
    img= np.array(image)
    height  , width  = img.shape[:2]
    M = cv.getRotationMatrix2D((width/2 , height/2 ),angle , 1)
    rotated_img = cv.warpAffine(img, M, (width , height))
    return rotated_img

st.title("IMAGE CONVERTER")
st.subheader("Upload an image file ")

img_file =st.file_uploader("Upload a image" , type =['png' , 'jpg', 'jpeg'])

st.subheader("rotate the image")
angle = st.slider("Chose the angle: ", -180 , 180 , 0 , 1)

if img_file is not None:
    image = Image.open(img_file)
    rotated_img  = rotate_img(image , angle)
    st.image(rotated_img)