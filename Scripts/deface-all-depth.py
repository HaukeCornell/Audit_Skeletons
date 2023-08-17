import os
import subprocess
import concurrent.futures

deface_command = 'deface'

# Define your main directory here
main_directory = 'H:/Mocap_Audit_Data_Identifiable'

def anonymize_file(filepath):
    filename = os.path.basename(filepath)
    dirpath = os.path.dirname(filepath)

    # Check if the corresponding anonymized file exists
    anonymized_file_name = filename.rsplit('.', 1)[0] + '_anonymized.mp4'
    anonymized_file = os.path.join(dirpath, anonymized_file_name)
    if os.path.exists(anonymized_file) or "_anonymized.mp4" in filename:
        print(f"Skipping {filepath} as anonymized file exists or it is an anonymized file.")
        return

    subprocess.run([deface_command, filepath])

with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:  # Limit to 3 concurrent tasks
    tasks = []
    for dir_path, dirs, files in os.walk(main_directory):
        for filename in files:
            if (filename.startswith(('color', 'left', 'right')) and filename.endswith('.mp4')) and "_anonymized.mp4" not in filename:
                full_file_path = os.path.join(dir_path, filename)
                tasks.append(executor.submit(anonymize_file, full_file_path))

    for task in concurrent.futures.as_completed(tasks):
        task.result()

print("Anonymization completed.")
