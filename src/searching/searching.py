def linear_search(arr, target):
    # Your code here
    # Index
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    
    # enumerate
    for i, el in enumerate(arr):
        if el == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # not found
