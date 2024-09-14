import os
import ast

# Specify the directory path
folder_path = 'codebase'

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


            