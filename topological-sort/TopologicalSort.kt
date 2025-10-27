fun topologicalSort(graph: Map<Int, List<Int>>): List<Int> {
    val visited = mutableSetOf<Int>()
    val stack = mutableListOf<Int>()
    
    fun dfs(node: Int) {
        if (node in visited) return
        visited.add(node)
        
        graph[node]?.forEach { neighbor ->
            dfs(neighbor)
        }
        
        stack.add(node)
    }
    
    graph.keys.forEach { node ->
        dfs(node)
    }
    
    return stack.reversed()
}

fun main() {
    val graph = mapOf(
        0 to listOf(1, 2),
        1 to listOf(3),
        2 to listOf(3),
        3 to emptyList()
    )
    
    println(topologicalSort(graph))
}
