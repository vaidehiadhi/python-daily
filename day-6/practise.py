def calculate(a,b, symbol):
    if symbol == "+" :
        return a + b
    elif symbol == "-":
        return a - b
    elif symbol == "*" :
        return a * b
    elif symbol == "%" :
        return a % b
    elif symbol == "/" :
        return a/b
    else:
        return "invalid symbol"
a = int(input("enter the first number: "))   
b = int(input("enter the second number: "))
symbol = input("enter the symbol: ")
print(calculate(a, b, symbol))


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum/len(numbers))

average(5,2)


# Write a function square(num) that returns the square of a number.
# Call it with 5 and print the result.

def square_num(a):
    return a * a

print(square_num(5))

# Write a function greet(name="Guest") that prints a greeting.
# Call it once with a name and once without passing anything.

def greet(name = "Guest"):
    print(name)

greet("Alice")
greet()

# Write a function add_numbers(a, b=10) that returns the sum.

# Call it with two arguments (e.g., add_numbers(5, 7))

# Call it with only one argument (e.g., add_numbers(5))

def add_numbers(a, b= 10):
    return a + b

print(add_numbers(5, 7))
print(add_numbers(5))

# Write a function introduce(name, age) that takes keyword arguments.

def introduce(name, age):
    return name, age 

print(introduce(age= 22, name= "vaidehi"))

# Write a function multiply_all(*args) that multiplies any number of numbers passed to it.

def multiply_all(*args): # since it is a tuple you have to iterate 
    mul = 1 
    for i in args:
        mul = mul * i
    return mul
print(multiply_all(3,4,5,6))