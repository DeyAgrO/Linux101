import os
import random
import string

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

# Function to create a random filename with 'sorint' in the middle
def random_filename_with_sorint(length, extension):
    letters = string.ascii_lowercase
    part1 = ''.join(random.choice(letters) for _ in range(length // 2))
    part2 = ''.join(random.choice(letters) for _ in range(length // 2))
    return f"{part1}sorint{part2}.{extension}"

# Function to create a random filename
def random_filename(length, extension):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length)) + '.' + extension

# Function to create files with specified extensions
def create_files(directory, num_files, extension):
    for _ in range(num_files):
        filename = random_filename(10, extension)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            f.write('')

# Function to create files containing 'sorint' in the name, excluding '.txt' extension
def create_sorint_files(directory, num_files, extensions):
    extensions = [ext for ext in extensions if ext != 'txt']
    for _ in range(num_files):
        random_extension = random.choice(extensions)
        filename = random_filename_with_sorint(7, random_extension)  # Adjusted length to fit 'sorint' in the middle
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            f.write('')

# Main script
def main():
    user = os.getenv('USER')
    base_directory = f'/home/{user}/random-d3'
    
    # Check if the base directory exists
    if os.path.exists(base_directory):
        print_colored(f"The directory {base_directory} already exists. No files will be created.", "33")  # Yellow
        return  # Exit the function without creating any files
    
    # Create the base directory
    os.makedirs(base_directory)
    print_colored(f"Created the directory {base_directory}.", "32")  # Green
    
    # Create files with specified extensions
    create_files(base_directory, 16, 'txt')
    create_files(base_directory, 20, 'mp4')
    create_files(base_directory, 19, 'mp3')
    create_files(base_directory, 22, 'wav')
    create_files(base_directory, 27, 'jpeg')
    
    # Random extensions for additional files
    random_extensions = ['doc', 'xls', 'ppt', 'gif', 'png', 'bmp', 'zip', 'tar', 'iso', 'bin']
    for _ in range(25):
        random_extension = random.choice(random_extensions)
        create_files(base_directory, 1, random_extension)
    
    # Create files with 'sorint' in the name and random extensions excluding 'txt'
    all_extensions = ['mp4', 'mp3', 'wav', 'jpeg'] + random_extensions
    create_sorint_files(base_directory, 9, all_extensions)

if __name__ == "__main__":
    main()