#!/usr/bin/env python3
from LibreOffice import connect_libre

if __name__ == "__main__":
    # Attempt to connect to LibreOffice
    document = connect_libre()
    if isinstance(document, Exception):
        print(f"Error: Cannot connect to LibreOffice. {document}")
        exit(1)

    services = document.getSupportedServiceNames()
    print(f"Connected to Supported services: {services}")

    # Determine the type of the connected document
    if document.supportsService("com.sun.star.sheet.SpreadsheetDocument"):
        print("Connected to a Calc spreadsheet.")

    elif document.supportsService("com.sun.star.text.TextDocument"):
        print("Connected to a Writer document.")

    elif document.supportsService("com.sun.star.presentation.PresentationDocument"):
        print("Connected to an Impress presentation.")

    elif document.supportsService("com.sun.star.formula.FormulaProperties"):
        print("Connected to an Math Document.")

    elif document.supportsService("com.sun.star.drawing.DrawingDocument"):
        print("Connected to an Drawing Document.")

    else:
        print("Connected to an unsupported document type.")

