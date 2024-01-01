import sqlite3
import pandas as pd
import streamlit as st

conn = sqlite3.connect('blog.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS posts (author TEXT NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, date DATE NOT NULL)')

# Do not close the connection and cursor here

def add_post(author, title, content, date):
    try:
        # Insert a new row into the posts table
        c.execute('INSERT INTO posts (author, title, content, date) VALUES (?,?,?,?)', (author, title, content, date))
        # Save the changes to the database
        conn.commit()
    except sqlite3.Error as e:
        # Print the error message
        print(e)

def get_all_posts():
    try:
        # Select all the rows from the posts table
        c.execute('SELECT * FROM posts')
        # Fetch all the results
        data = c.fetchall()
        # Return the data
        return data
    except sqlite3.Error as e:
        # Print the error message
        print(e)
        # Return an empty list in case of an exception
        return []

def get_post_by_title(title):
    try:
        # Select the row from the posts table that matches the title
        c.execute('SELECT * FROM posts WHERE title=?', (title,))
        # Fetch the result
        data = c.fetchone()
        # Return the data
        return data
    except sqlite3.Error as e:
        # Print the error message
        print(e)

def delete_post(title):
    try:
        # Delete the row from the posts table that matches the title
        c.execute('DELETE FROM posts WHERE title=?', (title,))
        # Save the changes to the database
        conn.commit()
    except sqlite3.Error as e:
        # Print the error message
        print(e)

# Close the connection and cursor here, after all operations are completed

# Define HTML templates
title_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Author: {}</h6>
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""

post_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<h6>Author: {}</h6>
<h6>Date: {}</h6>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;">
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""

# Sidebar menu
menu = ["Home", "View Posts", "Add Post", "Search", "Manage"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.title("Welcome to the club blog")
    st.write("Use this blog to upload any interesting or fun things you find related to coding, or just anything in general!")
    st.write("You can view, add, search, and manage posts using the sidebar menu.")
    st.write("Enjoy!")
elif choice == "View Posts":
    st.title("View Posts")
    st.write("Here you can see all the posts in the blog.")
    # Get all the posts from the database
    posts = get_all_posts()
    # Display each post as a card
    for post in posts:
        unique_key = f"read_more_{post[1]}_{post[0]}"  # Appending author's name to ensure uniqueness
        st.markdown(title_temp.format(post[1], post[0], post[2][:50] + "..."), unsafe_allow_html=True)
        # Add a button to view the full post
        if st.button(f"Read More {post[1]}", key=unique_key):
            st.markdown(post_temp.format(post[1], post[0], post[3], post[2]), unsafe_allow_html=True)
elif choice == "Add Post":
    st.title("Add Post")
    st.write("Here you can add a new post to the blog.")
    # Create a form to get the post details
    with st.form(key="add_form"):
        author = st.text_input("Author")
        title = st.text_input("Title")
        content = st.text_area("Content")
        date = st.date_input("Date")
        submit = st.form_submit_button("Submit")
    # If the form is submitted, add the post to the database
    if submit:
        add_post(author, title, content, date)
        st.success("Post added successfully")
elif choice == "Search":
    st.title("Search")
    st.write("Here you can search for a post by title or author.")
    # Create a text input to get the search query
    query = st.text_input("Enter your query")
    # If the query is not empty, search for the matching posts
    if query:
        # Get all the posts from the database
        posts = get_all_posts()
        # Filter the posts by the query
        results = [post for post in posts if query.lower() in post[0].lower() or query.lower() in post[1].lower()]
        # Display the results
        if results:
            st.write(f"Found {len(results)} matching posts:")
            for result in results:
                unique_key = f"read_more_{result[1]}_{result[0]}"  # Appending author's name to ensure uniqueness
                st.markdown(title_temp.format(result[1], result[0], result[2][:50] + "..."), unsafe_allow_html=True)
                # Add a button to view the full post
                if st.button(f"Read More {result[1]}", key=unique_key):
                    st.markdown(post_temp.format(result[1], result[0], result[3], result[2]), unsafe_allow_html=True)
        else:
            st.write("No matching posts found")
elif choice == "Manage":
    st.title("Manage")
    st.write("Here you can delete posts or view some statistics.")
    # Create a selectbox to choose a post to delete
    titles = [post[1] for post in get_all_posts()]
    title = st.selectbox("Select a post to delete", titles)
    # Add a button to confirm the deletion
    if st.button("Delete"):
        delete_post(title)
        st.success("Post deleted successfully")
    # Create a checkbox to show some statistics
    if st.checkbox("Show statistics"):
        # Get all the posts from the database
        posts = get_all_posts()
        # Convert the posts to a dataframe
        df = pd.DataFrame(posts, columns=["author", "title", "content", "date"])
        # Display
