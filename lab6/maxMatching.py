import EdmondsKarp
import DenseGraph

if __name__ == "__main__":

    Graph = DenseGraph.DenseGraph()

    Graph.AddVertex("s")
    Graph.AddVertex("t")

    vertices_linked = {} # A dict mark whether a node is already connected to s or t or not
    # Input part
    vertex_num = int(input())
    edge_num = int(input())
    for i in range(0, edge_num):
        u,v = input().split(' ') #get the node name and weight, note that here u,v,w are all str type

        #add the vertices to the graph's vertices' list
        #Note that the distance is intiailized to maxsize already
        Graph.AddVertex(u)
        Graph.AddVertex(v)

        #add the edge to the edge list
        Graph.AddEdge(u,v,int(1))

        if u not in vertices_linked:
            Graph.AddEdge("s",u,int(1))
            vertices_linked[u] = "True"

        if v not in vertices_linked:
            Graph.AddEdge(v,"t",int(1))
            vertices_linked[v] = "True"

    print(EdmondsKarp.EdKarp(Graph,"s","t"))

