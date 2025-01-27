import os

def grade():
    """
    Checks if the environment variables $HOME and $PATH exist and if their values are present in the file /home/$USER/exam/txt/env.txt.
    Returns:
        bool: True if the environment variables and their values are found, False otherwise.
    """
    # Get the environment variables
    home_dir = os.getenv('HOME')
    path_env = os.getenv('PATH')

    if home_dir is None or path_env is None:
        print("\033[91mError: Environment variables $HOME and/or $PATH not found.\033[0m")
        return False

    env_file = f"/home/{os.getenv('USER')}/exam/txt/env.txt"

    if os.path.exists(env_file):
        with open(env_file, "r") as file:
            env_content = file.read()

        if home_dir in env_content and path_env in env_content:
            print("\033[92mEnvironment variables $HOME and $PATH found in the file, and their values are correct.\033[0m")
            return True
        else:
            print("\033[91mError: The values of environment variables $HOME and/or $PATH not found in the file.\033[0m")
            return False
    else:
        print(f"\033[91mError: File '{env_file}' not found.\033[0m")
        return False