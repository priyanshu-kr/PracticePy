def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

arr = list(map(int, input("Enter numbers separated by space: ").split()))
print(arr)

target = int(input("Enter element to search: "))

print("Element is found at index " + str(linear_search(arr, target)) + ".")