"""
        Example usage:
        cell = sheet.getCellByPosition(col, row)
        # Set content
        content = CellContent(text="Hello, World!", formula=False)
        content.set_content(cell)

        # Apply formatting
        formatter = CellFormatter(justify="LT", fore_color=0xFF0000, back_color=0xFFFF00)
        formatter.apply_format(cell)

"""
import uno

class CellFormatter:
    def __init__(self, font="Verdana", size=16, bold=True, fore_color=0x000000, back_color=0xFFFFFF, justify="CC"):
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
