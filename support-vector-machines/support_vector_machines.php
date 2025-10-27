<?php
class MLAlgorithm {
    private $weights;
    
    public function fit($X, $y) {
        $this->weights = array_fill(0, count($X[0]), 0);
        echo "Model trained with " . count($X) . " samples\n";
    }
    
    public function predict($X) {
        return array_fill(0, count($X), 1);
    }
}

$model = new MLAlgorithm();
$X = [[1, 2], [3, 4]];
$y = [0, 1];
$model->fit($X, $y);
$pred = $model->predict([[2, 3]]);
echo "Prediction: " . $pred[0] . "\n";
?>
