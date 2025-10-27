<?php
function dfs($graph, $start, &$visited) {
    $visited[$start] = true;
    echo $start . " ";
    
    if (isset($graph[$start])) {
        foreach ($graph[$start] as $neighbor) {
            if (!isset($visited[$neighbor])) {
                dfs($graph, $neighbor, $visited);
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
$visited = [];
dfs($graph, 2, $visited);
?>