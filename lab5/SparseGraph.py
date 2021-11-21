from os import name
import sys

#The edge class
class Edge:

    #Initialize the edge with starting point v, end point v, and weight weight_t
    #Here u,v are represented using int in order to increase the visit speed using index
    def __init__(self, u:int, v:int, weight_t):
        self.start = u
        self.end = v
        self.weight = weight_t
        self.target_distance = 0 #this is the distance from given vertex to v. Future use.

    #Return the weight of the edge
    def GetEdgeWeight(self):
        return self.weight

    #Set the edge weight to be weight_t
    def SetEdgeWeight(self, weight_t:int):
        self.weight = weight_t

#The vertex class
class Vertex:

    #Initialize the vertex with the name of it
    #Initialize the previous node to None
    #Initialize the distance from this node to the source to be max
    #Initialize the it as un-visited
    #Note: what a vertex store is the distance between this vertex to a source node
    def __init__(self, name_t:str):
        self.name = name_t
        self.prev = None
        self.distance = sys.maxsize
        self.visited = False

    #Return the distance from this node to the source node(value of this node)
    def GetVertexValue(self):
        return self.distance

    #Set the vertex value(the distance from this node to the source node) to be value_t
    def SetVertexValue(self, value_t:int):
        self.distance = value_t

#The graph class
class SparseGraph:
    def __init__(self):
        self.edges = [] #an adjacency list
        self.vertices = [] #a list of vertices
        self.vertex_mapper = {} #A hash table, map each str type vertex name to the int type vertex number
        self.vertex_num = 0 #number of vertices in the graph
        self.edge_num = 0 #number of edges in the graph
    
    #REQUIRE: Both the begin point and the end point should already exist in the adjacency list/vertex list
    #Add the edge with start point u and end point v, with weight to be weight_t
    def AddEdge(self, u:str, v:str, weight_t:int):
        u_number = self.vertex_mapper[u]
        v_number = self.vertex_mapper[v]
        new_edge = Edge(u_number, v_number, weight_t)
        self.edges[u_number].append(new_edge) #append this edge to the corresponding bucket of the adjacency list
        self.edge_num = self.edge_num + 1

    #Remove the edge with starting point u and end point v, do nothing if such edge does not exists 
    def RemoveEdge(self, u:str, v:str):
        if(self.IsAdjacent(u,v) == True):
            u_number = self.vertex_mapper[u]
            v_number = self.vertex_mapper[v]
            for i, edge_t in enumerate(self.edges[u_number]):
                if (edge_t.end == v_number):
                    del(self.edges[u_number][i])
            #decrease the edge number
            self.edge_num = self.edge_num - 1

    #Add a vertex with name name_t, if the vertex already exist, do nothing
    def AddVertex(self, name_t:str):
        if(name_t not in self.vertex_mapper):
            self.vertex_mapper[name_t] = self.vertex_num #allocate a int to this vertex, note that we can do this insertion using index to dict
            self.vertex_num = self.vertex_num + 1 #increase the vertex number
            new_vertex = Vertex(name_t)
            self.vertices.append(new_vertex) #append the vertex to the list
            self.edges.append([]) #append a new slot to the end of the edge list so that the edges on this vertex can be inserted

    #Remove the vertex with name to be name_t, if there is no such vertex, do nothing
    def RemoveVertex(self, name_t:str):
        #If the vertex mapper does not have such node, then return 
        if(name_t not in self.vertex_mapper):
            return
        victim_number = self.vertex_mapper[name_t] #get the number corresponding to this vertex's name
        del(self.vertices[victim_number]) #delete the vertex in the vertex list
        del(self.edges[victim_number]) #delete all the edges that start from this vertex
        for elements in self.edges:
            for j,edge_t in enumerate(elements):
                if(edge_t.end == victim_number):
                    del(elements[j])

    #REQUIRE: u, v must be in the adjacency list
    #Return true if v is adjacent to u(the is an directed edge from u to v).
    #Return false if there is no such edge
    #Note: in a undirected graph, u is adjacent to v <=> v is adjacent to u
    def IsAdjacent(self, u, v):
        u_number = self.vertex_mapper[u]
        v_number = self.vertex_mapper[v]
        for edge_t in self.edges[u_number]:
            if(edge_t.end == v_number):
                return True
        #If v is not in the list, then we can deduce that the vertexs are not adjacent
        return False
