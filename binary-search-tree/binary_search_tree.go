package main
import "fmt"

type Node struct {
    data  int
    left  *Node
    right *Node
}

type BST struct {
    root *Node
}

func (bst *BST) Insert(data int) {
    bst.root = bst.insertNode(bst.root, data)
}

func (bst *BST) insertNode(node *Node, data int) *Node {
    if node == nil {
        return &Node{data: data}
    }
    if data < node.data {
        node.left = bst.insertNode(node.left, data)
    } else {
        node.right = bst.insertNode(node.right, data)
    }
    return node
}

func (bst *BST) Search(data int) *Node {
    return bst.searchNode(bst.root, data)
}

func (bst *BST) searchNode(node *Node, data int) *Node {
    if node == nil || node.data == data {
        return node
    }
    if data < node.data {
        return bst.searchNode(node.left, data)
    }
    return bst.searchNode(node.right, data)
}

func (bst *BST) Inorder() {
    bst.inorderTraversal(bst.root)
}

func (bst *BST) inorderTraversal(node *Node) {
    if node != nil {
        bst.inorderTraversal(node.left)
        fmt.Print(node.data, " ")
        bst.inorderTraversal(node.right)
    }
}

func main() {
    bst := &BST{}
    values := []int{50, 30, 70, 20, 40}
    for _, v := range values {
        bst.Insert(v)
    }
    bst.Inorder()
    fmt.Printf("\nSearch 40: %t\n", bst.Search(40) != nil)
}