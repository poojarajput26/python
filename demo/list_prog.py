
"""
Write a Python program that takes two lists and returns 
a new list containing the common elements (intersection) between them. 
Ensure that the result list contains only unique elements.
"""


def list_intersection(list1, list2):
    # Convert both lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection using the & operator
    intersection = list(set1 & set2)
    
    return intersection

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = list_intersection(list1, list2)

print("Intersection of lists:", result)
