#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
} LinkedList;

LinkedList* createList() {
    LinkedList* list = malloc(sizeof(LinkedList));
    list->head = NULL;
    return list;
}

void append(LinkedList* list, int data) {
    Node* newNode = malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    
    if (!list->head) {
        list->head = newNode;
        return;
    }
    
    Node* current = list->head;
    while (current->next) current = current->next;
    current->next = newNode;
}

void display(LinkedList* list) {
    Node* current = list->head;
    while (current) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    LinkedList* list = createList();
    append(list, 1);
    append(list, 2);
    append(list, 3);
    display(list);
    return 0;
}