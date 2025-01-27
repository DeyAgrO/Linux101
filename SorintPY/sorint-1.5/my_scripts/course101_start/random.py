import os

def print_colored(text, color_code):
    """Print text in the specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

def create_files_in_directory(directory):
    """Create random files in the specified directory."""
    try:
        # Generate 10 .mp3 files
        for i in range(10):
            file_name = f"random_{i}.mp3"
            file_path = os.path.join(directory, file_name)
            with open(file_path, "w") as file:
                file.write("This is a random .mp3 file.")

        # Generate 6 .mp4 files
        for i in range(6):
            file_name = f"random_{i}.mp4"
            file_path = os.path.join(directory, file_name)
            with open(file_path, "w") as file:
                file.write("This is a random .mp4 file.")

        # Generate 8 .jpg files
        for i in range(8):
            file_name = f"random_{i}.jpg"
            file_path = os.path.join(directory, file_name)
            with open(file_path, "w") as file:
                file.write("This is a random .jpg file.")

        # Generate 5 .wav files
        for i in range(5):
            file_name = f"random_{i}.wav"
            file_path = os.path.join(directory, file_name)
            with open(file_path, "w") as file:
                file.write("This is a random .wav file.")
        
        print_colored(f"Files have been created in the directory: {directory}", '32')

    except Exception as e:
        print_colored(f"An error occurred while creating files: {str(e)}", '31')

def main():
    try:
        # Get the current user's home directory
        user = os.getenv('USER')
        random_dir = f"/home/{user}/random"

        # Check if the 'random' directory exists
        if os.path.exists(random_dir):
            print_colored(f"The '{random_dir}' directory already exists.", '33')
        else:
            # Create the 'random' directory
            os.makedirs(random_dir)
            
            # Create files in the 'random' directory
            create_files_in_directory(random_dir)

    except Exception as e:
        print_colored(f"An error occurred: {str(e)}", '31')

if __name__ == "__main__":
    main()