def binary_search(arr, target)
  left, right = 0, arr.length - 1
  while left <= right
    mid = left + (right - left) / 2
    return mid if arr[mid] == target
    if arr[mid] < target
      left = mid + 1
    else
      right = mid - 1
    end
  end
  -1
end

arr = [1, 3, 5, 7, 9, 11]
puts binary_search(arr, 7)
puts binary_search(arr, 4)
