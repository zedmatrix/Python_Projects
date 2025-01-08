"""
        Example usage:
        getCell = GetCell(sheet)
        cell = getCell.get('A', 1)
        # Set content
        content = CellContent(text="Hello, World!", formula=False)
        content.set_content(cell)

        # Apply formatting
        formatter = CellFormatter(justify="LT", fore_color=0xFF0000, back_color=0xFFFF00)
        formatter.apply_format(cell)

        Example:
        getCell = GetCell(sheet)
        cell = getCell.get('A', 1)
        cell = getCell.get('B', 9)

        getRange = GetCellByRange(sheet)

        # Retrieve a range of cells (e.g., A1 to C3)
        cell_range = getRange.get('A', 1, 'C', 3)
"""
import uno
from LibreOffice.color_data import white, black

class GetCell:
    def __init__(self, sheet):
        self.sheet = sheet

    def get(self, column: str, row: int):
        """
        Fetch a cell object using column (A-Z) and row (1-based).
        """
        # Convert column letter to a zero-based index
        column_index = ord(column.upper()) - ord('A')
        row_index = row - 1
        return self.sheet.getCellByPosition(column_index, row_index)

class GetCellByRange:
    def __init__(self, sheet):
        self.sheet = sheet

    def get(self, top: str, left: int, bottom: str, right: int):
        """
        Fetch a cell object using column (A-Z) and row (1-based).
        """
        # Convert column letter to a zero-based index
        top_index = ord(top.upper()) - ord('A')
        left_index = left - 1
        bottom_index = ord(bottom.upper()) - ord('A')
        right_index = right - 1
        return self.sheet.getCellRangeByPosition(top_index, left_index, bottom_index, right_index)

class CellFormatter:
    def __init__(self, font="Verdana", size=16, bold=True, fore_color=black, back_color=white, justify="CC"):
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
        cell.setPropertyValue("CharFontName", self.font)
        cell.setPropertyValue("CharHeight", self.size)
        cell.setPropertyValue("CharWeight", self.weight)
        cell.setPropertyValue("CharColor", self.fore_color)
        cell.setPropertyValue("CellBackColor", self.back_color)
        cell.setPropertyValue("HoriJustify", self.hori_justify)
        cell.setPropertyValue("VertJustify", self.vert_justify)


class CellContent:
    def __init__(self, text="", formula=False):
        self.text = text
        self.formula = formula

    def set_content(self, cell):
        if self.formula:
            cell.Formula = self.text
        else:
            cell.String = self.text
