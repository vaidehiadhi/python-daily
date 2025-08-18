"""
📘 String Methods in Python
1. Changing Case

.upper() → Converts to uppercase

.lower() → Converts to lowercase

.title() → Capitalizes each word

.capitalize() → Capitalizes only the first character
"""

#Example 
s = "hello world"
print(s.upper())      # HELLO WORLD
print(s.lower())      # hello world
print(s.title())      # Hello World
print(s.capitalize()) # Hello world

"""
2. Stripping (Removing Spaces / Characters)

.strip() → Removes leading & trailing spaces (or given chars)

.lstrip() → Removes from the left only

.rstrip() → Removes from the right only
"""
#Example 
s = "   hello   "
print(s.strip())   # "hello"
print(s.lstrip())  # "hello   "
print(s.rstrip())  # "   hello"

"""
3. Finding & Counting

.find("sub") → Returns index of first occurrence (or -1 if not found)

.index("sub") → Like find, but gives error if not found

.count("sub") → Counts occurrences of substring
"""
#Example 
s = "banana"
print(s.find("na"))   # 2
print(s.index("na"))  # 2
print(s.count("a"))   # 3

"""
4. Replacing

.replace(old, new) → Replace substring with another
"""
#Example 
s = "I like cats"
print(s.replace("cats", "dogs"))  # "I like dogs"

"""
5. Splitting & Joining

.split() → Breaks string into a list

.join() → Joins list elements into a string
"""
#Example 
s = "a,b,c"
print(s.split(","))         # ['a', 'b', 'c']

words = ["Python", "is", "fun"]
print(" ".join(words))      # "Python is fun"

"""
6. Checking String Type

.startswith("sub") → Checks if string starts with substring

.endswith("sub") → Checks if string ends with substring

.isdigit() → Checks if string has only digits

.isalpha() → Only alphabets

.isalnum() → Alphabets or digits
"""
#Example 
s = "Python3"
print(s.startswith("Py"))  # True
print(s.endswith("on"))    # True
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True



