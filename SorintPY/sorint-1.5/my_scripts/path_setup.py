import sys
import os

def setup_path():
    """
    Ensures that the parent directory of the current script is in sys.path.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)  # This points to 'my_scripts'
    if parent_dir not in sys.path:
        sys.path.append(parent_dir)
