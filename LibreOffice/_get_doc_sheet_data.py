#!/usr/bin/env python3
import uno
from LibreOffice import connect_libre

if __name__ == "__main__":
    # Attempt to connect to LibreOffice
    document = connect_libre()
    if isinstance(document, Exception):
        print(f"Error: Cannot connect to LibreOffice. {document}")
        exit(1)

    services = document.getSupportedServiceNames()
    print(f"Connected to Supported services: {services}")

    # Inspect NumberFormatSettings properties
    settings = document.NumberFormatSettings
    property_set_info = settings.getPropertySetInfo()
    properties = property_set_info.getProperties()

    print("Available properties:")
    for prop in properties:
        print(f"- {prop.Name}")

    locale = document.getPropertyValue("CharLocale")
    print(f"Locale Language: {locale.Language}")
    print(f"Locale Country: {locale.Country}")
    print(f"Locale: {locale}")

    # Get All Property Data from a Cell
    sheet = document.Sheets['January']
    # Example cell: I = 8, 4 = 3
    cell = sheet.getCellByPosition(8, 3)
    properties = cell.getPropertySetInfo().getProperties()
    for prop in properties:
        print(f"{prop.Name} = {cell.getPropertyValue(prop.Name)}")
