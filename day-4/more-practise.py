"""
📝 Tricky Question 1:

Write a program that takes a year as input and checks if it’s a leap year.

👉 Rules for leap year:

A year is a leap year if it is divisible by 4 and not divisible by 100, OR if it is divisible by 400.

Examples:

2000 → Leap year

1900 → Not a leap year

2024 → Leap year

👉 What will your program print if the input is 1900?
"""

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a Leap year")
else:
    print("Not Leap Year")


"""
📝 Tricky Question 2: Grading System

Write a program that takes a student’s marks (0–100) and prints the grade:

90 and above → Grade A

75 to 89 → Grade B

50 to 74 → Grade C

Below 50 → Fail

👉 Example:

Input: 92 → Output: Grade A

Input: 68 → Output: Grade C

👉 Now, what will your program print if the input is 76?
"""

marks = int(input("enter student's marks (0-100): "))
if marks >= 90:
    print("Grade A")
elif marks >= 75 and marks <= 89:
    print("Grade B")
elif marks >=50 and marks <= 74:
    print("Grade C")
else:
    print("Fail")

"""
📝 Tricky Question 3: Divisibility Check

Write a program that takes a number x and:

If the number is divisible by 2, 3, and 5 → print "Divisible by 2, 3 and 5"

If it is divisible by only 2 and 3 → print "Divisible by 2 and 3"

If it is divisible by only 2 → print "Divisible by 2"

If it is not divisible by any of them → print "Not divisible by 2, 3 or 5"

👉 Example:

Input: 30 → Output: Divisible by 2, 3 and 5

Input: 6 → Output: Divisible by 2 and 3

Input: 4 → Output: Divisible by 2

Input: 7 → Output: Not divisible by 2, 3 or 5
"""

x = int(input("Enter the number: "))

if x % 2 == 0 and x % 3 == 0 and x % 5 == 0:
    print("Divisible by 2, 3 and 5")
elif x % 2 == 0 and x % 3 == 0:
    print("Divisible by 2 and 3")
elif x % 2 == 0:
    print("Divisible by 2")
elif x % 3 == 0 and x % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 2, 3 or 5")

# Triangle 

x = int(input("enter the first side of the triangle: "))
y = int(input("enter the second side of the triangle: "))
z = int(input("enter the third side of the triangle: "))

if x==y and y==z:
    print("Equilateral")
elif x==y or y==z or z==x:
    print("Isosceles")
else:
    print("Obtuse")