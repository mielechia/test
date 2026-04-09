# Database SQLite Commands:
# CREATE: create a new database 
# INSERT: add new data to the database
# SELECT: retrieve data from the database
# UPDATE: modify existing data in the database
# DELETE: remove data from the database
# JOIN: combine data from multiple tables based on a related column
# WHERE: filter data based on specific conditions
# GROUP BY: group data based on a specific column and perform aggregate functions
# ORDER BY: sort data based on a specific column in ascending or descending order
# LIMIT: limit the number of results returned by a query
# DISTINCT: return only unique values in a column
# COUNT: count the number of rows that match a specific condition
# SUM: calculate the total sum of a numeric column
# AVG: calculate the average value of a numeric column
# MIN: find the minimum value in a numeric column
# MAX: find the maximum value in a numeric column

#Example of a simple database manager class that implements basic CRUD operations using SQLite:
import sqlite3
class DatabaseManager: 
    def __init__(self, db_name='example.db'):
        self.db_name = db_name
        self.init_database()

#Initialise database (CREATE)
    def init_database(self):
        """"Initialize the database and create tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')

#Create a new user (INSERT)
    def create_user(self, name, email, age):
        """Insert a new user into the database."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO users (name, email, age) VALUES (?, ?, ?)''', (name, email, age))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"An error occurred: {e}")
            return None
        
    def create_post(self, user_id, title, content):
        """Insert a new post into the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)''', (user_id, title, content))
            return cursor.lastrowid

#Read data from the database# (SELECT)
    def get_all_users(self):
        """Get all users from the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()
    
    def get_user_by_id(self, user_id):
        """Get a user by their ID."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            return cursor.fetchone()
    
    def get_user_posts(self, user_id):
        """Get all posts by a specific user."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT p.id, p.title, p.content, p.created_at FROM posts p WHERE p.user_id = ? ORDER BY p.created_at DESC''', (user_id,))
            return cursor.fetchall()

#Update existing data in the database (UPDATE)
    def update_user_email(self, user_id, new_email):
        """Update a user's email address."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''UPDATE users SET email = ? WHERE id = ?''', (new_email, user_id))
                return cursor.rowcount
        except sqlite3.IntegrityError as e:
            print(f"An error occurred: {e}")
            return None
        
    def update_user_age(self, user_id, new_age):
        """Update a user's age."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''UPDATE users SET age = ? WHERE id = ?''', (new_age, user_id))
            return cursor.rowcount
        
#Delete data from the database (DELETE)
    def delete_user(self, user_id):
        """Delete a user and their posts from the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM posts WHERE user_id = ?''', (user_id,))   
            cursor.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
            return cursor.rowcount > 0
        
    def delete_post(self, post_id):
        """Delete a post from the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM posts WHERE id = ?''', (post_id,))
            return cursor.rowcount > 0
    
#Setup display menu and main function to run the database manager
    def display_menu(self):
        """Display the menu options to the user."""
        print("\n" + "="*30)
        print("Database Manager Menu")
        print("="*30)
        print("1. Create a new user")
        print("2. View all users") 
        print("3. Create a new post")
        print("4. View a user's posts")
        print("5. Update a user's email")
        print("6. Update a user's age")
        print("7. Delete a post")
        print("8. Delete a user")
        print("9. Exit")
        print("-"*30)

    def main(self):
        """Main function to run the database manager menu."""
        db = DatabaseManager()

        while True:
            db.display_menu()
            choice = input("Enter your choice (1-9): ").strip()
        
            if choice == '1':
                print("\nCreate a New User")
                name = input("Enter name: ").strip()
                email = input("Enter email: ").strip()
                try: 
                    age = int(input("Enter age: ").strip())
                    user_id = db.create_user(name, email, age)
                    if user_id:
                        print(f"User created Successfully! ID: {user_id}")
                    else:
                        print("Failed to create user.")
                except ValueError:
                    print("Invalid age. Please enter a number.")    

            elif choice == '2':
                print("\nAll Users:")
                users = db.get_all_users()
                if users:
                    for user in users:
                        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}, Created At: {user[4]}")
                else: 
                    print("No users found.")    

            elif choice == '3':
                print("\nCreate a New Post")
                try:
                    user_id = int(input("Enter user ID: ").strip())
                    title = input("Enter post title: ").strip()
                    content = input("Enter post content: ").strip()
                    post_id = db.create_post(user_id, title, content)
                    if post_id:
                        print(f"Post created successfully! ID: {post_id}")
                    else:
                        print("Failed to create post.")
                except ValueError:
                    print("Invalid user ID. Please enter a number.")

            elif choice == '4':
                print("\nView a User's Posts")
                try:
                    user_id = int(input("Enter user ID: ").strip())
                    posts = db.get_user_posts(user_id)
                    if posts:
                        for post in posts:
                            print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Created At: {post[3]}")
                    else:
                        print("No posts found for this user.")
                except ValueError:
                    print("Invalid user ID. Please enter a number.")
            
            elif choice == '5':
                print("\nUpdate User Email")
                try:
                    user_id = int(input("Enter user ID: ").strip())
                    new_email = input("Enter new email: ").strip()
                    if db.update_user_email(user_id, new_email):
                        print("Email updated successfully!")
                    else:
                        print("User not found or email update failed.")
                except ValueError:
                    print("Invalid user ID. Please enter a number.")
            
            elif choice == '6':
                print("\nUpdate User Age")
                try:
                    user_id = int(input("Enter user ID: ").strip())
                    new_age = int(input("Enter new age: ").strip())
                    if db.update_user_age(user_id, new_age):
                        print("Age updated successfully!")
                    else:
                        print("User not found or age update failed.")
                except ValueError:
                    print("Invalid input. Please enter numbers for user ID and age.")

            elif choice == '7':
                print("\nDelete Post")
                try:
                    post_id = int(input("Enter post ID to delete: ").strip())
                    confirm = input(f"Are you sure you want to delete post {post_id}? (Y/N): ").strip()
                    if confirm == 'Y':
                        if db.delete_post(post_id):
                            print(f"Post deleted successfully!")
                        else:
                            print(f"Post not found or deletion failed.")
                    else:   
                        print(f"Deletion Cancelled.")
                except ValueError:
                    print("Invalid post ID. Please enter a number.")                       

            elif choice == '8': 
                print("\nDelete User")
                try:
                    user_id = int(input("Enter user ID to delete: ").strip())
                    confirm = input(f"Are you sure you want to delete user {user_id}? (Y/N): ").strip()
                    if confirm == 'Y':
                        if db.delete_user(user_id):
                            print(f"User deleted successfully!")
                        else:
                            print(f"User not found or deletion failed.")
                    else:   
                        print(f"Deletion Cancelled.")
                except ValueError:
                    print("Invalid user ID. Please enter a number.")

            elif choice == '9':
                print("Exiting the Database Manager. Goodbye!")
                break

            else: 
                print("Invalid choice. Please enter a number between 1 and 9.")

        input("\nPress Enter to continue...")  # Pause before showing the menu again

if __name__ == "__main__":
    db = DatabaseManager()
    db.main()
