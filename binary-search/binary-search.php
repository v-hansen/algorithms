<?php
function binarySearch($arr, $target) {
    $left = 0;
    $right = count($arr) - 1;
    while ($left <= $right) {
        $mid = intval($left + ($right - $left) / 2);
        if ($arr[$mid] == $target) return $mid;
        if ($arr[$mid] < $target) $left = $mid + 1;
        else $right = $mid - 1;
    }
    return -1;
}

$arr = [1, 3, 5, 7, 9, 11];
echo binarySearch($arr, 7) . "\n";
echo binarySearch($arr, 4) . "\n";
?>
