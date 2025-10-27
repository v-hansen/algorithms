def matrix_multiply(a, b)
  rows_a, cols_a = a.length, a[0].length
  rows_b, cols_b = b.length, b[0].length
  
  return nil if cols_a != rows_b
  
  result = Array.new(rows_a) { Array.new(cols_b, 0) }
  
  (0...rows_a).each do |i|
    (0...cols_b).each do |j|
      (0...cols_a).each do |k|
        result[i][j] += a[i][k] * b[k][j]
      end
    end
  end
  
  result
end

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
puts matrix_multiply(a, b).inspect