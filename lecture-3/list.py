
# List of Numbers

numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # Output: 10


# List of Strings

fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana


# Mixed Data Types in a List

mixed_list = [25, "hello", 3.14, True]
print(mixed_list[2])  # Output: 3.14


# List Inside Another List (Nested List)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1]) 


# Adding & Removing Elements in a List

colors = ["red", "blue", "green"]
colors.append("yellow")  # Adds "yellow" at the end
colors.remove("blue")  # Removes "blue"
print(colors)  # Output: ['red', 'green', 'yellow']


# insert list
numbers = [1, 2, 4, 5]
numbers.insert(2, 3) 
print(numbers)


#extend list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2) 
print(list1)


#  Sorting a List

nums = [4, 1, 7, 3, 9]
nums.sort()
print(nums)  # Output: [1, 3, 4, 7, 9]


# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple

# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Removing elements
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# using pop
numbers = [10, 20, 30, 40, 50]
removed_item = numbers.pop(2)  # Removes element at index 2 (30)
print(numbers)  # Output: [10, 20, 40, 50]
print(removed_item)  # Output: 30


# using del
numbers = [10, 20, 30, 40, 50]
del numbers[1]  # Deletes element at index 1 (20)
print(numbers)


# ***********Questions ***************

# (1) Create a list with three colors.
# Print the first color from the list.

# (2) Create a list with three animals.
# Add a new animal to the list.
# Print the updated list.