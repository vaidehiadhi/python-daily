# Print the square of numbers from 1 to 10.

for i in range(11):
    print(i*i)


# Loop through the string "hello" and count how many vowels are there.

word = "hello"
count = 0
for i in word:
    if i in "aeiou":
        count = count + 1
print(count)

# Use nested loops to print a multiplication table (1–5).

for i in range(6):
    for j in range(6):
        print(i*j)

# Multiplication Table
num = 5
for i in range(11):
    print(num, "*", i, "=", num*i)