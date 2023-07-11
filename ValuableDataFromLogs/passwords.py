import os
import shutil
import sys

def copy_files(input_path, output_path):
    try:
        # create a generator for all subdirectories
        folder_gen = os.walk(input_path)
        folders = next(folder_gen)[1]

        print(f"Found {len(folders)} folders. Do you want to proceed? (y/n)")

        proceed = input()
        if proceed.lower() != 'y':
            print("Aborted by user")
            return

        for folder in sorted(folders):
            for dirpath, dirnames, filenames in os.walk(os.path.join(input_path, folder)):
                if "Passwords.txt" in filenames:
                    source_file = os.path.join(dirpath, "Passwords.txt")
                    # Take first 10 characters from the folder name
                    new_filename = folder[:10] + "_Passwords.txt"
                    destination_file = os.path.join(output_path, new_filename)
                    shutil.copy2(source_file, destination_file)
                    print(f"'Passwords.txt' has been copied from '{folder}' as '{new_filename}'")
                    break  # if file is found, skip remaining directories

    except KeyboardInterrupt:
        print("\nScript terminated by user")
        return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide the input and output paths")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isdir(input_path) or not os.path.isdir(output_path):
        print("Both input and output paths should be directories")
        sys.exit(1)

    copy_files(input_path, output_path)
