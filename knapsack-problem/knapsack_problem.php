<?php
function knapsack($weights, $values, $capacity) {
    $n = count($weights);
    $dp = array_fill(0, $n + 1, array_fill(0, $capacity + 1, 0));
    
    for ($i = 1; $i <= $n; $i++) {
        for ($w = 1; $w <= $capacity; $w++) {
            if ($weights[$i-1] <= $w) {
                $dp[$i][$w] = max(
                    $values[$i-1] + $dp[$i-1][$w-$weights[$i-1]],
                    $dp[$i-1][$w]
                );
            } else {
                $dp[$i][$w] = $dp[$i-1][$w];
            }
        }
    }
    
    return $dp[$n][$capacity];
}

function knapsackOptimized($weights, $values, $capacity) {
    $dp = array_fill(0, $capacity + 1, 0);
    
    for ($i = 0; $i < count($weights); $i++) {
        for ($w = $capacity; $w >= $weights[$i]; $w--) {
            $dp[$w] = max($dp[$w], $dp[$w - $weights[$i]] + $values[$i]);
        }
    }
    
    return $dp[$capacity];
}

$weights = [2, 1, 3];
$values = [4, 2, 3];
echo "2D DP: " . knapsack($weights, $values, 4) . "\n";
echo "1D DP: " . knapsackOptimized($weights, $values, 4) . "\n";
?>