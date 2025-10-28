import sys
sys.path.append('../../topological-sort')
from topological_sort import topological_sort_dfs

def test_basic_graph():
    graph = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}
    result = topological_sort_dfs(graph, 6)
    assert isinstance(result, list)
    assert len(result) == 6
