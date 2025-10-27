<?php
function linearSearch($arr, $target) {
    for ($i = 0; $i < count($arr); $i++) {
        if ($arr[$i] == $target) return $i;
    }
    return -1;
}

$arr = [1, 2, 3, 4, 5];
echo linearSearch($arr, 3);
?>