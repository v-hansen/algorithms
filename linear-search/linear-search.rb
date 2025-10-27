def linear_search(arr, target)
  arr.each_with_index { |val, i| return i if val == target }
  -1
end

puts linear_search([1,2,3,4,5], 3)