import os

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def create_days_file(file_path):
    """Create the 'days.txt' file and write numbers and days of the week."""
    try:
        with open(file_path, "w") as file:
            # Write the numbers 1 to 30
            for i in range(1, 31):
                file.write(str(i) + "\n")

            # Write the days of the week
            days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            for day in days_of_the_week:
                file.write(day + "\n")

        print_colored(f"The 'days.txt' file has been created in the home directory: {file_path}", '32')
    except Exception as e:
        print_colored(f"An error occurred while creating the file: {str(e)}", '31')

def main():
    try:
        # Create the days.txt file in the home directory
        home_dir = os.path.expanduser("~")
        file_path = os.path.join(home_dir, "days.txt")

        if os.path.exists(file_path):
            print_colored(f"The 'days.txt' file already exists in the home directory: {file_path}", '33')
        else:
            # Create the 'days.txt' file
            create_days_file(file_path)

    except Exception as e:
        print_colored(f"An error occurred: {str(e)}", '31')

if __name__ == "__main__":
    main()