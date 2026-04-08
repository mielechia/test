#MongoDB

from pymongo import MongoClient
from datetime import datetime, timezone
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()   

mongo_uri = os.getenv("MONGODB_ATLAS_CLUSTER_URI")

if not mongo_uri:
    print("MongoDB URI not found. Please check your .env file and ensure MONGODB_ATLAS_CLUSTER_URI is set correctly.")

class DatabaseManager:
    def __init__(self, db_name='example_db', connection_string=mongo_uri):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.users_collection = self.db.users
        self.post_collection = self.db.posts
        self.init_database()

    def init_database(self):
        """Initialize the database with collections and indexes if they do not exist."""
        # Create unique index on email for users
        self.users_collection.create_index('email', unique=True)
        # Create index on user_id for posts for better query performance
        self.post_collection.create_index('user_id')

    def create_user(self, name, email, age):
        """Create a new user document in the users collection."""
        user_doc = {
            'name': name,
            'email': email,
            'age': age,
            'created_at': datetime.now(timezone.utc)
            }
        try:
            result = self.users_collection.insert_one(user_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
    
    def create_post(self, user_id, title, content):
        """Create a new post"""
        try:
            # Convert string user_id to ObjectId if it's a valid ObjectId
            if not ObjectId.is_valid(user_id):
                print("Invalid user ID format. Please provide a valid ObjectId string.")
                return None
            
            user_object_id = ObjectId(user_id)

            if not self.users_collection.find_one({'_id': user_object_id}):
                print("User ID does not exist in the database. Please provide a valid user ID.")
                return None
            
            post_doc = {
                'user_id': user_object_id,
                'title': title,
                'content': content,
                'created_at': datetime.now(timezone.utc)
                }
            result = self.post_collection.insert_one(post_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating post: {e}")
            return None
        
#Read data from the database# (SELECT)     
    def get_all_users(self):
        """Retrieve all users from the users collection."""
        try:
            users = list(self.users_collection.find())
            for user in users:
                user['_id'] = str(user['_id'])  # Convert ObjectId to string for better readability
            return users
        except Exception as e:
            print(f"Error retrieving users: {e}")
            return []
        
    def get_user_by_id(self, user_id):
        """Retrieve a user by their ID."""
        try:
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
            
            user = self.users_collection.find_one({'_id': user_object_id})
            if user:
                user['_id'] = str(user['_id'])  # Convert ObjectId to string for better readability
            return user
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None
        
    def get_user_posts(self, user_id):
        """Retrieve all posts for a specific user."""
        try:
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
            
            posts = list(self.post_collection.find({'user_id': user_object_id}))
            for post in posts:
                post['_id'] = str(post['_id'])  # Convert ObjectId to string for better readability
                post['user_id'] = str(post['user_id'])  # Convert user_id to string for better readability  
            return posts
        
        except Exception as e:
            print(f"Error retrieving posts: {e}")
            return []

#Update existing data in the database (UPDATE)
    def update_user_email(self, user_id, new_email):
        """Update a user's email address."""
        try:
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
            
            result = self.users_collection.update_one(
                {'_id': user_object_id},
                {'$set': {'email': new_email}}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating user email: {e}")
            return False
        
    def update_user_age(self, user_id, new_age):
        """Update a user's age."""
        try:
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
            
            result = self.users_collection.update_one(
                {'_id': user_object_id},
                {'$set': {'age': new_age}}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating user age: {e}")
            return False
        
#Delete data from the database (DELETE)        
    def delete_user(self, user_id):
        """Delete a user and their associated posts."""
        try:
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
            
            # Delete the user
            result = self.users_collection.delete_one({'_id': user_object_id})
            if result.deleted_count > 0:
                # If the user was deleted, also delete their posts
                self.post_collection.delete_many({'user_id': user_object_id})
                return True
            return False
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        
    def delete_post(self, post_id):
        """Delete a post by its ID."""
        try:
            if ObjectId.is_valid(post_id):
                post_object_id = ObjectId(post_id)
            else:
                post_object_id = post_id
            
            result = self.post_collection.delete_one({'_id': post_object_id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting post: {e}")
            return False
    
#Close the database connection when done
    def close_connection(self):
        """Close the MongoDB connection."""
        self.client.close()

#Setup display menu and main function to run the database manager
    def display_menu(self):
        """Display the menu options to the user."""
        print("\n" + "="*30)
        print("MongoDB Database Manager")
        print("="*30)
        print("1. Create User")
        print("2. Create Post")
        print("3. Get All Users")
        print("4. Get User by ID")
        print("5. Get User's Posts")
        print("6. Update User Email")
        print("7. Update User Age")
        print("8. Delete User")
        print("9. Delete Post")
        print("0. Exit")

def main():
    """Main interactive CLI function to run the database manager."""
    try:
        db = DatabaseManager()
        print("Welcome to the MongoDB Database Manager!")
        print("MongoDB connection established successfully.")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        print("Please check your MongoDB connection settings and try again.")
        return  
        
    while True:
        db.display_menu()
        choice = input("Enter your choice(1-9, 0 to exit): ").strip()

        if choice == '1':
            print("\nCreate New User")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            try:
                age = int(input("Enter age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"User created successfully with ID: {user_id}")
                else:
                    print("Failed to create user.")
            except ValueError:
                    print("Invalid age. Please enter a number.")
            
        elif choice == '2':
            print("\nCreate New Post")
            user_id = input("Enter user ID: ").strip()
            title = input("Enter post title: ").strip()
            content = input("Enter post content: ").strip()
            post_id = db.create_post(user_id, title, content)
            if post_id:
                print(f"Post created successfully with ID: {post_id}")
            else:
                print("Failed to create post.")     

        elif choice == '3':
            print("\nCheck All Users:")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user['_id']}, Name: {user['name']}, Email: {user['email']}, Age: {user['age']}, Created At: {user['created_at']}")
            else:
                print("No users found.")

        elif choice == '4':
            print("\nCheck User by ID")
            user_id = input("Enter user ID: ").strip()
            user = db.get_user_by_id(user_id)
            if user:
                print(f"ID: {user['_id']}, Name: {user['name']}, Email: {user['email']}, Age: {user['age']}, Created At: {user['created_at']}")
            else:
                print("User not found.")    

        elif choice == '5': 
            print("\nView User's Posts")
            user_id = input("Enter user ID: ").strip()
            posts = db.get_user_posts(user_id)
            if posts:
                for post in posts:
                    print(f"\nID: {post['_id']}")
                    print(f"Title: {post['title']}")
                    print(f"Content: {post['content']}")
                    print(f"Created At: {post['created_at']}")
                    print("-"*30)
            else:
                print("No posts found for this user.")
            
        elif choice == '6':
            print("\nUpdate User Email")
            user_id = input("Enter user ID: ").strip()
            new_email = input("Enter new email: ").strip()
            if db.update_user_email(user_id, new_email):
                print("User email updated successfully.")
            else:
                print("Failed to update user email.")

        elif choice == '7':
            print("\nUpdate User Age")
            user_id = input("Enter user ID: ").strip()
            try:
                new_age = int(input("Enter new age: ").strip())
                if db.update_user_age(user_id, new_age):
                    print("User age updated successfully.")
                else:
                    print("Failed to update user age.")
            except ValueError:
                print("Invalid age. Please enter a number.")

        elif choice == '8':
            print("\nDelete User")
            user_id = input("Enter user ID to delete: ").strip()
            confirm = input("Are you sure you want to delete this user and all their posts? (yes/no): ").strip().lower()
            if confirm == 'yes':
                if db.delete_user(user_id):
                    print("User and their posts deleted successfully.")
                else:
                    print("Failed to delete user.")
            else:
                print("User deletion canceled.")
            
        elif choice == '9':
            print("\nDelete Post")
            post_id = input("Enter post ID: ").strip()
            confirm = input("Are you sure you want to delete this post? (yes/no): ").strip().lower()
            if confirm == 'yes':
                if db.delete_post(post_id):
                    print("Post deleted successfully.")
                else:
                    print("Failed to delete post.")
            else:
                print("Post deletion canceled.")
            
        elif choice == '0':
            print("Exiting the MongoDB Database Manager. Goodbye!")
            db.close_connection()
            print("MongoDB connection closed.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9, or 0 to exit.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
