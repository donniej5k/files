import re

def extract_emails_from_file(filename):
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read the entire content of the file
            file_content = file.read()

            # Regular expression pattern for matching email addresses
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            # Find all email addresses using re.findall()
            emails = re.findall(pattern, file_content)

            return emails

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
filename = input("Enter the path to the text file: ")

# Extract email addresses from the file
found_emails = extract_emails_from_file(filename)

# Print the extracted email addresses
if found_emails:
    print("Extracted email addresses:")
    for email in found_emails:
        print(email)
else:
    print("No email addresses found or file could not be processed.")
