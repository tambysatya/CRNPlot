# CRNPLOT: a tool for plotting Chemical Reaction Networks


# usage:

- for a single SBML file: specify the input SBML file as well as one or multiple outputs using the options `-cnr` (for the species-reactions graph), `-qg` for the quotient graph and/or `-ig` for the interaction graph. Use the option `--help` for a detailed list of all options.

```
python main.py -i model.xml -cnr model_cnr.png -qg model_qg.png -ig model_ig.png
```

- for multiple SBML files (command line):

```bash
./plot.sh input_dir output_dir
```

- To discard isolated species, add the option --no-isolated-species

- To get a list of all options

```
  python main.py --help
```

- remark: to display the hierarchy, simply add a rank annotation in each group declaration, e.g:
```xml
 <groups:listOfGroups>
      <groups:group groups:id="group_1" groups:name="group1" groups:kind="collection">
        <annotation>
          <rank>1</rank>
        </annotation>
        <groups:listOfMembers>
          ...
        </groups:listOfMembers>
      </groups:group>
     ... 
    </groups:listOfGroups>

```
# notes

How to cite this work:

Manvel Gasparyan, Satya Tamby, G.V. HarshaRani, Upinder S. Bhalla, and Ovidiu Radulescu, Automated hierarchical block decomposition of biochemical networks


