class MLAlgorithm
  def initialize
    @weights = []
  end
  
  def fit(x, y)
    @weights = Array.new(x[0].size, 0)
    puts "Model trained with #{x.size} samples"
  end
  
  def predict(x)
    Array.new(x.size, 1)
  end
end

model = MLAlgorithm.new
x = [[1, 2], [3, 4]]
y = [0, 1]
model.fit(x, y)
pred = model.predict([[2, 3]])
puts "Prediction: #{pred[0]}"
