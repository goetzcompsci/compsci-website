import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
st.set_page_config(page_title = "My Webpage", page_icon = ":tada", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

design = load_lottieurl("https://lottie.host/8cbaa832-90fc-4ccf-abd5-11de5f88f855/iucCFV7rLo.json")

st_lottie(design, height = 300, key="web")

def main():
    st.title("Web Design Resources")

    st.write(
        "Welcome to our web design resources page! Whether you're a beginner or an experienced web designer, "
        "we've curated a list of resources to help you enhance your web design skills."
    )

    st.header("Online Courses and Tutorials")
    st.markdown(
        "- [Codecademy - Web Development](https://www.codecademy.com/learn/introduction-to-web-development)"
    )
    st.markdown(
        "- [Coursera - Full Stack Web Development](https://www.coursera.org/specializations/full-stack)"
    )
    st.markdown(
        "- [freeCodeCamp - Responsive Web Design](https://www.freecodecamp.org/learn/)"
    )

    st.header("Web Design Tools")
    st.markdown(
        "- [Figma](https://www.figma.com/): Collaborative interface design tool."
    )
    st.markdown(
        "- [Adobe XD](https://www.adobe.com/products/xd.html): Design, prototype, and share user experiences."
    )
    st.markdown("- [Canva](https://www.canva.com/): Graphic design platform.")

    st.header("Web Design Blogs and Websites")
    st.markdown(
        "- [Smashing Magazine](https://www.smashingmagazine.com/): Web design and development articles."
    )
    st.markdown(
        "- [A List Apart](https://alistapart.com/): Web design and development insights."
    )
    st.markdown(
        "- [CSS-Tricks](https://css-tricks.com/): Tips, tricks, and techniques for web designers."
    )

    st.header("Books")
    st.markdown(
        "- [Don't Make Me Think by Steve Krug](https://www.sensible.com/dmmt.html)"
    )
    st.markdown(
        "- [Responsive Web Design by Ethan Marcotte](https://www.abookapart.com/products/responsive-web-design)"
    )

    st.header("Communities and Forums")
    st.markdown("- [Stack Overflow - Web Design](https://stackoverflow.com/questions/tagged/web-design)")
    st.markdown("- [Designer News](https://www.designernews.co/)")
    st.markdown("- [Reddit - r/web_design](https://www.reddit.com/r/web_design/)")

if __name__ == "__main__":
    main()
