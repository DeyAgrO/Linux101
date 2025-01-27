import subprocess
from config import SUDO_PASSWORD # ID=10492
import Modules.my_defs

def main():
    rpm_pkg = "httpd"  # Package name
    config_file = "/etc/httpd/conf/httpd.conf"  # Configuration file for the example
    error_line = "invalid_directive;"  # Example misconfiguration
    password = SUDO_PASSWORD  # Sudo password

    try:
        # Install the package
        Modules.my_defs.install_pkg(rpm_pkg, password)

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