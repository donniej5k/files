# Task 1: Directory Inspector
import os

def list_directory_contents(path):
    try:
        # Validate the directory path
        if not os.path.exists(path):
            print(f"Error: Path '{path}' does not exist.")
            return

        # List all files and subdirectories in the given path
        print(f"Contents of directory '{path}':")
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt user for directory path
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
print("Task 1 Complete")
# Task 2: File Size Reporter
import os

def report_file_sizes(directory):
    try:
        # Validate the directory path
        if not os.path.exists(directory):
            print(f"Error: Path '{directory}' does not exist.")
            return

        # Iterate through files in the directory and print their names and sizes
        print(f"File sizes in directory '{directory}':")
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                size = os.path.getsize(item_path)
                print(f"{item}: {size} bytes")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt user for directory path
directory_path = input("Enter the directory path: ")
report_file_sizes(directory_path)
print("Task 2 Complete")
# Task 3; File Extention Counter
import os
from collections import defaultdict

def count_file_extensions(directory):
    try:
        # Validate the directory path
        if not os.path.exists(directory):
            print(f"Error: Path '{directory}' does not exist.")
            return

        # Initialize a defaultdict to count file extensions
        extension_count = defaultdict(int)

        # Iterate through files in the directory and count extensions
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                _, extension = os.path.splitext(item)
                extension = extension.lower()  # Normalize extension to lower case
                extension_count[extension] += 1

        # Print the count of each file extension
        print(f"File extensions count in directory '{directory}':")
        for ext, count in extension_count.items():
            print(f"{ext}: {count}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt user for directory path
directory_path = input("Enter the directory path: ")
count_file_extensions(directory_path)
print("Task 3 complete")
