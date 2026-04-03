# List, by using []

# fruits = ["apple", "banana", "cherry"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["apple", 1, "banana", 2, "cherry", 3]
# empty_list = []

# # Accessing Elements
# print(fruits[0])  # Output: apple
# print(fruits[-1])  # Output: cherry
# print(numbers[1:4])  # Output: [2, 3, 4]
# print(numbers[:3])  # Output: [1, 2, 3]
# print(numbers[3:])  # Output: [4, 5]
# print(mixed[1:5])  # Output: [1, 'banana', 2, 'cherry']

# #List Operations
# fruits.append("orange")  # Add an element to the end of the list
# fruits.insert(1, "grape")  # Insert an element at a specific index
# fruits.remove("banana")  # Remove the first occurrence of an element
# fruits.pop()  # Remove and return the last element
# fruits.pop(1)  # Remove and return the element at a specific index
# fruits.clear()  # Remove all elements from the list 
# fruits.sort()  # Sort the list in ascending order
# fruits.reverse()  # Reverse the order of the list
# fruits.extend(["kiwi", "melon"])  # Extend the list by appending elements
# fruits.count("apple")  # Count the number of occurrences of an element
# fruits.index("kiwi")  # Return the index of the first occurrence of an element

# len(fruits)  # Get the number of elements in the list
# "apple" in fruits  # Check if an element is in the list
# fruits + ["melon"] # Concatenation
# fruits + ["kiwi" + "watermelon"] # Concatenation with 2 elements
# fruits * 2  # Repetition


#Exercise
# Create a lost os groceries and perform various operations on it.
groceries = ["milk", "bread", "eggs", "cheese", "fruits"]
groceries.append("vegetables")
groceries.insert(2, "butter")
groceries.remove("eggs")
groceries.pop()
groceries.pop(1)
groceries.clear()
groceries.extend(["rice", "pasta", "sauce", "salt"])
extra_grocreries = ["salt", "pepper", "rice", "pasta"]
groceries.extend(extra_grocreries)
groceries.append("rice")
groceries.append("sauce")
groceries.sort()
groceries.reverse()
groceries.count("rice")
groceries.index("pasta")

len(groceries)
"apple" in groceries
groceries + ["yogurt"]
groceries + ["olive oil" + "vinegar"]
groceries * 2 != "pepper"

print(groceries)

counts = [groceries.count(item) for item in set(groceries)]
largest_number = max(counts)
smallest_number = min(counts)
unique_items = list(set(groceries))
largest_grocery = unique_items[counts.index(largest_number)]
smallest_grocery = unique_items[counts.index(smallest_number)] 

print("number of groceries:", len(groceries))
print("largest number:", largest_number)
print("smallest number:", smallest_number)
print("most occurring grocery:", largest_grocery)
print("least occurring grocery:", smallest_grocery)