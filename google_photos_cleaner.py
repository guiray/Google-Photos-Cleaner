import os

def process_google_photos(folder):
    json_count = 0
    mp_count = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)

            # Delete JSON files
            if file.lower().endswith('.json'):
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    json_count += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

            # Rename .MP files to .mp4
            elif file.lower().endswith('.mp'):
                new_file_path = os.path.splitext(file_path)[0] + '.mp4'
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_path} -> {new_file_path}")
                    mp_count += 1
                except Exception as e:
                    print(f"Error renaming {file_path}: {e}")


    print(f"\nTotal JSON files deleted: {json_count}")
    print(f"Total .MP files renamed to .mp4: {mp_count}")

if __name__ == "__main__":
    folder_path = input("Enter the full path to your 'Google Photos' folder: ").strip('"')
    if os.path.isdir(folder_path):
        process_google_photos(folder_path)
    else:

        print("Invalid folder path. Please check and try again.")
