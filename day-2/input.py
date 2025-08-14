"""
2. Taking Input in Python
Using input() function
input() takes user input as a string by default.
"""
# syntax
# variable = input("enter the text you want to displayed on the console")

#Example 
a = input("enter your name")
print("my name is", a)

#numeric input 
b = int(input("enter your first number")) #you can either type cast it in front of the input function since the default is string
c = input("enter your second number")
print(b + int(c)) #or you can type cast it here 

#Multiple inputs 
v, g = input("enter the numbers").split()
print(int(v)+int(g))