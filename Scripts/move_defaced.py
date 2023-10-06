import os
import shutil

# Define the main directory where your files are located
main_directory = 'D:/Mocap_Audit_Data_Identifiable'

# Define the destination directory where you want to move the anonymized files
destination_directory = 'D:/Mocap_Audit_Data_Blurred'

# Iterate through all the files in the main directory and its subdirectories
for dir_path, dirs, files in os.walk(main_directory):
    for filename in files:
        # Check if the file ends with '_anonymized.mp4' or '_anonymized.mkv'
        if filename.endswith('_anonymized.mp4') or filename.endswith('_anonymized.mkv'):
            full_file_path = os.path.join(dir_path, filename)

            # Create the destination path by replacing the main directory with the destination directory
            dest_path = dir_path.replace(main_directory, destination_directory)
            os.makedirs(dest_path, exist_ok=True)

            dest_file_path = os.path.join(dest_path, filename)

            # Check if the file already exists at the destination
            if os.path.exists(dest_file_path):
                print(f"File {dest_file_path} already exists. Skipping.")
                continue

            # Move the file to the destination path or copy with shutil.copy()
            shutil.copy(full_file_path, dest_file_path)

print("Anonymized files moved successfully.")
