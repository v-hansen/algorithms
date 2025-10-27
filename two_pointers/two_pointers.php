<?php
function twoSum($arr, $target) {
    $left = 0;
    $right = count($arr) - 1;
    while ($left < $right) {
        $sum = $arr[$left] + $arr[$right];
        if ($sum == $target) return [$left, $right];
        $sum < $target ? $left++ : $right--;
    }
    return [];
}

$result = twoSum([1, 2, 3, 4, 6], 6);
echo "[{$result[0]}, {$result[1]}]\n";
?>
