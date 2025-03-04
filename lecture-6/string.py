# # Creating string : 
# string1 = "Hello, Python!"
# print(string1)


# # Accessing Characters in a String : Strings can be accessed using indexing and slicing.
# text = "Python"
# print(text[0])  # First character
# print(text[-1])  # Last character


# # Slicing (Access a Range of Characters):
# text = "Python"
# # print(text[0:5])   # 'Pyth' (first 4 characters)
# # print(text[1:5])    # Same as text[0:4]
# print(text[2:])    # 'thon' (from index 2 to end)
# print(text[-3:])   # 'hon' (last 3 characters)


# #  Modifying Strings (Convert to Upper & Lower Case) :
# text = "Hello Python"
# print(text.upper())  # Convert to uppercase (Capital)
# print(text.lower())  # Convert to lowercase (small)

# hello = "my name is deep. hello how are you"
# print(hello.upper())
# print(hello.capitalize())

# # Replace a Substring : 
# text = "I love Python"
# print(text.replace("love", "like"))  # Replace 'love' with 'like'


# # Removing Spaces : 
# text = "  Python  "
# print(text.strip())  # Remove spaces from both sides
# print(text.lstrip())  # Remove left-side spaces
# print(text.rstrip())  # Remove right-side spaces


# # String Concatenation & Repetition : 
# str1 = "Hello"
# str2 = "World"
# print(str1 + " " + str2)  # Concatenation
# print(str1 * 3)  # Repeat string 3 times
# OUT-PUT :  Hello World
# HelloHelloHello
# print((str1 + " ") * 3)



# # Splitting & Joining Strings : 
# text = "apple,banana,mango"
# print(text.split(","))  # Split at commas
# OUT-PUT : ['apple', 'banana', 'mango']


# # Joining a List into a String : 
# words = ['apple', 'banana', 'mango']
# print("*".join(words))  # Join with hyphen
# OUT-PUT : apple-banana-mango


# # Check if a String Contains a Substring : 
# text = "Python programming"
# print("Python" in text)  # Returns True
# print("Java" in text)    # Returns False
# OUT-PUT : True
# False


# Find Position of a Substring : 
# text = "I love Python"
# print(text.find("love"))  # Returns starting index of 'Python'
# OUT-PUT : 7

# Using format() Method : 
# name = "John"
# age = 25
# print("My name is {} and I am {} years old.".format(name, age))
# print(f"My name is {name} and I am {age} old...")
# OUT-PUT : My name is John and I am 25 years old.


# # Using f-strings : 
# name = "John"
# age = 25
# print(f"My name is {name} and I am {age} years old.")


# # Reversing a String : 
# text = "Python"
# print(text[::-1])  # Reverse string using slicing
# OUT-PUT: nohtyP


# Counting Occurrences : used in count
# text = "banana"
# print(text.count("n"))# Count occurrences of 'a'
# OUT-PUT : 3


# Checking String Properties : 
# text = "Python123"
# print(text.isalpha())  # False (contains numbers)
# print(text.isdigit())  # False (contains letters)
# print(text.isalnum())  # True (contains only letters & numbers)
# print(text.isspace())  # False (not only spaces)
# print(text.islower())  # False (has uppercase letters)
# print(text.isupper())  # False (has lowercase letters)

# Accessing Strings : 

# text = "Python"
# for char in text:
#     print(char)

#  Using while loop : 
# text = "Python"
# i = 0
# while i < len(text):
#     print(text[i])
#     i += 1


# Checking if a Character Exists in a String :
# text = "Python Programming"
# print("P" in text)     # True
# print("z" in text)     # False
# print("Python" in text)  # True
# print("Java" not in text)  # True
