<?php
function twoSum($arr, $target) {
    $left = 0;
    $right = count($arr) - 1;
    
    while ($left < $right) {
        $sum = $arr[$left] + $arr[$right];
        if ($sum == $target) {
            return [$left, $right];
        } elseif ($sum < $target) {
            $left++;
        } else {
            $right--;
        }
    }
    
    return [];
}

$arr = [1, 2, 3, 4, 5];
print_r(twoSum($arr, 7));
?>