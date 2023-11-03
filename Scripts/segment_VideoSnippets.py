import pandas as pd
import os
import subprocess


def segment_video(session, offset, start, end, input_dir, output_dir):
    input_file = f'{input_dir}/{session}/D-{session}/color_anonymized.mp4'

    # Check if the input file exists, skip processing if it doesn't
    if not os.path.exists(input_file):
        print(f"Skipping {session}: File {input_file} not found.")
        return
    
    output_file = f'{output_dir}/{session}_D_Ten.mp4'
    start_time = start + float(offset[:-1])  # Convert offset to float and add to start time
    duration = end - start

    # Construct the ffmpeg command
    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-ss', str(start_time),
        '-t', str(duration),
        '-y',  # Overwrite output file if it exists
        output_file
    ]

    # Execute the ffmpeg command
    subprocess.run(cmd, check=True)

def main():
    csv_file = '/media/farlab/Seagate Portable Drive/dev/Audit_Skeletons/Public_Test_Data/Mocap_Segmentation_example.csv'
    input_dir = '/media/farlab/Seagate Portable Drive/Video_Data_Blurred'
    output_dir = '/media/farlab/Seagate Portable Drive/dev/Audit_Skeletons/Public_Test_Data/Defaced_VideoSnippets'

    df = pd.read_csv(csv_file)
    df = pd.read_csv(csv_file)
    print(df.columns)
    for index, row in df.iterrows():
        segment_video(row['Session'], row['OffsetDepth'], row['Ten-Start'], row['Ten-End'], input_dir, output_dir)

if __name__ == '__main__':
    main()
