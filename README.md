# CRNPLOT: a tool for plotting Chemical Reaction Networks


# usage:

- for a single SBML file: specify the input SBML file as well as one or multiple outputs using the options `-cnr` (for the species-reactions graph), `-qg` for the quotient graph and/or `-ig` for the interaction graph. Use the option `--help` for a detailled list of all options.

```
python main.py -i model.xml -cnr model_cnr.png -qg model_qg.png -ig model_ig.png
```

- for multiple SBML files (command line):

```bash
./plot.sh input_dir output_dir
```

# notes

This work is part of the BlockBioNet project. The paper is under review.



