class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() { this.root = null; }
    
    insert(data) {
        this.root = this.insertNode(this.root, data);
    }
    
    insertNode(node, data) {
        if (!node) return new Node(data);
        if (data < node.data) node.left = this.insertNode(node.left, data);
        else node.right = this.insertNode(node.right, data);
        return node;
    }
    
    search(data) {
        return this.searchNode(this.root, data);
    }
    
    searchNode(node, data) {
        if (!node || node.data === data) return node;
        return data < node.data ? this.searchNode(node.left, data) : this.searchNode(node.right, data);
    }
}

const bst = new BST();
[50, 30, 70, 20, 40].forEach(x => bst.insert(x));
console.log(bst.search(40) ? "Found" : "Not found");