<?php
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
?>