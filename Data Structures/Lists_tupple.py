'''List as a Data Structure: A list in Python is a data structure that allows you to store a collection of items.
    These items can be of any data type, such as integers, strings, or even other lists. Lists are ordered, which means the order of elements in a list is preserved,
    and you can access elements by their position (index) in the list.
    Mutable: Lists in Python are mutable, which means you can modify their contents. You can add, remove, or change elements within a list after it has been created.
    This mutability distinguishes lists from some other data structures like tuples, which are immutable (cannot be changed once created).
    Here's a simple example of creating and manipulating a list in Python: '''

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[1] = 6
print(my_list)  # Output: [1, 6, 3, 4, 5]

# Adding elements
my_list.append(7)
print(my_list)  # Output: [1, 6, 3, 4, 5, 7]

# Removing elements
my_list.remove(3)
print(my_list)  # Output: [1, 6, 4, 5, 7]


'''In addition to basic operations like appending and removing elements, 
lists also support a wide range of operations and methods for more advanced manipulation, 
such as slicing, concatenation, sorting, and more.
Lists are a versatile and frequently used data structure in Python, making them essential for many programming tasks.'''

#1)Slicing: Slicing allows you to extract a portion of a list. You can specify a start and end index to create a new list containing elements from the original list within that range.
my_list = [1, 2, 3, 4, 5]

# Extract elements from index 1 to 3 (exclusive)
sliced_list = my_list[1:4]
print(sliced_list)  # Output: [2, 3, 4]

#2)Concatenation: You can concatenate (combine) two or more lists using the + operator.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

#3)Sorting: You can sort a list in ascending order using the sort() method or create a sorted copy using the sorted() function.

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sort the list in-place
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Create a sorted copy of the list
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

#4)Counting: You can count the number of occurrences of a specific element in a list using the count() method.

my_list = [1, 2, 2, 3, 2, 4, 2, 5]

count_of_2 = my_list.count(2)
print(count_of_2)  # Output: 4

#5)List Comprehensions: List comprehensions are a concise way to create new lists by applying an expression to each item in an existing list.

original_list = [1, 2, 3, 4, 5]

# Create a new list containing squares of elements from the original list
squared_list = [x**2 for x in original_list]
print(squared_list)  # Output: [1, 4, 9, 16, 25]

#-------------------------------------------------------------------------------------------------------------------------------------------------

'''Tuples in Python:

A tuple is a collection or ordered sequence of elements, similar to a list, but with a few key differences. The primary characteristics of tuples are:

Ordered: Tuples, like lists, maintain the order of elements, which means the position of each element within the tuple is preserved.

Immutable: One of the key distinctions between tuples and lists is that tuples are immutable. 
Once you create a tuple, you cannot change its contents (add, remove, or modify elements). 
This immutability makes tuples suitable for situations where you want to ensure that the data remains constant.

Heterogeneous: Tuples can contain elements of different data types, just like lists. You can have integers, strings, floats, or even other tuples as elements within a tuple.

Here's a simple example of creating and working with tuples in Python:'''

# Creating a tuple
my_tuple = (1, 2, 3, "Hello", 4.5)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Tuple is immutable, so you cannot modify its elements
# This will result in an error: my_tuple[0] = 10

# Slicing
sliced_tuple = my_tuple[1:4]
print(sliced_tuple)  # Output: (2, 3, "Hello")

# Concatenation
tuple1 = (1, 2)
tuple2 = ("a", "b")
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, "a", "b")


'''Since tuples are immutable,
 they are often used when you need to represent a collection of values that should not change throughout the program's execution.
 This immutability can provide safety and guarantees about the integrity of the data.'''