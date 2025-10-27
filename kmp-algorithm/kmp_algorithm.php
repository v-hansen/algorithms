<?php
function computeLPS($pattern) {
    $m = strlen($pattern);
    $lps = array_fill(0, $m, 0);
    $len = 0;
    $i = 1;
    
    while ($i < $m) {
        if ($pattern[$i] == $pattern[$len]) {
            $len++;
            $lps[$i] = $len;
            $i++;
        } else {
            if ($len != 0) {
                $len = $lps[$len - 1];
            } else {
                $lps[$i] = 0;
                $i++;
            }
        }
    }
    
    return $lps;
}

function KMPSearch($text, $pattern) {
    $n = strlen($text);
    $m = strlen($pattern);
    $lps = computeLPS($pattern);
    
    $i = 0;
    $j = 0;
    $matches = [];
    
    while ($i < $n) {
        if ($pattern[$j] == $text[$i]) {
            $i++;
            $j++;
        }
        
        if ($j == $m) {
            $matches[] = $i - $j;
            $j = $lps[$j - 1];
        } elseif ($i < $n && $pattern[$j] != $text[$i]) {
            if ($j != 0) {
                $j = $lps[$j - 1];
            } else {
                $i++;
            }
        }
    }
    
    return $matches;
}

$text = "ABABDABACDABABCABCABCABCABC";
$pattern = "ABABCABCABCABC";
$matches = KMPSearch($text, $pattern);
print_r($matches);
?>
