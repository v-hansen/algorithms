#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    
    Node(int data) : data(data), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;
    
public:
    LinkedList() : head(nullptr) {}
    
    void append(int data) {
        Node* newNode = new Node(data);
        
        if (!head) {
            head = newNode;
            return;
        }
        
        Node* current = head;
        while (current->next) current = current->next;
        current->next = newNode;
    }
    
    void prepend(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }
    
    void display() {
        Node* current = head;
        while (current) {
            cout << current->data << " -> ";
            current = current->next;
        }
        cout << "NULL" << endl;
    }
    
    bool search(int data) {
        Node* current = head;
        while (current) {
            if (current->data == data) return true;
            current = current->next;
        }
        return false;
    }
};

int main() {
    LinkedList list;
    list.append(1);
    list.append(2);
    list.prepend(0);
    list.display();
    cout << "Search 2: " << (list.search(2) ? "Found" : "Not found") << endl;
    return 0;
}