def quick_sort(arr)
  return arr if arr.length <= 1
  pivot = arr[0]
  less = arr[1..-1].select { |x| x < pivot }
  greater = arr[1..-1].select { |x| x >= pivot }
  quick_sort(less) + [pivot] + quick_sort(greater)
end

puts quick_sort([64,34,25,12,22,11,90]).inspect