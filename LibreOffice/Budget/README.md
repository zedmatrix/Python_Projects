# Python-Calc Bridge
Creating a Budget for 2025 using Python and Libre Office Calc <br>

opens the LibreOffice Calc <br>
    `../Start_LibreOffice.py --calc`

### Starts the Interface to open previous document
    ./Start_Budget.py

### Main script to interface with LibreOffice Calc
    ./Edit_Budget.py

### GetCell 
  New_Cell_Class.py version
  get the cell by sheet reference index and convert to 0-Index
```
    getCell = GetCell(sheet)
    cell = getCell('A', 1)
    cell = getCell('Z', 99)
```

### GetCellByRange
  get a cell range by sheet reference index and convert to 0-Index <br>
  creates a border around each cell in range A1:C3
```
    getRange = GetCell(sheet)
    cellrange = getRange('A', 1, 'C', 3, getrange=True)
    border = Border(color=bright_orange, width=50, vline=20, hline=20)
    border.create_border(cellrange)
    cellrange.merge(True)
```

### CellFormatter
  Works with both GetCell and GetCellByRange
```
    getCell = GetCell(sheet)
    cell = getCell('A', 1)
    getCell.set_format(
        font="Verdana", 
        size=16, 
        bold=True, 
        fore_color=black, 
        back_color=white, 
        justify="CC"
        )
    getCell.apply_format(cell)
```

### CellContent
  Works with both GetCell and GetCellByRange
```
    getCell = GetCell(sheet)
    cell = getCell.get('A', 1)
    cell.String = "Hello, World!"
    column = 'A'
    cell.Formula = f"=SUM(${column}$1:${column}$99"
```

### MergeCells
  merge cells in range A1:B2 ... Old function moved the GetCell in New_Cell_Class
```
    MergeCells(sheet, 'A', 1, 'B', 2)
```

### Border
  create a border around cell or cell range
```
    border = Border(
        color=dark_green,
        width=20,
        vline=0,
        hline=0
        )
    border.create_border(cell)
    border.create_border(cellrange)
```
