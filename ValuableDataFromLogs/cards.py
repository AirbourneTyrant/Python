import os
import shutil
import sys

def get_user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nUser requested to quit.")
        sys.exit(0)

def main():
    src_path = get_user_input("Enter the source path: ")
    dest_path = get_user_input("Enter the destination path: ")

    if not os.path.isdir(src_path):
        print(f"Source path {src_path} does not exist or is not a directory.")
        return

    if not os.path.isdir(dest_path):
        print(f"Destination path {dest_path} does not exist or is not a directory.")
        return

    subfolders = [f.name for f in os.scandir(src_path) if f.is_dir()]
    subfolders.sort()

    print(f"Number of folders: {len(subfolders)}")
    proceed = get_user_input("Do you want to proceed? (y/n): ")

    if proceed.lower() != 'y':
        print("User requested to quit.")
        return

    for folder in subfolders:
        check_folder = os.path.join(src_path, folder, 'CreditCards')

        if os.path.isdir(check_folder):
            new_folder_name = f"{folder[:10]}_CreditCards"
            new_folder_path = os.path.join(dest_path, new_folder_name)

            try:
                shutil.copytree(check_folder, new_folder_path)
                print(f'"{folder}" copied.')
            except Exception as e:
                print(f"Error while copying {folder}: {str(e)}")

if __name__ == "__main__":
    main()