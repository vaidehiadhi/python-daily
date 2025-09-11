# 🐍 Python Important Concepts (until Tuples)
# 1. Introduction to Python

# High-level, interpreted, dynamically typed programming language.

# No need to declare data types explicitly.

# print("Hello, Python!")

# 2. Variables and Data Types

# Variables store data in memory.

# Python is dynamically typed.

# x = 10        # integer
# y = 3.14      # float
# name = "Sam"  # string
# is_on = True  # boolean

# 3. Input and Output
# name = input("Enter your name: ")
# print("Hello", name)

# 4. Operators

# Arithmetic: + - * / % // **

# Comparison: == != > < >= <=

# Logical: and or not

# Assignment: = += -= *=

# Membership: in, not in

# a, b = 10, 3
# print(a + b)  # 13
# print(a // b) # 3 (floor division)

# 5. Conditional Statements
# age = 18
# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")

# 6. Loops

# for loop

# for i in range(5):
#     print(i)   # 0 1 2 3 4


# while loop

# n = 5
# while n > 0:
#     print(n)
#     n -= 1

# 7. Break, Continue, Pass
# for i in range(5):
#     if i == 3:
#         break      # exits loop
#     print(i)

# for i in range(5):
#     if i == 2:
#         continue   # skips iteration
#     print(i)

# for i in range(5):
#     pass           # placeholder

# 8. Functions
# def greet(name):
#     return f"Hello, {name}"

# print(greet("Sam"))

# 9. Data Structures
# (a) Strings

# Immutable, sequence of characters.

# s = "Python"
# print(s[0])        # P
# print(s.lower())   # python
# print(s[::-1])     # nohtyP

# (b) Lists

# Mutable, ordered collection.

# nums = [1, 2, 3, 4]
# nums.append(5)
# nums.remove(2)
# print(nums)        # [1, 3, 4, 5]

# (c) Tuples

# Immutable, ordered collection.

# Used when data should not be changed.

# t = (10, 20, 30)
# print(t[0])       # 10
# # t[1] = 50  ❌ error (immutable)