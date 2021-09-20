#include<stdio.h>
#include<malloc.h>
#include"hash.h"

typedef struct node_t {
    int key;
    int value;
    struct node_t * next;
}node;

typedef struct hash_table {
    node ** arr;
}h_table;

void * initializer(int size) {
    h_table * table = (h_table *)malloc(sizeof(h_table));
    table->arr = (node **)malloc(size * sizeof(node *));
    for(int i = 0; i< size ; i++) {
        table->arr[i] = NULL;
    }
    return table;
}

void insert(void * hashtable, int size, int key, int value) {

    //convert the void * to h_table *
    h_table * table = (h_table *)hashtable;

    //first calculate the hash value of key, and then go to that bucket
    int h_value = key % size;
    node * current_node = table->arr[h_value];

    //if the bucket is empty, we insert it
    if(current_node == NULL) {
        node * new_node = (node *)malloc(sizeof(node));
        new_node->key = key;
        new_node->value = value;
        new_node->next = NULL;
        table->arr[h_value] = new_node;
        return;
    }

    while (current_node != NULL) {

        //if the current node has the same key, then we update it
        if(current_node->key == key) {
            current_node->value = value;
            return;
        }

        else {

            //if current node has no successor, we insert the node at the back
            if(current_node->next == NULL) {
                node * new_node = (node *)malloc(sizeof(node));
                new_node->key = key;
                new_node->value = value;
                new_node->next = NULL;
                current_node->next = new_node;
                return; 
            }

            //else we continue to traverse down the chain
            else {
                current_node = current_node->next;
            }
        }
    }
}

void delete(void * hashtable, int size , int key) {

    //convert void * to h_table *
    h_table * table = (h_table *) hashtable;

    //first calculate the hash value of key, and then go to the bucket
    int h_value = key % size;
    node * current_node = table->arr[h_value];
    
    //base case1, there is no element in this bucket
    if(current_node == NULL) {
        return;
    }

    //base case2, there is only one element in this bucket
    if(current_node->next == NULL) {
        if(current_node->key == key) {
            free(current_node);
            current_node = NULL;
            table->arr[h_value] = NULL;
            return;
        }
        return;
    }

    //the case when there are more than two elements in the bucket
    else {
        if(current_node->key == key) {
            table->arr[h_value] = current_node->next;
            free(current_node);
            current_node = NULL;
            return;
        }
        else {
            while(current_node->next != NULL) {
                if((current_node->next)->key == key) {
                    node * victim = current_node->next;
                    current_node->next = (current_node->next)->next;
                    free(victim);
                    return;
                }
                else {
                    current_node = current_node->next;
                }
            }
        }
    }
}

void * search(void * hashtable, int size , int key) {

    //convert void * to h_table *
    h_table * table = (h_table *) hashtable;

    //calculate the h_value of the key and then go to the bucket
    int h_value = key % size;
    node * current_node = table->arr[h_value];

    while(current_node != NULL) {
        if(current_node->key == key) {
            return current_node;
        }
        current_node = current_node->next;
    }
    return NULL;
}

int getValue(void * element) {

    //convert void * to node *
    node * victim = (node *) element;
    return victim->value;
}

void freeHashtable(void * hashtable, int size) {

    //convert void * to h_table *
    h_table * table = (h_table *) hashtable;

    for(int i = 0; i<size; i++) {
        while(table->arr[i] != NULL) {
            node * victim = table->arr[i];
            table->arr[i] = (table->arr[i])->next;
            free(victim);
            victim = NULL;
        }
    }

    free(table->arr);
    free(table);
    table = NULL;
}
