# PDFConverter - Script

PDFConverter is a Python project that needs to be converted into an executable file in order to quickly interpret and convert a large number of tables into PDF format without requiring extensive user interaction.

![image](https://github.com/monambike/pdfconverter-pdftables-to-csv/assets/35270174/c14e73d1-4143-4134-b3da-29f57bbd6680)

## TABLE OF CONTENTS

- [LIBRARIES](#libraries)
- [FORMATS](#formats)
    - [Reading](#reading)
        - [Remove Double Quotes](#remove-double-quotes)
        - [Delete Empty Lines](#delete-empty-lines)
        - [Delete Empty Columns](#delete-empty-columns)
        - [Convert Header to Body](#convert-header-to-body)
        - [Remove Line Breaks](#remove-line-breaks)
        - [Replace Semicolon](#replace-semicolon)
    - [Conversion](#conversion)
        - [EXPORT \[withoutFormatting\]](#export-withoutformatting)
            - [Empty Data in Header](#empty-data-in-header)
            - [Line Breaks within Data](#line-breaks-within-data)
            - [Semicolon at the End of the Line](#semicolon-at-the-end-of-the-line)
            - [Space at the Beginning of the Line](#space-at-the-beginning-of-the-line)
            - [Quotes and One Column \(First Check\)](#quotes-and-one-column-first-check)
        - [EXPORT \[tableWithBlankCells\]](#export-tablewithblankcells)
            - [Empty Data](#empty-data)
            - [Adjacent Double Quotes](#adjacent-double-quotes)
            - [Space after Separator](#space-after-separator)
            - [Space between Separators and Double Quotes](#space-between-separators-and-double-quotes)
            - [Quotes and One Column (Second Check)](#quotes-and-one-column-second-check)
        - [EXPORT \[main\]](#export-main)
            - [Quotes at the Beginning](#quotes-at-the-beginning)
            - [Quotes at the End](#quotes-at-the-end)
            - [Empty Lines or Without Quotes (Second Check)](#empty-lines-or-without-quotes-second-check)
            - [Three Columns](#three-columns)
        - [EXPORT \[fullClear\]](#export-fullclear)

## LIBRARIES
### Python
List of libraries used for the development of the Python script:
- [**Pandas**](https://pandas.pydata.org/), for text conversion and DataFrame manipulation;
- [**Tabula**](https://tabula.technology/), for reading PDF files;
- Other standard libraries of the Python language were also used, such as [**Glob**](https://docs.python.org/3/library/glob.html) for retrieving only PDF files, [**OS**](https://docs.python.org/3/library/os.html) for system operations, [**argparse**](https://docs.python.org/3/library/argparse.html) for receiving and manipulating command-line arguments, among others.

## FORMATTING
Types of formatting and the files to which they were applied. When a file is shown to be exported (in table format), it means that all the formatting above the export will be applied.

## **Reading**
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

## **Conversion**
Formatting related to conversion.

### **Export \[withoutFormatting\]**
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

Caso seja:
```
"<data>";"Unnamed: 0";"<data>"
```
Fica como:
```
"<data>";"<data>"
```

<br>

#### Quebras de Linhas no Meio dos Dados
Remove quebras de linha caso elas ocorram no meio dos dados.

Caso seja:
```


"<data
data>"
```

Fica como:
```
"<data data>"
```

<br>

#### Ponto e Vírgula no Final da Linha
Remove ponto e vírgula `';'` caso seja no final da linha.
    
Caso seja:
```
"<data>";"<data>";
```

Fica como:
```
"<data>";"<data>"
```

<br>

#### Espaço no Início da Linha
Remove espaços no início das linhas.

Caso seja:
```
"<data>";"<data>"
 "<data>";"<data>"
"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>"
```

<br>

#### Aspas e Uma Coluna (Primeira Verificação)
Remove a linha caso ela possua aspas no ínicio e no final, e ainda por cima, possua apenas uma coluna ou menos.

Caso seja:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>
<data>"
```
Fica como:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>
<data>"
```

<br>

### **Exportação \[tableWithBlankCells\]**
Começa a realizar a exportação do arquivo para segurar a exeção de quando for convertida uma tabela que possui células vazias.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORTAÇÃO</th>
        </tr>
    </head>
    <body>
        <tr>
            <td>Folder Name:</td>
            <td>tableWithBlankCells</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\tableWithBlankCells"</td>
        </tr>
        <tr>
            <td>Descrição:</td>
            <td>
                O arquivo 'tableWithBlankCells' <br>
                é exportado nesse momento <br>
                com todas as formatações <br>
                realizadas acima.
            </td>
        </tr>
    </body>
</table>

<br>
<hr>
<br>

#### Dados Vazios
Remove dados que estão vazios `"";` e `;""`.

Caso seja:
```
"";"<data>";"<data>";"<data>"
"<data>";"<data>";"";"<data>"
"<data>";"<data>";"<data>";""
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

<br>

#### Aspas Duplas Adjacentes
Faz uma quebra de linha caso tenha aspas duplas uma do lado da outra.

Caso seja:
```
"<data>";"<data>""<data>";"<data>"
```
Fica como:
```
"<data>";"<data>"
"<data>";"<data>"
```

<br>

#### Espaço Após um Separador
Caso tenha um ponto e vírgula seguido de um espaço troca por uma quebra de linha

Caso seja:
```
"<Lorem ipsum>";"<Lorem ipsum>"; "<Lorem ipsum>";"<Lorem ipsum>"
```
Fica como:
```
"<Lorem ipsum>";"<Lorem ipsum>"
"<Lorem ipsum>";"<Lorem ipsum>"
```

<br>

#### Espaço entre Separadores e Aspas Duplas
Remove o conteúdo anterior caso tenha espaço entre os separadores e as aspas.

Caso seja:
```
"<Lorem ipsum>";"<Lorem ipsum>"; "<data>";"<data>"
```
Fica como:
```
"<data>";"<data>"
```

<br>

#### Aspas e Uma Coluna (Segunda Verificação)
Remove a linha caso ela possua aspas no ínicio e no final, e ainda por cima, possua apenas uma coluna ou menos.

Caso seja:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>
<data>"
```
Fica como:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>
<data>"
```

<br>

### **Exportação \[main\]**
Começa a realizar a exportação do arquivo principal.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORTAÇÃO</th>
        </tr>
    </head>
    <body>
        <tr>
            <td>Folder Name:</td>
            <td>main</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\main"</td>
        </tr>
        <tr>
            <td>Descrição:</td>
            <td>
                O arquivo 'main' <br>
                é exportado nesse momento <br>
                com todas as formatações <br>
                realizadas acima.
            </td>
        </tr>
    </body>
</table>

<br>
<hr>
<br>

#### Aspas no Início
Caso a linha não comece com aspas deleta.

Caso seja:
```
"<data>";"<data>";"<data>"
<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

<br>

#### Aspas no Final
Caso a linha não termine com aspas deleta.

Caso seja:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>
"<data>";"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

<br>

#### Linhas Vazias ou Sem Aspas (Segunda Verificação)
Linhas vazias que só possuem quebra de linha `'\n'` ou não possuem uma aspas dupla em nenhum lugar, serão excluídas.

Caso seja:
```



Lorem
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
Lorem ipsum

"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
"<data>";"<data>"
```

<br>

#### Três Colunas
Só escreve a linha caso tenha pelo menos três colunas ou mais.

Caso seja:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

<br>

### **Exportação \[fullClear\]**
Começa a realizar a exportação do arquivo principal com algumas modificações de formatação mais rígidas.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORTAÇÃO</th>
        </tr>
    </head>
    <body>
        <tr>
            <td>Folder Name:</td>
            <td>fullClear</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\fullClear"</td>
        </tr>
        <tr>
            <td>Descrição:</td>
            <td>
                O arquivo 'fullClear' <br>
                é exportado nesse momento <br>
                com todas as formatações <br>
                realizadas acima.
            </td>
        </tr>
    </body>
</table>

<br>
<hr>
