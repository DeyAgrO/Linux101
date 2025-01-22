import os
import subprocess

def can_su_to_user(username, password):
    try:
        # Try to switch to the specified user using the password, suppressing output
        result = subprocess.run(
            ['su', '-c', 'true', username],  # Use 'true' to minimize visible output
            input=password.encode(),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError:
        # If the su command fails, return False
        return False

def grade():
    missing_users = []
    cannot_su_to = []

    try:
        # Check if we can su to developer1 with the 'sorint' password
        if not can_su_to_user("developer1", "sorint"):
            cannot_su_to.append("developer1")
    except KeyError:
        missing_users.append("developer1")

    try:
        # Check if we can su to tester1 with the 'sorint' password
        if not can_su_to_user("tester1", "sorint"):
            cannot_su_to.append("tester1")
    except KeyError:
        missing_users.append("tester1")

    if missing_users:
        for user in missing_users:
            print(f"\033[91mError: The user '{user}' does not exist.\033[0m")

    if cannot_su_to:
        for user in cannot_su_to:
            print(f"\033[91mError: The user '{user}' does not have 'sorint' as a password.\033[0m")

    if not missing_users and not cannot_su_to:
        print("\033[92mBoth 'developer1' and 'tester1' users exist, and their password is 'sorint'.\033[0m")

if __name__ == "__main__":
    grade()