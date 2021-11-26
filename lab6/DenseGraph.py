import sys

# The vertex class
class Vertex:
    # initial the vertex with its name
    # note that since we use the adjacency matrix, the vertex class may not be used to maintain information
    def __init__(self, name):
        self.name = name
        self.distance = sys.maxsize

    # get the value(i.e. distance) of the vertex
    def getVertexValue(self):
        return self.distance

    # set the value (i.e. distance) of the vertex
    def setVertexValue(self, value:int):
        self.distance = value


# The graph class
class DenseGraph:

    def __init__(self):
        self.edges = []  #An adjacency matrix, i.e., a two dimensional array. We maintain the smallest edge in each bucket
        self.vertex_mapper = {} #A hash table, map each str type vertex name to the int type vertex number
        self.vertex_num = 0 #number of vertices in the graph
        self.edge_num = 0 #number of edges in the graph

    # REQUIRE: Both the begin node u and the end node v should already be in the adjacency matrix
    # Add edge with begin node u and end node v to the adjacency list
    def AddEdge(self, u:str, v:str, weight:int):
        u_number = self.vertex_mapper[u] # get the id number of u
        v_number = self.vertex_mapper[v] # get the id number of v
        self.edges[u_number][v_number] = weight
        self.edge_num = self.edge_num + 1

    # REQUIRE: The edge to be removed is valid
    # Remove the edge with begin node u and end node v from the adjacency list
    def RemoveEdge(self, u:str, v:str , weight:int):
        u_number = self.vertex_mapper[u] # get the id number of u
        v_number = self.vertex_mapper[v] # get the id number of v
        self.edges[u_number][v_number] = sys.maxsize #set the distance to be infinity
        self.edge_num = self.edge_num - 1

    # Add a vertex to the adjacency matrix
    def AddVertex(self, name):
        if name not in self.vertex_mapper: 
            self.vertex_mapper[name] = self.vertex_num # if the name is new, then we add the node to the mapper's last new bucket
            self.vertex_num = self.vertex_num + 1
            for element in self.edges:
                element:list
                element.append(sys.maxsize)
            empty_column = [sys.maxsize]*self.vertex_num # create a new column with with all the distance initialized to infinity
            self.edges.append(empty_column)

    # REQUIRE: The node is valid(already in the matrix)
    # Remove a vertex from the adjacency matrix
    def RemoveVertex(self,name):
        if name in self.vertex_mapper: #if the node is vaild
            id_number = self.vertex_mapper[name] #get the id_number of the victim
            del self.vertex_mapper[name] #first delete it from the mapper
            for element in self.edges:
                del element[id_number] # erase all the victims in the columns
            del self.edges[id_number] # erase the column corresponding to this node

    # return true is u and v are adjacent, return false otherwise
    def IsAdjacent(self, u:str, v:str):
        u_number = self.vertex_mapper[u]
        v_number = self.vertex_mapper[v]
        if (self.edges[u_number][v_number] == sys.maxsize):
            return False
        return True

    # return the distance between node u and v, return maxsize if they are not adjacent
    def getEdgeWeight(self, u:str, v:str):
        u_number = self.vertex_mapper[u]
        v_number = self.vertex_mapper[v]
        return self.edges[u_number][v_number]

    # Set the weight of the edge starts from node u and ends with node v
    def setEdgeWeight(self, u:str, v:str, weight:int):
        u_number = self.vertex_mapper[u]
        v_number = self.vertex_mapper[v]
        self.edges[u_number][v_number] = weight