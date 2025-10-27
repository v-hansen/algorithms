import java.util.*

data class Node(val name: String, val distance: Int) : Comparable<Node> {
    override fun compareTo(other: Node) = distance.compareTo(other.distance)
}

fun dijkstra(graph: Map<String, Map<String, Int>>, start: String): Map<String, Int> {
    val distances = mutableMapOf<String, Int>()
    val pq = PriorityQueue<Node>()
    
    graph.keys.forEach { distances[it] = Int.MAX_VALUE }
    distances[start] = 0
    pq.offer(Node(start, 0))
    
    while (pq.isNotEmpty()) {
        val current = pq.poll()
        
        if (current.distance > distances[current.name]!!) continue
        
        graph[current.name]?.forEach { (neighbor, weight) ->
            val distance = current.distance + weight
            if (distance < distances[neighbor]!!) {
                distances[neighbor] = distance
                pq.offer(Node(neighbor, distance))
            }
        }
    }
    
    return distances
}

fun main() {
    val graph = mapOf(
        "A" to mapOf("B" to 1, "C" to 4),
        "B" to mapOf("C" to 2, "D" to 5),
        "C" to mapOf("D" to 1),
        "D" to emptyMap()
    )
    
    println(dijkstra(graph, "A"))
}