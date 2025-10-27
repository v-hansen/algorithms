#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} Node;

Node* createNode(int data) {
    Node* node = malloc(sizeof(Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

Node* insert(Node* root, int data) {
    if (!root) return createNode(data);
    if (data < root->data) root->left = insert(root->left, data);
    else root->right = insert(root->right, data);
    return root;
}

Node* search(Node* root, int data) {
    if (!root || root->data == data) return root;
    return data < root->data ? search(root->left, data) : search(root->right, data);
}

void inorder(Node* root) {
    if (root) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

int main() {
    Node* root = NULL;
    int values[] = {50, 30, 70, 20, 40};
    for (int i = 0; i < 5; i++) root = insert(root, values[i]);
    inorder(root);
    printf("\nSearch 40: %s\n", search(root, 40) ? "Found" : "Not found");
    return 0;
}