class LinearRegression
  def initialize
    @w, @b = 0, 0
  end
  
  def fit(x, y)
    x_mean = x.sum.to_f / x.size
    y_mean = y.sum.to_f / y.size
    
    num = den = 0
    x.each_with_index do |xi, i|
      num += (xi - x_mean) * (y[i] - y_mean)
      den += (xi - x_mean) ** 2
    end
    @w = num / den
    @b = y_mean - @w * x_mean
  end
  
  def predict(x)
    @w * x + @b
  end
end

model = LinearRegression.new
model.fit([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
puts model.predict(6) # 12.0
