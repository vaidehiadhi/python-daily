"""
🔹 What is a Function?

A function is like a reusable "mini-program" inside your code.
Instead of writing the same code again and again, you can put it inside a function and "call" it whenever you need.

Think of it like a blender:

You put in fruits (inputs → parameters)

The blender does its job (code inside the function → logic)

You get a smoothie (output → return value)
"""

# 🔹 Basic Function Structure

# Here’s the simplest function:

def greet():
    print("hello, world!")

# def → keyword that tells Python you’re defining a function

# greet → function name

# () → parentheses (for inputs, if any)

# : → start of the function block

# Indented code inside = function body

# To use it (call the function):
greet()

"""
🔹 Functions with Parameters (Inputs)

We can pass information into a function:
"""

def greet(name):
    print(f"hello there {name}")

greet("vaidehi")
greet("bob")

"""
🔹 Functions with Return Values (Outputs)

Instead of just printing, functions can give back data using return.
"""

def add(a, b):
    return a + b

result = add(5,5)
print(result)

# Here, return hands back the value so you can store it, print it, or use it in another calculation.

def area_rect(a,b):
    area = a * b
    return area

result = area_rect(5, 2)
print(result)

"""
✅ Summary:

Define with def function_name(parameters):

Write indented code inside.

Use return if you want to give something back.

Call the function with arguments.
"""
