#include<stdio.h>
#include<malloc.h>
#include"dictionary.h"

typedef struct node_t {
    int value;
    int key;
    struct node_t * prev;
    struct node_t * next;
}node;

typedef struct dict_t {
    struct node_t * first;
    struct node_t * last;
}my_dictionary;

void * initializer() {
    my_dictionary * new_dict = (my_dictionary *)malloc(sizeof(my_dictionary));
    new_dict->first = new_dict->last = NULL;
    return new_dict;
}

void * search(void * dictionary, int key) {
    my_dictionary * dictionary_t = (my_dictionary *) dictionary;
    if(dictionary_t->first == NULL) {
        return NULL;
    }
    else {
        node * current_node = dictionary_t->first;
        while(current_node->key < key) {
            if(current_node->next == NULL) {
                return NULL;
            }
            else {
                current_node = current_node->next;
            }
        }

        //case1: find the key 
        if(current_node->key == key) {
            return current_node;
        }

        //case2: current_node->key > key, we fail to find
        else {
            return NULL;
        }
    }
}

void insert(void * dictionary, int key, int value) {
    my_dictionary * dictionary_t = (my_dictionary *) dictionary;

    //if the dictionary is originally empty
    if(dictionary_t->first == NULL) {

        //allocate the space
        node * new_node = (node *)malloc(sizeof(node));

        //update the value
        new_node->key = key;
        new_node->value = value;
        new_node->next = new_node->prev = NULL; 
        dictionary_t->first = dictionary_t->last = new_node;
    }
    else {
        node * current_node = dictionary_t->first;
        while(current_node->key < key) {

            //if the current node is already the last one, we insert the node at the back
            if(current_node == dictionary_t->last) {
                
                //allocate the space
                node * new_node = (node *)malloc(sizeof(node));

                //update the value
                new_node->key = key;
                new_node->value = value;
                new_node->prev = dictionary_t->last;
                new_node->next = NULL;
                current_node->next = new_node;
                dictionary_t->last = new_node;

            }

            //else we continue to next key-value pair
            else {
                current_node = current_node->next;
            }
        }

        //case1: we find that there is already a same key, then update the value
        if(current_node->key == key) {
            current_node->value = value;
        }

        //case2: we end up with current_node->key > key, we insert in the middle
        else {

            //allocate the space 
            node * new_node = (node *)malloc(sizeof(node));

            //update the value
            new_node->key = key;
            new_node->value = value;
            new_node->prev = current_node->prev;
            new_node->next = current_node;

            //if the node is not inserted at the very first of the list, we update the prev
            if(current_node->prev != NULL) {
                (current_node->prev)->next = new_node;
            }
            //else we need to update the first pointer
            else {
                dictionary_t->first = new_node;
            }
            current_node->prev = new_node;
        }
    }
}

void delete(void * dictionary, int key) {
    my_dictionary * dictionary_t = (my_dictionary *) dictionary;
    node * victim = search(dictionary_t, key);
    if(victim != NULL) {

        //if the victim is the end of the list
        if(victim == dictionary_t->last) {

            //if the victim->prev is not NULL, which means there is more than 1 element in the list, we update the prev node
            if(victim->prev != NULL) {
                (victim->prev)->next = NULL;
            }
            else {
                dictionary_t->first = NULL;
            }
            dictionary_t->last = victim->prev;
            free(victim);
            victim = NULL;
        }

        //else if the victim is the first of the list
        else if(victim == dictionary_t->first) {
            (victim->next)->prev = NULL;
            dictionary_t->first = victim->next;
            free(victim);
            victim = NULL;
        }

        //else we delete a middle element in the list 
        else {
            (victim->next)->prev = victim->prev;
            (victim->prev)->next = victim->next;
            free(victim);
            victim = NULL;
        }
    }
}

void * minimum(void * dictionary) {
    my_dictionary * dictionary_t = (my_dictionary *) dictionary;    
    return dictionary_t->first;
}

void * maximum(void * dictionary) {
    my_dictionary * dictionary_t = (my_dictionary *) dictionary;
    return dictionary_t->last;
}

void * predecessor(void * dictionary, int key) {
    my_dictionary * dictionary_t = (my_dictionary *) dictionary;
    node * victim = search(dictionary_t,key);

    //if the input is invalid, i.e., there is no key
    if(victim == NULL) {
        return NULL;
    }
    return victim->prev;
}

void * successor(void * dictionary, int key) {
    my_dictionary * dictionary_t = (my_dictionary *) dictionary;
    node * victim = search(dictionary_t,key);

    //if the input is invalid, i.e., there is no key
    if(victim == NULL) {
        return NULL;
    }
    return victim->next;
}

void free_dict(void * dictionary) {
    my_dictionary * dictionary_t = (my_dictionary *) dictionary;
    node * current_node = dictionary_t->last;
    while(current_node != NULL) {
        node * victim = current_node;
        current_node = current_node->prev;
        dictionary_t->last = victim->prev;
        free(victim);
        victim = NULL;
    }
    free(dictionary);
    dictionary = NULL;
}

int getkey(void * element) {
    node * element_t = (node *) element;
    return element_t->key;
}

int getvalue(void * element) {
    node * element_t = (node *) element;
    return element_t->value;
}
