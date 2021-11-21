import fibonacci_heap
import SparseGraph

# Declare two structrues
Heap = fibonacci_heap.FiboHeap()
Graph = SparseGraph.SparseGraph()

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

#Set the the distance to the source node to be zero, and its prev to None
#Set it as visited
Graph.vertices[Graph.vertex_mapper[s]].distance = 0
Graph.vertices[Graph.vertex_mapper[s]].prev = None
Graph.vertices[Graph.vertex_mapper[s]].visited = True

#Update all its neighbors and insert it into the Heap
for edge_t in Graph.edges[Graph.vertex_mapper[s]]:
    edge_t:SparseGraph.Edge
    Graph.vertices[edge_t.end].distance = edge_t.weight
    Graph.vertices[edge_t.end].prev = s
    edge_t.target_distance = edge_t.weight
    new_FiboNode = fibonacci_heap.FiboNode(edge_t.target_distance,edge_t)
    Heap.Insert(new_FiboNode)

#While the heap is not empty, we extract min node, mark it as visited and then do a further push
while Heap.isEmpty() == False:
    min_edge = Heap.ExtractMin().struct
    v_number = min_edge.end
    # print(Graph.vertices[v_number].name)
    # print(min_edge.weight)

    #if we find that the node is already visited, we continue to extract
    if(Graph.vertices[v_number].visited == True):
        continue

    #else we visit that node and further analyze all its neighbors, update the neighbors
    #If the neighbor is not visited (it is still in the Heap), we update it
    Graph.vertices[v_number].visited = True
    # print(Graph.vertices[v_number].name, "is", Graph.vertices[v_number].visited)
    for edge_t in Graph.edges[v_number]:
        curr_vertex = edge_t.end
        if(not Graph.vertices[curr_vertex].visited) and Graph.vertices[curr_vertex].distance > Graph.vertices[v_number].distance + edge_t.weight:
            Graph.vertices[curr_vertex].distance = Graph.vertices[v_number].distance + edge_t.weight
            edge_t.target_distance = Graph.vertices[v_number].distance + edge_t.weight
            Graph.vertices[curr_vertex].prev = Graph.vertices[v_number].name

            new_FiboNode = fibonacci_heap.FiboNode(edge_t.target_distance, edge_t)
            Heap.Insert(new_FiboNode)

# for i in Graph.vertices:
#     if (i.visited == False):
#         print(i.name, False)
result = []
curr_vertex = t
while  curr_vertex != None:
    # print(curr_vertex)
    # print("s allc to:",Graph.vertex_mapper[t])
    result.append(curr_vertex)
    # if(curr_vertex == None):
    #     print("None")
    x = Graph.vertex_mapper[curr_vertex]
    curr_vertex = Graph.vertices[x].prev
    # print(curr_vertex)
result.reverse()
print(result)




    
