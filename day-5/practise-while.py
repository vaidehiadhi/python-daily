# Counting Up
# Write a while loop that prints numbers from 1 to 10.

i = 0
while i <= 10:
    print(i)
    i = i+1

# Countdown
# Write a while loop that prints numbers from 10 down to 1, then prints "Blast off!".

i = 10
while i >= 1:
    print(i)
    i = i - 1
print("Blast off!")

# Sum of Numbers
# Use a while loop to calculate the sum of numbers from 1 to 100.

i = 1
sum = 0
while i <= 100:
    sum = sum + i 
    i = i + 1
    print(sum)

# Multiplication Table
# Ask the user for a number (e.g., 5) and use a while loop to print its multiplication table up to 10.

num = int(input("enter the number: "))
i = 1
while i <= 10:
    print("5 X", i, "=", num * i)
    i = i + 1

# Guess the Number
# Write a program that keeps asking the user to guess a number until they guess it correctly.
# (Hint: Use while with input and break when correct.)

while True:
    password = input("enter you password: ")
    if password != "happy birthday!":
        print("incorrect password")
    else:
        print("correct password")
        break 

# Reverse Digits
# Use a while loop to reverse the digits of a number.
# Example: If the input is 1234, the output should be 4321.

num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10 
print(rev)

