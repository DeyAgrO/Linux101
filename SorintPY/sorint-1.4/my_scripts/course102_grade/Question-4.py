import os

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def check_known_hosts():
    known_hosts_path = os.path.expanduser('~/.ssh/known_hosts')
    try:
        with open(known_hosts_path, 'r') as file:
            lines = file.readlines()
        return len(lines)
    except FileNotFoundError:
        return 0

def check_ssh_keys():
    ssh_dir = os.path.expanduser('~/.ssh/')
    private_key = os.path.join(ssh_dir, 'sorintKey')
    public_key = os.path.join(ssh_dir, 'sorintKey.pub')
    return os.path.isfile(private_key) and os.path.isfile(public_key)

def grade():
    known_hosts_count = check_known_hosts()
    ssh_keys_ok = check_ssh_keys()

    if known_hosts_count > 0:
        print_colored(f"You have {known_hosts_count} known host entries and that is good :)", "92")  # Green
    else:
        print_colored("You don't have any entries in the known host.", "91")  # Red

    if ssh_keys_ok:
        print_colored("You have the sorintKey and sorintKey.pub files.", "92")  # Green
    else:
        print_colored("You don't have the sorintKey and sorintKey.pub files.", "91")  # Red

if __name__ == "__main__":
    grade()