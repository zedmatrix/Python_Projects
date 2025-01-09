"""
Usage:
    Initialize pointer: get_cell = GetCell(sheet)
                        cell = get_cell('C', 3) or
                        cell_range = get_cell("B", 2, getrange=True, nRight="D", nBottom=5)

Parameters
    nLeft	is the column index of the first cell inside the range.
    nTop	is the row index of the first cell inside the range.
    nRight	is the column index of the last cell inside the range.
    nBottom	is the row index of the last cell inside the range.

    set_format( font=Arial
                size=12
                bold=True
                fore_color=dark_green 0x000000 referenced value
                back_color=light_green 0xffffff referenced value
                justify="LC" 6 positional reference (L)eft,(C)enter,(R)ight (T)op,(C)enter,(B)ottom
    apply_format(cell) or
    apply_format(cell_range)
"""

import uno
from LibreOffice.color_data import white, black

class GetCell:
    def __init__(self, sheet):
        self.sheet = sheet

    def __call__(self, nLeft: str, nTop: int, getrange: False, nRight=None, nBottom=None):
        # Convert column letter to a zero-based index
        left_column = ord(nLeft.upper()) - ord('A')
        top_index = nTop - 1
        if not getrange:
            return self.sheet.getCellByPosition(left_column, top_index)
        else:
            right_column = ord(nRight.upper()) - ord('A')
            bottom_index = nBottom - 1
            return self.sheet.getCellRangeByPosition(left_column, top_index, right_column, bottom_index)

    def set_format(self, font="Verdana", size=10, bold=True, fore_color=black, back_color=white, justify="CC"):
        self.font = font
        self.size = size
        self.weight = 150 if bold else 100
        self.fore_color = fore_color
        self.back_color = back_color
        self.set_justification(justify)

    def set_justification(self, justify):
        self.hori_justify = {"L": 0, "C": 2, "R": 1}.get(justify[0], 2)  # Default to Center
        self.vert_justify = {"T": 0, "C": 2, "B": 1}.get(justify[1], 2)  # Default to Center

    def apply_format(self, cell):
        try:
            cell.setPropertyValue("CharFontName", self.font)
            cell.setPropertyValue("CharHeight", self.size)
            cell.setPropertyValue("CharWeight", self.weight)
            cell.setPropertyValue("CharColor", self.fore_color)
            cell.setPropertyValue("CellBackColor", self.back_color)
            cell.setPropertyValue("HoriJustify", self.hori_justify)
            cell.setPropertyValue("VertJustify", self.vert_justify)
        except Exception as e:
            print(f"Failed to apply format: {e}")
