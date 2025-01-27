def install_package(rpm_pkg, password):
    print("Installing {rpm_pkg}")
    run_command("yum install -y {rpm_pkg}", password)


def run_command(command, password):
    """Run a system command with elevated privileges."""
    # Use 'echo' to pass the password to 'sudo' (this is just an example; be cautious with plaintext passwords)
    complete_command = f"echo {password} | sudo -S {command}"
    process = subprocess.Popen(complete_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        print(f"Error: {stderr.decode().strip()}")
    else:
        print(stdout.decode().strip())

def run_command(command, password):
    """Run a shell command with sudo and password."""
    full_command = f"echo {password} | sudo -S {command}"
    try:
        result = subprocess.run(
            full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr}")