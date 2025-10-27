<?php
function quickSort($arr) {
    if (count($arr) <= 1) return $arr;
    
    $pivot = $arr[0];
    $less = $greater = [];
    
    for ($i = 1; $i < count($arr); $i++) {
        if ($arr[$i] < $pivot) {
            $less[] = $arr[$i];
        } else {
            $greater[] = $arr[$i];
        }
    }
    
    return array_merge(quickSort($less), [$pivot], quickSort($greater));
}

$arr = [64, 34, 25, 12, 22, 11, 90];
print_r(quickSort($arr));
?>