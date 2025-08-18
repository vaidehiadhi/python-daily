# if-else statement to check whether a person can drive or not 
age = int(input("Enter your age: "))
print("Your age is", age)

if age > 18:
    print(f"You can drive since you are {age} years old ")
else:
    print(f"You cannot drive since you are only {age} years old")


#Simple if-else example 
apple_price = 210
budget_price = 200

if apple_price <= budget_price:
    print("add to cart")
else:
    print("increase the budget or buy bananas")


#elif Example
num = int(input("enter a number b/w 0-9: "))
print(num)

if num > 0:
    print("valid")
elif num == 0:
    print("valid")
elif num == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    print("also valid")
else:
    print("enter a valid number b/w 0-9")

#elif example-2
num = int(input("enter a number: "))
if num < 0:
    print("nagative number")
elif num == 0:
    print("zero number")
else:
    print("positive number")

"""
📝 Practice Problem 1:

Write a program that takes a number x and:

Prints "Positive" if the number is greater than 0

Prints "Negative" if the number is less than 0

Prints "Zero" if the number is exactly 0

👉 What will the program print if x = -8?
"""

x = int(input("Enter a number: "))
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")


"""
📝 Practice Problem 2:

Write a program that takes an integer age and:

Prints "Child" if age < 13

Prints "Teenager" if 13 ≤ age < 20

Prints "Adult" if age ≥ 20

👉 What will your program print if age = 15?
"""
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 13 or age < 20:
    print("Teenager")
else:
    print("Adult")


"""
📝 Practice Problem 3 (Nested if):

Write a program that takes a number x and:

If x is positive, check if it’s even or odd:

Print "Positive Even" if it’s even

Print "Positive Odd" if it’s odd

If x is 0, print "Zero"

If x is negative, print "Negative"

👉 What will your program print if x = 14?
""" 

x = int(input("enter a number: "))
if x > 0:
    if x % 2 == 0:
        print("Positive Even")
    else:
        print("Positive odd")
elif x == 0:
    print("zero")
else:
    print("Negative")





