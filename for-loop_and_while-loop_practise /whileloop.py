# Print numbers from 1 to 10 using a while loop.

i = 0 
while i<=10:
    print(i)
    i = i + 1

# Print all numbers from 50 down to 1.

i = 50
while i >= 0:
    print(i)
    i = i-1

# Keep asking the user for a password until they enter "open123".
while True:
    password = input("enter the password: ")
    if password != "open123":
        print("incorrect password")
    else:
        print("enter correct answer")
        break

# Print the sum of digits of a number, e.g. 1234 → 1+2+3+4 = 10.
num = 1234
total = 0

while num > 0:
    digit = num % 10        
    total += digit         
    num //= 10            
print(total)

# Print the factorial of a given number using a while loop.

num = 5 | factorial = 1 |i = 1
while i <= num:
    factorial *= i   
    i += 1  
print("Factorial of", num, "is", factorial)

# Print the Fibonacci sequence up to 100 using a while loop.
a, b = 0, 1

while a <= 100:
    print(a)
    a, b = b, a + b 

# Keep asking the user to enter numbers and stop only when they type "stop".

while True:
    user_input = input("Enter a number (or type 'stop' to quit): ")
    
    if user_input.lower() == "stop": 
        print("ok stopped")
        break
    else:
        num = int(user_input)
        print("You entered:", num)

