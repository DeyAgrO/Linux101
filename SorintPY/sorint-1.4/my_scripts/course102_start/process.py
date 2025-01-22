import subprocess
import psutil

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def count_sleep_processes():
    """Count the number of running 'sleep' processes."""
    count = 0
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'sleep':
            count += 1
    return count

def start_sleep_processes(count, duration):
    """Start the specified number of 'sleep' processes."""
    try:
        for _ in range(count):
            subprocess.Popen(['sleep', str(duration)])
        return True
    except Exception as e:
        print_colored(f"An error occurred while starting sleep processes: {str(e)}", '31')
        return False

def main():
    try:
        # Number of sleep processes to start
        process_count = 3
        # Duration in seconds (24 hours)
        sleep_duration = 24 * 60 * 60

        # Check the number of existing 'sleep' processes
        existing_processes = count_sleep_processes()
        
        if existing_processes >= 2:
            print_colored(f"There are already {existing_processes} 'sleep' processes running.", '33')
        else:
            if start_sleep_processes(process_count, sleep_duration):
                print_colored(f"Started {process_count} 'sleep' processes each for {sleep_duration} seconds.", '32')

    except Exception as e:
        print_colored(f"An error occurred: {str(e)}", '31')

if __name__ == "__main__":
    main()