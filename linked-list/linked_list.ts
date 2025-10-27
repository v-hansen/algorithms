class ListNode {
    data: number;
    next: ListNode | null = null;
    
    constructor(data: number) {
        this.data = data;
    }
}

class LinkedList {
    private head: ListNode | null = null;
    
    append(data: number): void {
        const newNode = new ListNode(data);
        
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
    
    prepend(data: number): void {
        const newNode = new ListNode(data);
        newNode.next = this.head;
        this.head = newNode;
    }
    
    display(): void {
        let current = this.head;
        const values: string[] = [];
        while (current) {
            values.push(current.data.toString());
            current = current.next;
        }
        console.log(values.join(" -> ") + " -> null");
    }
    
    search(data: number): boolean {
        let current = this.head;
        while (current) {
            if (current.data === data) return true;
            current = current.next;
        }
        return false;
    }
}

const list = new LinkedList();
list.append(1);
list.append(2);
list.prepend(0);
list.display();
console.log("Search 2:", list.search(2));