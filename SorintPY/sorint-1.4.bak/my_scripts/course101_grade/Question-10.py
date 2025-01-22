import os
import pwd
import grp

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def check_directory_ownership(directory, expected_owner, expected_group):
    try:
        stat_info = os.stat(directory)
        owner = pwd.getpwuid(stat_info.st_uid).pw_name
        group = grp.getgrgid(stat_info.st_gid).gr_name

        if owner == expected_owner and group == expected_group:
            print_colored(f"The directory '{directory}' exists and belongs to user '{owner}' and group '{group}'.", "92")
            return True
        elif owner != expected_owner:
            print_colored(f"Error: The directory '{directory}' does not belong to user '{expected_owner}'.", "91")
            return False
        else:
            print_colored(f"Error: The directory '{directory}' does not belong to group '{expected_group}'.", "91")
            return False
    except FileNotFoundError:
        print_colored(f"Error: The directory '{directory}' does not exist.", "91")
        return False

def check_symlink_exists(source, target):
    try:
        if os.path.islink(target):
            actual_target = os.path.realpath(os.readlink(target))
            expected_target = os.path.realpath(source)
            if actual_target == expected_target:
                print_colored(f"The symbolic link '{target}' -> '{source}' exists.", "92")
                return True
            else:
                print_colored(f"Error: The symbolic link '{target}' exists but points to '{actual_target}' instead of '{expected_target}'.", "91")
                return False
        else:
            print_colored(f"Error: The symbolic link '{target}' does not exist.", "91")
            return False
    except FileNotFoundError:
        print_colored(f"Error: The directory '{target}' does not exist.", "91")
        return False

def grade():
    if check_directory_ownership("/partage", "tester1", "sorint"):
        check_symlink_exists("/partage", "/tmp/shared")

if __name__ == "__main__":
    grade()