class LogisticRegression
  def initialize(learning_rate = 0.01, iterations = 1000)
    @learning_rate = learning_rate
    @iterations = iterations
    @weights = nil
    @bias = 0
  end
  
  def sigmoid(z)
    1.0 / (1.0 + Math.exp(-z))
  end
  
  def fit(x, y)
    n_samples, n_features = x.length, x[0].length
    @weights = Array.new(n_features, 0)
    
    @iterations.times do
      linear_pred = x.map { |xi| xi.zip(@weights).map { |a, b| a * b }.sum + @bias }
      predictions = linear_pred.map { |z| sigmoid(z) }
      
      cost = -y.zip(predictions).map { |yi, pi| yi * Math.log(pi) + (1 - yi) * Math.log(1 - pi) }.sum / n_samples
      
      dw = Array.new(n_features, 0)
      (0...n_features).each do |j|
        dw[j] = x.zip(predictions, y).map { |xi, pi, yi| xi[j] * (pi - yi) }.sum / n_samples
      end
      db = predictions.zip(y).map { |pi, yi| pi - yi }.sum / n_samples
      
      @weights = @weights.zip(dw).map { |w, dw_j| w - @learning_rate * dw_j }
      @bias -= @learning_rate * db
    end
  end
  
  def predict(x)
    x.map do |xi|
      z = xi.zip(@weights).map { |a, b| a * b }.sum + @bias
      sigmoid(z) >= 0.5 ? 1 : 0
    end
  end
end

lr = LogisticRegression.new
lr.fit([[1, 2], [2, 3], [3, 4], [4, 5]], [0, 0, 1, 1])
puts lr.predict([[2.5, 3.5], [1.5, 2.5]]).inspect