<?php
class Node {
    public $data;
    public $left;
    public $right;
    
    public function __construct($data) {
        $this->data = $data;
        $this->left = null;
        $this->right = null;
    }
}

class BST {
    private $root;
    
    public function __construct() {
        $this->root = null;
    }
    
    public function insert($data) {
        $this->root = $this->insertNode($this->root, $data);
    }
    
    private function insertNode($node, $data) {
        if ($node === null) {
            return new Node($data);
        }
        
        if ($data < $node->data) {
            $node->left = $this->insertNode($node->left, $data);
        } else {
            $node->right = $this->insertNode($node->right, $data);
        }
        
        return $node;
    }
    
    public function search($data) {
        return $this->searchNode($this->root, $data);
    }
    
    private function searchNode($node, $data) {
        if ($node === null || $node->data === $data) {
            return $node;
        }
        
        if ($data < $node->data) {
            return $this->searchNode($node->left, $data);
        }
        
        return $this->searchNode($node->right, $data);
    }
    
    public function inorder() {
        $this->inorderTraversal($this->root);
    }
    
    private function inorderTraversal($node) {
        if ($node !== null) {
            $this->inorderTraversal($node->left);
            echo $node->data . " ";
            $this->inorderTraversal($node->right);
        }
    }
}

$bst = new BST();
$values = [50, 30, 70, 20, 40];
foreach ($values as $value) {
    $bst->insert($value);
}
$bst->inorder();
echo "\nSearch 40: " . ($bst->search(40) ? "Found" : "Not found") . "\n";
?>