#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<malloc.h>

#ifndef _UNION_FIND_H_
#define _UNION_FIND_H_

typedef struct node_t {
    struct node_t * parent;
    int tag;
    int rank;
} node;

//GenSet initialize one node
node * GenSet(node * in_node) {
    in_node = (node *)malloc(sizeof(node));
    in_node->parent = in_node;
    in_node->rank = 0;
    return in_node;
}

//Find return the root node of the node 
node * Find(node * in_node) {
    if(in_node->parent != in_node) {
        in_node->parent = Find(in_node->parent);
    }
    return in_node->parent;
}


//Union glue the root node of x and y together
void Union(node * x, node * y) {
    node * x_root = Find(x);
    node * y_root = Find(y);
    if(x_root->rank > y_root->rank) {
        y_root->parent = x_root;
    }
    else {
        x_root->parent = y_root;
    }
    if(x_root->rank == y_root->rank) {
        y_root->rank++;
    }
}

typedef struct edge_t {
    node * node_1;
    node * node_2;
    int weight;
} edge;

//constructor
edge * GenEdge(edge * e) {
    e = (edge *)malloc(sizeof(edge));
    e->node_1 = GenSet(e->node_1);
    e->node_2 = GenSet(e->node_2);
    e->weight = 0;
    return e;
}

//destructor
void DesEdge(edge * e) {
    free(e->node_1);
    free(e->node_2);
    free(e);
}

void swap(edge * x, edge * y) {
    edge temp = * x;
    * x = * y;
    * y = temp; 
}

//input the edges array and the left point, right point, which initially are 0 and size - 1, sort the array in non-decreasing order
edge ** sort_edge (edge ** arr, int left, int right) {
    //choose the first element as pivot
    int pivotat = 0;

    //base case
    if(left >= right) {
        return arr;
    }

    // two counters from first and last
    int i = left;
    int j = right;
    while(1) {

        //iterate for i until find the first element with weight greater than weight of arr[0], 
        //or i > j, since all elements righter than j are bigger than pivot, we end
        while (1) {
            if( i > j || arr[i]->weight > arr[left]->weight ) {
                break;
            }
            else {
                i++;
            }
        }

        while(1) {
            if( j < i || arr[j]->weight < arr[left]->weight ) {
                break;
            }
            else {
                j--;
            }
        }

        if(i < j) {
            swap (arr[i],arr[j]);
        }
        //else we finish the searching and quit the loop
        else{
            swap(arr[j],arr[left]);
            pivotat = j;
            break;
        }
    }
    arr = sort_edge(arr,left, pivotat-1);
    arr = sort_edge(arr,pivotat+1,right);
    return arr;
}

//input the edges array and the left point, right point, which initially are 0 and size - 1, sort the array in non-decreasing order
edge ** sort_edge_by_node2 (edge ** arr, int left, int right) {
    //choose the first element as pivot
    int pivotat = 0;

    //base case
    if(left >= right) {
        return arr;
    }

    // two counters from first and last
    int i = left;
    int j = right;
    while(1) {

        //iterate for i until find the first element with weight greater than weight of arr[0], 
        //or i > j, since all elements righter than j are bigger than pivot, we end
        while (1) {
            if( i > j || arr[i]->node_2->tag > arr[left]->node_2->tag ) {
                break;
            }
            else {
                i++;
            }
        }

        while(1) {
            if( j < i || arr[j]->node_2->tag < arr[left]->node_2->tag ) {
                break;
            }
            else {
                j--;
            }
        }

        if(i < j) {
            swap (arr[i],arr[j]);
        }
        //else we finish the searching and quit the loop
        else{
            swap(arr[j],arr[left]);
            pivotat = j;
            break;
        }
    }
    arr = sort_edge_by_node2(arr,left, pivotat-1);
    arr = sort_edge_by_node2(arr,pivotat+1,right);
    return arr;
}

//input the edges array and the left point, right point, which initially are 0 and size - 1, sort the array in non-decreasing order
edge ** sort_edge_by_node1 (edge ** arr, int left, int right) {
    //choose the first element as pivot
    int pivotat = 0;

    //base case
    if(left >= right) {
        return arr;
    }

    // two counters from first and last
    int i = left;
    int j = right;
    while(1) {

        //iterate for i until find the first element with weight greater than weight of arr[0], 
        //or i > j, since all elements righter than j are bigger than pivot, we end
        while (1) {
            if( i > j || arr[i]->node_1->tag > arr[left]->node_1->tag ) {
                break;
            }
            else {
                i++;
            }
        }

        while(1) {
            if( j < i || arr[j]->node_1->tag < arr[left]->node_1->tag ) {
                break;
            }
            else {
                j--;
            }
        }

        if(i < j) {
            swap (arr[i],arr[j]);
        }
        //else we finish the searching and quit the loop
        else{
            swap(arr[j],arr[left]);
            pivotat = j;
            break;
        }
    }
    arr = sort_edge_by_node1(arr,left, pivotat-1);
    arr = sort_edge_by_node1(arr,pivotat+1,right);
    return arr;
}

int * cut(char * str) {
    int * result = (int *)malloc(3 * sizeof(int));
    for (int i = 0; i < 3; i++) {
        char * numbers = strtok(str, " ");
        result [i] = atoi(numbers);
    }
    return result;
}
#endif

