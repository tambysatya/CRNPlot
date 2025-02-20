
from enum import Enum
import random

from utils import *


modifier_edge_color = "\"#3191f3\"" # color of the edges between modifiers and reactions

class VertexType (Enum):
    REVERSIBLE_REACTION = 1
    IRREVERSIBLE_REACTION = 2
    SPECIE = 3
    MODIFIER = 4

class Vertex:
    def __init__ (self, identifier, name, vertex_type):
        self.identifier = identifier
        self.name = name
        self.vertex_type = vertex_type

class Graph:
    def __init__(self):
        self.vertices = {}
        self.connected_vertices = set() #to track isolated vertices
        self.directed = set()
        self.undirected = set()

    
    def addVertex (self, identifier, name, vertex_type : VertexType):
        if not (identifier in self.vertices):
            self.vertices[identifier] = Vertex(identifier, name, vertex_type)


    def addDirectedEdge (self, x, y):
        self.directed.add((x,y))
        self.connected_vertices.add(x)
        self.connected_vertices.add(y)

    def addUndirectedEdge (self, x, y):
        self.undirected.add((x,y))
        self.connected_vertices.add(x)
        self.connected_vertices.add(y)





    def print (self):
        print ("vertices: ", str(self.vertices))
        print ("directed edges", str(self.directed_neighbors))
        print ("undirected edges", str(self.undirected_neighbors))


    def toDot(self, filename, grouped_vertices, colors=None, discard_isolated_vertices=False, discard_self_loops=False):
        with open(filename, "w") as file:
            file.write("digraph {\n")
            for group_name, group in grouped_vertices.items():
                file.write("subgraph cluster_" + group_name +"{\n")
                #file.write ("label="+ group_name + "\n")
                file.write ("bgcolor=\"#ededed\"\n")
                #file.write ("graph[style=dotted]\n")
                for v in group:
                    if discard_isolated_vertices == False or v in self.connected_vertices:
                        file.write (v)
                        match self.vertices[v].vertex_type:
                            case VertexType.REVERSIBLE_REACTION:
                                file.write("\t[shape=circle label=\"\" fixedsize=true width=0.3 height=0.3]\n")
                            case VertexType.IRREVERSIBLE_REACTION:
                                file.write("\t[shape=square label=\"\"  fixedsize=true width=0.3 height=0.3 ]\n")
                            case VertexType.SPECIE:
                                if None == colors:
                                    file.write (f"\t[shape=rectangle style=\"rounded,filled\" fillcolor={random_color()}]\n")
                                else:
                                    file.write (f"\t[shape=rectangle style=\"rounded,filled\" fillcolor={colors[v]}]\n")
                file.write ("}")

            for edge in self.directed:
                if discard_self_loops == False or edge[0] != edge[1]:
                    file.write (f"{edge[0]} -> {edge[1]}\n")
            for edge in self.undirected:
                if discard_self_loops == False or edge[0] != edge[1]:
                    file.write (f"{edge[0]} -> {edge[1]} [dir=none color={modifier_edge_color}]\n")

            file.write ("}")










    
