
import libsbml

from utils import *

import os

def get_dotfile(input_filename, dotfilename):
    mdl = libsbml.readSBML(input_filename).getModel()
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
    
    g.toDot (dotfilename, grouped_vertices)


def compile_dotfile (dotfilename, pngfilename):

    extension = pngfilename.split('.')[-1]
    if extension == 'png':
        os.system(f"dot -Tpng {dotfilename} > {pngfilename}")
    else:
        os.system(f"dot -Tsvg {dotfilename} > {pngfilename}")


def remove_dotfile (filename):
    os.system(f"rm {filename}")


