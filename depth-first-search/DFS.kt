fun dfs(graph: Map<Int, List<Int>>, start: Int, visited: MutableSet<Int>) {
    visited.add(start)
    print("$start ")
    
    graph[start]?.forEach { neighbor ->
        if (neighbor !in visited) {
            dfs(graph, neighbor, visited)
        }
    }
}

fun main() {
    val graph = mapOf(
        0 to listOf(1, 2),
        1 to listOf(2),
        2 to listOf(0, 3),
        3 to listOf(3)
    )
    
    val visited = mutableSetOf<Int>()
    dfs(graph, 2, visited)
}