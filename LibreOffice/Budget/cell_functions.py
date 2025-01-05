"""
    Cell Function Reference
        MergeCells()


"""

# Merge Cells
def MergeCells(sheet, col_left: str, start_row, col_right: str, end_row):
    start_col = ord(col_left.upper()) - ord('A')
    end_col = ord(col_right.upper()) - ord('A')
    cell_range = sheet.getCellRangeByPosition(start_col, start_row, end_col, end_row)
    cell_range.merge(False)
    cell_range.merge(True)
