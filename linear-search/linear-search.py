def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [5, 2, 8, 1, 9, 3]
print(linear_search(arr, 8))
print(linear_search(arr, 7))
