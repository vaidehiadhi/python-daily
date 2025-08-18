"""
Notes: Conditional Statements in Python
1. if Statement

Used to check a condition.

If condition is True, block executes.
"""
#Example 
x = 10
if x > 5:
    print("x is greater than 5")

"""
2. if-else

Executes one block if condition is True, otherwise executes another block.
"""
#Example
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

"""
3. if-elif-else

Used when you have multiple conditions to check.

elif stands for else if.
"""
#Example
x = 10
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
elif x < 10:
    print("Small number")
else:
    print("Large number")

"""
4. Nested if

You can put an if statement inside another if.

Useful when checking multiple levels of conditions.
"""
#Example 
x = 15
if x > 0:
    if x % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")

"""
5. Important Notes

Indentation (spaces) is very important in Python.

Any non-zero value or non-empty string is treated as True.

You can use comparison operators (>, <, >=, <=, ==, !=) and logical operators (and, or, not) in conditions.
"""