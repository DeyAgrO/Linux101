import os

def grade():
    # Code to search for
    code_to_find = "SO6ZK9200LFQ82"
    
    # Get the current user's home directory
    user_home = os.path.expanduser("~")
    file_path = os.path.join(user_home, "exam/txt/rpmcode.txt")
    
    # ANSI escape codes for colors
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"{RED}The file {file_path} does not exist.{RESET}")
        return
    
    # Read and check the file for the code
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if code_to_find in content:
                print(f"{GREEN}The RPM code is correct{RESET}")
            else:
                print(f"{RED}The RPM code couldn't be found{RESET}")
    except Exception as e:
        print(f"{RED}An error occurred: {e}{RESET}")

if __name__ == "__main__":
    grade()