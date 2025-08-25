# 1. 🔹 What is a List?
# A list in Python is a mutable, ordered collection of elements.

# It can store different data types (integers, strings, floats, booleans, even other lists).

# Lists are defined using square brackets [ ].

list = [10, "hello", 3.14, True]

# 2. 🔹 Creating Lists

# Empty lists
list = []

# numeric lists 
num_list = [1, 2, 3, 4, 5]

# mixed data types
mixed = ["hello", 1, 3, 6.82, False]

#nested lists 
list_in = [1,2,3,[3,4,5]]

#using list()
# nums = list((1,2,3))

# 3. 🔹 Accessing List Elements

# Lists are indexed (positions start at 0).

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# 4. 🔹 Slicing Lists
nums = [10, 20, 30, 40, 50]
print(nums[1:4]) #[20, 30, 40]
print(nums[:3]) #[10, 20, 30]
print(nums[2:]) #[30, 40, 50]
print(nums[::2]) #[10, 30, 50]

# 5. 🔹 Modifying Lists

# Lists are mutable → you can change them after creation.

fruits1 = ["apple", "banana", "cherry"]
fruits1[1] = "blueberry"
print(fruits1) #["apple", "blueberry", "cherry"]

#adding new items 
fruits1.append("guava") # adds to the end of the list os ["apple", "blueberry", "cherry", "guava"]
fruits1.insert(2, "jammon")

# 6. 🔹 Removing Items

fruits2 = ["apple", "banana", "cherry", "banana"]
fruits2.remove("banana") #removes the first occurance of banana 
fruits2.pop(1) #removes at index position 1
fruits2.pop() #removes the last element 
del fruits2[0] #deletes the item at 0
fruits.clear() #empties the list 

# 7. 🔹 Searching in Lists
numbers = [10, 20, 30, 40, 20]

print(20 in numbers)        # True
print(numbers.index(30))    # 2 (first index of 30)
print(numbers.count(20))    # 2 (number of times 20 appears)

# 8. 🔹 Sorting & Reversing
nums = [4, 1, 7, 3, 9]

nums.sort()         # [1, 3, 4, 7, 9] (ascending)
nums.sort(reverse=True)  # [9, 7, 4, 3, 1]

words = ["banana", "apple", "cherry"]
words.sort(key=len)  # sort by length

nums.reverse()      # reverses the list

# 9. 🔹 Copying Lists
# ⚠️ Direct assignment creates a reference, not a copy!
a = [1, 2, 3]
b = a               # same list reference
c = a.copy()        # shallow copy
# d = list(a)         # another shallow copy

# 10. 🔹 List Comprehensions

value = [i for i in range(5) ]
print(value)

square = [i*i for i in range(10)]
print(square)

condition = [i*i for i in range(10) if i%2 == 0]
print(condition)

pairs = [(x, y) for x in [1,2] for y in [3,4]]
print(pairs)









