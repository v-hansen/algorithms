<?php
class LinearRegression {
    private $w, $b;
    
    public function fit($X, $y) {
        $X_mean = array_sum($X) / count($X);
        $y_mean = array_sum($y) / count($y);
        
        $num = 0; $den = 0;
        for ($i = 0; $i < count($X); $i++) {
            $num += ($X[$i] - $X_mean) * ($y[$i] - $y_mean);
            $den += pow($X[$i] - $X_mean, 2);
        }
        $this->w = $num / $den;
        $this->b = $y_mean - $this->w * $X_mean;
    }
    
    public function predict($x) {
        return $this->w * $x + $this->b;
    }
}

$model = new LinearRegression();
$model->fit([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]);
echo $model->predict(6) . "\n"; // 12
?>
