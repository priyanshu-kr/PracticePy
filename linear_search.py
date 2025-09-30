## Simple linear search algo which finds only first occurrence of target

# def linear_search(arr, target):
#     for i, value in enumerate(arr):
#         if value == target:
#             return i
#     return -1

# arr = list(map(int, input("Enter numbers separated by space: ").split()))
# print(arr)

# target = int(input("Enter element to search: "))

# print("Element is found at index " + str(linear_search(arr, target)) + ".")



# linear search which finds all occurrences of target

def linear_search_all(arr, target):
    indices = []
    for i, value in enumerate(arr):
        if value == target:
            indices.append(i)
    if len(indices) == 0:
        return -1  # Return -1 if target not found at all
    return indices

arr = list(map(int, input("Enter numbers separated by space: ").split()))
print(arr)

target = int(input("Enter element to search: "))

result = linear_search_all(arr, target)
if result == -1:
    print("Element not found.")
else:
    print("Element found at indices:", result)