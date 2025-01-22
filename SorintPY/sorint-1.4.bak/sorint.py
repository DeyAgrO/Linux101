#!/usr/bin/env python3

import sys
import os
import subprocess

# Determine the script directory
script_dir = os.path.dirname(os.path.realpath(__file__))
scripts_path = os.path.join('/usr/lib/sorint', 'my_scripts')

def print_help():
    help_text = """
usage: sorint [ option <course number>  --help ] [--course-help [CourseNumber]]

Sorint the specified course.

options:
    start <courseXXX>               Start the specified course
    grade <courseXXX>          Grade the course and check if you passed

  --help                Show this help message and exit.

  --course-help    [course number]
                        Show detailed help for the specified course.

course numbers:
    course101           Course of DAY 1: Basics of Linux Commands and User Management
    course102           Course of DAY 2: Usage of Processes, Log Monitoring, and SSH
    course103           Course of DAY 3: Networking, File Systems, and Packages

Examples:

    sorint start course101          => to start Linux day 1
    
    sorint grade course103          => to check if you passed the Lab Exercise
    
    sorint --course-help course101  => to see extra help for each course

Author:
    Ibraheem IBRAHEEM & GPT 4 thank you Enjoy the training :)
"""
    print(help_text.strip())

def print_course_help(course):
    """
    Print detailed help information for the specified course.
    """
    course_help = {
        "course101": """
course101 details:
tail    = Print out the last 10 lines of a file
          use [-n 5] to print the last 5 lines
head    = Print out the first 10 lines of a file
          use [-n 5] to print the first 5 lines
echo    = Print out a value of environment variables or write into a file
          example: echo $HOSTNAME
mkdir   = Create a new directory
          example: mkdir new_directory
touch   = Create an empty file or update the timestamp of an existing file
          example: touch new_file.txt
vim     = Open the vim text editor
          example: vim file.txt
cp      = Copy files or directories
          example: cp source.txt destination.txt
mv      = Move or rename files or directories
          example: mv old_name.txt new_name.txt
rm      = Remove files or directories
          example: rm file.txt or rm -r /directory
cat     = Concatenate and display files
          example: cat file.txt
ln -s   = Create a symbolic link to a file or directory
          example: ln -s target link_name
useradd = Add a new user
          example: sudo useradd newuser
groupadd = Add a new group
          example: sudo groupadd newgroup
usermod = Modify a user's account
          example: sudo usermod -aG groupname username
passwd  = Change a user's password
chmod   = Change file permissions
          example: chmod 755 file.txt
chown   = Change file owner and group
          example: sudo chown user:group file.txt
alias   = Create an alias for a command
          example: alias ll='ls -la'
variable=something = Set an environment variable
          example: export PATH=/usr/local/bin:$PATH
*       = Wildcard to represent multiple files
          example: rm *.txt
less    = View file contents one screen at a time
          example: less file.txt
/       = Search within a file when using `less`
          example: /search_term
""",
        "course102": """
course102 details:
ssh-keygen = Generate a new SSH key pair
          example 1: ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
          example 2: ssh-keygen -t ed25519 -C "your_email@example.com"
          To generate a custom SSH key with a specific file name:
          example: ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f ~/.ssh/custom_rsa_key
ssh-copy-id = Copy your SSH key to a remote server
          example 1: ssh-copy-id user@remote_host
          example 2: ssh-copy-id -i ~/.ssh/custom_rsa_key.pub user@remote_host
ssh       = Connect to a remote server via SSH
          example 1: ssh user@remote_host
          example 2: ssh -p 2222 user@remote_host
kill      = Terminate a process by its ID
          example 1: kill 1234
          example 2: kill -9 1234
ps        = Display information about active processes
          example 1: ps aux
          example 2: ps -ef
ps eux    = Display detailed information about processes
          example 1: ps eux | grep 'nginx'
          example 2: ps eux --forest
grep      = Search for patterns in text
          example 1: grep 'search_term' file.txt
          example 2: ps aux | grep 'nginx'
          example 3: systemctl list-units | grep 'nginx'
          example 4: journalctl -u nginx | grep 'error'
systemctl = Control the systemd system and service manager
          example 1: sudo systemctl restart nginx
          example 2: sudo systemctl status nginx
          example 3: sudo systemctl list-units | grep 'nginx'
journalctl = View logs collected by the systemd journal
          example 1: sudo journalctl -u nginx
          example 2: sudo journalctl --since '2023-06-01' --until '2023-06-30'
          example 3: sudo journalctl -u nginx | grep 'error'
""",
        "course103": """
course103 details:
hostnamectl = Control the system hostname
          example 1: hostnamectl set-hostname new-hostname
          example 2: hostnamectl status
          example 3: hostnamectl set-icon-name computer-laptop
nmcli = Command-line tool for controlling NetworkManager
          example 1: nmcli device status
          example 2: nmcli connection up id 'WiFi-Connection'
          example 3: nmcli device wifi list
nmtui = Text user interface for NetworkManager
          example 1: nmtui (opens interactive interface)
          example 2: nmtui edit 'Connection Name'
          example 3: nmtui connect 'Connection Name'
dnf = Package manager for RPM-based distributions
          example 1: sudo dnf install package_name
          example 2: sudo dnf update
          example 3: sudo dnf remove package_name
firewall-cmd = Command-line interface for firewalld
          example 1: sudo firewall-cmd --add-service=http --permanent
          example 2: sudo firewall-cmd --reload
          example 3: sudo firewall-cmd --list-all
<name>.repo = Repository configuration file for YUM/DNF
          example 1: sudo vi /etc/yum.repos.d/your-repo-name.repo (to create/edit a repo file)
          example 2: sudo dnf repolist
          example 3: sudo dnf config-manager --add-repo http://example.com/path/to/repo
lsblk = List information about block devices
          example 1: lsblk
          example 2: lsblk -f
          example 3: lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT
mount = Mount a filesystem
          example 1: sudo mount /dev/sda1 /mnt
          example 2: mount | grep '^/dev'
          example 3: sudo umount /mnt (to unmount)
find = Search for files in a directory hierarchy
          example 1: find /home -name '*.txt'
          example 2: find /var -type d -name 'log'
          example 3: find / -perm 644
sudoers.d = Directory for sudoers configuration files
          example 1: sudo visudo -f /etc/sudoers.d/username (to edit sudoers file for a user)
          example 2: %group ALL=(ALL) NOPASSWD: ALL (type of group configs)
          example 3: sudo cat /etc/sudoers.d/username (to view contents of a sudoers file)
"""
    }

    if course in course_help:
        print(course_help[course].strip())
    else:
        print(f"No detailed help available for course: {course}")

def main():
    if len(sys.argv) < 2:
        print("Usage: sorint <command> <course>")
        sys.exit(1)

    if sys.argv[1] == "--help":
        print_help()
        sys.exit(0)
    elif sys.argv[1] == "--course-help":
        if len(sys.argv) < 3:
            print("Usage: sorint --course-help <course>")
            sys.exit(1)
        print_course_help(sys.argv[2])
        sys.exit(0)
    elif len(sys.argv) < 3:
        print("Usage: sorint <command> <course>")
        sys.exit(1)

    command = sys.argv[1]
    course = sys.argv[2]

    if command == "start":
        subprocess.run(["python3", os.path.join(scripts_path, "start.py"), course])
    elif command == "grade":
        subprocess.run(["python3", os.path.join(scripts_path, "grade.py"), course])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()