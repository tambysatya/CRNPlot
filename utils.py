
import libsbml
import random
import os
import re


def random_color():
        red = random.randint(128,255)
        green = random.randint(128,255)
        blue = random.randint(128,255)

        red_hex = hex(red)[2:]
        green_hex = hex(green)[2:]
        blue_hex = hex(blue)[2:]
        return f"\"#{red_hex}{green_hex}{blue_hex}\""


def get_groups (mdl):
    """
        - returns the dictionary of groups and the list species belonging to it
        - if the sbml file does not have groups, the dictionary is empty
    """
    mplugins = mdl.getPlugin("groups")
    grouped_vertices = {}
    ranks = {}

    if mplugins != None:
        groups = mplugins.getListOfGroups()

        for group in groups:
            name = group.getName()
            print ("processing group: ", group)
            vertices = []
            for member in group.getListOfMembers():
                vertices.append(member.id_ref)
            annotations = group.getAnnotationString()
            match = re.search("<rank>([0-9]+)</rank>", annotations)
            rank=None
            if match:
                rank = match.group(1)
            grouped_vertices[name] = vertices
            ranks[name] = rank
            print ("\tmembers=", vertices, " rank=", rank)
        
    return grouped_vertices, ranks


def generate_colors_for_species(mdl):
    colors = {}
    for specie in mdl.getListOfSpecies():
        colors[specie.getId()] = random_color()
    return colors

def generate_dotfile_name(pngfilename):
    base_output = ".".join(pngfilename.split('.')[:-1]) #os.path.basename(pngfilename).split('.')[0]
    dotfilename = base_output + ".dot"
    return dotfilename




def obtain_id (obj):
    identifier = obj.getId()
    if None == identifier or '' == identifier:
        return obj.getMetaId()
    return identifier


