import subprocess
import re

# Import variables from config.py ID=10492
from config import SUDO_PASSWORD

def run_sudo_command(command, password):
    """Run a command with sudo and return the output."""
    full_command = f'echo {password} | sudo -S {command}'
    
    try:
        result = subprocess.run(full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return e.stdout.strip(), e.stderr.strip()

def grade():
    # ANSI escape codes for colors
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    # Command to list enabled services
    command = "firewall-cmd --list-services"
    
    output, error = run_sudo_command(command, SUDO_PASSWORD)
    
    if error:
        print(f"{RED}Error checking firewall services: {error}{RESET}")
        return
    
    # Use regular expressions to match whole words
    http_enabled = re.search(r'\bhttp\b', output)
    https_enabled = re.search(r'\bhttps\b', output)
    
    if http_enabled:
        print(f"{GREEN}http Firewall service is enabled{RESET}")
    else:
        print(f"{RED}http Firewall service is not enabled{RESET}")
    
    if https_enabled:
        print(f"{GREEN}https Firewall service is enabled{RESET}")
    else:
        print(f"{RED}https Firewall service is not enabled{RESET}")

if __name__ == "__main__":
    grade()