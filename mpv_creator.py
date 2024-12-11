#!/usr/bin/env python3
import argparse
import subprocess

# Open File for write mode (use 'a' for appending)
myfile = open('mpv_list.m3u', 'wt')

def Parse_Dir(result):
    lines = result.stdout.strip().split("\n")
    parsed_results = []
    for line in lines:
        print(f"Raw Line {line}")    #Debugging
        parts = line.split(" ", 1)
        if len(parts) == 2:
            parsed_results.append((parts[0], parts[1]))
        else:
            print(f"Unexpected line format: {line}")

    for timestamp, file_path in parsed_results:
        print(f"File: {file_path}")
        myfile.write("%s\n" % file_path )

# Instantiate the parser
parser = argparse.ArgumentParser(description='MPV Shuffle Script Creator')
parser.add_argument('mpv_path', type=str,
                    help='An path string argument')
args = parser.parse_args()

# Validate and execute the command
# Optional: f"find {args.mpv_path} -name '*.mp4' -type f -printf '%T@ %p\\n' | sort -r",
try:
    print(f"Listing details for: {args.mpv_path}")
    result = subprocess.run(
        f"find '{args.mpv_path}' -name '*.mkv' -type f -printf '%T@ %p\n' | shuf -n 20",
        check=True,
        text=True,
        capture_output=True,
        shell=True
    )
    print("Command output:")
    #print(result.stdout)    #Debugging
    Parse_Dir(result)

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
    print(f"Error output:\n{e.stderr}")
except FileNotFoundError:
    print("The 'find' command was not found on this system.")

myfile.close
