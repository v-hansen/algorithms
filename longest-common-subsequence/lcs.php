<?php
function lcs($X, $Y) {
    $m = strlen($X);
    $n = strlen($Y);
    $L = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
    
    for ($i = 0; $i <= $m; $i++) {
        for ($j = 0; $j <= $n; $j++) {
            if ($i == 0 || $j == 0) {
                $L[$i][$j] = 0;
            } elseif ($X[$i-1] == $Y[$j-1]) {
                $L[$i][$j] = $L[$i-1][$j-1] + 1;
            } else {
                $L[$i][$j] = max($L[$i-1][$j], $L[$i][$j-1]);
            }
        }
    }
    
    return $L[$m][$n];
}

echo lcs("ABCDGH", "AEDFHR");
?>