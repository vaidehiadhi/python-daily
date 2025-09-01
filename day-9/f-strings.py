message = "Hello my name is {0} and i live in {1} and i am studying at {2}"
name = "vaidehi"
city = "sydney"
uni = "UNSW"
print(message.format(name, city, uni))

# same thing using f strings 

print(f"Hello my name is {name}, i live in {city}, and i study at {uni}")

"""
🔹 What is an f-string?

Introduced in Python 3.6+.

A way to embed variables or expressions directly inside strings using {}.

Start the string with f or F.
"""

name = "Amit"
print(f"Hello, {name}!")   # Output: Hello, Amit!

"""
1. Embedding Variables

You can insert variable values directly inside {}.
"""
age = 20
print(f"I am {age} years old.")   # Output: I am 20 years old.

"""
2. Expressions Inside f-strings

You can run Python expressions inside {}.
"""
a, b = 5, 3
print(f"Sum = {a+b}")       # Output: Sum = 8
print(f"Square = {a**2}")   # Output: Square = 25

"""
3. Calling Functions

Functions can also be called inside {}.
"""
def greet(name):
    return f"Hello, {name}!"

print(f"{greet('Ravi')}")   # Output: Hello, Ravi!

"""
4. Formatting Numbers

You can format numbers (decimals, percentages, etc.) using :
"""
pi = 3.1415926535
print(f"Pi = {pi:.2f}")     # Output: Pi = 3.14   (2 decimal places)

num = 1234567
print(f"{num:,}")           # Output: 1,234,567   (comma separator)

percent = 0.8567
print(f"{percent:.2%}")     # Output: 85.67%

"""
5. Formatting Width & Alignment

You can control width, alignment, and padding.
"""
name = "Python"
print(f"{name:>10}")   # Right aligned (width 10)
print(f"{name:<10}")   # Left aligned (width 10)
print(f"{name:^10}")   # Center aligned (width 10)

num = 42
print(f"{num:05}")     # Output: 00042 (padded with zeros, width 5)

"""
6. Debugging with =

Python 3.8+ introduced =, which shows both the expression and its value.
"""
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")
# Output: x=10, y=20, x+y=30

"""
7. Using Dictionaries with f-strings

Access dictionary values directly.
"""
student = {"name": "Asha", "marks": 95}
print(f"Student: {student['name']}, Marks: {student['marks']}")

"""
8. Using Lists/Tuples in f-strings

Access elements directly.
"""
fruits = ["apple", "banana", "cherry"]
print(f"My favorite fruit is {fruits[1]}")
# Output: My favorite fruit is banana

"""
9. Multiline f-strings

You can also use them with triple quotes.
"""
name = "Rahul"
age = 22
print(f"""
Name: {name}
Age: {age}
""")

"""
10. Escaping Braces

To print { or }, use double braces {{ or }}.
"""
print(f"Use {{}} to show braces in f-strings")
# Output: Use {} to show braces in f-strings

"""
✅ Summary

Start with f"" or f''.

Use {} to embed variables/expressions.

Support formatting (decimal places, alignment, padding).

Python 3.8+ allows var= for debugging.
"""
