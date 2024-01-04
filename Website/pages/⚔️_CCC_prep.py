from PIL import Image
import streamlit as st

img1 = Image.open("Images\img1")
st.title("CCC Prep")

st.subheader("This page was built to help you prepare for the CCC")
st.write("Below you will find helpful resources, such as youtube videos and past competetion questions")

with st.container():
    st.write("---")
    st.write("##")
    image_coloumn, text_coloumn = st.coloums((1, 2))
    with image_coloumn:
        st.image(img1)
    with text_coloumn:
        st.subheader("Step by step guide on how to solve previous competiton questions")
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=LGGhxbYa9v8)")
