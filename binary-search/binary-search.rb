def binary_search(arr, target)
  left, right = 0, arr.length - 1
  while left <= right
    mid = (left + right) / 2
    return mid if arr[mid] == target
    arr[mid] < target ? left = mid + 1 : right = mid - 1
  end
  -1
end

puts binary_search([1,2,3,4,5], 3)