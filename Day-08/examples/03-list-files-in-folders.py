import os

def list_files_in_folder(folder_path):
    """
    Attempts to list files in a folder.
    Returns a tuple: (list_of_files, error_message)
    """
    try:
        # os.listdir() gives us a list of everything in the folder
        files = os.listdir(folder_path)
        return files, None  # Success! No error message.
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    # input().split() takes a long string "folder1 folder2" and cuts it into a list ["folder1", "folder2"]
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    # Loop through each folder in our list
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        
        if files:
            print(f"Files in {folder_path}:")
            # Loop through the files in this specific folder
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()

