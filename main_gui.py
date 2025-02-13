
from tkinter import filedialog, Tk
from dotfiles import *
import os, sys



if __name__ == '__main__':

    root = Tk()
    root.withdraw()

    files_paths = filedialog.askopenfilenames( 
                parent=root,
                title="Select SBML file(s)",
                filetypes=[("All files", "*.*")]
    ) 

    if not files_paths: # If no file is selected
        print("No files selected.\n")
        sys.exit(1)

    directory_path = filedialog.askdirectory(title='Select Directory to Save Output')

    files_names = [os.path.basename(file_path).split('.')[0] for file_path in files_paths]

    for file_path, file_name in zip (files_paths,files_names):
       
        output_dotfile = directory_path+"/"+file_name + ".dot"
        output_png = directory_path+"/"+file_name + ".png"
        plot_graph(file_path,output_png)
