import streamlit as st
from PyPDF2 import PdfReader

st.title("PDF TEXT EXTRACTOR")
Uploaded_file = st.file_uploader("upload a pdf" , type = 'pdf')

if Uploaded_file is not None:
    reader = PdfReader(Uploaded_file)
    total_pages = len(reader.pages)
    st.write("total pages" , total_pages)

    text = ""
    for i in range(total_pages):
        text += reader.pages[i].extract_text()

    st.text_area(text , height=400)
        
