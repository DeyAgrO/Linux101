import os
import datetime
import random
import socket
import subprocess

# Import variables from config.py
from config import SUDO_PASSWORD

# Path to the log file
LOG_FILE = '/var/log/secure'


# Generate a random PID
def generate_pid():
    return random.randint(1000, 99999)


# Get the hostname before the first dot
def get_hostname():
    return socket.gethostname().split('.')[0]


# Generate a log entry
def generate_log_entry():
    now = datetime.datetime.now()
    username = "bernard"
    ip_address = "192.168.1.312"
    pid = generate_pid()
    myhost = get_hostname()
    return f"{now.strftime('%b %d %H:%M:%S')} {myhost} sshd[{pid}]: Failed password for invalid user {username} from {ip_address} port 12345 ssh2"


# Write the log entry to the file with elevated privileges
def write_log_entry_with_privileges():
    log_entry = generate_log_entry()
    try:
        # Command to append the log entry to the log file
        command = f"echo '{log_entry}' | tee -a {LOG_FILE}"
        
        # Use subprocess to run the command with sudo
        proc = subprocess.Popen(
            ['sudo', '-S', 'bash', '-c', command],  # Use 'bash -c' to run the full command
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Enable text mode for strings instead of bytes
        )
        # Provide the sudo password to the subprocess
        stdout, stderr = proc.communicate(input=f"{SUDO_PASSWORD}\n")

        if proc.returncode == 0:
            print("\033[92mLog entry written successfully.\033[0m")
        else:
            print(f"\033[91m[ERROR] Failed to write log entry: {stderr.strip()}\033[0m")
    except Exception as e:
        print(f"\033[91m[ERROR] Unexpected error while writing log entry: {e}\033[0m")


# Main function
def main():
    try:
        write_log_entry_with_privileges()
    except Exception as e:
        print(f"\033[91m[ERROR] Failed to write log entry: {e}\033[0m")


if __name__ == '__main__':
    main()