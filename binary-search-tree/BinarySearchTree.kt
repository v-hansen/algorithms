class Node(var data: Int) {
    var left: Node? = null
    var right: Node? = null
}

class BST {
    private var root: Node? = null
    
    fun insert(data: Int) {
        root = insertRec(root, data)
    }
    
    private fun insertRec(root: Node?, data: Int): Node {
        if (root == null) return Node(data)
        
        if (data < root.data) root.left = insertRec(root.left, data)
        else root.right = insertRec(root.right, data)
        
        return root
    }
    
    fun search(data: Int): Boolean = searchRec(root, data)
    
    private fun searchRec(root: Node?, data: Int): Boolean {
        if (root == null) return false
        if (root.data == data) return true
        return if (data < root.data) searchRec(root.left, data) else searchRec(root.right, data)
    }
}

fun main() {
    val bst = BST()
    listOf(50, 30, 70, 20, 40).forEach { bst.insert(it) }
    println(bst.search(40))
}