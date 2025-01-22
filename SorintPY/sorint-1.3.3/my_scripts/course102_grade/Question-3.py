import os
import ipaddress

import os

# Check if the IP address in the file matches the target IP address that was in the /var/log/secure

def grade():
    # Get the current user's home directory
    home_dir = os.path.expanduser("~")

    # Construct the full path to the file
    file_path = os.path.join(home_dir, "exam", "txt", "ip.txt")

    try:
        # Check if the file exists
        if os.path.isfile(file_path):
            # Read the contents of the file
            with open(file_path, "r") as file:
                ip_address = file.read().strip()

            # Check if the IP address in the file matches the target IP address
            if ip_address == "192.168.1.312":
                print("\033[92mThe file contains the correct IP address.\033[0m")
            else:
                print("\033[91mThe IP address in the file is incorrect.\033[0m")
        else:
            print("\033[91mThe file does not exist.\033[0m")
    except (FileNotFoundError, IOError):
        print("\033[91mError: Unable to access the file.\033[0m")

if __name__ == "__main__":
    grade()