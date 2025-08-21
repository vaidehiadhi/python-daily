# Functions are used to repeat a logic code multiple times

"""
for example lets take the below example of calculating the geometric mean of numbers a, b and c, d
"""

# a = 6
# b = 7
# gmean = (a*b)/(a+b)
# print(gmean)

# c = 8
# d = 9
# gmean = (c*d)/(c+d)
# print(gmean)

"""
notice is the above code we have repeated the logic for just different numbers for cases like these and more complex code we can use functions 
"""

def gmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

gmean(6, 7)
gmean(8, 9)

def greater_num(a, b):
    if a > b:
        print(a ,"is greater")
    else:
        print(b ,"is greater")

greater_num(6, 7)
greater_num(8, 9)

"""
here we used functions and solved the same example in a simpler way 
"""

def lesser_num(a,b):
    pass                #pass is used to write the function later so that you dont get an error 