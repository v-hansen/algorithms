class LinearRegression
  def initialize
    @slope = 0
    @intercept = 0
  end
  
  def fit(x, y)
    n = x.length
    sum_x = x.sum
    sum_y = y.sum
    sum_xy = x.zip(y).map { |xi, yi| xi * yi }.sum
    sum_x2 = x.map { |xi| xi * xi }.sum
    
    @slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x).to_f
    @intercept = (sum_y - @slope * sum_x) / n.to_f
  end
  
  def predict(x)
    x.map { |xi| @slope * xi + @intercept }
  end
end

lr = LinearRegression.new
lr.fit([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
puts lr.predict([6, 7]).inspect