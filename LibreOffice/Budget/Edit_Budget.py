#!/usr/bin/env python3
"""
    LibreOffice - Python Interface
        Document-Calc Creator
"""
from LibreOffice.connect_libre import connect_libre
from LibreOffice.Budget import *
import uno
from com.sun.star.table import BorderLine

if __name__ == "__main__":
    document = connect_libre()
    if isinstance(document, Exception):
        print(f"Error: Cannot connect to LibreOffice. {document}")
        exit(1)

    services = document.getSupportedServiceNames()
    print(f"Connected to Supported services: {services}")


    month = 'December'
    sheet = document.Sheets[month]
    cell = sheet.getCellByPosition(0, 0)
    border = Border(width=50, color=bright_orange)
    border.create_border(cell)

    # year = 2025
    # for index, month in enumerate(months):
    #     if month not in document.Sheets:
    #         document.Sheets.insertNewByName(month, index)
    #         print(f"Created sheet: {month}")
    #     sheet = document.Sheets[month]
    #     row = sheet.Rows[0]
    #     row.Height = 600
    #     MergeCells(sheet, 'A', 0, 'I', 0)
    #     cell = sheet.getCellByPosition(0, 0)
    #     content = CellContent(text=f"{month} {year} Monthly Summary", formula=False)
    #     content.set_content(cell)
    #     formatter = CellFormatter()
    #     formatter.apply_format(cell)
    #     print(f"Formatted Sheet: {month}")
