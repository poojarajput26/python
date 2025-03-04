# 3) WAP to find particular string using simple for loop and simple if condition : 


# List of fruits
list1 = ["apple", "banana", "mango"]
# String we want to find
search_string = "banana"
# Using a for loop and if condition to find the string
for fruit in list1:
    if fruit == search_string:
        print(f"Found: {fruit}")
        break  # Exit the loop once the string is found
else:
    print(f"{search_string} is not in the list.")
