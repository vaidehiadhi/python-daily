"""
1. Strings in Python

A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

Strings are immutable, meaning you cannot change them after creation.
"""

#Example 
s1 = 'Hello'
s2 = "World"
s3 = '''Python
is fun!'''
print(s1)        # Hello
print(s2)        # World
print(s3)        # Multiline string

"""
2. String Indexing

Strings are indexed (like arrays).

Indexing starts at 0 for the first character, and you can also use negative indexing for accessing characters from the end.
"""

#Example 
word = "Python"
print(word[0])   # P (first character)
print(word[2])   # t (third character)
print(word[-1])  # n (last character)
print(word[-3])  # h (third from end)

"""
3. String Slicing

Slicing extracts a part of a string using the format:
string[start:end:step]
start → index where slice begins (default = 0)

end → index where slice stops (excluded!)

step → jump size (default = 1)
"""

#Example 
word = "Programming"

print(word[0:6])     # Progra (characters from 0 to 5)
print(word[:6])      # Progra (same as above, start is 0)
print(word[4:])      # ramming (from index 4 to end)
print(word[::2])     # Pormig (every 2nd character)
print(word[::-1])    # gnim margorP (reverse string)

"""
4. String Operations

Concatenation (+): "Hello" + "World" → "HelloWorld"

Repetition (*): "Hi" * 3 → "HiHiHi"

Membership (in): 'a' in "banana" → True
"""