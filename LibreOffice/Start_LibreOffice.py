#!/usr/bin/env python3
import argparse, subprocess

def open_office(option, document=None):
    try:
        command = f"libreoffice {option} --accept=\"socket,host=localhost,port=2002;urp;\""
        if document:
            command += f" \"{document}\""
        print(f"Running command: {command}")
        subprocess.run(command, check=True, text=True, shell=True)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print(f"Error output:\n{e.stderr}")
    except FileNotFoundError:
        print("The 'libreoffice' command was not found on this system.")

parser = argparse.ArgumentParser(description="Start LibreOffice Interface")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--calc", action="store_true", help="Start LibreCalc")
group.add_argument("--write", action="store_true", help="Start LibreWriter")
group.add_argument("--web", action="store_true", help="Start LibreHTML Writer")
parser.add_argument("--doc", type=str, help="Open a specific document")

args = parser.parse_args()
print(args)

if args.calc:
    print("Starting LibreCalc...")
    open_office("--calc")

elif args.write:
    print("Starting LibreWriter...")
    open_office("--writer")

elif args.web:
    print("Starting LibreWeb...")
    open_office("--web")

elif args.doc:
    print(f"Opening document: {args.doc}")
    open_office("", document=args.doc)

else:
    print("Usage:")
    print("  calc   Start LibreCalc")
    print("  write  Start LibreWriter")
    print("  web    Start LibreWeb")
    print("  --doc <filename>   Open a specific document")

""" --writer            Creates an empty Writer document.
   --calc              Creates an empty Calc document.
   --draw              Creates an empty Draw document.
   --impress           Creates an empty Impress document.
   --base              Creates a new database.
   --global            Creates an empty Writer master (global) document.
   --math              Creates an empty Math document (formula).
   --web               Creates an empty HTML document."""
