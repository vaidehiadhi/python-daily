"""
3. Operators in Python
Operators = Symbols that perform operations on variables/values.

| Operator | Meaning             | Example       |
| -------- | ------------------- | ------------- |
| `+`      | Addition            | `3 + 2 → 5`   |
| `-`      | Subtraction         | `5 - 3 → 2`   |
| `*`      | Multiplication      | `4 * 2 → 8`   |
| `/`      | Division (float)    | `5 / 2 → 2.5` |
| `//`     | Floor Division      | `5 // 2 → 2`  |
| `%`      | Modulus (Remainder) | `5 % 2 → 1`   |
| `**`     | Exponentiation      | `2 ** 3 → 8`  |
"""

# Example 
a, b = 10, 3
print(a + b)   # 13
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

"""
3.2 Logical Operators
| Operator | Meaning                      | Example                     |
| -------- | ---------------------------- | --------------------------- |
| `and`    | True if both are True        | `(5 > 2 and 10 > 5) → True` |
| `or`     | True if at least one is True | `(5 > 2 or 2 > 10) → True`  |
| `not`    | Inverts the result           | `not(5 > 2) → False`        |

"""

#Example 
x = 5
print(x > 3 and x < 10)  # True
print(x > 3 or x > 10)   # True
print(not(x > 3))        # False

"""
3.3 Bitwise Operators
(Bitwise = Operates on binary representation of numbers)
| Operator | Meaning            | Example       |     |         |
| -------- | ------------------ | ------------- | --- | ------- |
| `&`      | AND                | `5 & 3 → 1`   |     |         |
| \`       | \`                 | OR            | \`5 | 3 → 7\` |
| `^`      | XOR                | `5 ^ 3 → 6`   |     |         |
| `~`      | NOT (Inverts bits) | `~5 → -6`     |     |         |
| `<<`     | Left Shift         | `5 << 1 → 10` |     |         |
| `>>`     | Right Shift        | `5 >> 1 → 2`  |     |         |
"""

#Example 
a, b = 5, 3   # In binary: 101 & 011
print(a & b)  # 1  (binary: 001)
print(a | b)  # 7  (binary: 111)
print(a ^ b)  # 6  (binary: 110)
print(~a)     # -6
print(a << 1) # 10 (binary: 1010)
print(a >> 1) # 2  (binary: 10)


