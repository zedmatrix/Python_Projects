"""
Initialization module for the LibreOffice project.
Contains constants, essential imports, and the connection function for LibreOffice.
"""

import uno
from LibreOffice.connect_libre import connect_libre
from LibreOffice.document_info import set_document_info, get_document_info
from LibreOffice.document_class import MyDocClass
from typing import Final

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

__all__ = ['connect_libre', 'set_document_info', 'get_document_info', 'MyDocClass',
           'dark_green', 'light_green', 'dark_red', 'light_red', 'light_grey', 'white', 'black', 'bright_orange', 'light_cyan']
