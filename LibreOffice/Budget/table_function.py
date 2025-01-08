from LibreOffice.color_data import *
from cell_class import CellFormatter, CellContent, GetCell, GetCellByRange
from cell_functions import MergeCells, CellHeight, CellWidth
from border_class import Border

def create_table(sheet, table, col: str, row: int):
    # Initialize Table
    getRange = GetCellByRange(sheet)
    getCell = GetCell(sheet)
    init_col = col
    final_col = chr(ord(init_col) + 3)
    init_row = row

    # Function Start
    for key in table.keys():
        value = table[key]
        print(f"{key}: {value}") #test

        if key == 'title':
            title = value[0]
            style = value[1]
            if 'fore_color' in style:
                fore_color = style['fore_color']
                print(f"Foreground Color: {fore_color}") #test
            else:
                fore_color = black
                print(f"Default fore_color: {black}") #test

            if 'back_color' in style:
                back_color = style['back_color']
                print(f"Foreground Color: {back_color}") #test
            else:
                back_color = white
                print(f"Default fore_color: {white}") #test

            if title:
                cell_format = CellFormatter(size=8, justify="CC", fore_color=fore_color, back_color=back_color)
                cell_range = getRange.get(init_col, init_row, final_col, init_row)
                cell_range.merge(True)
                cell = getCell.get(init_col, init_row)
                cell.String = title
                cell_format.apply_format(cell_range)

        elif key == 'headers':
            col_index = ord(init_col)
            row_index = init_row + 1
            headers = value
            for header in headers:
                cell = getCell.get(chr(col_index), row_index)
                cell_format = CellFormatter(size=8, justify="CC", fore_color=fore_color, back_color=back_color)
                cell_format.apply_format(cell)
                border = Border(color=black, width=10, vline=10, hline=0)
                border.create_border(cell)

                if header:
                    cell.String = header
                col_index += 1

        elif key == 'row_headers':
            row_index = init_row + 2
            headers = value
            for header in headers:
                cell = getCell.get(init_col, row_index)
                cell_format = CellFormatter(size=10, bold=False, justify="LC", fore_color=black, back_color=light_grey)
                cell_format.apply_format(cell)
                cell.String = header
                row_index += 1
            cell_range = getRange.get(init_col, init_row + 2, final_col, row_index - 1)
            border = Border(color=black, width=10, vline=0, hline=0)
            border.create_border(cell_range)

        elif key == 'summary':
            cell_range = getRange.get(init_col, row_index, final_col, row_index)
            border = Border(color=black, width=30, vline=0, hline=0)
            border.create_border(cell_range)
            cell_format = CellFormatter(size=8, justify="CC", fore_color=black, back_color=light_grey)
            cell_format.apply_format(cell_range)
            cell = getCell.get(init_col, row_index)
            cell.String = value
