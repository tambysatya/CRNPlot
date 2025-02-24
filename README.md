# CRNPLOT: a tool for plotting Chemical Reaction Networks


# usage:

- for a single SBML file: specify the input SBML file as well as one or multiple outputs using the options `-cnr` (for the species-reactions graph), `-qg` for the quotient graph and/or `-ig` for the interaction graph. Use the option `--help` for a detailled list of all options.

```
python main.py -i model.sbml -cnr model_cnr.png -qg model_qg.png -ig model_ig.png
```

- for multiple SBML files (command line):

```bash
./plot.sh input_dir output_dir
```

- for multiple SBML files (GUI)

```bash
python main_gui.py
```

# library usage:

## at low level:

- `readSBML.py`: builds the *Chemical Reaction Network* from a SBML model using `g=buildGraph (model)`
- create a list of groups, which is a list of pairs: `groups : [(name, list of vertices)]`
- `graph.py`: converts a *Chemical Reaction Network* into  a dotfile using `g.toDot("model.dot", groups)`
- select the engine you need, *e.g.* 
    ```bash
        dot -Tpng model.dot > model.png
    ```

## helpers: `dotfile.py`:

- `get_dotfile ("model.sbml", "model.dot")` converts a SBML file into a dotfile
- `compile_dotfile ("model.dot", "model.png")` calls `dot` directly from python
- `plot_graph ("model.sbml", "model.png", remove_dot=True)` does the both steps above, then removes the intermediary dotfile if specified




