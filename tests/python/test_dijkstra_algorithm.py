import sys
sys.path.append('../../dijkstra-algorithm')
from dijkstra_algorithm import dijkstra

def test_shortest_path():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    result = dijkstra(graph, 'A')
    assert result['D'] == 4
