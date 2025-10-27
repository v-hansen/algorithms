#!/usr/bin/env python3
import os

def complete_ml_small_implementations():
    """Completa implementações pequenas de ML"""
    
    # Linear Regression - expandir implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linear-regression"
    
    files_to_expand = [
        ("linear_regression.rb", """class LinearRegression
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
puts lr.predict([6, 7]).inspect"""),
        
        ("linear_regression.php", """<?php
class LinearRegression {
    private $slope = 0;
    private $intercept = 0;
    
    public function fit($x, $y) {
        $n = count($x);
        $sum_x = array_sum($x);
        $sum_y = array_sum($y);
        $sum_xy = 0;
        $sum_x2 = 0;
        
        for ($i = 0; $i < $n; $i++) {
            $sum_xy += $x[$i] * $y[$i];
            $sum_x2 += $x[$i] * $x[$i];
        }
        
        $this->slope = ($n * $sum_xy - $sum_x * $sum_y) / ($n * $sum_x2 - $sum_x * $sum_x);
        $this->intercept = ($sum_y - $this->slope * $sum_x) / $n;
    }
    
    public function predict($x) {
        $predictions = [];
        foreach ($x as $xi) {
            $predictions[] = $this->slope * $xi + $this->intercept;
        }
        return $predictions;
    }
}

$lr = new LinearRegression();
$lr->fit([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]);
print_r($lr->predict([6, 7]));
?>""")
    ]
    
    for filename, code in files_to_expand:
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

    # Logistic Regression - expandir implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/logistic-regression"
    
    files_to_expand = [
        ("logistic_regression.rb", """class LogisticRegression
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
puts lr.predict([[2.5, 3.5], [1.5, 2.5]]).inspect"""),
        
        ("logistic_regression.php", """<?php
class LogisticRegression {
    private $learning_rate;
    private $iterations;
    private $weights;
    private $bias;
    
    public function __construct($learning_rate = 0.01, $iterations = 1000) {
        $this->learning_rate = $learning_rate;
        $this->iterations = $iterations;
        $this->bias = 0;
    }
    
    private function sigmoid($z) {
        return 1.0 / (1.0 + exp(-$z));
    }
    
    public function fit($x, $y) {
        $n_samples = count($x);
        $n_features = count($x[0]);
        $this->weights = array_fill(0, $n_features, 0);
        
        for ($iter = 0; $iter < $this->iterations; $iter++) {
            $predictions = [];
            for ($i = 0; $i < $n_samples; $i++) {
                $z = $this->bias;
                for ($j = 0; $j < $n_features; $j++) {
                    $z += $x[$i][$j] * $this->weights[$j];
                }
                $predictions[] = $this->sigmoid($z);
            }
            
            $dw = array_fill(0, $n_features, 0);
            for ($j = 0; $j < $n_features; $j++) {
                for ($i = 0; $i < $n_samples; $i++) {
                    $dw[$j] += $x[$i][$j] * ($predictions[$i] - $y[$i]);
                }
                $dw[$j] /= $n_samples;
            }
            
            $db = 0;
            for ($i = 0; $i < $n_samples; $i++) {
                $db += $predictions[$i] - $y[$i];
            }
            $db /= $n_samples;
            
            for ($j = 0; $j < $n_features; $j++) {
                $this->weights[$j] -= $this->learning_rate * $dw[$j];
            }
            $this->bias -= $this->learning_rate * $db;
        }
    }
    
    public function predict($x) {
        $predictions = [];
        foreach ($x as $xi) {
            $z = $this->bias;
            for ($j = 0; $j < count($xi); $j++) {
                $z += $xi[$j] * $this->weights[$j];
            }
            $predictions[] = $this->sigmoid($z) >= 0.5 ? 1 : 0;
        }
        return $predictions;
    }
}

$lr = new LogisticRegression();
$lr->fit([[1, 2], [2, 3], [3, 4], [4, 5]], [0, 0, 1, 1]);
print_r($lr->predict([[2.5, 3.5], [1.5, 2.5]]));
?>""")
    ]
    
    for filename, code in files_to_expand:
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_remaining_small_files():
    """Completa arquivos muito pequenos restantes"""
    
    # Binary Search - expandir implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/binary-search"
    
    files_to_expand = [
        ("binary-search.py", """def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))"""),
        
        ("binary-search.js", """function binarySearch(arr, target) {
    let left = 0, right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    
    return -1;
}

function binarySearchRecursive(arr, target, left = 0, right = arr.length - 1) {
    if (left > right) return -1;
    
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return mid;
    else if (arr[mid] < target) return binarySearchRecursive(arr, target, mid + 1, right);
    else return binarySearchRecursive(arr, target, left, mid - 1);
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5));
console.log(binarySearchRecursive([1, 2, 3, 4, 5, 6, 7, 8, 9], 5));""")
    ]
    
    for filename, code in files_to_expand:
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

if __name__ == "__main__":
    print("Completando implementações de ML e arquivos pequenos...")
    complete_ml_small_implementations()
    complete_remaining_small_files()
    print("Implementações de ML e arquivos pequenos completados!")
