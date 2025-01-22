import os

def check_bashrc_alias():
    home_dir = os.path.expanduser("~")
    bashrc_file = os.path.join(home_dir, ".bashrc")

    # Check if the bashrc file exists
    if not os.path.exists(bashrc_file):
        print(f"\033[91mError: {bashrc_file} does not exist.\033[0m")
        return False

    # Check if the bashrc file contains the specified string
    with open(bashrc_file, 'r') as file:
        if "alias ipa=\"ip --color a\"" in file.read():
            return True
        else:
            return False

def grade():
    if check_bashrc_alias():
        print(f"\033[92mThe 'alias ipa=\"ip --color a\"' is present in the .bashrc file 'don't forget to run (source .bashrc)'.\033[0m")
    else:
        print(f"\033[91mThe 'alias ipa=\"ip --color a\"' is not present in the .bashrc file.\033[0m")

if __name__ == "__main__":
    grade()