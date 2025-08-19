"""
📘 Python for Loops — Detailed Notes
1. What is a for loop?

A for loop is used to iterate (loop) over a sequence (like a list, tuple, string, dictionary, or range).

It allows you to repeat a block of code multiple times, once for each element in the sequence.
"""
#syntax
# for variable in sequence:
    # code block

# looping over list 
list = ["apple", "banana", "cherry"]
for i in list:
    print(i)


"""
3. Using range() with for

range(start, stop, step) generates a sequence of numbers.

Commonly used when you want to repeat something a specific number of times.
"""

for i in range(10): # n-1
    print(i)

for i in range(1, 15, 3): #(start, end, step)
    print(i)

"""
Looping thru string
"""

name = input("enter your name: ")
for i in name:
    print(i)

"""
5. Looping through a Dictionary
"""

person = {"name": "vaidehi", "age": 22, "city": "sydney"}
for i in person:
    print(i, ":", person[i])

# Using .items() is even cleaner:
for key, value in person.items():
    print(key, ":", value)

"""
6. Nested for Loops

A loop inside another loop.
"""

colors = ["red", "green", "blue"]
objects = ["car", "pen"]

for color in colors:
    for obj in objects:
        print(color, obj)

"""
7. Using break and continue

break: Exit the loop completely.

continue: Skip the current iteration and move to the next one.
"""

# break
for num in range(1, 6):
    if num == 3:
        break
    print(num)

# continue
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

"""
8. The else clause in a for loop

The else block runs after the loop finishes normally (without a break).
"""

for i in range(5):
    print(i)
else:
    print("Loop finished successfully!")


"""
9. Loop with enumerate()

enumerate() gives you both index and value.
"""

list = ["a", "b", "c"]
for index, name in enumerate(list):
    print(index, name)

"""
10. Loop with zip()

Loop over two (or more) lists at the same time.
"""

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, "scored", score)




