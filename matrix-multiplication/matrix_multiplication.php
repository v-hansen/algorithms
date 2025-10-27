<?php
function matrixMultiply($a, $b) {
    $rowsA = count($a);
    $colsA = count($a[0]);
    $colsB = count($b[0]);
    
    $result = array_fill(0, $rowsA, array_fill(0, $colsB, 0));
    
    for ($i = 0; $i < $rowsA; $i++) {
        for ($j = 0; $j < $colsB; $j++) {
            for ($k = 0; $k < $colsA; $k++) {
                $result[$i][$j] += $a[$i][$k] * $b[$k][$j];
            }
        }
    }
    
    return $result;
}

$a = [[1, 2], [3, 4]];
$b = [[5, 6], [7, 8]];

$result = matrixMultiply($a, $b);
foreach ($result as $row) {
    echo implode(" ", $row) . "\n";
}
?>