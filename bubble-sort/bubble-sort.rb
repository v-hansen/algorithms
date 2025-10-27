def bubble_sort(arr)
  n = arr.length
  (0...n).each do |i|
    (0...(n-i-1)).each do |j|
      if arr[j] > arr[j+1]
        arr[j], arr[j+1] = arr[j+1], arr[j]
      end
    end
  end
  arr
end

puts bubble_sort([64, 34, 25, 12, 22, 11, 90]).inspect