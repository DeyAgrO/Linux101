import subprocess

# Check if there is sleep process running in the background

def get_sleep_process_count():
    try:
        # Run the `ps` command to get all processes, and grep for `sleep`
        result = subprocess.run(['ps', 'aux'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()

        # Count the number of 'sleep' processes, excluding the grep process itself
        sleep_count = sum(1 for line in output.splitlines() if 'sleep' in line and 'grep' not in line)
        
        return sleep_count
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return 0

def grade():
    sleep_count = get_sleep_process_count()

    if sleep_count <= 1:
        print("\033[92msleep processes are Terminated.\033[0m")
    else:
        print("\033[91m2 or more sleep processes are running in the background. use the \033[92mkill\033[0m \033[91mcommand\033[0m")

if __name__ == "__main__":
    grade()
