import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

design = load_lottieurl("https://lottie.host/13d77e78-3b44-473f-8b88-42c896052df7/HUAKWOIYUO.json")

st_lottie(design, height = 300, key="game")

def main():
    st.title("Java Resources for Learners")

    st.write(
        "Welcome to our Java resources page! Here you'll find a collection of "
        "useful Java materials to help you learn and improve your skills."
    )

    st.header("Online Courses and Tutorials")
    st.markdown(
        "- [Codecademy - Learn Java](https://www.codecademy.com/learn/learn-java)"
    )
    st.markdown(
        "- [Coursera - Java Programming and Software Engineering Fundamentals](https://www.coursera.org/specializations/java-programming)"
    )
    st.markdown(
        "- [edX - Introduction to Java: Programming and Software Engineering Fundamentals](https://www.edx.org/learn/java)"
    )

    st.header("Documentation and Guides")
    st.markdown(
        "- [Official Java Documentation](https://docs.oracle.com/en/java/)"
    )
    st.markdown(
        "- [W3Schools Java Tutorial](https://www.w3schools.com/java/)"
    )
    st.markdown("- [Baeldung - Java Guides](https://www.baeldung.com/)")

    st.header("Interactive Platforms and Coding Practice")
    st.markdown(
        "- [HackerRank - Java Practice](https://www.hackerrank.com/domains/tutorials/10-days-of-java)"
    )
    st.markdown(
        "- [LeetCode - Java](https://leetcode.com/problemset/all/?topicSlugs=java&listId=2wpw8j)"
    )
    st.markdown(
        "- [Exercism - Java Track](https://exercism.io/tracks/java/exercises)"
    )

    st.header("Books")
    st.markdown("- [Effective Java by Joshua Bloch](https://www.oreilly.com/library/view/effective-java/9780134686097/)")
    st.markdown("- [Java: The Complete Reference by Herbert Schildt](https://www.oracle.com/java/technologies/javase/javaref.html)")

    st.header("Community and Forums")
    st.markdown("- [Stack Overflow - Java](https://stackoverflow.com/questions/tagged/java)")
    st.markdown("- [Reddit - r/javahelp](https://www.reddit.com/r/javahelp/)")

if __name__ == "__main__":
    main()
