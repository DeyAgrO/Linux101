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

def install_mysql(password):
    run_command("yum install -y mysql-server", password)

def configure_mysql_logging(password):
    config_lines = [
        "[mysqld]",
        "log-error=/var/log/mysql/mysqld.log"
    ]
    config_file = "/etc/my.cnf"
    config_content = "\n".join(config_lines)
    command = f"echo '{config_content}' | sudo tee -a {config_file}"
    run_command(command, password)

def misconfigure_mysql(password):
    error_line = "invalid_option"
    config_file = "/etc/my.cnf"
    command = f"echo '{error_line}' | sudo tee -a {config_file}"
    run_command(command, password)

def create_log_directory(password):
    run_command("mkdir -p /var/log/mysql", password)
    run_command("chown mysql:mysql /var/log/mysql", password)
    run_command("chmod 755 /var/log/mysql", password)

def start_mysql(password):
    run_command("systemctl daemon-reload", password)
    run_command("systemctl restart mysqld", password)

def main():
    sudo_password = "sorint"
    install_mysql(sudo_password)
    create_log_directory(sudo_password)
    configure_mysql_logging(sudo_password)
    misconfigure_mysql(sudo_password)
    start_mysql(sudo_password)

if __name__ == "__main__":
    main()
