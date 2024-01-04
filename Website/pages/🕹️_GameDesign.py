import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

design = load_lottieurl("https://lottie.host/c93e6916-ada7-48fc-9c5b-70b99724a6d8/urXLKZNyYe.json")

st_lottie(design, height = 300, key="game")

def main():
    st.title("Game Design Resources")

    st.write(
        "Welcome to our game design resources page! Whether you're a beginner or an experienced game developer, "
        "we've curated a list of resources to help you enhance your game design skills."
    )

    st.header("Online Courses and Tutorials")
    st.markdown(
        "- [Coursera - Game Design and Development](https://www.coursera.org/specializations/game-design)"
    )
    st.markdown(
        "- [Udemy - Complete C# Unity Game Developer 3D](https://www.udemy.com/course/unitycourse/)"
    )
    st.markdown(
        "- [Pluralsight - Introduction to Game Design](https://www.pluralsight.com/courses/game-design-introduction)"
    )

    st.header("Game Engines and Tools")
    st.markdown(
        "- [Unity](https://unity.com/): A powerful and flexible game development engine."
    )
    st.markdown(
        "- [Unreal Engine](https://www.unrealengine.com/): A popular game development engine with stunning graphics capabilities."
    )
    st.markdown("- [Godot Engine](https://godotengine.org/): An open-source game engine.")

    st.header("Game Design Blogs and Websites")
    st.markdown(
        "- [Gamasutra](http://www.gamasutra.com/): The Art & Business of Making Games."
    )
    st.markdown(
        "- [Game Designing](https://www.gamedesigning.org/): Resources for game designers."
    )
    st.markdown(
        "- [Extra Credits - Game Design](https://www.youtube.com/user/ExtraCreditz): YouTube channel with insightful videos on game design."
    )

    st.header("Books")
    st.markdown(
        "- [The Art of Game Design: A Book of Lenses by Jesse Schell](https://artofgamedesign.com/)"
    )
    st.markdown("- [Rules of Play by Katie Salen and Eric Zimmerman](https://mitpress.ublish.com/book/rules-of-play)")

    st.header("Communities and Forums")
    st.markdown("- [Unity Forum](https://forum.unity.com/)")
    st.markdown("- [GameDev.net Forums](https://www.gamedev.net/forums/)")
    st.markdown("- [Reddit - r/gamedev](https://www.reddit.com/r/gamedev/)")

if __name__ == "__main__":
    main()
