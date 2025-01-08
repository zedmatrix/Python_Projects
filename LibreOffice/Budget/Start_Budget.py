#!/usr/bin/env python3
"""

    LibreOffice - Python Interface
        Document-Calc Creator
        This Will Have a Debug Terminal from LibreOffice until closed

"""

from LibreOffice.connect_libre import connect_libre, open_office
from LibreOffice.document_class import MyDocClass
from unohelper import systemPathToFileUrl
import uno
import os

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
