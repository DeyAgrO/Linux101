import os
import random
import string

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def generate_random_text_file(file_path):
    """Generate a file with random text and a specific token on the 78th line."""
    try:
        with open(file_path, "w") as file:
            for i in range(100):
                if i == 77:  # 78th line (zero-based indexing)
                    file.write("ansible-api-token=3092DJA9N9J2198DJ12PUD9AZ82JJE\n")
                else:
                    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(20, 50)))
                    file.write(random_text + "\n")
        print_colored(f"Random text file generated: {file_path}", '32')
    except Exception as e:
        print_colored(f"An error occurred while creating the file: {str(e)}", '31')

def main():
    try:
        # Get the current user's home directory
        user = os.getenv('USER')
        file_path = f"/home/{user}/code.txt"

        # Check if 'code.txt' exists
        if os.path.exists(file_path):
            print_colored(f"The file 'code.txt' already exists.", '33')
        else:
            # Generate the random text file
            generate_random_text_file(file_path)

    except Exception as e:
        print_colored(f"An error occurred: {str(e)}", '31')

if __name__ == "__main__":
    main()