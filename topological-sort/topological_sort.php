<?php
function dfs($node, $graph, &$visited, &$stack) {
    $visited[$node] = true;
    
    if (isset($graph[$node])) {
        foreach ($graph[$node] as $neighbor) {
            if (!isset($visited[$neighbor])) {
                dfs($neighbor, $graph, $visited, $stack);
            }
        }
    }
    
    array_push($stack, $node);
}

function topologicalSort($graph) {
    $visited = [];
    $stack = [];
    
    foreach (array_keys($graph) as $node) {
        if (!isset($visited[$node])) {
            dfs($node, $graph, $visited, $stack);
        }
    }
    
    return array_reverse($stack);
}

$graph = [
    0 => [1, 2],
    1 => [3],
    2 => [3],
    3 => []
];

$result = topologicalSort($graph);
print_r($result);
?>