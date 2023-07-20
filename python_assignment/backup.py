import os
import shutil
import argparse
import datetime

def get_unique_filename(destination_dir, filename):
    base_name, extension = os.path.splitext(filename)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_filename = f"{base_name}_{timestamp}{extension}"
    return os.path.join(destination_dir, unique_filename)

def backup_files(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        while os.path.exists(destination_file):
            filename = get_unique_filename(destination_dir, filename)
            destination_file = os.path.join(destination_dir, filename)

        try:
            shutil.copy(source_file, destination_file)
            print(f"Copied '{filename}' to '{destination_dir}'")
        except Exception as e:
            print(f"Error occurred while copying '{filename}': {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup files from a source directory to a destination directory.")
    parser.add_argument("source_dir", help="Path to the source directory.")
    parser.add_argument("destination_dir", help="Path to the destination directory.")
    args = parser.parse_args()

    backup_files(args.source_dir, args.destination_dir)
