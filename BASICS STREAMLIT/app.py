import streamlit as st

# title
st.title('THIS IS TITLE')

# header
st.header("HEADER")

# subheader
st.subheader("SUBHEADER")

# text
st.text("this the text")

# markdown
st.markdown("STREAMLIT")

# IF WE USE # WITH THE TEXT IN MARKDOWN IT WILL CONVER IT INTO HEADING
st.markdown("# HEADING1") 

# THE MORE YOU USE THE HASH , THE LESS THE SIZE OF THE HEADING
st.markdown("## HEADING2")
st.markdown("### HEADING3")
st.markdown("#### HEADING4")

# to make the statement or character bold use **(double) or __(double)
st.markdown("this is **STREAMLIT**") 
st.markdown("this is __stremlit__")

# to make statement or character italic use *(single) or _(single)
st.markdown("this is *streamlit*")
st.markdown("this is _streamlit_")

# to make statement or charcater both bold and italic use ***(triple) or ___(triple)
st.markdown("this is ***streamlit***")
st.markdown("this is ___streamlit___")

# to make th bullet points

st.markdown("""
- Python
- Machine Learning
- Streamlit
""")

st.markdown("""
1. Load Data
2. Train Model
3. Show Results
""")

st.write(range(1,10))

st.text(range(1,10))
