<?php
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
?>