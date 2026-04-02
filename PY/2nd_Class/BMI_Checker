(Check your BMI now for free!)

name = input("Enter your name: ")

# Height validation
while True:
    try:
        height = float(input("Enter your height (in M): "))
        if height > 0:
            break
        else:
            print("Height must be positive!")
    except ValueError:
        print("Please enter a valid number of height!")

# Weight validation
while True: 
    try: 
        weight = float(input("Enter your weight (in KG): "))
        if weight > 0 :
            break
        else:
            print("Weight must be positive!")
    except ValueError:
        print("Please enter a valid number of Weight!")

# BMI Calculation
BMI = (weight / height ** 2)

if BMI <= 18.5:
    check = "Underweight"
elif BMI <= 24.9:
    check = "Normal"
elif BMI <= 29.9:
    check = "Overweight"
else:
    check = "Obesity"

#Print
print(f"Hello, {name}!")
print(f"You are {weight} KG and {height} M tall.") 
print(f"Your BMI is {BMI:.2f}.")
print(f"You are classified as {check}.")