
import libsbml
import graph 
from graph import VertexType


test_mdl = libsbml.readSBML("test.xml").getModel()




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
        g.addVertex(identifier, name, VertexType.REACTION)

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



        
def get_dotfile(mdl):
    g = buildGraph(mdl)
    mplugins = mdl.getPlugin("groups")
    groups = mplugins.getListOfGroups()

    grouped_vertices = []

    for group in groups:
        name = group.getName()
        print ("processing group: ", group)
        vertices = []
        for member in group.getListOfMembers():
            vertices.append(member.id_ref)
        grouped_vertices.append((name, vertices))
        print ("\tmembers=", vertices)
    
    g.toDot ("test.dot", grouped_vertices)




            
            


