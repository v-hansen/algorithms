<?php
function dijkstra($graph, $start) {
    $distances = [];
    foreach ($graph as $node => $neighbors) {
        $distances[$node] = PHP_INT_MAX;
    }
    $distances[$start] = 0;
    
    $pq = [[$start, 0]];
    
    while (!empty($pq)) {
        usort($pq, function($a, $b) { return $a[1] - $b[1]; });
        list($current, $currentDistance) = array_shift($pq);
        
        if ($currentDistance > $distances[$current]) continue;
        
        foreach ($graph[$current] as $neighbor => $weight) {
            $distance = $currentDistance + $weight;
            if ($distance < $distances[$neighbor]) {
                $distances[$neighbor] = $distance;
                $pq[] = [$neighbor, $distance];
            }
        }
    }
    
    return $distances;
}

$graph = [
    'A' => ['B' => 1, 'C' => 4],
    'B' => ['C' => 2, 'D' => 5],
    'C' => ['D' => 1],
    'D' => []
];
print_r(dijkstra($graph, 'A'));
?>