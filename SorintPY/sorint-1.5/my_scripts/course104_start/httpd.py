import subprocess

def run_command(command, password):
    """Run a shell command with sudo and password."""
    full_command = f"echo {password} | sudo -S {command}"
    try:
        result = subprocess.run(full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr}")

def install_httpd(password):
    run_command("yum install -y httpd", password)

def configure_httpd():
    error_line = "ErrorDirective InvalidDirective"
    config_file = "/etc/httpd/conf/httpd.conf"
    try:
        with open(config_file, "a") as file:
            file.write(f"\n{error_line}\n")
    except IOError as e:
        print(f"Error writing to {config_file}: {e}")

def start_httpd(password):
    run_command("systemctl start httpd", password)

def main():
    sudo_password = "sorint"
    install_httpd(sudo_password)
    configure_httpd()
    start_httpd(sudo_password)

if __name__ == "__main__":
    main()
