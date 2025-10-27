def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

print(linear_search([1, 2, 3, 4, 5], 3))
print(linear_search_recursive([1, 2, 3, 4, 5], 3))