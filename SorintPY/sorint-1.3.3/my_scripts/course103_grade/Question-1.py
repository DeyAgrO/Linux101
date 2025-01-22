import socket
import sys

def grade():
    # Hostname to check
    # Change this to the desired hostname
    required_hostname = 'alma9.sorint.exam.com'

    # Get the current hostname
    current_hostname = socket.gethostname()

    # ANSI escape codes for colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BLUE = '\033[94m'

    # Check if the current hostname matches the required hostname
    if current_hostname != required_hostname:
        print(f"{RED}The hostname does not match {BLUE}{required_hostname}.{RESET}")
    else:
        print(f"{GREEN}The hostname matches {BLUE}{required_hostname}{RESET}")

if __name__ == "__main__":
    grade()