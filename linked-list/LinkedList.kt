class Node(var data: Int) {
    var next: Node? = null
}

class LinkedList {
    private var head: Node? = null
    
    fun append(data: Int) {
        val newNode = Node(data)
        if (head == null) {
            head = newNode
            return
        }
        
        var current = head
        while (current?.next != null) {
            current = current.next
        }
        current?.next = newNode
    }
    
    fun prepend(data: Int) {
        val newNode = Node(data)
        newNode.next = head
        head = newNode
    }
    
    fun display() {
        var current = head
        while (current != null) {
            print("${current.data} -> ")
            current = current.next
        }
        println("null")
    }
    
    fun search(data: Int): Boolean {
        var current = head
        while (current != null) {
            if (current.data == data) return true
            current = current.next
        }
        return false
    }
}

fun main() {
    val list = LinkedList()
    list.append(1)
    list.append(2)
    list.prepend(0)
    list.display()
    println("Search 2: ${list.search(2)}")
}