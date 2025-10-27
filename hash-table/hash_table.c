#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 10

typedef struct Node {
    char* key;
    int value;
    struct Node* next;
} Node;

typedef struct {
    Node* buckets[SIZE];
} HashTable;

int hash(char* key) {
    int sum = 0;
    for (int i = 0; key[i]; i++) sum += key[i];
    return sum % SIZE;
}

void put(HashTable* ht, char* key, int value) {
    int index = hash(key);
    Node* node = malloc(sizeof(Node));
    node->key = strdup(key);
    node->value = value;
    node->next = ht->buckets[index];
    ht->buckets[index] = node;
}

int get(HashTable* ht, char* key) {
    int index = hash(key);
    Node* node = ht->buckets[index];
    while (node) {
        if (strcmp(node->key, key) == 0) return node->value;
        node = node->next;
    }
    return -1;
}

int main() {
    HashTable ht = {0};
    put(&ht, "key1", 100);
    printf("%d\n", get(&ht, "key1"));
    return 0;
}