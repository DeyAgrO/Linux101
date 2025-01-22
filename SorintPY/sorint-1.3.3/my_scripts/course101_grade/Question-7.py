import os
import grp

def grade():
    missing_groups = []
    try:
        grp.getgrnam("devops")
    except KeyError:
        missing_groups.append("devops")
    try:
        grp.getgrnam("testers")
    except KeyError:
        missing_groups.append("testers")

    if missing_groups:
        print(f"\033[91mError: The following groups do not exist: {', '.join(missing_groups)}.\033[0m")
    else:
        print("\033[92mThe 'devops' and 'admin' groups already exist.\033[0m")

if __name__ == "__main__":
    grade()