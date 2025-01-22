import os

# Check the contents of the head.txt are the first 10 lines of days.txt and the content of tail.txt file are the last 7 lines of the days.txt

def grade():
    # Define the expected contents of the files
    expected_head_contents = "\n".join(str(i) for i in range(1, 11))
    expected_tail_contents = "\n".join(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    # Check the contents of the head.txt file
    head_file_path = os.path.join(os.path.expanduser("~"), "exam", "txt", "head.txt")
    if os.path.isfile(head_file_path):
        with open(head_file_path, "r") as head_file:
            actual_head_contents = head_file.read().strip()
        if actual_head_contents == expected_head_contents:
            print("\033[32mhead.txt file contains the expected contents (1 to 10 on each line).\033[0m")
        else:
            print("\033[31mhead.txt file does not contain the expected contents.\033[0m")
    else:
        print("\033[31mhead.txt file does not exist.\033[0m")

    # Check the contents of the tail.txt file
    tail_file_path = os.path.join(os.path.expanduser("~"), "exam", "txt", "tail.txt")
    if os.path.isfile(tail_file_path):
        with open(tail_file_path, "r") as tail_file:
            actual_tail_contents = tail_file.read().strip()
        if actual_tail_contents == expected_tail_contents:
            print("\033[32mtail.txt file contains the expected contents (Monday to Sunday on each line).\033[0m")
        else:
            print("\033[31mtail.txt file does not contain the expected contents.\033[0m")
    else:
        print("\033[31mtail.txt file does not exist.\033[0m")

if __name__ == "__main__":
    grade()