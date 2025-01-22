import os
import grp
import subprocess

def user_belongs_to_group(username, group_name):
    try:
        # Get the list of groups the user belongs to
        user_groups = [g.gr_name for g in grp.getgrall() if username in g.gr_mem]
        
        # Check if the user belongs to the specified group
        return group_name in user_groups
    except KeyError:
        # If the user or group doesn't exist, return False
        return False

def grade():
    tester1_in_testers = user_belongs_to_group("tester1", "testers")
    developer1_in_devops = user_belongs_to_group("developer1", "devops")

    if tester1_in_testers and developer1_in_devops:
        print("\033[92mBoth 'tester1' and 'developer1' users belong to their respective groups.\033[0m")
    else:
        if not tester1_in_testers:
            print("\033[91mError: The 'tester1' user does not belong to the 'testers' group.\033[0m")
        if not developer1_in_devops:
            print("\033[91mError: The 'developer1' user does not belong to the 'devops' group.\033[0m")

if __name__ == "__main__":
    grade()