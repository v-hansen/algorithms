<?php
class KMeans {
    private $k;
    private $maxIters;
    private $centroids;
    
    public function __construct($k = 3, $maxIters = 100) {
        $this->k = $k;
        $this->maxIters = $maxIters;
    }
    
    public function fit($X) {
        $nSamples = count($X);
        $nFeatures = count($X[0]);
        
        // Initialize centroids randomly
        $this->centroids = [];
        for ($i = 0; $i < $this->k; $i++) {
            $randomIdx = rand(0, $nSamples - 1);
            $this->centroids[$i] = $X[$randomIdx];
        }
        
        for ($iter = 0; $iter < $this->maxIters; $iter++) {
            $labels = [];
            
            // Assign points to closest centroid
            for ($i = 0; $i < $nSamples; $i++) {
                $minDist = PHP_FLOAT_MAX;
                $label = 0;
                for ($j = 0; $j < $this->k; $j++) {
                    $dist = 0;
                    for ($d = 0; $d < $nFeatures; $d++) {
                        $dist += pow($X[$i][$d] - $this->centroids[$j][$d], 2);
                    }
                    if ($dist < $minDist) {
                        $minDist = $dist;
                        $label = $j;
                    }
                }
                $labels[$i] = $label;
            }
            
            // Update centroids
            $newCentroids = array_fill(0, $this->k, array_fill(0, $nFeatures, 0));
            $counts = array_fill(0, $this->k, 0);
            
            for ($i = 0; $i < $nSamples; $i++) {
                for ($j = 0; $j < $nFeatures; $j++) {
                    $newCentroids[$labels[$i]][$j] += $X[$i][$j];
                }
                $counts[$labels[$i]]++;
            }
            
            for ($i = 0; $i < $this->k; $i++) {
                if ($counts[$i] > 0) {
                    for ($j = 0; $j < $nFeatures; $j++) {
                        $newCentroids[$i][$j] /= $counts[$i];
                    }
                }
            }
            $this->centroids = $newCentroids;
        }
        
        // Final assignment
        $finalLabels = [];
        for ($i = 0; $i < $nSamples; $i++) {
            $minDist = PHP_FLOAT_MAX;
            $label = 0;
            for ($j = 0; $j < $this->k; $j++) {
                $dist = 0;
                for ($d = 0; $d < $nFeatures; $d++) {
                    $dist += pow($X[$i][$d] - $this->centroids[$j][$d], 2);
                }
                if ($dist < $minDist) {
                    $minDist = $dist;
                    $label = $j;
                }
            }
            $finalLabels[$i] = $label;
        }
        return $finalLabels;
    }
}

$X = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]];
$kmeans = new KMeans(2);
$labels = $kmeans->fit($X);
echo implode(" ", $labels) . "\n";
?>
