
import argparse
import os
import libsbml

from dotfiles import *
from crn_graph import *
from interaction_graph import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", help="the sbml file to be processed.", required=True)
    parser.add_argument("-crn", "--crn_file", help="the CRN output png file.")
    parser.add_argument("-qg", "--quotient_file", help="the quotient graph png file.")
    parser.add_argument("-ig", "--interaction_file", help="the interaction graph png file.")
    parser.add_argument("--remove-dot", help="if the dotfile should be removed", action="store_true")
    parser.add_argument("--no-isolated-species", help="removes the isolated vertices", action="store_true", default=False)
    parser.add_argument("--no-self-loops", help="do not display self interactions", action="store_true", default=False)

    args = parser.parse_args()


    crn = args.crn_file
    qg = args.quotient_file
    ig = args.interaction_file
    rm_dot = args.remove_dot
    discard_isolated_vertices = args.no_isolated_species
    discard_self_loops = args.no_self_loops


    if None == crn and None == qg and None == ig:
        parser.print_help()
        exit(1)

    mdl = libsbml.readSBML(args.input_file).getModel()
    groups, ranks = get_groups(mdl)
    colors = generate_colors_for_species(mdl)

    if None != crn:
        dotfile = generate_dotfile_name(crn)
        g = CNRGraph(mdl)
        g.toDot(dotfile, groups, colors, discard_isolated_vertices=discard_isolated_vertices, discard_self_loops=discard_self_loops)
        compile_dotfile(dotfile, crn)
        if rm_dot:
            remove_dotfile(dotfile)

    if None != qg:
        dotfile = generate_dotfile_name(qg)
        g = InteractionGraph(mdl)
        quotient_graph_to_dot(g,ranks, dotfile, colors, discard_isolated_vertices=discard_isolated_vertices, discard_self_loops=discard_self_loops)
        compile_dotfile(dotfile, qg)
        if rm_dot:
            remove_dotfile(dotfile)




    if None != ig:
        dotfile = generate_dotfile_name(ig)
        g = InteractionGraph(mdl)
        interaction_graph_to_dot(g, dotfile, colors, discard_isolated_vertices=discard_isolated_vertices, discard_self_loops=discard_self_loops)
        compile_dotfile(dotfile, ig)
        if rm_dot:
            remove_dotfile(dotfile)










