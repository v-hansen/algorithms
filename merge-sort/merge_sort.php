<?php
function mergeSort($arr) {
    if (count($arr) <= 1) return $arr;
    
    $mid = intval(count($arr) / 2);
    $left = mergeSort(array_slice($arr, 0, $mid));
    $right = mergeSort(array_slice($arr, $mid));
    
    return merge($left, $right);
}

function merge($left, $right) {
    $result = [];
    $i = $j = 0;
    
    while ($i < count($left) && $j < count($right)) {
        if ($left[$i] <= $right[$j]) {
            $result[] = $left[$i++];
        } else {
            $result[] = $right[$j++];
        }
    }
    
    while ($i < count($left)) $result[] = $left[$i++];
    while ($j < count($right)) $result[] = $right[$j++];
    
    return $result;
}

$arr = [64, 34, 25, 12, 22, 11, 90];
print_r(mergeSort($arr));
?>
