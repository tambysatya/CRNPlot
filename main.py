
import argparse
import os
import libsbml

from dotfiles import *
from readSBML import buildGraph
from interaction_graph import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", help="the sbml file to be processed.", required=True)
    parser.add_argument("-cnr", "--cnr_file", help="the CNR output png file.")
    parser.add_argument("-qg", "--quotient_file", help="the quotient graph png file.")
    parser.add_argument("-ig", "--interaction_file", help="the interaction graph png file.")
    parser.add_argument("--remove_dot", help="if the dotfile should be removed", action="store_true")

    args = parser.parse_args()

    cnr = args.cnr_file
    qg = args.quotient_file
    ig = args.interaction_file
    rm_dot = args.remove_dot

    if None == cnr and None == qg and None == ig:
        parser.print_help()
        exit(1)

    mdl = libsbml.readSBML(args.input_file).getModel()
    groups = get_groups(mdl)
    colors = generate_colors_for_species(mdl)

    if None != cnr:
        dotfile = generate_dotfile_name(cnr)
        g = buildGraph(mdl)
        g.toDot(dotfile, groups, colors=colors)
        compile_dotfile(dotfile, cnr)
        if rm_dot:
            remove_dotfile(dotfile)

    if None != qg:
        dotfile = generate_dotfile_name(qg)
        g = InteractionGraph(mdl)
        quotient_graph_to_dot(g, dotfile, colors=colors)
        compile_dotfile(dotfile, qg)
        if rm_dot:
            remove_dotfile(dotfile)




    if None != ig:
        dotfile = generate_dotfile_name(ig)
        g = InteractionGraph(mdl)
        interaction_graph_to_dot(g, dotfile, colors=colors)
        compile_dotfile(dotfile, ig)
        if rm_dot:
            remove_dotfile(dotfile)










