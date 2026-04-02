single_quote = 'miele'
double_quote = "miele"
triple_quote = """m
i
e
l
e"""

print(single_quote)
print("double_quote:",double_quote)
print(f"triple_quote:\n{triple_quote}")



text = "Miele is three years old"

print(text[0])
print(text[-1])
print(text[0:9])
print(text[:15])
print(text[9:])

print(len(text))
print(text.strip())
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("Miele","Jason"))



name = "Miele"
age = "three"

message_1 = f"My name is {name} and I am {age} years old."
message_2 = "My name is {} and I am {} years old.".format(name, age)
message_3 = "My name is %s and I am %s years old." % (name, age)

print(message_1)
print(message_2)
print(message_3)

print(f"My name is {name} and I am {age} years old.")

print(f"message_1:\n{message_1}")
print(f"message_2:\n{message_2}")
print(f"message_3:\n{message_3}")



paragraph = """Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

#Word Count
words = paragraph.split()
word_count = len(words)

#Character Count
character_count = len(paragraph)

#Sentence Count
sentence_count = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')

print("Word Count:", word_count)
print("Characters Count:", character_count)
print("Sentence Count:", sentence_count)

