def linear_search(arr, target)
  arr.each_with_index do |val, i|
    return i if val == target
  end
  -1
end

arr = [5, 2, 8, 1, 9, 3]
puts linear_search(arr, 8)
puts linear_search(arr, 7)
