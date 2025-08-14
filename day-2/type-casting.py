'''
1. Typecasting in Python
Typecasting = Converting one data type into another.

Types of Typecasting
1.1 Implicit Typecasting (Type Conversion by Python Automatically)
Done automatically by Python when safe (no data loss).

'''
# Example:
a = 5
b = 2.5
c = a + b
print(c) # python converts automatically to the higher data type to minimize data loss

"""
1.2 Explicit Typecasting (Manual Conversion)
Done by using functions: int(), float(), str(), list(), tuple(), etc.
"""
# Example:
x = 100
y = 6
z = x + float(y) #int to float using float()
print(z)

d = "100"
e = "32"
print(int(d) + int(e)) #string to int using int()


