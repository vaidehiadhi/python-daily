"""🔹 What is a Docstring?

A docstring is a string literal written just after the definition of a function, class, or module.

Used to document what the code does.
"""
# Enclosed in triple quotes (""" or '''), so it can span multiple lines.

"""
1. Function Docstrings

Placed right after the def line to explain what the function does.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(add.__doc__)  
# Output: Return the sum of a and b.

"""
2. Multi-line Function Docstring

Explain purpose, parameters, and return value.
"""
def greet(name, age):
    """
    Greet the user with their name and age.

    Parameters:
        name (str): The person's name.
        age (int): The person's age.

    Returns:
        str: A greeting message.
    """
    return f"Hello {name}, you are {age} years old."


"""
3. Module Docstrings

At the top of a file, describe what the module contains.
"""
"""
This module provides math utility functions
like addition, subtraction, and multiplication.
"""

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

# 4. Class Docstrings

# Placed inside a class to describe its purpose.

class Student:
    """
    A class to represent a student.

    Attributes:
        name (str): Name of the student
        age (int): Age of the student
    """

    def __init__(self, name, age):
        """Initialize student with name and age."""
        self.name = name
        self.age = age

"""
5. Accessing Docstrings

Use the .__doc__ attribute.
"""

print(Student.__doc__)
print(Student.__init__.__doc__)

"""
6. Conventions (PEP 257)

Start with a short summary (first line).

Add more details if needed (next lines).
"""
# Use triple quotes (""").

# First letter capitalized, end with a period.

"""
7. Difference between Comments and Docstrings

Comments (#): For developers, ignored by Python.
"""
# Docstrings ("""): Stored in program, can be accessed at runtime (__doc__), useful for documentation tools.

# ✅ Summary

# Docstrings are for documentation (functions, classes, modules).

# Always use triple quotes """.

# Can be single-line or multi-line.

# Access using .__doc__.

# Follow PEP 257 style guide.

