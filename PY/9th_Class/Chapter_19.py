# import streamlit as st
# import datetime

# st.title("Chapter 19: Streamlit Web App Personal Dashboard")

# #sidebar for inputs
# st.sidebar.header("User Information")

# name = st.sidebar.text_input("Enter your name:")
# age = st.sidebar.number_input("Enter your age:", min_value=1, max_value=120, value=25)
# favorite_color = st.sidebar.color_picker("Favourite Colour", "#FF6B6B")
# hobbies = st.sidebar.multiselect(
#     "Your Hobbies", ["Reading", "Traveling", "Cooking", "Sports", "Music", "Gaming"],
#     default=["Reading", "Traveling"]
# )

# #Main content
# if name:
#     st.header(f"Welcome, {name}!")
    
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.metric("Age", f"{age} years")
    
#     with col2:
#         st.metrics("Hobbies", len(hobbies))
    
#     with col3:
#         birth_year = datetime.datetime.now().year - age
#         st.metric("Birth Year", birth_year)

# #Display hobbies
# if hobbies:
#     st.subheader("Your Hobbies:")
#     for hobby in hobbies:
#         st.write(f"- {hobby}")

# #Fun fact
#     st.subheader("Fun Fact:")
#     days_lived = age * 365
#     st.write(f"You have lived approximately {days_lived} days!")

# else:
#     st.warning("Please enter your name in the sidebar to see your personalized dashboard.")



#STREAMLIT (MONGO)

from time import strftime

from time import strftime

import requests
import streamlit as st
import re
import pandas as pd
from datetime import datetime
import json

#configure the page
st.set_page_config(
    page_title="MongoDB Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

#API base URL (assuming FastAPI backend is running on localhost:8001)
api_base_url = "http://localhost:8001"

def check_api_connection():
    """Check if the FASTAPI server is running"""
    try:
        response = requests.get(f"{api_base_url}/health")
        if response.status_code == 200:
            return True
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
    return False

def create_user(name, email, age):
    """Create a new user via API."""
    try: 
        response = requests.post(
            f"{api_base_url}/users/", 
            json={"name": name, "email": email, "age": age})
        
        if response.status_code == 201:
            return response.json(), True
        else:
            return {"detail": response.text}, False
    except Exception as e:
        return {"detail": str(e)}, False
  
def create_post(user_id, title, content):
    """Create a new post for a user via API."""
    try:
        response = requests.post(
            f"{api_base_url}/posts/", 
            json={"user_id": user_id, "title": title, "content": content})
        
        if response.status_code == 201:
            return response.json(), True
        else:
            return {"detail": response.text}, False
    except Exception as e:
        return {"detail": str(e)}, False

def get_all_users():
    """Retrieve all users from API."""
    try:
        response = requests.get(f"{api_base_url}/users/")
        if response.status_code == 200:
            return response.json(), True
        else:
            st.error(f"Failed to fetch users: {response.text}")
    except Exception as e:
        st.error(f"Error fetching users: {e}")
    return [], False

def get_user_posts(user_id):
    """Retrieve all posts for a specific user via API."""
    try:
        response = requests.get(f"{api_base_url}/users/{user_id}/posts")
        if response.status_code == 200:
            return response.json(), True
        else:
            st.error(f"Failed to fetch posts: {response.text}")
    except Exception as e:
        st.error(f"Error fetching posts: {e}")
    return [], False

def get_all_posts_from_users(users):
    """Helper to get all posts across all users for the dashboard."""
    all_posts = []
    for user in users:
        posts, success = get_user_posts(user['id'])
        if success:
            all_posts.extend(posts)
    return all_posts, True

def put_user_email(user_id, email):
    """Update a user's email via API."""
    try:
        response = requests.put(
            f"{api_base_url}/users/{user_id}/email",
            json={"email": email}
        )
        if response.status_code == 200:
            return response.json(), True
        else:
            return {"detail": response.text}, False
    except Exception as e:
        return {"detail": str(e)}, False

def put_user_age(user_id, age):
    """Update a user's age via API."""
    try:
        response = requests.put(
            f"{api_base_url}/users/{user_id}/age",
            json={"new_age": age}  # Needs to match API
        )
        if response.status_code == 200:
            return response.json(), True
        else:
            return {"detail": response.text}, False
    except Exception as e:
        return {"detail": str(e)}, False

def delete_user(user_id):
    """Delete a user via API."""
    try:
        response = requests.delete(f"{api_base_url}/users/{user_id}")
        if response.status_code == 200 or response.status_code == 204:
            return {}, True
        else:
            return {"detail": response.text}, False
    except Exception as e:
        return {"detail": str(e)}, False

def delete_post(post_id):
    """Delete a post via API."""
    try:
        response = requests.delete(f"{api_base_url}/posts/{post_id}")
        if response.status_code == 200 or response.status_code == 204:
            return {}, True
        else:
            return {"detail": response.text}, False
    except Exception as e:
        return {"detail": str(e)}, False

def main():
    st.title("MongoDB Dashboard with FastAPI Backend")
    st.markdown("This dashboard allows you to interact with a MongoDB database through a FastAPI backend. You can create, read, update, and delete users and their posts.")

    #Check API connection
    if not check_api_connection():
        st.error("Cannot connect to API. Please ensure the FastAPI server is running on localhost:8001.")
        st.info("Run: `uvicorn Chapter_18:app --port 8001` in the 'PY/8th Class' folder to start the FastAPI server.")
        return
    
    st.success("Connected to API successfully!")

    #Sidebar for navigation
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Dashboard", "Users", "Posts"]
        )
    if page == "Dashboard":
        dashboard_page()
    
    elif page == "Users":
        user_page()
    
    elif page == "Posts":
        post_page()

def user_page():
    st.header("User Management")
    
    #Create tabs for different user operations
    tab1, tab2, tab3, tab4 = st.tabs(["Create User", "View Users", "Update User", "Delete User"])

    with tab1:
        st.subheader("Create a New User")
        with st.form("create_user_form"):
            col1, col2 = st.columns(2)
            with col1:  
                name = st.text_input("Name", placeholder="Enter your name")
                email = st.text_input("Email", placeholder="Enter your email")
            with col2:
                age = st.number_input("Age", min_value=1, max_value=120, value=25)
            
            submitted = st.form_submit_button("Create User", type="primary")

            if submitted:
                if name and email:
                    result, success = create_user(name, email, age)
                    if success:
                        st.success(f"User '{name}' created successfully! ID: {result['id']}")
                        st.rerun()
                    else:
                        st.error(f"Failed to create user: {result.get('detail', 'Unknown error')}")
                else:
                    st.warning("Please fill in all fields to create a user.")
    
    with tab2:
        st.subheader("View All Users")
        users, success = get_all_users()

        if users and success:
            #Convert list of users to DataFrame for better display
            df = pd.DataFrame(users)
            st.dataframe(df)

            #Display users in a nice table
            st.dataframe(
                df[["id", "name", "email", "age", "created_at"]],
                use_container_width=True,
                hide_index=True
            )

            #Show user count
            st.info(f"Total Users: {len(users)}")
        else:
                st.info("No users found.")

    with tab3:
        st.subheader("Manage User Information")
        users, success = get_all_users()

        if users and success:
            #Select user to update
            user_options = {f"{user['name']} ({user['email']})": user['id'] for user in users}
            selected_user = next(user for user in users if user['id'] == st.selectbox("Select User to Update", options=list(user_options.values()), format_func=lambda x: next(key for key, value in user_options.items() if value == x)))

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Update User**")
                with st.form("update_user_form"):
                    new_email = st.text_input("New Email", value=selected_user['email'])
                    new_age = st.number_input("New Age", min_value=1, max_value=120, value=selected_user['age'])

                    if st.form_submit_button("Update User", type="primary"):
                       result, success = put_user_email(selected_user['id'], new_email)
                       if success:
                           st.success("User information updated successfully!")
                           st.rerun()
                       else:
                           st.error(f"Failed to update user: {result.get('detail', 'Unknown error')}")
                        
                    if st.form_submit_button("Update Age", type="secondary"):
                        result, success = put_user_age(selected_user['id'], new_age)
                        if success:
                            st.success("User information updated successfully!")
                            st.rerun()
                        else:
                            st.error(f"Failed to update user: {result.get('detail', 'Unknown error')}")

            with col2:
                st.write("**Delete User**")
                st.warning("Deleting a user will also delete all their posts. This action cannot be undone.")
                if st.button("Delete User", type="primary"):
                    # Basic delete implementation
                    result, success = delete_user(selected_user['id'])
                    if success:
                        st.success("User deleted successfully!")
                        st.rerun()
                    else:
                        st.error(f"Failed to delete user: {result.get('detail', 'Unknown error')}")

def post_page():
    st.header("Post Management")

    #Create tabs for different post operations
    tab1, tab2, tab3 = st.tabs(["Create Post", "View Posts", "Manage Post"])

    with tab1:
        st.subheader("Create a New Post")
        users, user_success = get_all_users()

        #Get users for dropdown selection
        if users and user_success:
            user_options = {f"{user['name']} ({user['email']})": user['id'] for user in users}
            selected_user_display = st.selectbox("Select User for Post", options=list(user_options.values()), format_func=lambda x: next(key for key, value in user_options.items() if value == x))

            with st.form("create_post_form"):
                title = st.text_input("Post Title", placeholder="Enter post title")
                content = st.text_area("Post Content", placeholder="Enter post content")
                submitted = st.form_submit_button("Create Post", type="primary")

            if submitted:
                if selected_user_display and title and content:
                    user_id = selected_user_display
                    result, success = create_post(user_id, title, content)
                    if success:
                        st.success(f"Post '{title}' created successfully!")
                        st.rerun()
                    else:
                      st.error(f"Failed to create post: {result.get('detail', 'Unknown error')}")
                else:
                   st.warning("Please fill in all fields to create a post.")
        else:
            st.info("No users found. Please create a user before creating posts.")

    with tab2:
        st.subheader("View User Posts")
        
        users, users_success = get_all_users()
        posts, success = get_all_posts_from_users(users) if users_success else ([], False)

        if success and posts:
            for post in posts:
                with st.expander(f"{post['title']} (by {post['user_id'][:8]}...)"):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**Content** {post['content']}")
                        st.caption(f"**Created At**: {post['created_at']}"), strftime("%Y-%m-%d %H:%M:%S")
                    with col2:
                        st.write(f"**User_ID:** {post['user_id'][:8]}... **")     
                        if st.button("Delete Post", key=f"delete_{post['id']}", type="primary"):
                            # Basic delete implementation
                            result, success = delete_post(post['id'])
                            if success:
                                st.success("Post deleted successfully!")
                                st.rerun()
                            else:
                                st.error(f"Failed to delete post: {result.get('detail', 'Unknown error')}")   
                
            st.info(f"Total Posts: {len(posts)}")
        else:
            st.info("No posts found.")
        
        with tab3:
            st.subheader("Post by User")

            users, users_sucess = get_all_users()

            if users and users_sucess:
                user_options = {f"{user['name']} ({user['email']})": user['id'] for user in users}
                selected_user_display = st.selectbox("Select User to View Posts", options=list(user_options.values()), format_func=lambda x: next(key for key, value in user_options.items() if value == x))

                if selected_user_display:
                    user_id = selected_user_display
                    posts, success = get_user_posts(user_id)

                    if success and posts:
                        for post in posts:
                            # To display the name instead of ID, we can reverse lookup or use the formatted value
                            display_name = next(key for key, value in user_options.items() if value == user_id)
                            with st.expander(f"{post['title']} (by {display_name})"):
                                st.write(f"**Content**: {post['content']}")
                                st.caption(f"**Created At**: {post['created_at']}"), strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        st.info("No posts found for this user.")
            else:
                st.info("No users found. Please create a user before viewing posts.")

def dashboard_page():
    st.header("Dashboard Overview")
    st.markdown("This dashboard provides an overview of users and posts in the MongoDB database. Use the navigation sidebar to manage users and posts.")

    #Get data for dashboard metrics
    users, users_success = get_all_users()
    posts, posts_success = get_all_posts_from_users(users) if users_success else ([], False)

    if users_success and posts_success:
        #Metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Users", len(users))

        with col2:
            st.metric("Total Posts", len(posts))

        with col3:
            avg_age = sum(user['age'] for user in users) / len(users) if users else 0
            st.metric("Average User Age", f"{avg_age:.1f} years")

        with col4:
            posts_per_user = len(posts) / len(users) if users else 0
            st.metric("Average Posts per User", f"{posts_per_user:.1f}")

        st.markdown("### Recent Users")
        recent_users = sorted(users, key=lambda x: x['created_at'], reverse=True)
        for user in recent_users[:5]:
            st.write(f"- {user['name']} ({user['email']}) - Age: {user['age']} - Created At: {user['created_at']}")
    else:
        st.info("No data available to display on the dashboard.")

        #Charts
        if users:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("User Age Distribution")
                age_data = [user['age'] for user in users]
                st.bar_chart(pd.Series(age_data).value_counts().sort_index())

            with col2:
                st.subheader("Recent Activity")
                if posts:
                    #Post by date
                    posts_df = pd.DataFrame(posts)
                    posts_df['date'] = pd.to_datetime(posts_df['created_at']).dt.date
                    daily_posts = posts_df.groupby('date').size()
                    st.line_chart(daily_posts)
                
        #Recent posts
        st.subheader("Recent Posts")
        if posts:
            recent_posts = sorted(posts, key=lambda x: x['created_at'], reverse=True)
            for post in recent_posts[:5]:
                st.write(f". **{post['title']}** - {pd.to_datetime(post['created_at']).strftime('%Y-%m-%d %H:%M:%S')} - User ID: {post['user_id'][:8]}...")
        else: 
            st.info("No posts found to display.")
    
if __name__ == "__main__":
    main()