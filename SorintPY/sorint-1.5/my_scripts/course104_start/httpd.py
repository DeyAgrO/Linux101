import subprocess

# Import variables from config.py ID=10492
from config import SUDO_PASSWORD


def run_command(command, password):
    """Run a shell command with sudo and password."""
    full_command = f"echo {password} | sudo -S {command}"
    try:
        result = subprocess.run(
            full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{full_command}': {e.stderr}")


def install_httpd(password):
    """Install the httpd package."""
    print("Installing httpd...")
    run_command("yum install -y httpd", password)


def configure_httpd(password):
    """Append an error line to the HTTPD configuration file with elevated privileges."""
    error_line = "ErrorDirective InvalidDirective"
    config_file = "/etc/httpd/conf/httpd.conf"

    try:
        # Use echo and tee to append the error line to the config file with sudo
        command = f"echo '{error_line}' | sudo tee -a {config_file}"
        run_command(command, password)
    except Exception as e:
        print(f"[ERROR] Failed to configure HTTPD: {e}")


def start_httpd(password):
    """Start the httpd service."""
    run_command("systemctl start httpd", password)


def main():
    install_httpd(SUDO_PASSWORD)
    configure_httpd(SUDO_PASSWORD)
    start_httpd(SUDO_PASSWORD)


if __name__ == "__main__":
    main()