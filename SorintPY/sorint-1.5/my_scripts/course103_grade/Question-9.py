import subprocess
import os
import re

# Import variables from config.py ID=10492
from config import SUDO_PASSWORD

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def run_sudo_command(command, password):
    """Run a command with sudo privileges using the provided password."""
    try:
        result = subprocess.run(
            f"echo {password} | sudo -S {command}",
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print_colored(f"Error running command: {e.stderr}", "31")  # Red
        return None

def check_sudoers_rule(password):
    """Check if users in the 'sorint' group do not need to enter the sudo password."""
    rule_pattern = re.compile(r"%sorint\s+ALL=\(ALL\)\s+NOPASSWD:\s+ALL")

    def check_file(file_content):
        for line in file_content.splitlines():
            if rule_pattern.search(line):
                return True
        return False

    sudoers_file = "/etc/sudoers"
    sudoers_d_dir = "/etc/sudoers.d"

    # Check the main sudoers file
    sudoers_content = run_sudo_command(f"cat {sudoers_file}", password)
    if sudoers_content and check_file(sudoers_content):
        print_colored("The sudoers rule for group 'sorint' is correctly set in /etc/sudoers.", "32")  # Green
        return

    # Check files in the sudoers.d directory
    if os.path.isdir(sudoers_d_dir):
        sudoers_d_files = run_sudo_command(f"ls {sudoers_d_dir}", password)
        if sudoers_d_files:
            for entry in sudoers_d_files.splitlines():
                entry_path = os.path.join(sudoers_d_dir, entry)
                entry_content = run_sudo_command(f"cat {entry_path}", password)
                if entry_content and check_file(entry_content):
                    print_colored(f"The sudoers rule for group 'sorint' is correctly set in {entry_path}.", "32")  # Green
                    return

    print_colored("The sudoers rule for group 'sorint' is not set.", "31")  # Red

def grade():
    check_sudoers_rule(SUDO_PASSWORD)

if __name__ == "__main__":
    grade()