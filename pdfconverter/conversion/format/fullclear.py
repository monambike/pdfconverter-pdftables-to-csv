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
# [i] Conversão
from pdfconverter.conversion.format import main, tablewithblankcells
# [i] Formatação de String
from pdfconverter.stringformat import stringformat


#region PUBLIC METHODS

def MakeFile(ReadingMethod):
    fvar.fullclear_OutputTxt = fvar.path_Export + fvar.rootPath + "\\" + ReadingMethod + "\\fullClear\\" + fvar.filename_PDF + ".txt"
    # [>] Abre o arquivo principal (ainda não totalmente pronto pa-
    # ra ser jogado em uma tabela possui mais dados, porém estrutu-
    # ra ainda não tão idealizada)
    with open(fvar.fullclear_OutputTxt, "a", encoding="UTF-8") as TextFile:
        # [>] Formata o arquivo e escreve um novo arquivo de saída
        TextFile.write(FormatTextFile(fvar.filepath_ExportTxt))

def FormatTextFile(TextFilePath):
    newString = ""
    # [i] Abre o arquivo original presente na pasta 'withoutFormat-
    # ting' para criar formatações baseadas nele
    with open(TextFilePath, "r", encoding="UTF-8") as TextFile:
        # [i] Navega por cada linha do documento de texto
        for line in TextFile:
            # [>] Realiza as formatações já existentes em tableWithBlankCells
            line = tablewithblankcells.FormatString(line)
            # [>] Realiza as formatações já existentes em main
            line = main.FormatString(line)
            # [>] Realiza a formatação do módulo vigente
            line = FormatString(line)

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
    if (formatString.IsSmallTable()): return ""
    
    return formatString.String

#endregion