import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

design = load_lottieurl("https://lottie.host/5e2306ce-3d2f-4ef5-bd4d-16c625a61409/UVKIHr7BjU.json")

st_lottie(design, height = 300, key="game")

def main():
    st.title("Python Resources for Learners")

    st.write(
        "Welcome to our Python resources page! Here you'll find a collection of "
        "useful Python materials to help you learn and improve your skills."
    )

    st.header("Online Courses and Tutorials")
    st.markdown(
        "- [Codecademy - Python](https://www.codecademy.com/learn/learn-python-3)"
    )
    st.markdown(
        "- [Coursera - Python for Everybody](https://www.coursera.org/specializations/python)"
    )
    st.markdown("- [edX - Introduction to Python: Absolute Beginner](https://www.edx.org/learn/python)")

    st.header("Documentation and Guides")
    st.markdown(
        "- [Official Python Documentation](https://docs.python.org/3/)"
    )
    st.markdown(
        "- [W3Schools Python Tutorial](https://www.w3schools.com/python/)"
    )
    st.markdown("- [Real Python](https://realpython.com/)")

    st.header("Interactive Platforms and Coding Practice")
    st.markdown(
        "- [HackerRank - Python Practice](https://www.hackerrank.com/domains/tutorials/10-days-of-python)"
    )
    st.markdown(
        "- [LeetCode - Python](https://leetcode.com/problemset/all/?topicSlugs=array&listId=zf7zupt)"
    )
    st.markdown(
        "- [Exercism - Python Track](https://exercism.io/tracks/python/exercises)"
    )

    st.header("Books")
    st.markdown("- [Python Crash Course by Eric Matthes](https://nostarch.com/pythoncrashcourse2e)")
    st.markdown("- [Fluent Python by Luciano Ramalho](https://www.oreilly.com/library/view/fluent-python/9781491946237/)")

    st.header("Community and Forums")
    st.markdown("- [Stack Overflow - Python](https://stackoverflow.com/questions/tagged/python)")
    st.markdown("- [Reddit - r/learnpython](https://www.reddit.com/r/learnpython/)")

if __name__ == "__main__":
    main()
