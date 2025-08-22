def factorial(a):
    fact = 1
    i = 1
    while i <= a:
        fact = fact * i
        i = i + 1
    return fact 

print(factorial(5))

def reverse_num(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10 
    return rev 

print(reverse_num(1234))

def fibonacci():
    a, b = 0, 1
    while a <= 50:
        print(a)
        a, b = b, a + b

print(fibonacci())

def sum_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10
    return sum

print(sum_digits(1234))
