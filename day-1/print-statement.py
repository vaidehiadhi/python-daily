'''2. print() Statement
The print() function displays output to the console.

Syntax:
print(*objects, sep=' ', end='\n')
*objects → items to print (can be strings, numbers, variables, etc.)
sep → how to separate multiple items (default: space ' ')
end → what to print at the end (default: newline \n)
'''
# Examples:
print("A", "B", "C")            # Output: A B C
print("A", "B", "C", sep='-')   # Output: A-B-C
print("Hello", end=' ')         # Doesn't go to new line
print("World")                  # Continues same line