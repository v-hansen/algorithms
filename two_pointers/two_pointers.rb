def two_sum(arr, target)
  left, right = 0, arr.length - 1
  while left < right
    sum = arr[left] + arr[right]
    return [left, right] if sum == target
    sum < target ? left += 1 : right -= 1
  end
  []
end

puts two_sum([1, 2, 3, 4, 6], 6).inspect # [1, 3]
