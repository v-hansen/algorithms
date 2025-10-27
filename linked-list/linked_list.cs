using System;

class Node {
    public int data;
    public Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    private Node head;
    
    public void Append(int data) {
        Node newNode = new Node(data);
        
        if (head == null) {
            head = newNode;
            return;
        }
        
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }
    
    public void Prepend(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }
    
    public void Display() {
        Node current = head;
        while (current != null) {
            Console.Write(current.data + " -> ");
            current = current.next;
        }
        Console.WriteLine("NULL");
    }
    
    public bool Search(int data) {
        Node current = head;
        while (current != null) {
            if (current.data == data) return true;
            current = current.next;
        }
        return false;
    }
}

class Program {
    static void Main() {
        LinkedList list = new LinkedList();
        list.Append(1);
        list.Append(2);
        list.Prepend(0);
        list.Display();
        Console.WriteLine("Search 2: " + (list.Search(2) ? "Found" : "Not found"));
    }
}