import subprocess
from config import SUDO_PASSWORD # ID=10492
import Modules.my_defs



def create_log_directory(password):
    """Create and set permissions for the MySQL log directory."""
    Modules.my_defs.run_command("mkdir -p /var/log/mysql", password)
    Modules.my_defs.run_command("chown mysql:mysql /var/log/mysql", password)
    Modules.my_defs.run_command("chmod 755 /var/log/mysql", password)

import subprocess
from config import SUDO_PASSWORD # ID=10492
import Modules.my_defs

def main():
    rpm_pkg = "mysql"  # Package name
    error_line = "invalid_option"
    password = SUDO_PASSWORD  # Sudo password
    config_lines = [
        "[mysqld]",
        "log-error=/var/log/mysql/mysqld.log"
    ]
    config_file = "/etc/my.cnf"  # Configuration file for the example

    try:
        # Install the package
        Modules.my_defs.install_pkg(rpm_pkg, password)

        # Create MySQL Directory
        create_log_directory(SUDO_PASSWORD)

        # Misconfigure the package
        Modules.my_defs.misconfigure_pkg(rpm_pkg, config_file, error_line, password)
        
        # Configure Logging Options
        Modules.my_defs.configure_pkg_logging(config_lines, config_file, rpm_pkg, password)

        # Start the service
        Modules.my_defs.daemon_reload(password)

        # If all steps succeed
        print(f"\033[92m'{rpm_pkg}' Ready For Troubleshooting.\033[0m")
    except Exception as e:
        # If any step fails
        print(f"\033[91m[ERROR] The script for {rpm_pkg} did not end successfully: {e}\033[0m")

if __name__ == "__main__":
    main()