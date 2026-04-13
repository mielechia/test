#FASTAPI (Mongo)

from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from bson.objectid import ObjectId
from Mongo_Chapter_16 import DatabaseManager
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Mongo Database API", version="1.0.0")

#Pydantic model for request/response validation

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    age: int
    created_at: datetime

class PostCreate(BaseModel):
    user_id: str
    title: str
    content: str

class PostResponse(BaseModel):
    id: str
    user_id: str
    title: str
    content: str
    created_at: datetime    

class PostResponseWithUser(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime

#Initialise database
try:
    db = DatabaseManager()
except Exception as e:
    print(f"Error connecting to database: {e}")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database connection error")
    db = None

@app.on_event("startup")
async def startup_event():
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database connection error")
    print("Application startup: Database connection established")

@app.on_event("shutdown")
async def shutdown_event():
    if db is not None:
        db.close()
    print("Application shutdown: Database connection closed")  

@app.get("/")
async def root():
    return {"message": "Welcome to the Mongo Database API!, version 1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/users/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user in the database."""
    try:
        user_id = db.create_user(user.name, user.email, user.age)
        if user_id:
            return {"id": str(user_id), "message": "User created successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create user. Email may already exist.")
    except Exception as e:
        print(f"Error creating user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating user")

@app.post("/posts/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate):
    """Create a new post in the database."""
    try:
        if not ObjectId.is_valid(post.user_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format")
        
        #Check if user exists before creating post
        user = db.get_user_by_id(post.user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        post_id = db.create_post(post.user_id, post.title, post.content)
        if post_id:
            return {"id": str(post_id), "message": "Post created successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create post")
    except HTTPException:
        raise    
    except Exception as e:
        print(f"Error creating post: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating post")

@app.get("/users/", response_model=List[UserResponse])
async def get_all_users():
    """Retrieve all users from the database."""
    try:
        users = db.users_collection.find()
        return [UserResponse(
                    id=str(user["_id"]),
                    name=user["name"],
                    email=user["email"],
                    age=user["age"],
                    created_at=user["created_at"]
                ) for user in users]
    except Exception as e:
        print(f"Error retrieving users: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving users") 

@app.get("/users/{user_id}", response_model=List[UserResponse])
async def get_all_users(user_id: str):
    """Retrieve users by id from the database."""
    try:
        if not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format")
        
        users = db.users_collection.find_one({"_id": ObjectId(user_id)})
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        return UserResponse(
                id=str(users["_id"]),
                name=users["name"],
                email=users["email"],
                age=users["age"],
                created_at=users["created_at"]
                )
    except HTTPException:
        raise    
    except Exception as e:
        print(f"Error retrieving users: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving users")
 
@app.get("/users/{user_id}/posts", response_model=List[PostResponseWithUser])
async def get_posts_by_user(user_id: str):
    """Retrieve all posts for a specific user."""
    try:
        if not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format")
        
        #Check if user exists before retrieving posts
        user = db.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        posts = db.get_user_posts(user_id)
        return [PostResponseWithUser(
                    id=str(post["_id"]),
                    title=post["title"],
                    content=post["content"],
                    created_at=post["created_at"]
                ) for post in posts]
    except HTTPException:
        raise    
    except Exception as e:
        print(f"Error retrieving posts: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving posts")
    
    @app.put("/users/{user_id}/email", response_model=UserResponse)
    #Update user email by id
    async def update_user_email(user_id: str, new_email: EmailStr):
        """Update a user's email address."""
        try:
            if not ObjectId.is_valid(user_id):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format")
            
            updated_user = db.update_user_email(user_id, new_email)
            if updated_user:
                return UserResponse(
                    id=str(updated_user["_id"]),
                    name=updated_user["name"],
                    email=updated_user["email"],
                    age=updated_user["age"],
                    created_at=updated_user["created_at"]
                )
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        except HTTPException:
            raise    
        except Exception as e:
            print(f"Error updating user email: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error updating user email")

@app.put("/users/{user_id}/age", response_model=UserResponse)
async def update_user_age(user_id: str, new_age: int):
    """Update a user's age."""
    try:
        if not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format")
        
        updated_user = db.update_user_age(user_id, new_age)
        if updated_user:
            return UserResponse(
                id=str(updated_user["_id"]),
                name=updated_user["name"],
                email=updated_user["email"],
                age=updated_user["age"],
                created_at=updated_user["created_at"]
            )
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except HTTPException:
        raise    
    except Exception as e:
        print(f"Error updating user age: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error updating user age")
    
@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    """Delete a user and all their posts from the database."""
    try:
        if not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format")
        
        user = db.users_collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        sucess = db.delete_user(user_id)
        if sucess:
            return {"message": "User and their posts deleted successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except HTTPException:
        raise    
    except Exception as e:
        print(f"Error deleting user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting user")
    
@app.delete("/posts/{post_id}", response_model=dict)
async def delete_post(post_id: str):
    """Delete a post from the database."""
    try:
        if not ObjectId.is_valid(post_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid post ID format")
        
        post = db.posts_collection.find_one({"_id": ObjectId(post_id)})
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

        sucess = db.delete_post(post_id)
        if sucess:
            return {"message": "Post deleted successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    except HTTPException:
        raise    
    except Exception as e:
        print(f"Error deleting post: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting post")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
