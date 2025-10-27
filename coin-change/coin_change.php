<?php
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

function coinChangeWays($coins, $amount) {
    $dp = array_fill(0, $amount + 1, 0);
    $dp[0] = 1;
    
    foreach ($coins as $coin) {
        for ($i = $coin; $i <= $amount; $i++) {
            $dp[$i] += $dp[$i - $coin];
        }
    }
    
    return $dp[$amount];
}

$coins = [1, 3, 4];
echo "Min coins: " . coinChange($coins, 6) . "\n";
echo "Ways: " . coinChangeWays($coins, 6) . "\n";
?>