import os
import importlib
import sys

def grade_course(course_name):
    """
    Runs all the scripts in the corresponding 'grade' directory and reports the results.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(base_dir)
    grade_dir = os.path.join(parent_dir, 'my_scripts', f'{course_name}_grade')

    # Adding the parent directory to sys.path
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

    if os.path.isdir(grade_dir):
        filenames = [f for f in os.listdir(grade_dir) if f.endswith('.py') and f != '__init__.py']
        filenames.sort(key=lambda x: int(x.split('-')[1].split('.')[0]))

        for filename in filenames:
            module_name = f'my_scripts.{course_name}_grade.{os.path.splitext(filename)[0]}'
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, 'grade'):
                    try:
                        module.grade()
                        print(f"\033[33m'{filename}' graded Finished.\033[0m")
                    except Exception as e:
                        print(f"\033[31m'{filename}' failed to grade: {e}\033[0m")
                else:
                    print(f"\033[33mNo 'grade()' function found in '{filename}'\033[0m")
            except ModuleNotFoundError as e:
                print(f"\033[31mModule '{module_name}' not found: {e}\033[0m")
    else:
        print(f"Directory '{grade_dir}' not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: grade.py <course_name>")
        sys.exit(1)

    course_name = sys.argv[1]
    grade_course(course_name)

if __name__ == "__main__":
    main()