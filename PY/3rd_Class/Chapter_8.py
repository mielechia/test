# #Sets

# #Sets are unordered collections of unique elements. They are defined using curly braces {} or the set() function. Here are some examples of sets:
# fruits = {"apple", "banana", "orange"}
# colors = set(["red", "green", "blue"])

# #Set Operation
# fruits.add("grape")  # Add an element to the set
# fruits.remove("banana")  # Remove an element from the set
# fruits.discard("banana")  # Remove an element from the set without raising an error if it doesn't exist
# fruits.clear()  # Remove all elements from the set
# fruits.update(["kiwi", "melon"])  # Add multiple elements to the set
# print(fruits)  # Output: {'kiwi', 'melon'}

# #Sets support various operations, such as union, intersection, difference, and symmetric difference. Here are some examples of these operations:
# #Union: You can combine two sets using the | operator or the union() method.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1 | set2
# print(union_set)  # Output: {1, 2, 3, 4, 5}
# print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
# #-combine without duplicates

# #Intersection: You can find the common elements between two sets using the & operator or the intersection() method.
# intersection_set = set1 & set2
# print(intersection_set)  # Output: {3}
# print(set1.intersection(set2))  # Output: {3}
# #-find duplicates

# #Difference: You can find the elements that are in one set but not in another using the - operator or the difference() method.
# difference_set = set1 - set2
# print(difference_set)  # Output: {1, 2}
# print(set1.difference(set2))  # Output: {1, 2}
# #-find elements in set1 but not in set2
# print(set2.difference(set1))  # Output: {4, 5}
# #-find elements in set2 but not in set1

# #Symmetric Difference: You can find the elements that are in either set but not in both using the ^ operator or the symmetric_difference() method.
# symmetric_difference_set = set1 ^ set2
# print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
# print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}
# #-find elements in set1 or set2 but not in both
# #-find non-duplicates

# #Sets also support membership testing using the in keyword.
# print(2 in set1)  # Output: True
# print(5 in set1)  # Output: False
# #-Check if an element is in or not in the set
# #-Check if 2 or 5 is in set1

# #You can also use the len() function to get the number of elements in a set.
# print(len(set1))  # Output: 3
# print(len(set2))  # Output: 3
# #-Get the number of elements in set1 and set2


#Exercise: Create a system that stores student grades as tuples (name, subject, grade) and uses sets to find unique subjects and students. 

grades = [("Alice", "Math", 85), ("Bob", "Science", 92), ("Alice", "Science", 78), ("Charlie", "Math", 90), ("Bob", "Math", 88), ("Alice", "English", 95)] 

unique_students = set()
unique_subjects = set()
for grade in grades:
    unique_students.add(grade[0])  # Add the student's name (index 0) to the unique_students set
    unique_subjects.add(grade[1])  # Add the subject (index 1) to the unique_subjects set

print("unique_students:", unique_students)  # Output: {'Alice', 'Bob', 'Charlie'}
print("unique_subjects:", unique_subjects)  # Output: {'Math', 'Science', 'English'}        

#Another example:
# Extract unique students (index 0) from each tuple
unique_students = set(grade[0] for grade in grades)
# Extract unique subjects (index 1) from each tuple
unique_subjects = set(grade[1] for grade in grades)

print("unique_students:", unique_students)  # Output: {'Alice', 'Bob', 'Charlie'}
print("unique_subjects:", unique_subjects)  # Output: {'Math', 'Science', 'English'}
