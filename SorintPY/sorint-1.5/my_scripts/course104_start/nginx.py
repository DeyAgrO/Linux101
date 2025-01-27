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
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr}")

def install_nginx(password):
    run_command("yum install -y epel-release", password)
    run_command("yum install -y nginx", password)

def configure_nginx_logging():
    config_lines = [
        "error_log /var/log/nginx/error.log;"
    ]
    config_file = "/etc/nginx/nginx.conf"
    try:
        with open(config_file, "a") as file:
            file.write("\n".join(config_lines) + "\n")
    except IOError as e:
        print(f"Error writing to {config_file}: {e}")

def misconfigure_nginx():
    # Adding an invalid configuration directive
    error_line = "invalid_directive;"
    config_file = "/etc/nginx/nginx.conf"
    try:
        with open(config_file, "a") as file:
            file.write(f"\n{error_line}\n")
    except IOError as e:
        print(f"Error writing to {config_file}: {e}")

def start_nginx(password):
    run_command("systemctl daemon-reload", password)
    run_command("systemctl restart nginx", password)

def main():
    sudo_password = "sorint"
    install_nginx(sudo_password)
    configure_nginx_logging()
    misconfigure_nginx()
    start_nginx(sudo_password)

if __name__ == "__main__":
    main()