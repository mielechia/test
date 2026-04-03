# Tuples are immutable sequences, typically used to store collections of heterogeneous data. They are defined using parentheses (). Here are some examples of tuples:       
coordinates = (10, 20)
person = ("Miele", 26, "Researcher")
single_item = (82,)

#Tuples can be accessed using indexing, just like lists. However, since tuples are immutable, you cannot modify their elements after they have been created. You can also unpack tuples into variables: 
x, y = coordinates
name, age, profession = person 
#Tuples can be used in various applications, such as returning multiple values from a function, storing fixed collections of data, and as keys in dictionaries (since they are immutable). They are also more memory-efficient than lists, making them a good choice for storing large amounts of data that do not need to be modified.
#Example of returning multiple values from a function using a tuple:
def get_person_info():
    name = "Miele"
    age = 26
    profession = "Researcher"
    return name, age, profession
person_info = get_person_info()
print(person_info)  # Output: ('Miele', 26, 'Researcher')
#Example of using a tuple as a key in a dictionary:
location_data = {(10, 20): "Park", (30, 40): "Museum"} 
print(location_data[(10, 20)])  # Output: Park

#Tuples can also be nested, meaning you can have tuples within tuples. This allows for more complex data structures. For example:
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  # Output: (1, 2)
print(nested_tuple[0][1])  # Output: 2  

#In summary, tuples are a powerful and efficient way to store and manage collections of data that do not need to be modified. They provide a convenient way to group related data together and can be used in various applications throughout Python programming. 

#Tuples support various operations, such as concatenation, repetition, and membership testing. Here are some examples of these operations:
#Concatenation: You can concatenate two tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
#Repetition: You can repeat a tuple using the * operator.
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
#Membership Testing: You can check if an element is in a tuple using the in keyword.
print(2 in tuple1)  # Output: True
print(5 in tuple1)  # Output: False
#You can also use the len() function to get the number of elements in a tuple, and the count() method to count the occurrences of a specific element in a tuple.
print(len(tuple1))  # Output: 3
print(tuple1.count(2))  # Output: 1 

#Tuple Operations
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20
print(person[0])  # Output: Miele
print(person[1])  # Output: 26
print(person[2])  # Output: Researcher 
print(len(person))  # Output: 3
print(single_item[0])  # Output: 82 
