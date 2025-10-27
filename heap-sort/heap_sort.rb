def heapify(arr, n, i)
  largest = i
  left, right = 2*i+1, 2*i+2
  
  largest = left if left < n && arr[left] > arr[largest]
  largest = right if right < n && arr[right] > arr[largest]
  
  if largest != i
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)
  end
end

def heap_sort(arr)
  n = arr.length
  
  (n/2-1).downto(0) { |i| heapify(arr, n, i) }
  (n-1).downto(1) do |i|
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)
  end
  
  arr
end

puts heap_sort([64, 34, 25, 12, 22, 11, 90]).inspect