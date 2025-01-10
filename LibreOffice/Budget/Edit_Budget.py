#!/usr/bin/env python3
"""
    LibreOffice - Python Interface
        Enter Receipt Data Script
"""
import uno
from LibreOffice.connect_libre import connect_libre
from LibreOffice.Budget.receipt_function import enter_receipt

if __name__ == "__main__":
    document = connect_libre()
    if isinstance(document, Exception):
        print(f"Error: Cannot connect to LibreOffice. {document}")
        exit(1)

    services = document.getSupportedServiceNames()
    print(f"Connected to Supported services: {services}")

    year = 2025
    month = 'January'
    print(f" Updating Sheet {month} ")
    sheet = document.Sheets[month]

    enter_receipt(sheet,
                  store_name='',
                  category='',
                  amount=0,
                  tax=0,
                  card='',
                  date='day-month-year',
                  description='')
