<?php
function sieveOfEratosthenes($n) {
    $prime = array_fill(0, $n + 1, true);
    $prime[0] = $prime[1] = false;
    
    for ($p = 2; $p * $p <= $n; $p++) {
        if ($prime[$p]) {
            for ($i = $p * $p; $i <= $n; $i += $p) {
                $prime[$i] = false;
            }
        }
    }
    
    $primes = [];
    for ($i = 2; $i <= $n; $i++) {
        if ($prime[$i]) {
            $primes[] = $i;
        }
    }
    
    return $primes;
}

print_r(sieveOfEratosthenes(30));
?>