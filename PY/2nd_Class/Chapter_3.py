

name = input("Enter your name: ")

# Height validation
while True:
    try:
        height = float(input("Enter your height (in feet): "))
        if height > 0:
            break
        else:
            print("Height must be positive!")
    except ValueError:
        print("Please enter a valid number of height!")

# Age validation
while True: 
    try: 
        age = int(input("Enter your age: "))
        if age > 0 :
            break
        else:
            print("Age must be positive!")
    except ValueError:
        print("Please enter a valid number of age!")


print(f"Hello, {name}!")
print(f"You are {age} years old and {height} feet tall.")
