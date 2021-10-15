#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include"union_find.h"

int main() {
    int eSize = 0;
    int vSize = 0;
    char * buffer = NULL;
    size_t input_size = 1;

    //read in the first line and convert it to int
    getline(&buffer,&input_size, stdin);
    eSize = atoi(buffer);

    //read in the second line and convert it to int
    getline(&buffer,&input_size,stdin);
    vSize = atoi(buffer);

    //test
    //printf("eSize is = %d",eSize);
    //printf("vSize is = %d", vSize);

    //we first initialize all the nodes
    node ** nodes = (node **)malloc(vSize * sizeof(node *));
    for (int i = 0; i < vSize; i++) {
        nodes[i] = GenSet(nodes[i]);
    }

    //then read in edges
    edge ** edges = (edge **)malloc(eSize * sizeof(edge *));
    for(int i = 0 ; i < eSize; i++) {
        edges[i] = GenEdge(edges[i]);
    }
    for(int i = 0; i < eSize ; i++) {        
        char string_1 [10];
        char string_2 [10];
        char string_3 [10];
        scanf("%s", string_1);
        scanf("%s", string_2);
        scanf("%s", string_3);

        //we ensure the first node is smaller
        if(atoi(string_1)<atoi(string_2)) {
            (edges[i]->node_1)->tag = atoi(string_1);
            (edges[i]->node_2)->tag = atoi(string_2);
        }
        else {
            (edges[i]->node_1)->tag = atoi(string_2);
            (edges[i]->node_2)->tag = atoi(string_1);            
        }
        edges[i]-> weight = atoi(string_3);
    }

    //test
    // for(int i = 0; i < eSize; i++) {
    //     printf("%d ",edges[i]->node_1->tag);
    //     printf("%d ", edges[i]->node_2->tag);
    //     printf("%d ", edges[i]->weight);
    //     printf("\n");
    // }

    //sort thr edges to be non-decreasing order
    sort_edge(edges, 0, eSize-1);

    //test
    // for(int i = 0; i < eSize; i++) {
    //     printf("%d ",edges[i]->node_1->tag);
    //     printf("%d ", edges[i]->node_2->tag);
    //     printf("%d ", edges[i]->weight);
    //     printf("\n");
    // }

    edge ** T  = (edge **)malloc(eSize * sizeof(edge *));
    int T_top = 0;
    for(int i = 0; i < eSize; i++) {

        //if the two points in the edge is not connected before
        if(Find(nodes[edges[i]->node_1->tag]) != Find(nodes[edges[i]->node_2->tag])) {
            //add the edge to the stack
            T[T_top] = edges[i];
            T_top++;

            //union two points
            Union(nodes[edges[i]->node_1->tag], nodes[edges[i]->node_2->tag]);
        }
    }



    T = sort_edge_by_node2(T,0,T_top-1);
    T = sort_edge_by_node1(T,0,T_top-1);

    for(int i = 0 ; i < T_top-1; i++) {
         if(T[i]->node_1->tag == T[i+1]->node_1->tag && T[i]->node_2->tag > T[i+1]->node_2->tag) {
            swap(T[i],T[i+1]);
         }
    }

    for(int i = 0; i < T_top; i++) {
        printf("%d--%d\n", T[i]->node_1->tag, T[i]->node_2->tag);
    }


    for(int i = 0; i < vSize ; i++) {
        free(nodes[i]);
    }
    for(int i = 0; i < eSize ; i++) {
        DesEdge(edges[i]);
    }
    free(nodes);
    free(edges);
}
