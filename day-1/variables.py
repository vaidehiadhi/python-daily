"""4. Variables
Variables are names that store data.
Think of them as labels for boxes holding values.

Rules for naming:

Start with a letter or _

Can’t start with a number

Only letters, numbers, and _ allowed

Case-sensitive (name ≠ Name)
"""
# Examples:
age = 25
name = "Alice"
price = 99.99

print(name, "is", age, "years old.")

# Data Structures
'''
Python’s main built-in data structures:

Type	Example	Mutable?
List	[1, 2, 3]	✅ Yes
Tuple	(1, 2, 3)	❌ No
Set	{1, 2, 3}	✅ Yes (but no duplicates)
Dict	{"key": "value", "age": 25}	✅ Yes
'''
# Example:
# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coords = (10, 20)

# Set
colors = {"red", "blue", "green"}

# Dictionary
person = {"name": "John", "age": 30}