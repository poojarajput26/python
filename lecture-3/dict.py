# Create Dict:

# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "course": "Computer Science"
}

# Accessing values using keys
print(student["name"])  # Output: John
print(student["age"])   # Output: 20


# add and update dict value :

student["grade"] = "A"  # Adding a new key-value pair
student["age"] = 21     # Updating an existing key

print(student)
# Output: {'name': 'John', 'age': 21, 'course': 'Computer Science', 'grade': 'A'}


# Remove elements:

del student["course"]  # Deleting a key-value pair
print(student)  
# Output: {'name': 'John', 'age': 21, 'grade': 'A'}

student.pop("grade")  # Using pop() to remove a key
print(student)
# Output: {'name': 'John', 'age': 21}


# pop example
student = {"name": "John", "age": 21, "grade": "A"}

removed_value = student.pop("grade")  # Removes 'grade' and returns its value
print(student)  # Output: {'name': 'John', 'age': 21}
print(removed_value)  # Output: A


# ************* Example ***********

"""
Create a dictionary named person with the following details:
"name" → "Alice"
"age" → 25
"city" → "New York"
"profession" → "Engineer"

Add a new key "hobby" with the value "Painting".
Update "age" to 26.
Remove "city" using pop().
Print the updated dictionary.

"""