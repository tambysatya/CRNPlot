
import libsbml
import graph 
from graph import VertexType

import argparse
import subprocess






def obtain_id (obj):
    identifier = obj.getId()
    if None == identifier or '' == identifier:
        return obj.getMetaId()
    return identifier

def buildGraph (mdl):
    g = graph.Graph()

    species = mdl.getListOfSpecies()
    reactions = mdl.getListOfReactions()

    for specie in species:
        name = specie.getName()
        identifier = obtain_id(specie)
        if name == None:
            name=identifier

        print ("adding specie: ", name, " id=", identifier)    
        g.addVertex(identifier, name, VertexType.SPECIE)

    for reaction in reactions:
        name = reaction.getName()
        identifier = obtain_id(reaction)
        if name == None:
            name=identifier
        print("processing reaction: ", name) 
        if reaction.getReversible():
            g.addVertex(identifier, name, VertexType.REVERSIBLE_REACTION)
        else:
            g.addVertex(identifier, name, VertexType.IRREVERSIBLE_REACTION)


        for modifier in reaction.getListOfModifiers():
            modifier_id = modifier.getSpecies()
            g.addUndirectedEdge (modifier_id, identifier)
            print ("\tadding modifier=", modifier_id)

        for reactant in reaction.getListOfReactants():
            g.addDirectedEdge(reactant.getSpecies(), identifier)
            print ("\tadding reactant=", reactant.getSpecies())

        for product in reaction.getListOfProducts():
            product_id = product.getSpecies()
            g.addDirectedEdge(identifier, product_id)
            print ("\tadding product=", product_id)



    return g



        

