<?php
class Node {
    public $data;
    public $next;
    
    public function __construct($data) {
        $this->data = $data;
        $this->next = null;
    }
}

class LinkedList {
    private $head;
    
    public function __construct() {
        $this->head = null;
    }
    
    public function append($data) {
        $newNode = new Node($data);
        
        if ($this->head === null) {
            $this->head = $newNode;
            return;
        }
        
        $current = $this->head;
        while ($current->next !== null) {
            $current = $current->next;
        }
        $current->next = $newNode;
    }
    
    public function prepend($data) {
        $newNode = new Node($data);
        $newNode->next = $this->head;
        $this->head = $newNode;
    }
    
    public function display() {
        $current = $this->head;
        while ($current !== null) {
            echo $current->data . " -> ";
            $current = $current->next;
        }
        echo "NULL\n";
    }
    
    public function search($data) {
        $current = $this->head;
        while ($current !== null) {
            if ($current->data === $data) {
                return true;
            }
            $current = $current->next;
        }
        return false;
    }
}

$list = new LinkedList();
$list->append(1);
$list->append(2);
$list->prepend(0);
$list->display();
echo "Search 2: " . ($list->search(2) ? "Found" : "Not found") . "\n";
?>