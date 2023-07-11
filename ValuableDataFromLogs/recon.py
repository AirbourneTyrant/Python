import os
import shutil
import sys
import time

def read_keywords_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            keywords = file.read().split(',')
        return [keyword.lower().strip() for keyword in keywords]
    except FileNotFoundError:
        print("Keywords file not found.")
        sys.exit(1)

def search_and_move_files(input_path, keywords):
    try:
        file_list = sorted([f for f in os.listdir(input_path) if f.endswith('.txt')])
        print(f"Found {len(file_list)} text files. Do you want to proceed? (y/n)")

        proceed = input()
        if proceed.lower() != 'y':
            print("Aborted by user")
            return

        match_folder = os.path.join(input_path, 'match')
        if not os.path.exists(match_folder):
            os.mkdir(match_folder)

        for filename in file_list:
            with open(os.path.join(input_path, filename), 'r', encoding='utf-8') as file:
                if any(keyword in file.read().lower() for keyword in keywords):
                    file.close()  # explicitly close the file, even though 'with' statement should handle this
                    time.sleep(0.5)  # wait a half second
                    shutil.move(os.path.join(input_path, filename), match_folder)
                    print(f"'{filename}' moved to 'match' folder.")

    except KeyboardInterrupt:
        print("\nScript terminated by user")
        return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide the input path and keywords file path")
        sys.exit(1)

    input_path = sys.argv[1]
    keywords_file_path = sys.argv[2]

    if not os.path.isdir(input_path) or not os.path.isfile(keywords_file_path):
        print("The input path should be a directory and the keywords file path should be a file.")
        sys.exit(1)

    keywords = read_keywords_file(keywords_file_path)
    search_and_move_files(input_path, keywords)