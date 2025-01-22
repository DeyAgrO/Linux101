import os

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def check_texts_file(file_path):
    """Check if the file has 16 entries and each line ends with .txt."""
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        if len(lines) != 16:
            print_colored(f"The file '{file_path}' does not contain all the .txt files.", "31")  # Red
            return
        
        for line in lines:
            if not line.strip().endswith('.txt'):
                print_colored(f"Error: Line '{line.strip()}' in {file_path} does not end with .txt.", "31")  # Red
                return
        
        print_colored(f"{file_path} is valid.", "32")  # Green
    except FileNotFoundError:
        print_colored(f"Error: {file_path} not found.", "31")  # Red

def check_sorint_file(file_path):
    """Check if the file has 9 entries and each line contains the word 'sorint'."""
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        if len(lines) != 9:
            print_colored(f"The file '{file_path}' does not contain 9 entries.", "31")  # Red
            return
        
        for line in lines:
            if 'sorint' not in line:
                print_colored(f"Error: Line '{line.strip()}' in {file_path} does not contain 'sorint'.", "31")  # Red
                return
        
        print_colored(f"{file_path} is valid.", "32")  # Green
    except FileNotFoundError:
        print_colored(f"Error: {file_path} not found.", "31")  # Red

def grade():
    user = os.getenv('USER')
    texts_file_path = f"/home/{user}/exam/txt/texts.txt"
    sorint_file_path = f"/home/{user}/exam/txt/sorint.txt"
    
    check_texts_file(texts_file_path)
    check_sorint_file(sorint_file_path)

if __name__ == "__main__":
    grade()