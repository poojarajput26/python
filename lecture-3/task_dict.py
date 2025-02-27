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

OUT-PUT : {'name': 'Alice', 'age': 26, 'profession': 'Engineer', 'hobby': 'Painting'}


# Step 1: Create dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "profession": "Engineer"
}

# Step 2: Add a new key-value pair
person["hobby"] = "Painting"

# Step 3: Update age
person["age"] = 26

# Step 4: Remove city using pop()
person.pop("city")

# Step 5: Print updated dictionary
print(person)
