#ifndef DICTIONARY_DICTIONARY_H
#define DICTIONARY_DICTIONARY_H
void *initializer();
// EFFECT: Initialize an empty dictionary

void *search(void* dictionary, int key);
// EFFECT: Given a dictionary, return the pointer to the element(key-value pair) specified by the key, return NULL if not found.

void insert(void* dictionary, int key, int value);
// EFFECT: If the key does not exist, insert an element(a key-value pair) to this dictionary. If key already exists, update the value.

void delete(void* dictionary,int key);
// EFFECT: Delete an element(key-value pair) specified by the key. If it does not exist, do nothing

void *minimum(void* dictionary);
// EFFECT: return the element(key-value pair) with the smallest key

void *maximum(void* dictionary);
// EFFECT: return the element(key-value pair) with the largest key

void *predecessor(void* dictionary, int key);
// EFFECT: retrieve the pointer to the element(key-value pair) just before a given key

void *successor(void* dictionary, int key);
// EFFECT: retrieve the pointer to the element(key-value pair) just after a given key

void free_dict(void* dictionary);
// EFFECT: free the memory allocated for this dictionary

int getkey(void* element);
// EFFECT: Given a pointer to the element, return the key

int getvalue(void* element);
// EFFECT: Given a pointer to the element, return the value

#endif //DICTIONARY_DICTIONARY_H