import uno
from com.sun.star.table import BorderLine

class Border:
    def __init__(self, color=0x000000, width=20, vline=20, hline=20):
        self.color = color
        self.width = width
        self.hline = hline
        self.vline = vline

    def create_border(self, cell):
        # Create the top, bottom, left, and right BorderLine objects
        border_line = BorderLine()
        border_line.OuterLineWidth = self.width
        border_line.InnerLineWidth = 0
        border_line.Color = self.color

        # Create horizontal and vertical BorderLine objects
        horiz_line = BorderLine()
        horiz_line.OuterLineWidth = self.width
        horiz_line.InnerLineWidth = 0
        horiz_line.Color = self.color

        verti_line = BorderLine()
        verti_line.OuterLineWidth = self.width
        verti_line.InnerLineWidth = 0
        verti_line.Color = self.color

        # Access and update the cell's table border
        table_border = cell.TableBorder
        table_border.TopLine = border_line
        table_border.IsTopLineValid = True
        table_border.BottomLine = border_line
        table_border.IsBottomLineValid = True
        table_border.LeftLine = border_line
        table_border.IsLeftLineValid = True
        table_border.RightLine = border_line
        table_border.IsRightLineValid = True
        table_border.HorizontalLine = horiz_line
        table_border.IsHorizontalLineValid = True
        table_border.VerticalLine = verti_line
        table_border.IsVerticalLineValid = True

        # Set the updated border back to the cell
        cell.TableBorder = table_border
