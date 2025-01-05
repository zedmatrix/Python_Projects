"""
Initialization module for the LibreOffice project.
Contains constants, essential imports, and the connection function for LibreOffice.
"""

from cell_class import CellFormatter, CellContent, GetCell, GetCellByRange
from cell_functions import MergeCells
from border_class import Border
from typing import Final

# Header Constants
months = [ "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December" ]

# Color constants
dark_green: Final[int] = 0xa0d5a0
light_green: Final[int] = 0x97ff97
dark_red: Final[int] = 0xb60000
light_red: Final[int] = 0xffa2a2
light_grey: Final[int] = 0xeeeeee
white: Final[int] = 0xffffff
black: Final[int] = 0x000000
bright_orange: Final[int] = 0xf97f05
light_cyan: Final[int] = 0xc6e6e6

__all__ = ['months', 'CellFormatter', 'CellContent', 'letter_col', 'MergeCells', 'Border', 'GetCell', 'GetCellByRange',
           'dark_green', 'light_green', 'dark_red', 'light_red', 'light_grey', 'white', 'black', 'bright_orange', 'light_cyan']
