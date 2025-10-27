import java.util.*

fun bfs(graph: Map<Int, List<Int>>, start: Int) {
    val visited = mutableSetOf<Int>()
    val queue: Queue<Int> = LinkedList()
    
    visited.add(start)
    queue.offer(start)
    
    while (queue.isNotEmpty()) {
        val node = queue.poll()
        print("$node ")
        
        graph[node]?.forEach { neighbor ->
            if (neighbor !in visited) {
                visited.add(neighbor)
                queue.offer(neighbor)
            }
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
    
    bfs(graph, 2)
}