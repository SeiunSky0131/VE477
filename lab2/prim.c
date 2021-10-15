#include<stdio.h>
#include"union_find.h"

int min(int a, int b) {
    return (a >= b) ? b : a;
}

int alles_zero(edge ** arr, int size) {
    int flag = 1;
    for(int i = 0; i < size; i++) {
        if(arr[i]->weight != 0) {
            flag = 0;
            break;
        }
    }
    return flag;
}

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

//sort the edges first by node_2 and then by node_1, this ensure the order
edges = sort_edge_by_node2(edges,0,eSize-1);
edges = sort_edge_by_node1(edges,0,eSize-1);

//now we are able to perform the Prim's algorithm

//A fact: every node should have exactly one edge from union to it
//declare a distance array to store the edges with smallest distance between the Union and the other points. Initialize them to be max
edge ** distance = ( edge **)malloc(vSize * sizeof(int));
for (int i = 0; i < vSize; i++) {
    GenEdge(distance[i]);
    distance[i]->node_1 = NULL;
    distance[i]->node_2 = nodes[i];
    distance[i]->weight = __INT_MAX__;
}

//T is used for store the edges
edge ** T  = (edge **)malloc(eSize * sizeof(edge *));
int T_top = 0;

//the loop is terminated if the distance from union to every point is 0
while(alles_zero(distance,vSize) != 1) {
    //for every edge that has one end in the union and the other end no in the union, update the corresponding distance
    for(int i = 0 ; i < eSize; i++) {
        if(Find(nodes[edges[i]->node_1->tag]) == Find(nodes[0]) && Find(nodes[edges[i]->node_2->tag]) != Find(nodes[0])) {
            distance[edges[i]->node_2->tag]->weight =  min(edges[i]->weight, distance[edges[i]->node_2->tag]->weight);
            distance[edges[i]->node_2->tag]->node_1 = edges[i]->node_1;
        }
    }

    // we go through the distance array and choose the node with smallest distance, union it with root and update the distance
    int min_distance = __INT_MAX__;
    int min_tag = 0;
    for (int i = 0; i < vSize ; i++) {
        if(distance[i]->weight > 0 && distance[i]->weight < min_distance) {
            min_distance = distance[i]->weight;
            min_tag = i;
        }
    }
    Union(nodes[0],nodes[min_tag]);
    distance[min_tag]->weight = 0;
    T[T_top] = distance[min_tag];
    T_top++;
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
    for(int i = 0; i < vSize ; i++) {
        DesEdge(edges[i]);
    }
    free(nodes);
    free(edges);
free(distance);
return 0;
}
