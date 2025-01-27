import subprocess

# Import variables from config.py ID=10492
from config import SUDO_PASSWORD


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


def install_mysql(password):
    """Install MySQL server using yum."""
    print("[INFO] Installing MySQL server...")
    run_command("yum install -y mysql-server", password)


def configure_mysql_logging(password):
    """Configure MySQL logging with elevated privileges."""
    print("[INFO] Configuring MySQL logging...")
    config_lines = [
        "[mysqld]",
        "log-error=/var/log/mysql/mysqld.log"
    ]
    config_file = "/etc/my.cnf"

    try:
        # Use `echo` and `tee` to append configuration lines to the MySQL config file
        command = f"echo '{chr(10).join(config_lines)}' | sudo tee -a {config_file}"
        run_command(command, password)
        print(f"[INFO] Successfully configured logging in {config_file}.")
    except Exception as e:
        print(f"[ERROR] Failed to configure MySQL logging: {e}")


def misconfigure_mysql(password):
    """Add an invalid directive to MySQL configuration with elevated privileges."""
    print("[INFO] Misconfiguring MySQL...")
    error_line = "invalid_option"
    config_file = "/etc/my.cnf"

    try:
        # Use `echo` and `tee` to append the invalid directive to the MySQL config file
        command = f"echo '{error_line}' | sudo tee -a {config_file}"
        run_command(command, password)
        print(f"[INFO] Successfully added invalid directive to {config_file}.")
    except Exception as e:
        print(f"[ERROR] Failed to misconfigure MySQL: {e}")


def create_log_directory(password):
    """Create and set permissions for the MySQL log directory."""
    print("[INFO] Creating MySQL log directory...")
    run_command("mkdir -p /var/log/mysql", password)
    run_command("chown mysql:mysql /var/log/mysql", password)
    run_command("chmod 755 /var/log/mysql", password)
    print("[INFO] MySQL log directory created and permissions set.")


def start_mysql(password):
    """Start or restart the MySQL service."""
    print("[INFO] Starting MySQL service...")
    run_command("systemctl daemon-reload", password)
    run_command("systemctl restart mysqld", password)
    print("[INFO] MySQL service started successfully.")


def main():
    print("[INFO] Starting the MySQL setup process...")
    install_mysql(SUDO_PASSWORD)
    create_log_directory(SUDO_PASSWORD)
    configure_mysql_logging(SUDO_PASSWORD)
    misconfigure_mysql(SUDO_PASSWORD)
    start_mysql(SUDO_PASSWORD)
    print("[INFO] MySQL setup completed.")


if __name__ == "__main__":
    main()