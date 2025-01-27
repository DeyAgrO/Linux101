import subprocess
import re
from Modules.config import SUDO_PASSWORD # ID=10492

def run_sudo_command(command, password):
    """Run a command with sudo and return the output."""
    full_command = f'echo {password} | sudo -S {command}'
    try:
        result = subprocess.run(full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, e.stderr.strip()

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def grade():
    repo_file = '/etc/yum.repos.d/librewolf.repo'
    
    # Check if the repo file exists with sudo privileges
    command = f'ls {repo_file}'
    output, error = run_sudo_command(command, SUDO_PASSWORD)
    
    if error:
        print_colored("The librewolf.repo file does not exist.", "31")  # Red
        return False

    # Read the repo file with sudo privileges
    command = f'cat {repo_file}'
    output, error = run_sudo_command(command, SUDO_PASSWORD)
    
    if error:
        print_colored(f"Error reading the librewolf.repo file: {error}", "31")  # Red
        return False

    # Define the required configuration lines with case-insensitive regex patterns
    required_config = {
        'name': r'name\s*=\s*librewolf',
        'baseurl': r'baseurl\s*=\s*https://rpm\.librewolf\.net',
        'gpgcheck': r'gpgcheck\s*=\s*1',
        'gpgkey': r'gpgkey\s*=\s*https://rpm\.librewolf\.net/pubkey\.gpg',
        'enabled': r'enabled\s*=\s*1'
    }

    # Check if the required configuration is present in the file
    for key, pattern in required_config.items():
        if not re.search(pattern, output, re.IGNORECASE):
            print_colored(f"The configuration for '{key}' is not correctly set.", "31")  # Red
            return False

    print_colored("The LibreWolf repository is correctly configured and enabled.", "32")  # Green
    return True

if __name__ == "__main__":
    grade()