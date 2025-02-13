
import argparse
import os

from dotfiles import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", help="the sbml file to be processed.", required=True)
    parser.add_argument("-o", "--output_file", help="the output png file.", required=True)
    args = parser.parse_args()

    plot_graph(args.input_file, args.output_file)

