#Module

def add(a, b): #add two numbers and return the result
    return a + b

def multiply(a, b): #multiply two numbers and return the result
    return a * b

def factorial(n): #calculate the factorial of a number
    if n <=1:
        return 1
    return n * factorial(n - 1)

PI = 3.14159 #constant for pi

class calculator: #a simple calculator class
    def __init__(self):
        self.history = [] #store history of calculations
    
    def calculate(self, operation, a, b):
        if operation == "add":
            result = add(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        else:
            raise ValueError("Unsupported operation")
        
        self.history.append(f"{operation}({a}, {b}) = {result}") #store the calculation in history
        return result
    
    def get_history(self): #return the history of calculations
        return self.history 
    