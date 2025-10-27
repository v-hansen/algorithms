def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Test
arr = [1, 2, 3, 4, 6]
print(two_sum(arr, 6))  # [1, 3]
