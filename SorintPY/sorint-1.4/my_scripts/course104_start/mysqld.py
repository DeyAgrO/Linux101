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

def install_mysql(password):
    run_command("yum install -y mysql-server", password)

def configure_mysql_logging():
    config_lines = [
        "[mysqld]",
        "log-error=/var/log/mysql/mysqld.log"
    ]
    config_file = "/etc/my.cnf"
    try:
        with open(config_file, "a") as file:
            file.write("\n".join(config_lines) + "\n")
    except IOError as e:
        print(f"Error writing to {config_file}: {e}")

def misconfigure_mysql():
    error_line = "invalid_option"
    config_file = "/etc/my.cnf"
    try:
        with open(config_file, "a") as file:
            file.write(f"\n{error_line}\n")
    except IOError as e:
        print(f"Error writing to {config_file}: {e}")

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
    configure_mysql_logging()
    misconfigure_mysql()
    start_mysql(sudo_password)

if __name__ == "__main__":
    main()