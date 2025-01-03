"""
Connect to LibreOffice using the UNO API.

Returns:
    The currently active LibreOffice document object if connected successfully, or an Exception if an error occurs.

Example:
    document = connect_libre()
    if isinstance(document, Exception):
        print(f"Error: Cannot connect to LibreOffice. {document}")
        exit(1)

    if document.supportsService("com.sun.star.sheet.SpreadsheetDocument"):
        print("Connected to a Calc spreadsheet.")
    elif document.supportsService("com.sun.star.text.TextDocument"):
        print("Connected to a Writer document.")
    elif document.supportsService("com.sun.star.presentation.PresentationDocument"):
        print("Connected to an Impress presentation.")
    else:
        print("Connected to an unsupported document type.")
"""

import uno

def connect_libre() -> uno.Any:
    try:
        local_context = uno.getComponentContext()
        resolver = local_context.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", local_context
        )
        ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
        desktop = ctx.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", ctx
        )
        document = desktop.getCurrentComponent()

        return document

    except Exception as e:
        return e
