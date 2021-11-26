import sys
import DenseGraph
import queue

# This code is written based on the pseudo code given by Wikipedia:
# https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm

# return true if there is a path from source to sink, return false otherwise
# pred is an array that records the predecessor of a node, since we have no prev recorded in adjacency matrix and verices
def EdKarp(graph_t, source, sink):
    graph_t: DenseGraph.DenseGraph
    max_flow = 0
    # visited = [False] * graph_t.vertex_num

    while True:
        #do the BFS
        pred = [None] * graph_t.vertex_num
        q = queue.Queue() #define a queue for BFS, it contains int, the id of the vertices
        q.put(graph_t.vertex_mapper[source])
        while q.empty() == False:
            curr_vertex = q.get() #pop the first element in the queue
            # for all the neighbors of the poped node, if it is not visited and the distance is not infinite
            for v in range(0, len(graph_t.edges[curr_vertex])):
                if(v != graph_t.vertex_mapper[source] and pred[v] == None and graph_t.edges[curr_vertex][v] > 0 and graph_t.edges[curr_vertex][v] != sys.maxsize):
                    pred[v] = curr_vertex # update its predecessor
                    q.put(v) #push it into the queue
                    # print("push",v," into the queue")

        if pred[graph_t.vertex_mapper[sink]] != None:
            augment_flow = sys.maxsize  # set augment flow to be infinity, it will then be set to the min of all the edges found by BFS
            v_iterator = graph_t.vertex_mapper[sink]
            while v_iterator != graph_t.vertex_mapper[source]:
                augment_flow = min(augment_flow, graph_t.edges[pred[v_iterator]][v_iterator]) # get the min of the augment flow and the remaining capacity of forward edge
                v_iterator = pred[v_iterator]

            #traverse all the edge again, do the augment
            v_iterator = graph_t.vertex_mapper[sink]            
            while v_iterator != graph_t.vertex_mapper[source]:
                #do the augment
                graph_t.edges[pred[v_iterator]][v_iterator] -= augment_flow
                graph_t.edges[v_iterator][pred[v_iterator]] += augment_flow

                v_iterator = pred[v_iterator]
            max_flow += augment_flow
            # print("part max_flow = ",max_flow)
        else:
            return max_flow


if __name__ == "__main__":
    #here we use a dense graph, since an adjacency matrix can maintain a forward edge as well as a backward edge
    #hence it is perfect to represent a residue graph
    Graph = DenseGraph.DenseGraph()
    # Input part
    edge_num = int(input())
    for i in range(0, edge_num):
        u,v,weight = input().split(' ') #get the node name and weight, note that here u,v,w are all str type

        #add the vertices to the graph's vertices' list
        #Note that the distance is intiailized to maxsize already
        Graph.AddVertex(u)
        Graph.AddVertex(v)

        #add the edge to the edge list
        Graph.AddEdge(u,v,int(weight))
    s = str(input().strip('\r'))
    t = str(input().strip('\r'))

    # for elements in Graph.edges:
    #     for value in elements:
    #         print(value)

    print(EdKarp(Graph,s,t))
