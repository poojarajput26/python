# Creating a Set

# Creating a set
fruits = {"apple", "banana", "cherry"}

print(fruits)  # Output: {'apple', 'banana', 'cherry'}


# Duplicate Elements Are Not Allowed

numbers = {1, 2, 3, 4, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5} (4 appears only once)


# Adding Elements (add())

fruits = {"apple", "banana"}
fruits.add("orange")  # Adds 'orange' to the set
print(fruits)  # Output: {'apple', 'banana', 'orange'}


# Removing Elements (remove() & discard())

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")  # Removes 'banana'
# fruits.remove("grape")  #  Error: 'grape' is not in the set

fruits.discard("grape")  # No error, does nothing if item not found
print(fruits)  # Output: {'apple', 'cherry'}


# Union (| or union() Method)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # {1, 2, 3, 4, 5}
print(union_set)


# Intersection (& or intersection())

intersection_set = set1 & set2  # {3}
print(intersection_set)


# Difference (- or difference())

difference_set = set1 - set2  # {1, 2} (Elements in set1 but not in set2)
print(difference_set)


# Checking Membership in a Set

fruits = {"apple", "banana", "cherry"}

print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False

