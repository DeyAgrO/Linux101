import subprocess
from Modules.config import SUDO_PASSWORD # ID=10492

# ANSI color codes for messages
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"

# Function to print messages with colors
def print_message(color, message):
    print(f"{color}{message}{COLOR_RESET}")

def run_command(command, password=None):
    """Run a shell command with optional sudo password."""
    if password:
        full_command = f"echo {password} | sudo -S {command}"
    else:
        full_command = command
    try:
        result = subprocess.run(
            full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr}")


def install_pkg(rpm_pkg, password):
    """Install MySQL server using yum."""
    run_command(f"yum install -y {rpm_pkg}", password)

def configure_pkg_logging(config_lines, config_file, rpm_pkg, password):
    """Configure logging for a package with elevated privileges."""
    try:
        # Join the configuration lines with newlines
        config_content = "\n".join(config_lines)

        # Command to append configuration lines to the config file
        command = f"echo '{config_content}' | tee -a {config_file}"

        # Use subprocess to run the command with sudo
        proc = subprocess.Popen(
            ['sudo', '-S', 'bash', '-c', command],  # Use 'bash -c' to execute the full command
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Enable text mode for strings instead of bytes
        )

        # Provide the sudo password to the subprocess
        stdout, stderr = proc.communicate(input=f"{password}\n")

    except Exception as e:
        print(f"\033[91m[ERROR] Unexpected error while configuring {rpm_pkg} logging: {e}\033[0m")

def misconfigure_pkg(rpm_pkg, config_file, error_line, password):
    """Add an invalid directive to a package's configuration file with elevated privileges."""
    try:
        # Command to append the invalid directive to the config file
        command = f"echo '{error_line}' | tee -a {config_file}"

        # Use subprocess to run the command with sudo
        proc = subprocess.Popen(
            ['sudo', '-S', 'bash', '-c', command],  # Use 'bash -c' to execute the full command
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Enable text mode for strings instead of bytes
        )

        # Provide the sudo password to the subprocess
        stdout, stderr = proc.communicate(input=f"{password}\n")

    except Exception as e:
        print(f"\033[91m[ERROR] Unexpected error while Configuring {rpm_pkg}: {e}\033[0m")


def start_service(service, password):
    """Start the httpd service."""
    run_command("systemctl daemon-reload", password)
    run_command(f"systemctl start {service}", password)

def daemon_reload(password):
    run_command("systemctl daemon-reload", password)