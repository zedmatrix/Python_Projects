"""
    Removes a sheet by name from the Calc document.

    :param document: The connected LibreOffice Calc document.
    :param sheet: The name of the sheet to remove.
"""
import uno

def remove_sheet(document, sheet):
    try:
        sheets = document.Sheets

        if sheets.hasByName(sheet):
            sheets.removeByName(sheet)
            print(f"Sheet '{sheet}' removed successfully.")
        else:
            print(f"Sheet '{sheet}' does not exist.")
    except Exception as e:
        print(f"Error removing sheet '{sheet}': {e}")


def create_sheet(document, sheet, index):
    sheets = document.Sheets
    try:
        if sheet not in sheets:
            sheets.insertNewByName(sheet, index)
            print(f"Created sheet: {sheet} at Index: {index}")
    except Exception as e:
        print(f"Error removing sheet '{sheet}': {e}")
