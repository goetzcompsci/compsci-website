import streamlit as st

def display_intro():
    st.title("CCC Waterloo Coding Competition Prep")
    st.write(
        "Welcome to the CCC Waterloo Coding Competition preparation page! "
        "Here, you'll find resources and practice problems to help you prepare for the competition."
    )

def display_resources():
    st.header("Resources")
    st.markdown(
        "- [Official CCC Website](https://cemc.math.uwaterloo.ca/contests/computing.html)\n"
        "- [Previous Contest Problems](https://cemc.math.uwaterloo.ca/contests/past_contests.html#ccc)\n"
        "- [CCC Preparation Material](https://cemc.math.uwaterloo.ca/contests/computing/preparation.html)"
    )

def display_practice_problems():
    st.header("Practice Problems")
    # Replace the following with links or content related to practice problems
    st.markdown(
        "- [Problem 1](https://www.youtube.com/watch?v=bAE96sPIkjo)\n"
        "- [Problem 2](https://www.youtube.com/watch?v=hzZOcowJXbw)\n"
        "- [Problem 3](https://www.youtube.com/watch?v=GRO6H76aBFU)"
    )

def display_tips():
    st.header("Tips for Success")
    st.write(
        "1. **Understand the Basics:** Ensure you have a solid understanding of fundamental programming concepts."
        "\n\n2. **Practice Regularly:** Solve a variety of problems to improve your problem-solving skills."
        "\n\n3. **Manage Your Time:** Practice solving problems under time constraints."
    )

def main():
    display_intro()
    display_resources()
    display_practice_problems()
    display_tips()

if __name__ == "__main__":
    main()
