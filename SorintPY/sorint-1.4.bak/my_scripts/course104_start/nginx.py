import subprocess

def run_command(command, password=None):
    """Run a shell command with optional sudo password."""
    if password:
        full_command = f"echo {password} | sudo -S {command}"
    else:
        full_command = command
    try:
        result = subprocess.run(full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError:
        # Extract the service name if the command is a systemctl command
        if 'systemctl' in command:
            service_name = command.split()[2]
            print(f"Error running {service_name}.service")
        else:
            print(f"Error running command: {command}")

def install_nginx(password):
    run_command("yum install -y epel-release", password)
    run_command("yum install -y nginx", password)

def configure_nginx_logging(password):
    config_lines = [
        "error_log /var/log/nginx/error.log;"
    ]
    config_file = "/etc/nginx/nginx.conf"
    config_content = "\n".join(config_lines)
    command = f"echo '{config_content}' | sudo tee -a {config_file}"
    run_command(command, password)

def misconfigure_nginx(password):
    # Adding an invalid configuration directive
    error_line = "invalid_directive;"
    config_file = "/etc/nginx/nginx.conf"
    command = f"echo '{error_line}' | sudo tee -a {config_file}"
    run_command(command, password)

def start_nginx(password):
    run_command("systemctl daemon-reload", password)
    run_command("systemctl restart nginx", password)

def main():
    sudo_password = "sorint"
    install_nginx(sudo_password)
    configure_nginx_logging(sudo_password)
    misconfigure_nginx(sudo_password)
    start_nginx(sudo_password)

if __name__ == "__main__":
    main()
