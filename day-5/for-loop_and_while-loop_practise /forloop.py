# Print numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)

# Print the squares of numbers from 1 to 15.
for i in range(1, 16):
    print(i, "square is", i*i)

# Print the multiplication table of 7 (from 7 × 1 up to 7 × 10).

for i in range(1, 11):
    print("7 X", i, "=", 7*i)

# Given a list:

# fruits = ["apple", "banana", "cherry", "mango"]


# Print each fruit in uppercase.

fruits = ["apple", "banana", "cherry", "mango"]
for i in fruits:
    print(i.upper())

# Print all even numbers between 1 and 50.

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Calculate the sum of numbers from 1 to 100 using a for loop.

sum = 0
for i in range(1, 101):
    sum = sum +i
    print(sum)

# Print a right triangle pattern of stars with 5 rows:

# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

# Print all characters of the string "python" in reverse order using a for loop.

word = "python"
for i in range(len(word)-1, -1, -1):
    print(word[i])