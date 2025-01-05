"""
    LibreOffice - Python Interface
        Retrieve document information from the LibreOffice document and return it as a DocumentInfo instance.

        Parameters: document: The LibreOffice document object (e.g., from UNO API).
                    DocumentInfo: MyDocClass dictionary

        Returns: An instance of the DocumentInfo class containing the document properties.
"""
import uno
from LibreOffice.document_class import MyDocClass

def set_document_info(document, DocumentInfo):

    properties = document.DocumentProperties
    properties.Author = DocumentInfo["author"]
    properties.Title = DocumentInfo["title"]
    properties.Subject = DocumentInfo["subject"]
    properties.Description = DocumentInfo["comment"]
    properties.Generator = "LibreOffice Module for Python 0.1"

    # Save the file
    document.storeAsURL(DocumentInfo["file_url"], ())


def get_document_info(document, DocumentInfo: MyDocClass) -> dict:

    try:
        doc_properties = document.DocumentProperties

        for key in DocumentInfo.get_defined_keys():
            # Skip as LibreOffice doesn't store these
            if key in ["file_name", "file_path", "file_url"]:
                continue
            else:
                value = getattr(doc_properties, key, None)
                if key == "CreationDate":
                    try:
                        formatted_date = f"{value.Year:04d}-{value.Month:02d}-{value.Day:02d} " \
                                         f"{value.Hours:02d}:{value.Minutes:02d}:{value.Seconds:02d}"
                        DocumentInfo[key] = formatted_date
                    except AttributeError:
                        DocumentInfo[key] = None
                else:
                    DocumentInfo[key] = value
        return DocumentInfo
    except AttributeError as e:
        print(f"Error retrieving document info: {e}")
        return {}
