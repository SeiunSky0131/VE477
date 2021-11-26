import SparseGraph
import queue

# declare a SparseGraph
Graph = SparseGraph.SparseGraph()
# declare a queue
q = queue.Queue()

#declare a list as the result
result = []

# Input part
edge_num = int(input())
for i in range(0, edge_num):
    u,v = input().split(' ') #get the node name and weight, note that here u,v,w are all str type

    #add the vertices to the graph's vertices' list
    #Note that the distance is intiailized to maxsize already
    Graph.AddVertex(u)
    Graph.AddVertex(v)

    #add the edge to the edge list, for weight we just set it to a 0 
    #add two edges to represent undirected edge
    Graph.AddEdge(u,v,int(0))
    Graph.AddEdge(v,u,int(0))

# put the first vertice (node 0) into the queue and mark it as visited
q.put(Graph.vertices[Graph.vertex_mapper["0"]])
Graph.vertices[Graph.vertex_mapper["0"]].visited = True

while q.empty() == False:
    # pop the first element in the queue
    curr_vertex:SparseGraph.Vertex
    curr_vertex = q.get()
    curr_vertex_num = Graph.vertex_mapper[curr_vertex.name]

    #put it into the result list
    result.append(curr_vertex.name)

    # For each of the neighbor, if it is not visited, push it into the queue, mark it as visited
    for edge in Graph.edges[curr_vertex_num]:
        edge:SparseGraph.Edge
        end_node = edge.end
        if (Graph.vertices[end_node].visited == False):
            q.put(Graph.vertices[end_node])
            Graph.vertices[end_node].visited = True

for i in range(0, len(result)):
    print(result[i],end=" ")