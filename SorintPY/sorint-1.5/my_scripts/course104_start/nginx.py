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


def install_nginx(password):
    """Install the nginx package."""
    print("[INFO] Installing nginx...")
    run_command("yum install -y epel-release", password)
    run_command("yum install -y nginx", password)


def configure_nginx_logging(password):
    """Configure nginx to log to syslog with elevated privileges."""
    print("[INFO] Configuring nginx logging...")
    config_lines = [
        "error_log  syslog:server=unix:/var/log/nginx.sock debug;",
        "access_log syslog:server=[2001:db8::1]:1234,facility=local7,tag=nginx,severity=debug;"
    ]
    config_file = "/etc/nginx/nginx.conf"

    try:
        # Create a command to append configuration lines to the nginx config file
        command = f"echo '{chr(10).join(config_lines)}' | sudo tee -a {config_file}"
        run_command(command, password)
        print(f"[INFO] Successfully configured logging in {config_file}.")
    except Exception as e:
        print(f"[ERROR] Failed to configure nginx logging: {e}")


def misconfigure_nginx(password):
    """Add an invalid directive to nginx configuration with elevated privileges."""
    print("[INFO] Misconfiguring nginx...")
    error_line = "invalid_directive;"
    config_file = "/etc/nginx/nginx.conf"

    try:
        # Create a command to append the invalid directive to the nginx config file
        command = f"echo '{error_line}' | sudo tee -a {config_file}"
        run_command(command, password)
        print(f"[INFO] Successfully added invalid directive to {config_file}.")
    except Exception as e:
        print(f"[ERROR] Failed to misconfigure nginx: {e}")


def start_nginx(password):
    """Start or restart the nginx service."""
    print("[INFO] Starting nginx...")
    run_command("systemctl daemon-reload", password)
    run_command("systemctl restart nginx", password)
    print("[INFO] Nginx started successfully.")


def main():
    print("[INFO] Starting the nginx setup process...")
    install_nginx(SUDO_PASSWORD)
    configure_nginx_logging(SUDO_PASSWORD)
    misconfigure_nginx(SUDO_PASSWORD)
    start_nginx(SUDO_PASSWORD)
    print("[INFO] Nginx setup completed.")


if __name__ == "__main__":
    main()