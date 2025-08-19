"""
🐍 Python match / case (Structural Pattern Matching)

Introduced in Python 3.10, match statements allow you to write cleaner and more powerful conditional logic.
They are similar to switch statements in other languages, but more advanced — they can "match patterns," not just values.
"""

#Syntax
'''
match variable:
    case pattern1:
        # do something
    case pattern2:
        # do something else
    case _:
        # default / catch-all
'''
"""
match → keyword to start the statement

case → checks for patterns (like conditions)

_ → wildcard, works like else
"""

#Example 
day = input("enter the day: ")
match day:
    case "monday" | "tuesday" | "wednesday" | "thrusday" | "friday":
        print("it is a weekday")
    case "saturday" | "sunday":
        print("it is the weekend")
    case _:
        print("invaid day")


x = [1,2,3]
match x:
    case int():
        print("it is an integer")
    case float():
        print("it sis a floating number")
    case str():
        print("it is a string")
    case bool():
        print("it is boolean value")
    case _:
        print("default")

# can use if statements to match the patterns
num = 15
match num:
    case num if num % 3 == 0:
        print("it is divisible by 3")
    case num if num % 5 == 0 and num % 15 == 0:
        print("also divisible by 5 and 15")
    case _:
        print(num)

"""
✅ Key Points to Remember

match is more powerful than switch in other languages (supports pattern matching).

_ acts like a default case.

Can match values, types, sequences, and even unpack tuples/lists.

Guards (if) allow more fine-grained control.

Only available in Python 3.10+.
"""

