#FASTAPI (SQLite)

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime, timezone, timedelta
import sqlite3
from DB_Chapter_15 import DatabaseManager

app = FastAPI(title="SQLite Database API", version="1.0.0")

# Pydantic models for request and response validation
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    created_at: datetime = datetime.now(timezone(timedelta(hours=+8)))  # Set to current time in Eastern Time

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    created_at: datetime = datetime.now(timezone(timedelta(hours=+8)))  # Set to current time in Eastern Time

class PostCreate(BaseModel):
    user_id: int
    title: str
    content: str
    created_at: datetime = datetime.now(timezone(timedelta(hours=+8)))  # Set to current time in Eastern Time

class PostResponse(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    created_at: datetime = datetime.now(timezone(timedelta(hours=+8)))  # Set to current time in Eastern Time

class PostResponseForUser(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime = datetime.now(timezone(timedelta(hours=+8)))  # Set to current time in Eastern Time

#Initializing the database manager
db = DatabaseManager()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the SQLite Database API", "version": "1.0.0"}

@app.post("/users/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user in the database."""
    try:
        user_id = db.create_user(user.name, user.email, user.age)
        if user_id:
            return {"message": "User created successfully", "user_id": user_id}
        else:    
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Failed to create user. Email already exists."
            )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while creating the user: {str(e)}"
        )

@app.get("/users/", response_model=List[UserResponse])
async def get_all_users():
    """Retrieve all users from the database."""
    try:
        users = db.get_all_users()
        return [
            UserResponse(
                id=user[0],
                name=user[1],
                email=user[2],
                age=user[3],
                created_at=user[4]
            ) 
            for user in users
        ]
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while retrieving users: {str(e)}"
        )

app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """Retrieve a user by their ID."""
    try:
        with sqlite3.connect(db.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User not found."
            ) 
        
        return UserResponse(
            id=user[0],
            name=user[1],
            email=user[2],
            age=user[3],
            created_at=user[4]
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while retrieving the user: {str(e)}"
        )

@app.post("/posts/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate):
    """Create a new post for a user."""
    try:
        #Check if the user exists before creating the post
        with sqlite3.connect(db.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (post.user_id,))
            user = cursor.fetchone()
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="Failed to create post. User ID does not exist."
                )

        post_id = db.create_post(post.user_id, post.title, post.content)
        if post_id:
            return {"message": "Post created successfully", "post_id": post_id}
        else:    
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Failed to create post. User ID does not exist."
            )
    
    except HTTPException:
        raise    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while creating the post: {str(e)}"
        )

@app.get("/users/{user_id}/posts/", response_model=List[PostResponseForUser])
async def get_user_posts(user_id: int):
    """Retrieve all posts for a specific user."""
    try:
        #Check if the user exists before retrieving posts
        with sqlite3.connect(db.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="User not found."
                )

        posts = db.get_user_posts(user_id)
        return [
            PostResponseForUser(
                id=post[0],
                title=post[1],
                content=post[2],
                created_at=post[3]
            ) 
            for post in posts
        ]
    
    except HTTPException:
        raise    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while retrieving the user's posts: {str(e)}"
        )

@app.get("/posts/", response_model=List[PostResponse])
async def get_all_posts():
    """Retrieve all posts from the database."""
    try:
        with sqlite3.connect(db.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
            posts = cursor.fetchall()
        return [
            PostResponse(
                id=post[0],
                user_id=post[1],
                title=post[2],
                content=post[3],
                created_at=post[4]
            ) 
            for post in posts
        ]
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while retrieving posts: {str(e)}"
        )

@app.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    """Retrieve a post by its ID."""
    try:
        with sqlite3.connect(db.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
            post = cursor.rowcount == 0 and None or cursor.fetchone()

        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Post not found."
            ) 
        
        return PostResponse(
            id=post[0],
            user_id=post[1],
            title=post[2],
            content=post[3],
            created_at=post[4]
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while retrieving the post: {str(e)}"
        )   
    
@app.delete("/posts/{post_id}", response_model=dict)
async def delete_post(post_id: int):
    """Delete a post by its ID."""
    try:
        with sqlite3.connect(db.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
            post = cursor.rowcount == 0 and None or cursor.fetchone()  
            if not post:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="Post not found."
                )   
        
        success = db.delete_post(post_id)
        if success:    
            return {"message": "Post deleted successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Failed to delete post. Post ID does not exist."
            )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while deleting the post: {str(e)}"
        )

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):    
    """Delete a user by their ID."""
    try:
        with sqlite3.connect(db.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="User not found."
                )   
        success = db.delete_user(user_id)
        if success:
            return {"message": "User deleted successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Failed to delete user. User ID does not exist."
            )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while deleting the user: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
