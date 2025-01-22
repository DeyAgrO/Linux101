import subprocess
import re

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def run_command(command):
    """Run a shell command and return its output."""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip()

def grade():
    # Desired network settings
    required_ip = '172.168.1.200'
    required_gateway = '172.168.1.1'
    required_dns1 = '172.168.1.1'
    required_dns2 = '1.1.1.1'

    # ANSI escape codes for colors
    RED = '31'
    GREEN = '32'

    # Check if nmcli is available
    if not run_command("which nmcli"):
        print_colored("nmcli command not found. Please ensure NetworkManager is installed.", RED)
        return

    # Query connection details using nmcli
    connection_name = 'sorint'
    connection_details = run_command(f"nmcli connection show {connection_name}")

    if not connection_details:
        print_colored(f"Connection '{connection_name}' not found.", RED)
        return

    # Extract IP address
    ip_match = re.search(r"ipv4.addresses:\s+(\S+)", connection_details)
    ip_set = ip_match and ip_match.group(1).startswith(required_ip)

    # Extract gateway
    gateway_match = re.search(r"ipv4.gateway:\s+(\S+)", connection_details)
    gateway_set = gateway_match and gateway_match.group(1) == required_gateway

    # Extract and split DNS settings
    dns_match = re.search(r"ipv4.dns:\s+([\S,]+)", connection_details)
    dns_set_1 = dns_set_2 = False
    if dns_match:
        dns_servers = dns_match.group(1).split(',')
        dns_set_1 = required_dns1 in dns_servers
        dns_set_2 = required_dns2 in dns_servers

    # Print results
    if ip_set:
        print_colored(f"IP address is correctly set to {required_ip}", GREEN)
    else:
        print_colored(f"IP address not set to {required_ip}", RED)

    if gateway_set:
        print_colored(f"Gateway is correctly set to {required_gateway}", GREEN)
    else:
        print_colored(f"Gateway not set to {required_gateway}", RED)

    if dns_set_1:
        print_colored(f"DNS1 is correctly set to {required_dns1}", GREEN)
    else:
        print_colored(f"DNS1 not set to {required_dns1}", RED)

    if dns_set_2:
        print_colored(f"DNS2 is correctly set to {required_dns2}", GREEN)
    else:
        print_colored(f"DNS2 not set to {required_dns2}", RED)

if __name__ == "__main__":
    grade()