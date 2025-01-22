import os
import re

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def check_command_usage(commands):
    history_file = os.path.expanduser('~/.bash_history')
    used_commands = {cmd: False for cmd in commands}

    try:
        with open(history_file, 'r') as file:
            history_lines = file.readlines()

        for line in history_lines:
            for cmd in commands:
                # Use regex to find the command as a whole word
                if re.search(r'\b' + re.escape(cmd) + r'\b', line):
                    used_commands[cmd] = True

        all_used = True
        for cmd, used in used_commands.items():
            if used:
                print_colored(f"Good Work on using the {cmd} command.", "32")  # Green
            else:
                print_colored(f"You didn't use the {cmd} command.", "31")  # Red
                all_used = False

        if all_used:
            print_colored("All necessary commands to control processes are used. Thank you for paying attention.", "32")  # Green
    except FileNotFoundError:
        print_colored(f"History file {history_file} not found.", "31")  # Red

def grade():
    commands_to_check = ['grep']
    check_command_usage(commands_to_check)

if __name__ == "__main__":
    grade()