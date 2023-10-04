'''Dictionaries in Python:

A dictionary is a versatile and unordered collection of key-value pairs. It is a fundamental data structure in Python and is often referred to as a "mapping" or "associative array."
 The primary characteristics of dictionaries are:

Key-Value Pairs: Dictionaries consist of pairs of keys and their associated values. Each key in a dictionary is unique, and it is used to access the corresponding value.

Unordered: Unlike lists and tuples, dictionaries are unordered, meaning there is no defined order for the key-value pairs. 
In Python 3.7 and later, dictionaries maintain insertion order (as of Python 3.7), but you should not rely on this behavior in earlier versions.

Mutable: Dictionaries are mutable, which means you can add, update, or remove key-value pairs after the dictionary is created.

Heterogeneous: Dictionaries can store values of different data types, both as keys and as values.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Here's a detailed example of creating and working with dictionaries in Python:'''

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values by keys
print(my_dict["name"])  # Output: "John"
print(my_dict["age"])   # Output: 30

# Modifying values
my_dict["age"] = 31
print(my_dict["age"])   # Output: 31

# Adding new key-value pairs
my_dict["country"] = "USA"

# Removing key-value pairs
del my_dict["city"]

# Checking for key existence
if "name" in my_dict:
    print("Name is in the dictionary.")

# Dictionary iteration
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Dictionary methods
keys = my_dict.keys()        # Get a list of keys
values = my_dict.values()    # Get a list of values
items = my_dict.items()      # Get a list of key-value pairs

# Nested dictionaries
nested_dict = {
    "person": {
        "name": "Alice",
        "age": 25
    }
}
print(nested_dict["person"]["name"])  # Output: "Alice"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' 1)Adding Items to a Dictionary:
To add a new key-value pair to an existing dictionary, you can simply assign a value to a new key:'''
my_dict = {"name": "John", "age": 30}

# Adding a new key-value pair
my_dict["city"] = "New York"

print(my_dict)
# Output: {"name": "John", "age": 30, "city": "New York"}

#You can also use the update() method to add multiple key-value pairs from another dictionary:

my_dict = {"name": "John", "age": 30}
new_data = {"city": "New York", "country": "USA"}

my_dict.update(new_data)

print(my_dict)
# Output: {"name": "John", "age": 30, "city": "New York", "country": "USA"}
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''2)Deleting Items from a Dictionary:
To remove a specific key-value pair from a dictionary, you can use the del statement:'''
my_dict = {"name": "John", "age": 30}

# Deleting the "age" key-value pair
del my_dict["age"]

print(my_dict)
# Output: {"name": "John"}

#You can also use the pop() method to remove a key-value pair and retrieve the value associated with that key:
my_dict = {"name": "John", "age": 30}

# Removing and retrieving the "age" key-value pair
removed_age = my_dict.pop("age")

print(my_dict)
# Output: {"name": "John"}
print(removed_age)
# Output: 30

#If you want to remove the last inserted key-value pair from the dictionary (since Python 3.7+), you can use the popitem() method:
my_dict = {"name": "John", "age": 30}

# Removing and retrieving the last inserted key-value pair
removed_item = my_dict.popitem()

print(my_dict)
# Output: {"name": "John"}
print(removed_item)
# Output: ('age', 30)
