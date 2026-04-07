#Inheritance allows us to create a new class that is a modified version of an existing class. The new class (called the child class) inherits attributes and methods from the existing class (called the parent class), and can also have its own unique attributes and methods.

class Parent:
    def __init__(self,name):
       self.name = name 

    def greet(self):
        return f"Hello, I am {self.name} from the Parent Class."
    
class Child(Parent):
    def __init__ (self, name, age):
        super(). __init__ (name) # Call the parent class's __init__ method to initialize the name attribute
        self.age = age # Initialize the age attribute specific to the Child class
    def greet(self): # Override the greet method from the Parent class
            return f"Hello, I am {self.name} and I am {self.age} years old from the Child Class."

# Create an instance of the Child class
child_instance = Child("Alice", 10)
print(child_instance.greet()) # Output: Hello, I am Alice and I am 10 years old from the Child Class.

#In this example, the Child class inherits from the Parent class. The Child class has its own __init__ method that initializes both the name (inherited from Parent) and age attributes. It also overrides the greet method to provide a different greeting message. When we create an instance of the Child class and call the greet method, it uses the overridden version defined in the Child class.

#Polymorphism allows us to use a single interface to represent different types of objects. In Python, this is often achieved through method overriding, where a child class provides a specific implementation of a method that is already defined in its parent class.
def print_greeting(hello):
    print(hello.greet())
# Create instances of Parent and Child classes
parent_instance = Parent("Evelyn")
child_instance = Child("Miele", 3)
# Use the print_greeting function to demonstrate polymorphism
print_greeting(parent_instance) # Output: Hello, I am Evelyn from the Parent Class.
print_greeting(child_instance) # Output: Hello, I am Miele and I am 3 years old from the Child Class.
#In this example, the print_greeting function takes an object (hello) and calls its greet method. Both the Parent and Child classes have a greet method, but they provide different implementations. When we pass an instance of the Parent class to print_greeting, it calls the greet method defined in the Parent class. When we pass an instance of the Child class, it calls the overridden greet method defined in the Child class. This demonstrates polymorphism, as the same function can work with different types of objects and call their respective methods.

#Another example of Inheritance and Polymorphism:
#Inheritance 
class shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return

class circle(shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class square(shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2

circle1 = circle("Circle", 5)
square1 = square("Square", 4)

print(f"The area of {circle1.name} is: {circle1.area()}")
print(f"The area of {square1.name} is: {square1.area()}")
# Output:
# The area of Circle is: 78.5
# The area of Square is: 16

#Polymorphism
def print_area(shape):
    print(f"The area of {shape.name} is: {shape.area()}")

#same output different code
print_area(circle1) # Output: The area of Circle is: 78.5
print_area(square1) # Output: The area of Square is: 16

#or with a list of shapes
shapes = [circle("Circle", 3), square("Square", 5), circle("Circle", 7), square("Square", 2)]
for shape in shapes:
    print_area(shape)
# Output:
# The area of Circle is: 28.26
# The area of Square is: 25
# The area of Circle is: 153.86
# The area of Square is: 4

