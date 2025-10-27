class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }
    
    append(data) {
        const newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
            return;
        }
        
        let current = this.head;
        while (current.next) {
            current = current.next;
        }
        current.next = newNode;
    }
    
    prepend(data) {
        const newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
    }
    
    delete(data) {
        if (!this.head) return;
        
        if (this.head.data === data) {
            this.head = this.head.next;
            return;
        }
        
        let current = this.head;
        while (current.next && current.next.data !== data) {
            current = current.next;
        }
        
        if (current.next) {
            current.next = current.next.next;
        }
    }
    
    display() {
        const elements = [];
        let current = this.head;
        while (current) {
            elements.push(current.data);
            current = current.next;
        }
        return elements;
    }
}

const ll = new LinkedList();
ll.append(1);
ll.append(2);
ll.append(3);
console.log(ll.display()); // [1, 2, 3]
