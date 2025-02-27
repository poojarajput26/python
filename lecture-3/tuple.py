#(1) how to change items in tuple ?
# first convert into list and change items and then convert in tuple


fruits = ("apple", "banana", "cherry")


fruits_list = list(fruits)

fruits_list[1] = "blueberry"


fruits = tuple(fruits_list)

print(fruits)  # Output: ('apple', 'blueberry', 'cherry')


# (2) remove elements in tuple:

fruits = ("apple", "banana", "cherry")

fruits_list = list(fruits)

fruits_list.remove("banana")


fruits = tuple(fruits_list)

print(fruits)  # Output: ('apple', 'cherry')


# (3) delete tuple:

fruits = ("apple", "banana", "cherry")
del fruits

