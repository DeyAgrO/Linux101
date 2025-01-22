import os
import datetime
import random
import socket
import subprocess

log_file = '/var/log/secure'
user_password = 'sorint'

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

# Write the log entry to the file
def write_log_entry():
    with open(log_file, 'a') as f:
        f.write(generate_log_entry() + '\n')

# Function to execute the script with elevated privileges
def execute_with_privileges():
    try:
        script_path = os.path.abspath(__file__)
        proc = subprocess.Popen(['sudo', 'python3', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate(input=user_password.encode(), timeout=5)  # Provide the password to sudo
        if proc.returncode != 0:
            print(f"\033[91mError writing log entry: {stderr.decode().strip()}\033[0m")
        else:
            print("\033[92mLog entry written successfully.\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[91mError writing log entry: {e}\033[0m")
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    if os.geteuid() != 0:
        execute_with_privileges()
    else:
        try:
            write_log_entry()
            print("Log entry written successfully.")
        except Exception as e:
            print(f"Error writing log entry: {e}")

if __name__ == '__main__':
    main()
