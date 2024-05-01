import os
from lexer import parser, execute_parse_tree, add_node, parseGraph, draw, nx, plt

def run_lex_file(file_path):
  with open(file_path, 'r') as file:
    data = file.read()
    root = add_node({"type":"ROOT", "label":"ROOT"})
    result = parser.parse(data)
    try:
      parseGraph.add_edge(root["counter"], result["counter"]) # Add an edge from the root node to the result node.
    except TypeError:
      return
    except Exception as e:
      print(e)
    draw = False
    labels = nx.get_node_attributes(parseGraph, 'label') # Get the labels of the nodes in the parse tree.
    if (draw):
        
        # pos = graphviz_layout(parseGraph, prog="dot")  # commented out if on MacOs (not supported)
        nx.draw(parseGraph,labels=labels, with_labels=True, font_weight='bold') # pos=pos)
        plt.show()

  execute_parse_tree(parseGraph)

def main():
  while True:
    # Print a menu to choose file to be read
    examples_path = "examples/"
    os.system('cls')
    print(" Choose a file to read:")
    print("---------------------------")
    # List all .lex files in examples folder
    files = [file for file in os.listdir(examples_path) if file.endswith(".lex")]
    for i, file in enumerate(files):
      # print last file with a different format:
      padding = ' ' * (15 - len(file))
      print(f" ├── {file}{padding} -> ({i+1})")
    print(" └── (exit)          -> (x)")

    # Get user input
    file_index = input("> ")
    if file_index == 'x':
      break
    try:
      file_index = int(file_index)
    except ValueError:
      input("Invalid option . . . ")
      continue
    if file_index < 1 or file_index > len(files):
      input("Invalid option . . . ")
      continue
    file_path = examples_path + files[file_index-1]
    run_lex_file(file_path)
    input("\nPress Enter to continue . . . ")
  
if __name__ == "__main__":
  main()