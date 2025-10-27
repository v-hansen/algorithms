<?php
function bfs($graph, $start) {
    $visited = [];
    $queue = [$start];
    $visited[$start] = true;
    
    while (!empty($queue)) {
        $node = array_shift($queue);
        echo $node . " ";
        
        if (isset($graph[$node])) {
            foreach ($graph[$node] as $neighbor) {
                if (!isset($visited[$neighbor])) {
                    $visited[$neighbor] = true;
                    $queue[] = $neighbor;
                }
            }
        }
    }
}

$graph = [
    0 => [1, 2],
    1 => [2],
    2 => [0, 3],
    3 => [3]
];
bfs($graph, 2);
?>