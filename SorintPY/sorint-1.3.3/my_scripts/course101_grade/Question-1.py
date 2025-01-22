import os

def grade():
    """
    Checks if the following directories exist:
    /home/$USER/exam/txt
    /home/$USER/exam/mp4
    /home/$USER/exam/mp3
    """
    user = os.getenv('USER')
    txt_dir = f"/home/{user}/exam/txt"
    mp4_dir = f"/home/{user}/exam/mp4"
    mp3_dir = f"/home/{user}/exam/mp3"

    txt_exists = os.path.isdir(txt_dir)
    mp4_exists = os.path.isdir(mp4_dir)
    mp3_exists = os.path.isdir(mp3_dir)

    if txt_exists:
        print(f"\033[92mThe directory '{txt_dir}' exists.\033[0m")
    else:
        print(f"\033[91mThe directory '{txt_dir}' does not exist.\033[0m")

    if mp4_exists:
        print(f"\033[92mThe directory '{mp4_dir}' exists.\033[0m")
    else:
        print(f"\033[91mThe directory '{mp4_dir}' does not exist.\033[0m")

    if mp3_exists:
        print(f"\033[92mThe directory '{mp3_dir}' exists.\033[0m")
    else:
        print(f"\033[91mThe directory '{mp3_dir}' does not exist.\033[0m")

    return txt_exists and mp4_exists and mp3_exists

if __name__ == "__main__":
    grade()