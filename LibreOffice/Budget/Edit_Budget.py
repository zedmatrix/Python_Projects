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


        month = months[0]
    sheet = document.Sheets[month]

    getCell = GetCell(sheet)
    # get cell using sheet reference and return 0-Index 
    cell = getCell.get('A', 2)
    cell.String = f"{month}"
    cell = getCell.get('B', 3)
    cell.Formula = "=SUM($A$20:$A$30)"

    getRange = GetCellByRange(sheet)
    # using valid sheet reference as getRange converts to 0-Index and from letter reference (upper)
    cell_range = getRange.get('f', 3, 'i', 10)
    border = Border(width=30, color=black)
    border.create_border(cell_range)

    # Still operates on the last cell referenced from getCell sheet
    border = Border(width=50, color=bright_orange)
    border.create_border(cell)

    # Format and Merge A-I a budget banner for every monthly sheet
    year = 2025
    for index, month in enumerate(months):
        if month not in document.Sheets:
            document.Sheets.insertNewByName(month, index)
            print(f"Created sheet: {month}")
        sheet = document.Sheets[month]
        getCell = GetCell(sheet)
        row = sheet.Rows[0]
        row.Height = 600
        MergeCells(sheet, 'A', 0, 'I', 0)
        cell = getCell.get('A', 1)
        
        content = CellContent(text=f"{month} {year} Monthly Summary", formula=False)
        content.set_content(cell)
        formatter = CellFormatter()
        formatter.apply_format(cell)
        print(f"Formatted Sheet: {month}")
