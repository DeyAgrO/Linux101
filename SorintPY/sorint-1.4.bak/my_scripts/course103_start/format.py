import subprocess
import os

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

def check_filesystem(disk, sudo_password):
    """Check if the disk has a filesystem."""
    command = f'blkid {disk}'
    output, error = run_sudo_command(command, sudo_password)
    
    if error:
        if "exit status 2" in error:  # blkid returns exit status 2 if the disk has no recognizable filesystem
            return False
        print_colored(f"Error checking filesystem on {disk}: {error}", "31")  # Red
        return None
    
    return True

def main():
    sudo_password = "sorint"  # Replace with your actual sudo password or securely prompt for it
    disk = "/dev/sdb"
    
    # Check if the disk exists
    if not os.path.exists(disk):
        print_colored(f"The disk {disk} does not exist.", "31")  # Red
        return False

    # Check if the disk has a filesystem
    has_filesystem = check_filesystem(disk, sudo_password)
    
    if has_filesystem is None:
        return False
    
    if has_filesystem:
        print_colored(f"The disk {disk} already has a filesystem.", "33")  # Yellow
        return True
    
    # Step 1: Unmount the disk if it's mounted
    command = f'umount {disk}'
    output, error = run_sudo_command(command, sudo_password)
    
    if error and "not mounted" not in error:
        print_colored(f"Error unmounting {disk}: {error}", "31")  # Red
        return False
    
    # Step 2: Create the ext4 filesystem
    command = f'mkfs.ext4 {disk}'
    output, error = run_sudo_command(command, sudo_password)
    
    if error:
        print_colored(f"Error formatting {disk} with ext4: {error}", "31")  # Red
        return False

    print_colored(f"Successfully formatted {disk} with ext4 filesystem.", "32")  # Green
    return True

if __name__ == "__main__":
    main()