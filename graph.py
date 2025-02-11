
from enum import Enum

class VertexType (Enum):
    REACTION = 1
    SPECIE = 2
    MODIFIER = 3

class Vertex:
    def __init__ (self, identifier, name, vertex_type):
        self.identifier = identifier
        self.name = name
        self.vertex_type = vertex_type

class Graph:
    def __init__(self):
        self.vertices = {}
        self.directed = set()
        self.undirected = set()

    
    def addVertex (self, identifier, name, vertex_type : VertexType):
        if not (identifier in self.vertices):
            self.vertices[identifier] = Vertex(identifier, name, vertex_type)


    def addDirectedEdge (self, x, y):
        self.directed.add((x,y))

    def addUndirectedEdge (self, x, y):
        self.undirected.add((x,y))



    def print (self):
        print ("vertices: ", str(self.vertices))
        print ("directed edges", str(self.directed_neighbors))
        print ("undirected edges", str(self.undirected_neighbors))


    def toDot(self, filename, grouped_vertices):
        with open(filename, "w") as file:
            file.write("digraph {\n")

            #for v in self.vertices:
            #    file.write (v)
            #    match self.vertices[v].vertex_type:
            #        case VertexType.REACTION:
            #            file.write(" [shape=box]")
            #        case _:
            #            file.write ("[shape=circle]")
            #    file.write("\n")

            for group_name, group in grouped_vertices:
                file.write("subgraph cluster_" + group_name +"{\n")
                file.write ("label="+ group_name + "\n")
                file.write ("graph[style=dotted]\n")
                for v in group:
                    file.write (v)
                    match self.vertices[v].vertex_type:
                        case VertexType.REACTION:
                            file.write("\t[shape=box]\n")
                        case _:
                            file.write ("\t[shape=circle]\n")


                file.write ("}")

            for edge in self.directed:
                file.write (f"{edge[0]} -> {edge[1]}\n")
            for edge in self.undirected:
                file.write (f"{edge[0]} -> {edge[1]} [dir=None]\n")

            file.write ("}")










    
