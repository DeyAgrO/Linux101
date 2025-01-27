import subprocess

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def run_command(command, password):
    """Run a command with sudo privileges without password prompt."""
    try:
        result = subprocess.run(
            f"echo {password} | sudo -S {command}",
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return None, e.stderr

def restart_network_manager(password):
    """Restart NetworkManager to resolve version mismatch issues."""
    command = "systemctl restart NetworkManager"
    _, error = run_command(command, password)
    if error:
        print_colored(f"Error restarting NetworkManager: {error}", "31")  # Red
        return False
    return True

def main():
    # User credentials (change these as needed)
    username = 'sorint'
    password = 'sorint'

    # Network interface and new connection name
    interface = 'eth1'
    new_connection = 'sorint'

    # Check if the new connection already exists
    check_connection_command = f"nmcli connection show {new_connection}"
    stdout, stderr = run_command(check_connection_command, password)
    if stdout:
        print_colored(f"Connection {new_connection} already exists. No changes will be made.", "33")  # Yellow
        return
    elif "no such connection profile" not in stderr:
        print_colored(f"Error checking connection: {stderr}", "31")  # Red
        return

    # Delete all existing connections for the interface
    list_connections_command = f"nmcli -t -f NAME,DEVICE connection show"
    connections, error = run_command(list_connections_command, password)
    if error:
        if "Warning: nmcli" in error and "NetworkManager" in error and "versions don't match" in error:
            print_colored(f"Version mismatch detected. Attempting to restart NetworkManager...", "33")  # Yellow
            if not restart_network_manager(password):
                print_colored("Failed to resolve version mismatch. Exiting.", "31")  # Red
                return
            # Re-run the command after restarting NetworkManager
            connections, error = run_command(list_connections_command, password)
            if error:
                print_colored(f"Error listing connections: {error}", "31")  # Red
                return
        else:
            print_colored(f"Error listing connections: {error}", "31")  # Red
            return

    if connections:
        for line in connections.split('\n'):
            if line.strip():
                name, device = line.split(':')
                if device == interface:
                    delete_command = f"nmcli connection delete \"{name}\""
                    _, error = run_command(delete_command, password)
                    if error:
                        print_colored(f"Error deleting connection {name}: {error}", "31")  # Red
                        return

    # Create a new connection and configure it with specific IP, gateway, and DNS
    create_command = (
        f"nmcli connection add type ethernet ifname {interface} con-name {new_connection} "
        f"ipv4.method manual ipv4.addresses 10.10.10.10/24 ipv4.gateway 10.10.10.10 "
        f"ipv4.dns '10.10.10.10' connection.autoconnect yes"
    )
    _, error = run_command(create_command, password)
    if error:
        print_colored(f"Error creating connection {new_connection}: {error}", "31")  # Red
        return

    # Set the new connection as primary and bring it up
    modify_command = f"nmcli connection modify {new_connection} connection.autoconnect-priority 1"
    _, error = run_command(modify_command, password)
    if error:
        print_colored(f"Error modifying connection {new_connection}: {error}", "31")  # Red
        return

    up_command = f"nmcli connection up {new_connection}"
    _, error = run_command(up_command, password)
    if error:
        print_colored(f"Error bringing up connection {new_connection}: {error}", "31")  # Red
        return

    print_colored(f"Connection {new_connection} created and existing connections deleted.", "32")  # Green

if __name__ == "__main__":
    main()