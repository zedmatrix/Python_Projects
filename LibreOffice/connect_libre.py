"""
        Connect to LibreOffice using the UNO API.
    Returns: currently active LibreOffice document object if connected successfully
        or an Exception if an error occurs.
    Example:
        Start_Libreoffice.py
"""

import uno

def connect_libre() -> uno.Any:
    try:
        local_context = uno.getComponentContext()
        resolver = local_context.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", local_context
        )
        ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
        desktop = ctx.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", ctx
        )
        document = desktop.getCurrentComponent()

        return document

    except Exception as e:
        return e

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
