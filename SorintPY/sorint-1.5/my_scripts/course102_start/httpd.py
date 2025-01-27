import subprocess

#### Begin ID=10492
# from path_setup import setup_path
# setup_path()

# Import variables from config.py
from config import SUDO_PASSWORD
#### END ID

# ANSI color codes for messages
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"


# Function to run a command with sudo
def run_with_sudo(command):
    full_command = f'echo {SUDO_PASSWORD} | sudo -S {command}'
    process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout.decode(), stderr.decode()

# Function to print messages with colors
def print_message(color, message):
    print(f"{color}{message}{COLOR_RESET}")

# Main function
def main():
    print(SUDO_PASSWORD)
    # Check if httpd is already installed
    returncode, stdout, stderr = run_with_sudo('dnf list installed httpd')
    if returncode == 0:
        print_message(COLOR_YELLOW, "httpd package is already installed.")
    else:
        # Install httpd package
        print(SUDO_PASSWORD)
        print("Installing httpd package...")
        returncode, stdout, stderr = run_with_sudo('dnf -y install httpd')
        if returncode == 0:
            print_message(COLOR_GREEN, "httpd package installed successfully.")
        else:
            print_message(COLOR_RED, f"Error installing httpd package: {stderr}")
            return

    # Enable httpd service to start on boot
    print("Enabling httpd service...")
    returncode, stdout, stderr = run_with_sudo('systemctl enable httpd')
    if returncode == 0:
        print_message(COLOR_GREEN, "httpd service enabled successfully.")
    elif "already enabled" in stderr:
        print_message(COLOR_YELLOW, "httpd service is already enabled.")
    else:
        print_message(COLOR_RED, f"Error enabling httpd service: {stderr}")

    # Start httpd service
    print("Starting httpd service...")
    returncode, stdout, stderr = run_with_sudo('systemctl start httpd')
    if returncode == 0:
        print_message(COLOR_GREEN, "httpd service started successfully.")
    elif "already running" in stderr:
        print_message(COLOR_YELLOW, "httpd service is already running.")
    else:
        print_message(COLOR_RED, f"Error starting httpd service: {stderr}")

    # Check the status of httpd service
    print("Checking httpd service status...")
    returncode, stdout, stderr = run_with_sudo('systemctl status httpd')
    if returncode == 0:
        print_message(COLOR_GREEN, "httpd service is running.")
    else:
        print_message(COLOR_RED, f"Error: httpd service status is not running properly: {stderr}")

if __name__ == "__main__":
    print(SUDO_PASSWORD)
    main()