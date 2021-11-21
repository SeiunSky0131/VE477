import SparseGraph

#Declare one graph structure
Graph = SparseGraph.SparseGraph()

#Read in the information
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

# Set the source node
Graph.vertices[Graph.vertex_mapper[s]].distance = 0
Graph.vertices[Graph.vertex_mapper[s]].prev = None
Graph.vertices[Graph.vertex_mapper[s]].visited = True

#visit the neighbors of the source node
for edge_t in Graph.edges[Graph.vertex_mapper[s]]:
    Graph.vertices[edge_t.end].distance = edge_t.weight
    Graph.vertices[edge_t.end].prev = s

for i in range(0, Graph.vertex_num):
    relax = False        #a flag, if not true after one loop, it means the graph is already updated to best
    for element in Graph.edges:
        for edge_t in element:
            edge_t:SparseGraph.Edge
            u_number = edge_t.start
            v_number = edge_t.end
            tmp = Graph.vertices[u_number].distance + edge_t.weight
            if(tmp < Graph.vertices[v_number].distance):
                Graph.vertices[v_number].distance = tmp
                Graph.vertices[v_number].prev = Graph.vertices[u_number].name
                relax = True
    if relax == False:      #if false, we are able to end the loop, since the graph is the best
        break

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