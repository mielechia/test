#Code
age = 18

#Print
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


#Code
score =85

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "A-"
elif score >= 65:
    grade = "B+"
elif score >= 60:
    grade = "B-"
elif score >= 50:
    grade = "C"
else:
    grade = "Fail"

if score >= 50:
    note = "Congratulations!"
else: 
    note = "Sorry!"

#PRINT

if score >= 50:
    print(f"{note} Your grade is: {grade}")
else:
    print(f"{note} Your grade is: {grade}")


#Code
user_age = 26
has_license = True

#Print
if user_age >= 18 and has_license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")


#Code
day = "Saturday"

#Print
if day == "Saturday" or day == "Sunday":
    print("Yay! It's the weekend!")
else:
    print("It's a weekday.")

if day != "Saturday" or day != "Sunday"
    print("It's not the weekend!")

#Code
weather = "Sunny"
temperature = 23

#Print
if weather == "Sunny":
    if temperature > 26:
        print("It's sunny and warm.")
    else: 
        print("It's sunny but cool.")

if weather != "Sunny" and temperature >= 10