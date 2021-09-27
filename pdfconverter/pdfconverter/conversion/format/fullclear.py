from pdfconverter.stringformat import ManipulateString
from pdfconverter.__variables__ import fvar
from pdfconverter.conversion.format import main, tablewithblankcells

def MakeFile(ReadingMethod):
    txtFullClearPath = fvar.folderpath_Export + fvar.rootPath + "\\" + ReadingMethod + "\\fullClear\\" + fvar.filename_PDF + ".txt"
    
    with open(fvar.filepath_ExportTxt, "r", encoding="UTF-8") as txtFile:
        # [>] Abre o arquivo principal (ainda não totalmente pronto pa-
        # ra ser jogado em uma tabela possui mais dados, porém estrutu-
        # ra ainda não tão idealizada)
        txtFullClearFile = open(txtFullClearPath, "a", encoding="UTF-8")

        # [i] Navega por cada linha do documento de texto
        for line in txtFile:
            # [>] Realiza as formatações já existentes em tableWithBlankCells
            line = tablewithblankcells.Format(line)
            # [>] Realiza as formatações já existentes em main
            line = main.Format(line)

            # [>] Realiza a formatação atual do Main, e caso não  haja  ne-
            # nhuma divergência
            line = Format(line)

            if line != "":
                # [e] Exporta a linha para a pasta: \\fullClear
                txtFullClearFile.write(line)

def Format(String):
    """Caso retorne None não escreve a linha, caso contrário retorna como uma variável normalmente."""

    # [i]
    formatString = ManipulateString(String)

    # [i]
    formatString.String = tablewithblankcells.Format(formatString.String)
    formatString.String = main.Format(formatString.String)

    # [>] Caso a linha não comece com aspas deleta
    formatString.LineNotStartsWithDoubleQuotes()
    
    # [>] Caso a linha não termine com aspas deleta
    formatString.LineNotEndsWithDoubleQuotes()

    formatString.LineWithLinebreakOrWithoutDoubleQuote()
    
    # [i] Só escreve a linha se tiver pelo menos mais que 3 colunas
    # no arquivo fullClear
    if (formatString.IsSmallTable()):
        return ""
    
    return formatString.String