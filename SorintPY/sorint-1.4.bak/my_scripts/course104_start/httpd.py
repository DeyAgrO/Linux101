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

def install_httpd(password):
    run_command("yum install -y httpd", password)

def configure_httpd(password):
    error_line = "ErrorDirective InvalidDirective"
    config_file = "/etc/httpd/conf/httpd.conf"
    command = f"echo '{error_line}' | sudo tee -a {config_file}"
    run_command(command, password)

def start_httpd(password):
    run_command("systemctl start httpd", password)

def main():
    sudo_password = "sorint"
    install_httpd(sudo_password)
    configure_httpd(sudo_password)
    start_httpd(sudo_password)

if __name__ == "__main__":
    main()
