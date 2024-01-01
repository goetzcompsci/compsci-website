import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "My Webpage", page_icon = ":tada", layout = "wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#--------Assets--------

lottie_coding = load_lottieurl("https://lottie.host/0297b79a-d19d-44c1-9b1e-b3976265178d/2Jatvuni8E.json")
pic = load_lottieurl("https://lottie.host/a6a1d339-432b-4235-832d-3a67bd4b9a36/nkDj1J6V4w.json")

#---------Header----------
st_lottie(pic, height = 300, key="head")
#st.set_page_config(page_title = "My Webpage", page_icon = ":tada", layout = "wide")

st.header("Welcome to the Official Computer Science Club Website")
st.write("This website will provide you will all the resources you need to succeed in coding")
st.write("Meetings will be held every ...")

st.sidebar.success("Select a page above")
#-------Body---------------
with st.container():
    st.write("---")
    left_coloumn, right_coloumn = st.columns(2)
    with left_coloumn:
        st.subheader("What do you want to explore today?")
        st.write("##")
        st.write("Choose from a variety of subjects from the side panel")
    with right_coloumn:
        st_lottie(lottie_coding, height = 300, key="coding")
        

#--------Contact Form------------------
        
with st.container():
    st.write("---")
    st.header("Email Mr.habib")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/51031@dpcdsb.mail.elearningontario.ca" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_coloumn, right_coloumn = st.columns(2)
    with left_coloumn:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_coloumn:
        st.empty()