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

