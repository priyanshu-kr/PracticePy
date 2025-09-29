# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# searching for all occurrences of target
def binary_search_all(arr, target):
    arr_sorted = sorted(arr)  # Step 1: Sort the array
    indices = []
    left, right = 0, len(arr_sorted) - 1
    # Standard binary search loop to find any occurrence
    while left <= right:
        mid = (left + right) // 2
        if arr_sorted[mid] == target:
            # Expand around mid to find all occurrences
            i = mid
            while i >= 0 and arr_sorted[i] == target:
                i -= 1
            i += 1
            while i < len(arr_sorted) and arr_sorted[i] == target:
                indices.append(i)
                i += 1
            break
        elif arr_sorted[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return indices

print(binary_search_all([1, 52, 32, 4, 5, 52, 2, 4, 65, 52, 42], 52))