import streamlit as st
from PIL import Image

st.title('mainアプリ')
st.caption('これはテストアプリです')

image = Image.open('1546.png')
st.image(image,width=200)

