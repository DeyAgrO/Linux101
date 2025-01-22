import subprocess

# ANSI escape codes for colors
orange = '\033[38;5;214m'
yellow_blink = '\033[93;5m'
red = '\033[91m'
green = '\033[92m'
reset = '\033[0m'

def check_ssh_connection(ip_address, user):
    """Check if SSH connection is possible without a password."""
    try:
        # Construct the SSH command
        ssh_command = [
            'ssh',
            '-o', 'BatchMode=yes',  # This option ensures no password prompt
            '-o', 'ConnectTimeout=5',  # Timeout after 5 seconds
            f'{user}@{ip_address}',
            'exit'  # Just exit immediately after connecting
        ]
        
        # Run the SSH command
        result = subprocess.run(ssh_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check the return code to determine if connection was successful
        if result.returncode == 0:
            print(f"{green}Successfully connected to {ip_address} as {user} without a password.{reset}")
        else:
            print(f"{red}Failed to connect to {ip_address} as {user} without a password.{reset}")
            print(result.stderr.decode())
    except Exception as e:
        print(f"{red}An error occurred: {e}{reset}")

def grade():
    try:
        # Prompt to check if SSH key has been copied
        prompt = f"{orange}Did you copy the SSH ID to the remote host? ['Y'es] or ['N'o]: {reset}"
        answer = input(prompt).strip().lower()
        
        # List of acceptable positive responses
        positive_responses = {'yes', 'y'}
        
        if answer in positive_responses:
            # Prompt for the IP address with colored and blinking text
            ip_prompt = f"{orange}Enter the {yellow_blink}IP{reset}{orange} address of the remote host: {reset}"
            ip_address = input(ip_prompt).strip()
            
            # Define the user
            user = 'sorint'
            
            # Check SSH connection
            check_ssh_connection(ip_address, user)
        else:
            print(f"{orange}Continuing without checking SSH connection.{reset}")
    except KeyboardInterrupt:
        print(f"\n{red}Script interrupted by user. Exiting...{reset}")

if __name__ == "__main__":
    grade()