import streamlit as st

st.header("Goals")
st.subheader("This page is meant to let Mr.Habib know what your goals and expectations are with this club")
st.write("Please only submit one response")

st.write("---")

name = st.text_input("What is your name and grade?")

goal = st.text_input("What is your main subject of interest in terms of coding: ", " ")

experience = st.select_slider(
    'Select a color of the rainbow',
    options=['beginner', 'little experience', 'intermediate', 'advanced', 'Mr. Habib level'])


languages = st.multiselect(
    'Which languages do you know',
    ['Python', 'Java', 'JS', 'C++'])


note = st.text_input("Is there anything else you think Mr.Habib should know about?")

message = f'{name}, {goal}, {experience}, {languages}, {note}'

st.write(message)
