"""
📘 Python Tuples – Complete Notes
1. What is a Tuple?

A tuple is an ordered, immutable collection of items in Python.

Defined using parentheses ( ).

Can hold mixed data types (int, str, list, dict, etc.).
"""

# Examples
t1 = (1, 2, 3)               # tuple of integers
t2 = ("a", "b", "c")         # tuple of strings
t3 = (1, "hello", 3.5)       # mixed types
t4 = (1, [2, 3], (4, 5))     # nested tuple

"""
✅ Ordered
✅ Immutable
✅ Can contain duplicates
✅ Hashable if all elements inside are hashable
"""

# 2. Creating Tuples

t = ()                # empty tuple
t = (10,)             # single-element tuple (note the comma!)
t = 10, 20, 30        # tuple without parentheses (tuple packing)
a, b, c = t           # tuple unpacking

# 3. Tuple Indexing & Slicing

t = (10, 20, 30, 40, 50)

print(t[0])       # 10 (first element)
print(t[-1])      # 50 (last element)
print(t[1:4])     # (20, 30, 40)
print(t[::-1])    # (50, 40, 30, 20, 10) reversed

# 4. Immutability

# Tuples cannot be changed after creation.

t = (1, 2, 3)
# t[0] = 100 ❌ -> TypeError

# But if a tuple contains a mutable object (like a list), that object can be changed:

t = (1, [2, 3], 4)
t[1][0] = 99
print(t)   # (1, [99, 3], 4)

# 5. Tuple Methods

# Tuples have only two built-in methods:

t = (1, 2, 3, 2, 2, 4)

print(t.count(2))   # 3 (occurrences of 2)
print(t.index(3))   # 2 (first occurrence of 3)

# 6. Tuple Operations

# Concatenation
a = (1, 2) + (3, 4)     # (1, 2, 3, 4)

# Repetition
b = ("hi",) * 3         # ('hi', 'hi', 'hi')

# Membership test
print(2 in (1, 2, 3))   # True

# Length
print(len((1, 2, 3)))   # 3

# Min, Max, Sum (only for numeric tuples)
nums = (4, 7, 1, 9)
print(min(nums))  # 1
print(max(nums))  # 9
print(sum(nums))  # 21


# 7. Tuple Packing & Unpacking

# Packing
t = 1, "apple", 3.14
print(t)   # (1, 'apple', 3.14)

# Unpacking
a, b, c = t
print(a, b, c)   # 1 apple 3.14

# Extended unpacking
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a)   # 1
print(b)   # [2, 3, 4]
print(c)   # 5

# 8. Nested Tuples

nested = ((1, 2), (3, 4), (5, 6))
print(nested[1])     # (3, 4)
print(nested[1][0])  # 3


# 9. Tuples vs Lists

# | Feature         | Tuple `( )`            | List `[ ]`                  |
# | --------------- | ---------------------- | --------------------------- |
# | **Mutable**     | ❌ Immutable            | ✅ Mutable                   |
# | **Performance** | Faster (less memory)   | Slower                      |
# | **Methods**     | Few (`count`, `index`) | Many (append, remove, etc.) |
# | **Use Case**    | Fixed data, constants  | Dynamic data                |

# 10. Useful Functions with Tuples

t = (1, 2, 3, 4)

print(all(t))      # True (all non-zero/True)
print(any(t))      # True (at least one True)
print(sorted(t))   # [1, 2, 3, 4] (returns a list)
print(tuple("abc"))# ('a', 'b', 'c')

# 12. When to Use Tuples?

# When you want immutable data (e.g., constants).

# As dictionary keys (since tuples are hashable if they only contain hashable types).

# When you need faster performance than lists.

# For returning multiple values from functions.

def min_max(nums):
    return (min(nums), max(nums))

result = min_max([5, 2, 9, 1])
print(result)   # (1, 9)

"""
✨ Summary

Tuples are ordered, immutable, hashable collections.

Faster than lists, used for fixed collections.

Support packing, unpacking, indexing, slicing.

Only two methods: count(), index().

Useful in data integrity, function returns, dictionary keys.
"""