"""
---
---
---

## Package: pdfconverter >> conversion >> format
---
---
### Module Name: fullclear
---
### path: "pdfconverter\\\\\\\\conversion\\\\\\\\format\\\\\\\\fullclear.py"
---
---
Módulo relacionado à formatação FullClear.

---
---
---
"""


# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import fvar
# [i] Arquivo do terminal
from pdfconverter.terminalfile.message import error
# [i] Conversão
from pdfconverter.conversion.format import main, tablewithblankcells
# [i] Formatação de String
from pdfconverter.stringformat import stringformat


#region PUBLIC METHODS

def MakeFile(ReadingMethod):
    try:
        fvar.filepath_FullClear = fvar.folderpath_Result + "\\" + ReadingMethod + "\\fullClear\\" + fvar.filename_PDF + ".txt"
        # [>] Abre o arquivo principal (ainda não totalmente pronto pa-
        # ra ser jogado em uma tabela possui mais dados, porém estrutu-
        # ra ainda não tão idealizada)
        with open(fvar.filepath_FullClear, "a", encoding="UTF-8") as TextFile:
            # [>] Formata o arquivo e escreve um novo arquivo de saída
            TextFile.write(FormatTextFile(fvar.filepath_WithoutFormatting))
    except Exception as ExceptionError:
        error.Show("Ocorreu um erro desconhecido ao criar o arquivo com formatação 'fullclear'.", ExceptionError)

def FormatTextFile(TextFilePath):
    newString = ""
    # [i] Abre o arquivo original presente na pasta 'withoutFormat-
    # ting' para criar formatações baseadas nele
    with open(TextFilePath, "r", encoding="UTF-8") as TextFile:
        # [i] Navega por cada linha do documento de texto
        for line in TextFile:
            # [>] Realiza as formatações já existentes em tableWithBlankCells
            line = tablewithblankcells.FormatString(line)
            if line == ("" or None): continue
            # [>] Realiza as formatações já existentes em main
            line = main.FormatString(line)
            if line == ("" or None): continue
            # [>] Realiza a formatação do módulo vigente
            line = FormatString(line)
            if line == ("" or None): continue

            # [>] Adiciona à nova String
            newString += line
    # [>] Devolve pro método a nova String
    return newString

def FormatString(String):
    """Caso retorne None não escreve a linha, caso contrário retorna como uma variável normalmente."""

    # [>] Cria um novo objeto para manipular a String
    formatString = stringformat(String)

    # [>] Caso a linha não comece com aspas deleta
    formatString.LineNotStartsWithDoubleQuotes()
    
    # [>] Caso a linha não termine com aspas deleta
    formatString.LineNotEndsWithDoubleQuotes()

    # [>] Caso a linha tenha quebra de linha sem aspas duplas
    formatString.LineWithLinebreakOrWithoutDoubleQuote()
    
    # [i] Só escreve a linha se tiver pelo menos mais que 3 colunas
    # no arquivo fullClear
    if (formatString.Has3ColumnsOrMore()): return formatString.String

#endregion