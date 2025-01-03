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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start LibreOffice Interface")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--calc", action="store_true", help="Start LibreCalc")
    group.add_argument("--write", action="store_true", help="Start LibreWriter")
    group.add_argument("--web", action="store_true", help="Start LibreHTML Writer")
    group.add_argument("--draw", action="store_true", help="Start LibreDraw")
    group.add_argument("--impress", action="store_true", help="Start LibreMath")
    group.add_argument("--math", action="store_true", help="Start LibreMath")
    parser.add_argument("--doc", type=str, help="Open a specific document")

    args = parser.parse_args()
    print(args)

    if args.calc:
        print("Starting Libre Calc Spreadsheet")
        open_office("--calc")

    elif args.write:
        print("Starting Libre Writer Document")
        open_office("--writer")

    elif args.web:
        print("Starting Libre Web HTML Document")
        open_office("--web")

    elif args.draw:
        print("Starting Libre Draw")
        open_office("--draw")

    elif args.impress:
        print("Starting Libre Presentation")
        open_office("--impress")

    elif args.math:
        print("Starting Math Document")
        open_office("--math")

    elif args.doc:
        print(f"Opening document: {args.doc}")
        open_office("", document=args.doc)

    else:
        print("Usage:")
        print("  --calc    Start Libre Calc")
        print("  --write   Start Libre Writer")
        print("  --web     Start Libre Web")
        print("  --draw    Start Libre Draw")
        print("  --impress Start Libre Presentation")
        print("  --math    Start Libre Math Document")
        
        print("  --doc <filename>   Open a specific document")

"""
 --writer            Creates an empty Writer document.
 --calc              Creates an empty Calc document.
 --draw              Creates an empty Draw document.
 --impress           Creates an empty Impress document.
 --base              Creates a new database.
 --global            Creates an empty Writer master (global) document.
 --math              Creates an empty Math document (formula).
 --web               Creates an empty HTML document.
"""
