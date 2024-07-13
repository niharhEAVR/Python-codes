import os

def print_directory_contents(directory):
    try:
        # List all files and directories in the given directory
        contents = os.listdir(directory)
        
        # Print each item in the directory
        for item in contents:
            print(item)
            
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'.")

# Example usage:
directory_path = 'D:/'  # Replace with the directory path you want to list

print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)
