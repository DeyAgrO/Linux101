import os

# Check The API token

def grade():
    user = os.getenv('USER')
    file_path = f"/home/{user}/exam/txt/token.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            if "3092DJA9N9J2198DJ12PUD9AZ82JJE" in content:
                print("\033[92mAPI token found in the file.\033[0m")  # Green
            else:
                print("\033[91mAPI token not found in the file.\033[0m")  # Red
    else:
        print("\033[91mThe file 'token.txt' does not exist.\033[0m")  # Red

if __name__ == "__main__":
    grade()