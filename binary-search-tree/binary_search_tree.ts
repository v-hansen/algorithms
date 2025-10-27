class TreeNode {
    data: number;
    left: TreeNode | null = null;
    right: TreeNode | null = null;
    
    constructor(data: number) {
        this.data = data;
    }
}

class BST {
    private root: TreeNode | null = null;
    
    insert(data: number): void {
        this.root = this.insertRec(this.root, data);
    }
    
    private insertRec(node: TreeNode | null, data: number): TreeNode {
        if (!node) return new TreeNode(data);
        
        if (data < node.data) node.left = this.insertRec(node.left, data);
        else node.right = this.insertRec(node.right, data);
        
        return node;
    }
    
    search(data: number): boolean {
        return this.searchRec(this.root, data);
    }
    
    private searchRec(node: TreeNode | null, data: number): boolean {
        if (!node) return false;
        if (node.data === data) return true;
        return data < node.data ? this.searchRec(node.left, data) : this.searchRec(node.right, data);
    }
}

const bst = new BST();
[50, 30, 70, 20, 40].forEach(x => bst.insert(x));
console.log(bst.search(40));