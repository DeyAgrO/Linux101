import os
import subprocess

def run_sudo_command(command, sudo_password):
    """Run a command with sudo and return the output."""
    full_command = f'echo {sudo_password} | sudo -S {command}'
    try:
        result = subprocess.run(full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, e.stderr.strip()

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def grade():
    sudo_password = "sorint"  # Replace with your actual sudo password or securely prompt for it
    folder_path = "/external"
    device = "/dev/sdb"
    user = "sorint"
    group = "sorint"
    
    # Step 1: Check if the folder /external exists
    if not os.path.isdir(folder_path):
        print_colored(f"The folder {folder_path} does not exist.", "31")  # Red
        return False

    # Step 2: Check if the device /dev/sdb is mounted on /external
    command = f'mount | grep "on {folder_path} type"'
    output, error = run_sudo_command(command, sudo_password)
    
    if error:
        print_colored(f"Error checking mount status: {error}", "31")  # Red
        return False
    
    if not output or device not in output:
        print_colored(f"The device {device} is not mounted on {folder_path}.", "31")  # Red
        return False

    # Step 3: Check if the folder /external has ownership by user sorint and group sorint
    try:
        stat_info = os.stat(folder_path)
    except FileNotFoundError:
        print_colored(f"The folder {folder_path} does not exist.", "31")  # Red
        return False

    uid = stat_info.st_uid
    gid = stat_info.st_gid
    
    command = f'id -u {user}'
    output, error = run_sudo_command(command, sudo_password)
    
    if error:
        print_colored(f"Error retrieving UID for user {user}: {error}", "31")  # Red
        return False
    
    if not output or int(output) != uid:
        print_colored(f"The folder {folder_path} is not owned by the user {user}.", "31")  # Red
        return False
    
    command = f'id -g {group}'
    output, error = run_sudo_command(command, sudo_password)
    
    if error:
        print_colored(f"Error retrieving GID for group {group}: {error}", "31")  # Red
        return False
    
    if not output or int(output) != gid:
        print_colored(f"The folder {folder_path} is not owned by the group {group}.", "31")  # Red
        return False

    print_colored(f"The folder {folder_path} exists, {device} is mounted on it, and it is owned by {user}:{group}.", "32")  # Green
    return True

if __name__ == "__main__":
    # Always print this message at the beginning
    print_colored(f"In Case of any error use the command 'mkfs.ext4 /dev/sdb'", "33")  # Yellow
    
    # Proceed with the grading checks
    grade()