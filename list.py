list1 = [1, 2, "hello", "4"]
# print(list1[1:4])

list1.append(4)
# print(list1)

list2 = list1.copy()
# print(list2)

list1.clear()
# print(list1)

# print(list2.count(4))
# print(list2.count('4'))

list1.insert(0, 'g')
list1.insert(1, 'k')
# print(list1[0])

list1.extend(list2)
# print(list1)

# print(list1.count(4))

list1.remove("4")
# print(list1)

list1.pop()
# print(list1)

del list1[0]
# print(list1)

# print("apple" in list1)
# print(list2)
list2.reverse()
# print(list2)

# list2.sort()  # cannot be sorted bcz of mixed data types in the list
# print(list2)

list3 = [1, 5, 3, 4, 2]
list3.sort()    # this is inplace sorting in ascending order
list3.sort(reverse=True)   # this is inplace sorting in descending order
# print(list3)
sorted(list3, reverse=True)  # this is non-inplace sorting in descending order
# print(list3)   

list4 = ["apple", "banana", "kiwi", "mango", "kiwi", "orange"]
# print(list4.index("kiwi"))   # returns the index of the first occurrence of "kiwi"
# print(list4.index("kiwi", 3))  # returns the index of "kiwi" starting from index 3
# print(list4.index("kiwi", 0, 1))  # raises ValueError if "kiwi" is not found in the specified range   

# print(sum(list3))

# print(type(list3))  

# print(list(set(list4)))  # removes duplicates from the list and converts it to a set and then back to a list

###### List Comprehensions ###### 
# "Compact way to process all or part of the elements in a collection and return a list with the results"

squares = [x**2 for x in range(10)]
# print(squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
# print(even_squares)
# print([x**2 for x in range(10) if x % 2 != 0])

# print([x**2 for x in range(20) if x % 2 == 0 and x % 3 == 0])
# print([x**2 for x in range (20) if x%2 == 0 if x%3 == 0])

# print([(x, y) for x in range(3) for y in range(3)])  # Cartesian product
# print([(x, y) for x in range(3) if x % 2 == 0 for y in range(3) if y % 2 == 0])
# print([x + y for x in "abc" for y in "def"])

# print([x for x in "abc" if x not in "b"])




