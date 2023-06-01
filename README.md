# PDFConverter - Script

PDFConverter is a Python project that needs to be converted into an executable file in order to quickly interpret and convert a large number of tables into PDF format without requiring extensive user interaction.

You can also check the branchs [docs](https://github.com/monambike/pdfconverter-pdftables-to-csv/tree/docs) or the [desktop application](https://github.com/monambike/pdfconverter-pdftables-to-csv/tree/desktop) used for testing the call of this Script.

**Example of Script call:**

```
python pdfconverter.py --ImportPath "C:\\users\\dvp10\\desktop\\EDITAL (2).pdf" --ExportPath "C:\\users\\dvp10\\desktop" --PageNumber "all"
```

## Project Structure

![image](https://github.com/monambike/pdfconverter-pdftables-to-csv/assets/35270174/c14e73d1-4143-4134-b3da-29f57bbd6680)

## Table of Contents

- [LIBRARIES](#libraries)
- [FORMATTING](#formatting)
    - [File Read Handling](#file-read-handling)
        - [Remove Double Quotes](#remove-double-quotes)
        - [Delete Empty Lines](#delete-empty-lines)
        - [Delete Empty Columns](#delete-empty-columns)
        - [Convert Header to Body](#convert-header-to-body)
        - [Remove Line Breaks](#remove-line-breaks)
        - [Replace Semicolon](#replace-semicolon)
    - [Conversion File Handling](#conversion-file-handling)
        - [EXPORT \[withoutFormatting\]](#export-withoutformatting)
            - [Empty Data in Header](#empty-data-in-header)
            - [Line Breaks in the Middle of Data](#line-breaks-in-the-middle-of-data)
            - [Semicolon at the End of the Line](#semicolon-at-the-end-of-the-line)
            - [Space at the Beginning of the Line](#space-at-the-beginning-of-the-line)
            - [Quotes and One Column \(First Check\)](#quotes-and-one-column-first-check)
        - [EXPORT \[tableWithBlankCells\]](#export-tablewithblankcells)
            - [Empty Data](#empty-data)
            - [Adjacent Double Quotes](#adjacent-double-quotes)
            - [Space After a Separator](#space-after-a-separator)
            - [Space between Separators and Double Quotes](#space-between-separators-and-double-quotes)
            - [Quotes and One Column (Second Check)](#quotes-and-one-column-second-check)
        - [EXPORT \[main\]](#export-main)
            - [Quotes at the Beginning](#quotes-at-the-beginning)
            - [Quotes at the End](#quotes-at-the-end)
            - [Empty Lines or Without Quotes (Second Check)](#empty-lines-or-without-quotes-second-check)
            - [Three Columns](#three-columns)
        - [EXPORT \[fullClear\]](#export-fullclear)

## Libraries

List of libraries used for the development of the Python script:
- [**Pandas**](https://pandas.pydata.org/), for text conversion and DataFrame manipulation;
- [**Tabula**](https://tabula.technology/), for reading PDF files;
- Other standard libraries of the Python language were also used, such as [**Glob**](https://docs.python.org/3/library/glob.html) for retrieving only PDF files, [**OS**](https://docs.python.org/3/library/os.html) for system operations, [**argparse**](https://docs.python.org/3/library/argparse.html) for receiving and manipulating command-line arguments, among others.

## Formatting
Types of formatting and the files to which they were applied. When a file is shown to be exported (in table format), it means that all the formatting above the export will be applied.

## File Read Handling
Formatting related to reading.

#### Remove Double Quotes
Removes all double quotes from the DataFrame to avoid future issues.

#### Replace Semicolon
Replaces all semicolons in the DataFrame with commas to avoid conflicts.

#### Delete Empty Lines
Deletes all empty rows in the DataFrame.

#### Delete Empty Columns
Deletes all empty columns in the DataFrame.

#### Convert Header to Body
Converts the header to body to remove unnecessary and detrimental formatting.

#### Remove Line Breaks
Removes line breaks that occur when the PDF has a very long line.

## Conversion File Handling
Formatting related to conversion.

### Export \[withoutFormatting\]
Starts the first export, which is the export of the unformatted file that will be formatted later.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORT</th>
        </tr>
    </head>
    <body>
        <tr>
            <td>Folder Name:</td>
            <td>withoutFormatting</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\withoutFormatting"</td>
        </tr>
        <tr>
            <td>Description:</td>
            <td>
                 The 'withoutFormatting' file <br>
                is exported at this moment <br>
                without any formatting.
            </td>
        </tr>
    </body>
</table>

<br>
<hr>
<br>

<br>

#### Empty Data in Header
Removes empty data in the header.

#### If it is:
```
"<data>";"Unnamed: 0";"<data>"
```
It becomes:
```
"<data>";"<data>"
```

<br>

#### Line Breaks in the Middle of Data
Removes line breaks if they occur in the middle of the data.

If it is:
```
"<data
data>"
```
It becomes:
```
"<data data>"
```

<br>

#### Semicolon at the End of the Line
Removes semicolon `';'` if it is at the end of the line.

If it is:
```
"<data>";"<data>";
```
It becomes:
```
"<data>";"<data>"
```

<br>

#### Space at the Beginning of the Line
Removes leading spaces in the lines.

If it is:
```
"<data>";"<data>"
 "<data>";"<data>"
"<data>";"<data>"
```
It becomes:
```
"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>"
```

<br>

#### Quotes and One Column (First Check)
Removes the line if it has quotes at the beginning and end, and on top of that, it has only one column or less.

If it is:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>
<data>"
```
It remains the same:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>
<data>"
```

<br>

### Export \[tableWithBlankCells\]
Starts the export of the file to handle the exception when converting a table that has empty cells.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORT</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Folder Name:</td>
            <td>tableWithBlankCells</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\tableWithBlankCells"</td>
        </tr>
        <tr>
            <td>Description:</td>
            <td>
                The file 'tableWithBlankCells' <br>
                is exported at this moment <br>
                with all the formatting <br>
                applied above.
            </td>
        </tr>
    </tbody>
</table>

<br>
<hr>
<br>

#### Empty Data
Removes data that is empty `"";` and `;""`.

If it is:
```
"";"<data>";"<data>";"<data>"
"<data>";"<data>";"";"<data>"
"<data>";"<data>";"<data>";""
```
It becomes:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

<br>

#### Adjacent Double Quotes
Inserts a line break if there are double quotes side by side.

If it is:
```
"<data>";"<data>""<data>";"<data>"
```
It becomes:
```
"<data>";"<data>"
"<data>";"<data>"
```

<br>

#### Space After a Separator
If there is a semicolon followed by a space, it is replaced by a line break.

If it is:
```
"<Lorem ipsum>";"<Lorem ipsum>"; "<Lorem ipsum>";"<Lorem ipsum>"
```


It becomes:
```
"<Lorem ipsum>";"<Lorem ipsum>"
"<Lorem ipsum>";"<Lorem ipsum>"
```

<br>

#### Space Between Separators and Double Quotes
Removes the preceding content if there is a space between the separators and the quotes.

If it is:
```
"<Lorem ipsum>";"<Lorem ipsum>"; "<data>";"<data>"
```
It becomes:
```
"<data>";"<data>"
```

<br>

#### Quotes and One Column (Second Check)
Removes the line if it has quotes at the beginning and end, and on top of that, it has only one column or less.

If it is:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>
<data>"
```
It remains the same:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>
<data>"
```

<br>

### Export \[main\]
Starts the export of the main file.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORT</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Folder Name:</td>
            <td>main</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\main"</td>
        </tr>
        <tr>
            <td>Description:</td>
            <td>
                The file 'main' <br>
                is exported at this moment <br>
                with all the formatting <br>
                applied above.
            </td>
        </tr>
    </tbody>
</table>

<br>
<hr>
<br>

#### Quotes at the Beginning
Deletes the line if it doesn't start with quotes.

If it is:
```
"<data>";"<data>";"<data>"
<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```
It becomes:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

<br>

#### Quotes at the End
Deletes the line if it doesn't end with quotes.

If it is:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>
"<data>";"<data>";"<data>"
```
It becomes:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

<br>

#### Empty Lines or Without Quotes (Second Check)
Empty lines that only have line breaks `'\n'` or don't have a double quote anywhere will be deleted.

If it is:
```



Lorem
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
Lorem ipsum

"<data>";"<data>"
```
It becomes:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
"<data>";"<data>"
```

<br>

#### Three Columns
Only writes the line if it has at least three columns or more.

If it is:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```
It becomes:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

<br>

### Export \[fullClear\]
Starts the export of the main file with some stricter formatting modifications.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORT</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Folder Name:</td>
            <td>fullClear</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\fullClear"</td>
        </tr>
        <tr>
            <td>Description:</td>
            <td>
                The file 'fullClear' <br>
                is exported at this moment <br>
                with all the formatting <br>
                applied above.
            </td>
        </tr>
    </tbody>
</table>

<br>
<hr>
