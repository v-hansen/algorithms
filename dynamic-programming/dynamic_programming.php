<?php
function fibonacci($n) {
    if ($n <= 1) return $n;
    $dp = array_fill(0, $n + 1, 0);
    $dp[1] = 1;
    
    for ($i = 2; $i <= $n; $i++) {
        $dp[$i] = $dp[$i-1] + $dp[$i-2];
    }
    return $dp[$n];
}

function coinChange($coins, $amount) {
    $dp = array_fill(0, $amount + 1, $amount + 1);
    $dp[0] = 0;
    
    for ($i = 1; $i <= $amount; $i++) {
        foreach ($coins as $coin) {
            if ($coin <= $i) {
                $dp[$i] = min($dp[$i], $dp[$i - $coin] + 1);
            }
        }
    }
    
    return $dp[$amount] > $amount ? -1 : $dp[$amount];
}

function knapsack($weights, $values, $capacity) {
    $n = count($weights);
    $dp = array_fill(0, $n + 1, array_fill(0, $capacity + 1, 0));
    
    for ($i = 1; $i <= $n; $i++) {
        for ($w = 1; $w <= $capacity; $w++) {
            if ($weights[$i-1] <= $w) {
                $dp[$i][$w] = max(
                    $dp[$i-1][$w],
                    $dp[$i-1][$w-$weights[$i-1]] + $values[$i-1]
                );
            } else {
                $dp[$i][$w] = $dp[$i-1][$w];
            }
        }
    }
    return $dp[$n][$capacity];
}

echo "Fibonacci(10): " . fibonacci(10) . "\n";
echo "Coin change: " . coinChange([1, 3, 4], 6) . "\n";
echo "Knapsack: " . knapsack([2, 1, 3], [4, 2, 3], 4) . "\n";
?>