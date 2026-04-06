# # Tuples are immutable sequences, typically used to store collections of heterogeneous data. They are defined using parentheses (). Here are some examples of tuples:       
# coordinates = (10, 20)
# person = ("Miele", 26, "Researcher")
# single_item = (82,)

# #Tuples can be accessed using indexing, just like lists. However, since tuples are immutable, you cannot modify their elements after they have been created. You can also unpack tuples into variables: 
# x, y = coordinates
# name, age, profession = person 
# #Tuples can be used in various applications, such as returning multiple values from a function, storing fixed collections of data, and as keys in dictionaries (since they are immutable). They are also more memory-efficient than lists, making them a good choice for storing large amounts of data that do not need to be modified.
# #Example of returning multiple values from a function using a tuple:
# def get_person_info():
#     name = "Miele"
#     age = 26
#     profession = "Researcher"
#     return name, age, profession
# person_info = get_person_info()
# print(person_info)  # Output: ('Miele', 26, 'Researcher')
# #Example of using a tuple as a key in a dictionary:
# location_data = {(10, 20): "Park", (30, 40): "Museum"} 
# print(location_data[(10, 20)])  # Output: Park

# #Tuples can also be nested, meaning you can have tuples within tuples. This allows for more complex data structures. For example:
# nested_tuple = ((1, 2), (3, 4), (5, 6))
# print(nested_tuple[0])  # Output: (1, 2)
# print(nested_tuple[0][1])  # Output: 2  

# #In summary, tuples are a powerful and efficient way to store and manage collections of data that do not need to be modified. They provide a convenient way to group related data together and can be used in various applications throughout Python programming. 

# #Tuples support various operations, such as concatenation, repetition, and membership testing. Here are some examples of these operations:
# #Concatenation: You can concatenate two tuples using the + operator.
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# concatenated_tuple = tuple1 + tuple2
# print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
# #Repetition: You can repeat a tuple using the * operator.
# repeated_tuple = tuple1 * 3
# print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
# #Membership Testing: You can check if an element is in a tuple using the in keyword.
# print(2 in tuple1)  # Output: True
# print(5 in tuple1)  # Output: False
# #You can also use the len() function to get the number of elements in a tuple, and the count() method to count the occurrences of a specific element in a tuple.
# print(len(tuple1))  # Output: 3
# print(tuple1.count(2))  # Output: 1 

# #Tuple Operations
# print(coordinates[0])  # Output: 10
# print(coordinates[1])  # Output: 20
# print(person[0])  # Output: Miele
# print(person[1])  # Output: 26
# print(person[2])  # Output: Researcher 
# print(len(person))  # Output: 3
# print(single_item[0])  # Output: 82 


#Exercise Create Influencers Records

Influencers = [("Alice", 168.5, 45.3, "Fashion", "Instagram"),
               ("Jason", 180.3, 72.5, "Food", "TikTok"),
               ("Miele", 179.2, 68.0, "Travel", "YouTube"),
               ("Emily", 170.0, 59.0, "Fitness", "Instagram"),
               ("David", 182.5, 80.0, "Tech", "Twitter"),
               ("Sophia", 165.8, 55.0, "Beauty", "Facebook"),
               ("Michael", 175.0, 70.0, "Gaming", "Twitch"),
               ("Olivia", 160.2, 50.0, "Lifestyle", "Pinterest"),
               ("James", 178.4, 75.0, "Music", "SoundCloud")]

# First_name_in = [Influencers[0][0]]
# print(f"First influencer name: {First_name_in[0]}")

# Last_platform_in = [Influencers [-1] [4]]
# print(f"Last influencer platform: {Last_platform_in[0]}")

# Third_niche_in = [Influencers[2][3]]
# print(f"Third influencer niche: {Third_niche_in[0]}")

# for Influencer in Influencers:
#     name, height, weight, niche, platform = Influencer
#     print(f"{name} is a {niche} influencer on {platform}.")


# tallest = Influencers[0]  # Initialize tallest with the first influencer
# for influencer in Influencers:
#     if influencer[1] > tallest[1]:  # compare height
#         tallest = influencer
# name, height = tallest[0], tallest[1]
# print(f"{name} is {height}CM tall, and is the tallest Influencer.")

# lightest = Influencers[0]
# for influencer in Influencers:
#     if influencer[2] < lightest[2]:
#         lightest = influencer
# name, weight = lightest[0], lightest[2]
# print(f"{name} is {weight}KG, and is the lightest Influencer.")

# average_height = sum(influencer [1] for influencer in Influencers) / len(Influencers)
# print(f"Average height of the influencers is: {average_height:.2f}CM.")

# average_weight = sum(influencer [2] for influencer in Influencers) / len(Influencers)
# print(f"Average weight of the influencers is: {average_weight:.2f}KG.") 


inf_by_platform = {}
for influencer in Influencers:
    platform = influencer[4]  # Get the platform from the tuple
    if platform in inf_by_platform:
        inf_by_platform[platform] += 1  # Increment count if platform already exists
    else:
        inf_by_platform[platform] = 1  # Initialize count for new platform
print("Count of influencers by platform:")
for platform, count in inf_by_platform.items():
    print(f"{platform}: {count}")   

print(inf_by_platform)
