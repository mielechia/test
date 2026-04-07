#Module

from posixpath import dirname

from math_utils import add, multiply, factorial, PI, calculator 
#You can import specific functions, classes, or variables from a module using the from keyword.
#You can also import the entire module and access its contents using the module name as a prefix.
# import math_utils
result = add(5, 3)  # Using the add function from math_utils
print(f"Addition result: {result}")  #Output: 8

calc = calculator()  # Create an instance of the calculator class
result = calc.calculate("add", 10, 20)  # Use the calculate method to perform addition
print(f"Calculation result: {result}")  # Output: 30
print(f"Value of PI: {PI}")  # Output: 3.14159
print(f"Factorial of 5: {factorial(5)}")  # Output: 120
result = calc.calculate("multiply", 4, 5)  # Use the calculate method to perform multiplication
print(f"Calculation result: {result}")  # Output: 20 
print("Calculation history:", calc.get_history()) # Output: ['add(10, 20) = 30', 'multiply(4, 5) = 20']        


#Libraries
#libaries are collections of modules that provide additional functionality. You can use libraries to perform specific tasks without having to write the code yourself. For example, the math library provides functions for mathematical operations, and the datetime library provides functions for working with dates and times.
import os  # Importing the os library to work with the operating system
import sys  # Importing the sys library to access system-specific parameters and functions
import datetime  # Importing the datetime library to work with dates and times
import random  # Importing the random library to generate random numbers
import math  # Importing the math library to perform mathematical operations

sys.path.append(os.path.dirname(os.path.dirname(__file__))) # Add the parent directory to the system path to allow importing modules from that directory

now = datetime.datetime.now()  # Get the current date and time
today = datetime.date.today()  # Get the current date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")  # Format the current date and time as a string

print(f"Now date: {now}")  # Output: Now date: 2024-06-01 12:34:56.789012
print(f"Today's date: {today}")  # Output: Today date: 2024-06-01
print(f"Current date and time: {formatted_date}")  # Output: Current date and time: 2024-06-01 12:34:56

random_number = random.randint(1, 100)  # Generate a random integer between 1 and 100
random_choice = random.choice(['apple', 'banana', 'cherry'])  # Randomly select an item from a list 
numbers = [1, 2, 3, 4, 5]
choice = ['red', 'green', 'blue']
random.shuffle(numbers)  # Shuffle the list of numbers in place
random.shuffle(choice)  # Shuffle the list of choices in place

print(f"Random number: {random_number}")  # Output: Random number: 42
print(f"Random choice: {random_choice}")  # Output: Random choice: banana
print(f"Shuffled numbers: {numbers}")  # Output: Shuffled numbers: [3, 1, 5, 2, 4]
print(f"Shuffled choices: {choice}")  # Output: Shuffled choices: ['green', 'red', 'blue']

