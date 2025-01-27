import subprocess
from config import SUDO_PASSWORD # ID=10492
import Modules.my_defs

def install_nginx(password):
    Modules.my_defs.run_command("yum install -y epel-release", password)
    Modules.my_defs.run_command("yum install -y nginx", password)


def main():
    rpm_pkg = "nginx"  # Package name
    error_line = "invalid_directive;"
    password = SUDO_PASSWORD  # Sudo password
    config_lines = [
        "error_log  syslog:server=unix:/var/log/nginx.sock debug;",
        "access_log syslog:server=[2001:db8::1]:1234,facility=local7,tag=nginx,severity=debug;"
    ]
    config_file = "/etc/nginx/nginx.conf"

    try:
        # Install the package
        install_nginx(password)

        # Misconfigure the package
        Modules.my_defs.misconfigure_pkg(rpm_pkg, config_file, error_line, password)

        # Start the service
        Modules.my_defs.daemon_reload(password)

        # If all steps succeed
        print(f"\033[92m'{rpm_pkg}' Ready For Troubleshooting.\033[0m")
    except Exception as e:
        # If any step fails
        print(f"\033[91m[ERROR] The script for {rpm_pkg} did not end successfully: {e}\033[0m")

if __name__ == "__main__":
    main()