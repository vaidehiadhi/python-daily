"""
1. 🔹 What is a while loop?

A while loop is used to repeat a block of code as long as a condition is True.

👉 General syntax:
while condition:
    # code block

The condition is checked before each iteration.

If the condition is True, the code inside the loop runs.

When the condition becomes False, the loop stops.
"""

#Example 
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

"""
⚡ Key points:

The loop starts with count = 1.

Runs until count <= 5 is False.

count += 1 increases the value each iteration.
"""

"""
3. 🔹 Infinite Loop

If the condition never becomes False, the loop runs forever.

while True:
    print("This will run forever!")
💡 To stop it, press Ctrl + C.
So always make sure there’s a way for the loop to end.
"""

"""
4. 🔹 Using break (exit the loop early)

The break statement stops the loop immediately.
"""

#Example 
x = 1
while x <= 10:
    print(x)
    if x == 5:
        break   # exit when x is 5
    x += 1


"""
5. 🔹 Using continue (skip an iteration)

The continue statement skips the rest of the code in the current iteration and goes back to the top.
"""

#Example 
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue  # skip even numbers
    print(x)


"""
6. 🔹 while ... else

Just like for loops, a while loop can have an else clause.

The else part runs if the loop condition becomes False.

If the loop is stopped using break, the else part does not run.
"""

#Example
x = 1
while x <= 3:
    print("Loop:", x)
    x += 1
else:
    print("Loop finished without break")

"""
7. 🔹 Nested while loops

You can put a while loop inside another while loop.
"""

#Example 
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1



i = 0
while (i<3):
    print(i)
    i = i+1
print("done")

# Decrementing loop 

count = -5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("done")


"""
8. 🔹 Common Uses of while

Repeatedly ask for user input until it’s valid.

Run until a certain condition is met.

Infinite loops with break (used in games, servers, etc.).
"""

#Example 
password = ""
while password != "python123":
    password = input("Enter password: ")

print("Access Granted!")

"""
9. 🔹 Comparing for vs while

Use for when you know exactly how many times you need to loop.

Use while when you don’t know the number of iterations in advance (loop depends on condition).
"""

#Example 
# FOR loop (fixed range)
for i in range(5):
    print(i)

# WHILE loop (depends on condition)
i = 0
while i < 5:
    print(i)
    i += 1
