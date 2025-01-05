"""
    Document Storage Dictionary of LibreOffice Module
"""

class MyDocClass(dict):
    def __init__(self):
        self._keys = ["Title", "Author", "Subject", "Description", "Generator", "CreationDate",
                      "file_name", "file_path", "file_url"]
        for key in self._keys:
            self[key] = None

    def get_defined_keys(self):
        return self._keys

    def get_values(self):
        return '\n'.join(f"{key}: {self[key]}" for key in self._keys)
