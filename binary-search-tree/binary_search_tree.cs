using System;

class Node {
    public int data;
    public Node left, right;
    
    public Node(int data) {
        this.data = data;
        left = right = null;
    }
}

class BST {
    private Node root;
    
    public void Insert(int data) {
        root = InsertNode(root, data);
    }
    
    private Node InsertNode(Node node, int data) {
        if (node == null) return new Node(data);
        
        if (data < node.data) node.left = InsertNode(node.left, data);
        else node.right = InsertNode(node.right, data);
        
        return node;
    }
    
    public Node Search(int data) {
        return SearchNode(root, data);
    }
    
    private Node SearchNode(Node node, int data) {
        if (node == null || node.data == data) return node;
        
        return data < node.data ? SearchNode(node.left, data) : SearchNode(node.right, data);
    }
    
    public void Inorder() {
        InorderTraversal(root);
    }
    
    private void InorderTraversal(Node node) {
        if (node != null) {
            InorderTraversal(node.left);
            Console.Write(node.data + " ");
            InorderTraversal(node.right);
        }
    }
}

class Program {
    static void Main() {
        BST bst = new BST();
        int[] values = {50, 30, 70, 20, 40};
        foreach (int value in values) {
            bst.Insert(value);
        }
        bst.Inorder();
        Console.WriteLine("\nSearch 40: " + (bst.Search(40) != null ? "Found" : "Not found"));
    }
}