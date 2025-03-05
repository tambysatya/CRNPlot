
import libsbml
from itertools import combinations
import argparse
import random

from utils import *



class InteractionGraph ():
    """
        groups :: [(String, [Vertex])]
    """
    def __init__(self, mdl):
        self.directed_edges= set()
        self.undirected_edges = set()
        self.species = {}
        self.connected_vertices = set()

        self.groups = {} # map :: Group_Name -> [Vertex]
        self.vertex_group = {} # map :: Vertex -> Group_Name

        groups = get_groups(mdl)
        if groups == []:
            self.has_groups = False
        else:
            self.has_groups = True
            for group_name, vertices in groups.items():
                self.groups[group_name] = vertices
                for v in vertices:
                    self.vertex_group[v] = group_name
        self.build_interaction_graph(mdl)

    def add_edge (self, x, y):
        xy = (x,y)
        yx = (y,x)

        self.connected_vertices.add(x)
        self.connected_vertices.add(y)
        
        if xy in self.undirected_edges or yx in self.undirected_edges:
            return
        if xy in self.directed_edges:
            return
        if yx in self.directed_edges:
            self.directed_edges.remove(yx)
            self.undirected_edges.add(xy)
            return
        self.directed_edges.add(xy)

    

    def is_undirected_edge_present(self,x,y):
        return (x,y) in self.undirected_edges or (y,x) in self.undirected_edges
    def is_directed_edge_present(self,x,y):
        return (x,y) in self.directed_edges


    def add_reaction (self, reactants, products, modifiers):
        for r in reactants:
            reactant = r.getSpecies()
            self.add_edge(reactant, reactant) #self loop
            for p in products:
                product = p.getSpecies() 
                self.add_edge (reactant, product) #interactions between each pair (reactant, product)
        
        for xi, xj in combinations(reactants,2):
            ri, rj = xi.getSpecies(), xj.getSpecies()
            #bidirectional edge between each pair of reactants
            self.add_edge (ri, rj)
            self.add_edge (rj, ri) 

        for m in modifiers:
            modifier = m.getSpecies()
            for reactant in reactants:
                self.add_edge (modifier, reactant.getSpecies())
            for product in products:
                self.add_edge (modifier, product.getSpecies())

    def build_interaction_graph (self, mdl):


        for specie in mdl.getListOfSpecies():
            self.species[specie.getId()] = specie.getName()
        reactions = mdl.getListOfReactions()

        for reaction in reactions:
            reactants = reaction.getListOfReactants()
            products = reaction.getListOfProducts()
            modifiers = reaction.getListOfModifiers()

            self.add_reaction(reactants, products, modifiers)
            if reaction.getReversible():
                self.add_reaction (products, reactants, modifiers)
    def specieName (self, v):
        return "\"" + self.species[v] + "\""


def interaction_graph_to_dot(g, filename, colors, discard_isolated_vertices=False, discard_self_loops=False):
    with open(filename, "w") as file:
        file.write("digraph {\n")
        #file.write ("concentrate=true\n")
        for group_name, group in g.groups.items():
            file.write ("subgraph cluster_" + group_name + "{\n")
            file.write ("bgcolor=\"#ededed\"\n")
            #file.write ("peripheries=0\n")
            for v in group:
                if v in g.species and (discard_isolated_vertices == False or v in g.connected_vertices):
                    file.write (g.specieName(v) + f"[shape=rectangle style=\"rounded,filled\" fillcolor={colors[v]}]\n")
            file.write("}\n")

        for xi, xj in g.directed_edges:
            if discard_self_loops == False or xi != xj:
                file.write (f"{g.specieName(xi)} -> {g.specieName(xj)}\n")
        for xi, xj in g.undirected_edges:
            if discard_self_loops == False or xi != xj:
                file.write (f"{g.specieName(xi)} -> {g.specieName(xj)} [dir=both]\n")
        file.write("}")

def quotient_graph_to_dot (g, filename, colors, discard_isolated_vertices=False, discard_self_loops=False):
    with open(filename, "w") as file:
        file.write("digraph {\n")
        file.write ("compound=true\n")
        for group_name, group in g.groups.items():
            file.write ("subgraph cluster_" + group_name + "{\n")
            #file.write ("peripheries=0\n")
            file.write ("bgcolor=\"#ededed\"\n")
            for v in group:
                if v in g.species and (discard_isolated_vertices == False or v in g.connected_vertices):
                    file.write (g.specieName(v) + f"[shape=rectangle style=\"rounded,filled\" fillcolor={colors[v]}]\n")
            file.write("}\n")

        group_representant = {}
        group_directed_edges = set()
        group_undirected_edges = set()
        for xi, xj in g.directed_edges:
            group_i, group_j = g.vertex_group[xi], g.vertex_group[xj]
            if group_i == group_j:
                if discard_self_loops == False or xi != xj:
                    file.write (f"{g.specieName(xi)} -> {g.specieName(xj)}\n")
            elif (group_i, group_j) in group_undirected_edges:
                pass
            elif (group_j, group_i) in group_directed_edges:
                group_directed_edges.remove((group_j, group_i))
                group_undirected_edges.add ((group_i, group_j))
                group_undirected_edges.add ((group_j, group_i))
            else:
                group_directed_edges.add((group_i, group_j))
        for xi, xj in g.undirected_edges:
            group_i, group_j = g.vertex_group[xi], g.vertex_group[xj]
            if group_i == group_j:
                if discard_self_loops == False or xi != xj:
                    file.write (f"{g.specieName(xi)} -> {g.specieName(xj)} [dir=both] \n")
            elif (group_i, group_j) in group_undirected_edges:
                pass
            elif (group_j, group_i) in group_directed_edges:
                group_directed_edges.remove((group_j, group_i))
                group_undirected_edges.add ((group_i, group_j))
                group_undirected_edges.add ((group_j, group_i))
            else:
                group_directed_edges.add((group_i, group_j))

        for group_i, group_j in group_directed_edges:
           xi, xj = g.specieName(g.groups[group_i][0]), g.specieName(g.groups[group_j][0])
           file.write (f"{xi} -> {xj} [ltail=cluster_{group_i} lhead=cluster_{group_j} color=\"#3191f3\"]\n")
        for group_i, group_j in group_undirected_edges:
           xi, xj = g.specieName(g.groups[group_i][0]), g.specieName(g.groups[group_j][0])
           file.write (f"{xi} -> {xj} [ltail=cluster_{group_i} lhead=cluster_{group_j} dir=both color=\"#3191f3\"]\n")
        file.write("}")
