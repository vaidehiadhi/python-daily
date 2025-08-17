# 1. Greeting
name = input("Enter your name: ")
print(f"Hello {name}, welcome to Python!")

# 2. Decimal → Integer
x = float(input("Enter a decimal number: "))
print(int(x))

# 3. Multiply two integers
a, b = map(int, input("Enter the numbers: ").split())
print(a * b)

# 4. String number → Float with 2 decimals
c = float(input("Enter the number: "))
print(f"{c:.2f}")

print(2 ** 3 ** 2)