"""
Initialization module for the LibreOffice project.
Contains constants, essential imports, and the connection function for LibreOffice.
"""

import uno
from LibreOffice.connect_libre import connect_libre, open_office
from LibreOffice.document_info import set_document_info, get_document_info
from LibreOffice.document_class import MyDocClass

__all__ = ['connect_libre', 'open_office', 'set_document_info', 'get_document_info', 'MyDocClass']
