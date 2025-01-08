"""
    Cell Function Reference
        MergeCells(sheet, 'A', 1, 'B', 2)
        CellHeight(sheet, row (1-based), height= (300), optimal=True)
        CellWidth(sheet, column (Letter), width= (600), optimal=True)


"""

def MergeCells(sheet, col_left: str, start_row, col_right: str, end_row):
    start_col = ord(col_left.upper()) - ord('A')
    end_col = ord(col_right.upper()) - ord('A')
    cell_range = sheet.getCellRangeByPosition(start_col, start_row - 1, end_col, end_row - 1)
    cell_range.merge(False)
    cell_range.merge(True)

def CellHeight(sheet, row: int, height=300, optimal=True):
    try:
        row_index = row - 1
        row_object = sheet.Rows[row_index]
        if optimal:
            row_object.OptimalWidth = True
            print(f"Set row {row} to optimal height.")
        else:
            row_object.Height = height
            print(f"Set height of row {row} to {height}.")
    except Exception as e:
        print(f"Error setting height for row {row}: {e}")

def CellWidth(sheet, col: str, width=600, optimal=True):
    try:
        columns = sheet.getColumns()
        column = columns.getByName(col)
        if optimal:
            column.OptimalWidth = True
            print(f"Set column {col} to optimal width.")
        else:
            column.Width = width
            print(f"Set width of column {col} to {width}.")
    except Exception as e:
        print(f"Error setting width for column {col}: {e}")
