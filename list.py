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
print(list1[0])
