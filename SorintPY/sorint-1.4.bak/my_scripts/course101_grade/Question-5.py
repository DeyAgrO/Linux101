import os

def grade():
    user = os.getenv('USER')
    errors = []

    # Check for 10 .mp3 files in /home/$USER/exam/mp3 and not in /home/$USER/random
    mp3_dir = f"/home/{user}/exam/mp3"
    mp3_count = 0
    random_dir = f"/home/{user}/random"
    if not os.path.exists(mp3_dir) or not all(f.endswith(".mp3") for f in os.listdir(mp3_dir)):
        errors.append("\033[91mYou didn't move the mp3 files to the right place.\033[0m")
    else:
        mp3_count = len(os.listdir(mp3_dir))
        if mp3_count != 10:
            errors.append("\033[91mYou didn't move the mp3 files to the right place.\033[0m")
        if os.path.exists(random_dir) and any(f.endswith(".mp3") for f in os.listdir(random_dir)):
            errors.append("\033[91mYou didn't remove the mp3 files from the random directory.\033[0m")

    # Check for 6 .mp4 files in /home/$USER/exam/mp4 and not in /home/$USER/random
    mp4_dir = f"/home/{user}/exam/mp4"
    mp4_count = 0
    if not os.path.exists(mp4_dir) or not all(f.endswith(".mp4") for f in os.listdir(mp4_dir)):
        errors.append("\033[91mYou didn't move the mp4 files to the right place.\033[0m")
    else:
        mp4_count = len(os.listdir(mp4_dir))
        if mp4_count != 6:
            errors.append("\033[91mYou didn't move the mp4 files to the right place.\033[0m")
        if os.path.exists(random_dir) and any(f.endswith(".mp4") for f in os.listdir(random_dir)):
            errors.append("\033[91mYou didn't remove the mp4 files from the random directory.\033[0m")

    # Check for no .wav files in /home/$USER/random
    if os.path.exists(random_dir) and any(f.endswith(".wav") for f in os.listdir(random_dir)):
        errors.append("\033[91mYou didn't remove the .wav files.\033[0m")

    if not errors:
        print("\033[92mAll 'MP3, MP4, WAV' files are in the right place!\033[0m")
        return True
    else:
        for error in errors:
            print(error)
        return False

if __name__ == "__main__":
    if grade():
        print("\033[92mAll files are in the right place!\033[0m")
    else:
        print("\033[91mSome files are not in the right place.\033[0m")