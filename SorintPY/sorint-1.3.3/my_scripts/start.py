import os
import importlib
import sys

def run_scripts(course_name):
    """
    Runs all the scripts in the corresponding 'start' directory.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(base_dir)
    start_dir = os.path.join(parent_dir, 'my_scripts', f'{course_name}_start')

    # Adding the parent directory to sys.path
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

    if os.path.isdir(start_dir):
        for filename in os.listdir(start_dir):
            if filename.endswith('.py') and filename != '__init__.py' :
                module_name = f'my_scripts.{course_name}_start.{os.path.splitext(filename)[0]}'
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, 'main'):
                        module.main()
                    else:
                        print(f"No 'main()' function found in {filename}")
                except ModuleNotFoundError as e:
                    print(f"Module '{module_name}' not found: {e}")
    else:
        print(f"Directory '{start_dir}' not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: start.py <course_name>")
        sys.exit(1)

    course_name = sys.argv[1]
    run_scripts(course_name)

if __name__ == "__main__":
    main()