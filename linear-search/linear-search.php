<?php
function linearSearch($arr, $target) {
    for ($i = 0; $i < count($arr); $i++) {
        if ($arr[$i] == $target) return $i;
    }
    return -1;
}

$arr = [5, 2, 8, 1, 9, 3];
echo linearSearch($arr, 8) . "\n";
echo linearSearch($arr, 7) . "\n";
?>
