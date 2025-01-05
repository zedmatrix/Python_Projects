#!/usr/bin/env python3
"""
    LibreOffice - Python Interface
        Document-Calc Creator
"""
from LibreOffice.connect_libre import connect_libre
from LibreOffice.document_info import set_document_info, get_document_info
from LibreOffice.document_class import MyDocClass
from unohelper import systemPathToFileUrl
import uno
import os
import subprocess

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
    DocumentInfo = MyDocClass()
    DocumentInfo["file_name"] = "myBudget_2025.ods"
    DocumentInfo["file_path"] = os.path.expandvars("$HOME/Documents")
    file_path = os.path.expandvars(os.path.join(DocumentInfo["file_path"], DocumentInfo["file_name"]))
    DocumentInfo["file_url"] = systemPathToFileUrl(file_path)

    open_office('--calc', DocumentInfo["file_url"])

    document = connect_libre()
    if isinstance(document, Exception):
        print(f"Error: Cannot connect to LibreOffice. {document}")
        exit(1)

    services = document.getSupportedServiceNames()
    print(f"Connected to Supported services: {services}")

    # DocumentInfo["author"] = "Travis Tucker"
    # DocumentInfo["title"] = "Yearly Budget for 2025"
    # DocumentInfo["subject"] = "Yearly Budget"
    # DocumentInfo["comment"] = "Travis' Yearly Budget for 2025"
    #
    # set_document_info(document, DocumentInfo)

    get_document_info(document, DocumentInfo)

    print(DocumentInfo.get_values())
