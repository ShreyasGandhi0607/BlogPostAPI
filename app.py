import streamlit as st 
import requests

API_URL = "http://127.0.0.1:8000"

st.title("BlogPostAPI testing")

choice = st.sidebar.selectbox(
    "Select Action",
    ["View All Posts", "Create Post", "Update Post", "Delete Post"]
)

# ----------- View Posts -----------
if choice == "View All Posts":
    response = requests.get(f"{API_URL}/view")
    if response.status_code == 200:
        posts = response.json()
        if not posts:
            st.info("No blog posts found.")
        else:
            for pid, post in posts.items():
                st.subheader(post["title"])
                st.markdown(f"**Author:** {post['author']}")
                st.markdown(f"**Created At:** {post['created_at']}")
                st.markdown(f"**Content:** {post['content']}")
                st.markdown("---")
    else:
        st.error("Failed to fetch posts.")

elif choice == "Create Post":
    st.header("Create new Post")
    with st.form("create form"):
        title = st.text_input("Title")
        content = st.text_area("Content")
        author = st.text_input("Author")
        submit = st.form_submit_button("Create Post")

        if submit:
            payload = {
                "title" : title,
                "content" : content,
                "author" : author
            }

            response = requests.post(f"{API_URL}/create",json=payload)
            if response.status_code == 200:
                st.success("Post created sucessfully")
            else:
                st.error("Failed to create post.")

elif choice == "Update Post":
    st.header("✏️ Update Post")
    with st.form("update_form"):
        post_id = st.text_input("Post ID to Update (e.g., P001)")
        new_title = st.text_input("New Title")
        new_content = st.text_area("New Content")
        new_author = st.text_input("New Author")
        update = st.form_submit_button("Update Post")

        if update:
            update_payload = {}
            if new_title: update_payload["title"] = new_title
            if new_content: update_payload["content"] = new_content
            if new_author: update_payload["author"] = new_author

            res = requests.put(f"{API_URL}/edit/{post_id}", json=update_payload)
            if res.status_code == 200:
                st.success("Post updated successfully!")
            else:
                st.error("Update failed. Post may not exist.")

elif choice == "Delete Post":
    st.header("Delete post")

    delete_id = st.text_input("Post ID to Delete (e.g., P001)")
    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/delete/{delete_id}")
        if res.status_code == 200:
            st.success("Post deleted successfully!")
        else:
            st.error("Failed to delete post.")