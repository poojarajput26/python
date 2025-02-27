# (1) Create a list with three colors.
# Print the first color from the list.

# Create a list of colors
colors = ["Red", "Blue", "Green"]

# Print the first color
print("The first color is:", colors[0])

# OUTPUT : 
The first color is: Red


# (2) Create a list with three animals.
# Add a new animal to the list (without asking the user).
# Print the updated list.

# Create a list of animals
animals = ["Cat", "Dog", "Elephant"]

# Add a new animal (without user input)
animals.append("Lion")

# Print the updated list
print("Updated list:", animals)


# (3) Merging the list (+ Operator ):

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2 
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]


# (4) merge list (extend() Method)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2) 
print(list1)  # Output: [1, 2, 3, 4, 5, 6]


### Task find a item in multiple list

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Second list (index 1)
second_list = matrix[1]  
print(second_list)  # Output: [4, 5, 6]

item = matrix[1][0]  
print(item)  # Output: 4

item2 = matrix[1][2]
print(item2)  # Output: 6
