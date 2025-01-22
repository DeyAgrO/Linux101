import subprocess

def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return e.stdout.strip(), e.stderr.strip()

def grade():
    # ANSI escape codes for colors
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    # Check if httpd is installed
    stdout, error = run_command("dnf list installed | grep httpd")
    if "httpd.x86_64" not in stdout:
        print(f"{RED}httpd is not installed{RESET}")
        return
    print(f"{GREEN}httpd is installed{RESET}")
    
    # Check if httpd is enabled
    stdout, error = run_command("systemctl is-enabled httpd")
    if error or stdout != "enabled":
        print(f"{RED}httpd is not enabled{RESET}")
    else:
        print(f"{GREEN}httpd is enabled{RESET}")
    
    # Check if httpd is running
    stdout, error = run_command("systemctl is-active httpd")
    if error or stdout != "active":
        print(f"{RED}httpd is not running{RESET}")
    else:
        print(f"{GREEN}httpd is running{RESET}")

if __name__ == "__main__":
    grade()