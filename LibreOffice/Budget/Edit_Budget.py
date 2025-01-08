#!/usr/bin/env python3
"""
    LibreOffice - Python Interface
        Document-Calc Creator
"""
from LibreOffice.connect_libre import connect_libre
from LibreOffice.color_data import *
from LibreOffice.Budget.table_function import create_table
from LibreOffice.Budget.budget_data import (
    months, budget_summary, income_summary, expense_summary, home_expense, necessities,
    personal, transport, banking, pet_expense
    )
from cell_functions import MergeCells, CellHeight, CellWidth
import uno


if __name__ == "__main__":
    document = connect_libre()
    if isinstance(document, Exception):
        print(f"Error: Cannot connect to LibreOffice. {document}")
        exit(1)

    services = document.getSupportedServiceNames()
    print(f"Connected to Supported services: {services}")

    #month = months.index('January')
    #month = months.index('February')
    month = months.index('March')
    for month in months:
        if month == 'January' or month == 'February' or month == 'March':
            continue

        print(f'Updating Sheet {month}')
        sheet = document.Sheets[month]
        MergeCells(sheet, 'A', 1, 'N', 1)

        create_table(sheet, budget_summary, 'A', 3)
        create_table(sheet, income_summary, 'A', 8)
        create_table(sheet, expense_summary, 'A', 18)
        create_table(sheet, home_expense, 'F', 2)
        create_table(sheet, necessities, 'F', 12)
        create_table(sheet, personal, 'K', 2)
        create_table(sheet, transport, 'K', 12)
        create_table(sheet, banking, 'F', 22)
        create_table(sheet, pet_expense, 'K', 22)

        CellWidth(sheet, col='A', optimal=True)
        CellWidth(sheet, col='E', width=200, optimal=False)
        CellWidth(sheet, col='F', optimal=True)
        CellWidth(sheet, col='J', width=200, optimal=False)
        CellWidth(sheet, col='K', optimal=True)
