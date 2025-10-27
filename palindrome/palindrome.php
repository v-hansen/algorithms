<?php
function isPalindrome($str) {
    $str = strtolower($str);
    return $str === strrev($str);
}

echo isPalindrome("racecar") ? "true" : "false";
echo "\n";
echo isPalindrome("hello") ? "true" : "false";
echo "\n";
?>
