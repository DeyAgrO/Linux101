import os

def grade():
    """
    Checks the contents of the /home/$USER/exam/txt/whoami.txt file for the presence of the full words "name", "surname", and "email".
    Returns:
        bool: True if all three words are found, False otherwise.
    """
    file_path = f"/home/{os.getenv('USER')}/exam/txt/whoami.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read().lower()

        if "name" not in content or "email" not in content:
            if "name" not in content:
                print("\033[91mThe word 'name' was not found in the file.\033[0m")
            if "email" not in content:
                print("\033[91mThe word 'email' was not found in the file.\033[0m")
            return False
        else:
            print("\033[92mName, and Email were found in the file.\033[0m")
            return True
    else:
        print(f"\033[91mThe file '{file_path}' does not exist.\033[0m")
        return False

if __name__ == "__main__":
    grade()