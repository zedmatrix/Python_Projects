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

if __name__ == "__main__":
    document = connect_libre()
    if isinstance(document, Exception):
        print(f"Error: Cannot connect to LibreOffice. {document}")
        exit(1)

    services = document.getSupportedServiceNames()
    print(f"Connected to Supported services: {services}")

    DocumentInfo = MyDocClass()
    DocumentInfo["author"] = "<your name here>"
    DocumentInfo["title"] = "<title for document>"
    DocumentInfo["subject"] = "<subject>"
    DocumentInfo["comment"] = "<description shows up as Comment>"
    DocumentInfo["file_name"] = "<your filename>"
    DocumentInfo["file_path"] = "$HOME/Documents"

    file_path = os.path.expandvars(os.path.join(DocumentInfo["file_path"], DocumentInfo["file_name"]))
    DocumentInfo["file_url"] = systemPathToFileUrl(file_path)

    set_document_info(document, DocumentInfo)

    get_document_info(document, DocumentInfo)

    print(DocumentInfo.get_values())
