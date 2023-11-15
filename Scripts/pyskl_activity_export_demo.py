import os
import subprocess

input_dir = '/media/farlab/Seagate Portable Drive/dev/Audit_Skeletons/Public_Test_Data/Defaced_VideoSnippets'
output_dir = '/media/farlab/Seagate Portable Drive/dev/Audit_Skeletons/Public_Test_Data/Skeleton_ActivityOutput'

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# List all files in the input directory
for file in os.listdir(input_dir):
    if file.endswith(".mp4"):
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, file)

        # Construct the command
        cmd = [
            'python', 'demo/demo_skeleton.py',
            input_file, output_file
        ]

        # Execute the command
        subprocess.run(cmd, check=True)
