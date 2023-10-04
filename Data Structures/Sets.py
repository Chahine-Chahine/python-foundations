'''In Python, a set is a built-in data type used to store a collection of unique and unordered elements. Sets are similar to lists and tuples in that they can store multiple items, but unlike lists and tuples, sets do not allow duplicate values. This uniqueness property makes sets useful in various scenarios where you need to ensure that each element in the collection is unique.

Key characteristics of sets in Python:

Uniqueness: Sets cannot contain duplicate elements. If you attempt to add a duplicate element to a set, it will be ignored.

Unordered: Elements in a set have no specific order. You cannot access elements by their position (index) within the set.

Mutable: Sets are mutable, meaning you can add or remove elements after creating a set.

Heterogeneous: Sets can store elements of different data types.

Here's how you can create and work with sets in Python:

'''

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)

# Removing elements from a set
my_set.remove(3)  # Raises an error if the element is not found
my_set.discard(7)  # Removes the element if it exists, no error if not found

# Checking for the existence of an element
if 4 in my_set:
    print("4 is in the set.")

# Iterating through a set
for element in my_set:
    print(element)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)  # Union of two sets
intersection_set = set1.intersection(set2)  # Intersection of two sets
difference_set = set1.difference(set2)  # Set1 - Set2
symmetric_difference_set = set1.symmetric_difference(set2)  # Elements not in both sets

# Creating an empty set
empty_set = set()

# Converting a list to a set to remove duplicates
my_list = [1, 2, 2, 3, 3, 4]
unique_set = set(my_list)

print(unique_set)  # Output: {1, 2, 3, 4}


'''Sets are commonly used in Python for tasks that involve checking for the existence of unique elements, 
removing duplicates from a list, and performing set operations like union, intersection, and difference between two sets. 
They provide an efficient way to work with collections of unique values.'''