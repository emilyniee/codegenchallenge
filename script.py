import os
import ast
import networkx as nx
import matplotlib.pyplot as plt


# Specify the directory path
folder_path = 'codebase'
G = nx.DiGraph()

for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        
        # Check if it's a file (this check is redundant because os.walk already gives files)
        if os.path.isfile(file_path) and filename.endswith('.py'):
            # Open and parse the file
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"filename: {filename}")

                tree = ast.parse(content)
                # Filter only import statements (Import and ImportFrom nodes)
                import_statements = [node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]

                # Print the found import statements
                for stmt in import_statements:
                    print(ast.dump(stmt, indent=4))
                
                for node in ast.walk(tree):
                    # Process 'import' statements
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            imported_module = alias.name
                            G.add_edge(filename, imported_module)
                    # Process 'from ... import ...' statements
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            G.add_edge(filename, node.module)

nx.draw(G, with_labels=True)
plt.show()
