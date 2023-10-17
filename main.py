import importlib
import os
import os.path

def main():

    # Path of the code file
    path_to_code = os.path.dirname(os.path.abspath(__file__))

    # Get list of possible Python files
    python_files = [x for x in os.listdir(path_to_code) if x.lower().endswith(".py")]
    # Remove main.py from list
    python_files = list(filter(lambda x: x.lower() != "main.py", python_files))

    # Try to import each file from the list
    for python_file in python_files:
        try:
            obj = importlib.import_module(os.path.basename(python_file[:-3]))
        except ImportError:
            print(f"Error: couldn't import Python file '{python_file}' as a module.")

        try:
            print(f"Imported {python_file}: Hi {obj.name}!")
        except AttributeError:
            print(f"Error: Python file '{python_file}' doesn't contain the variable 'name'!")

if __name__ == "__main__":
    main()