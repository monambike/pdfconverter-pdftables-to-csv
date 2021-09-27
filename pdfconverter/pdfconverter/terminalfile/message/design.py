# [>] Geral
import pandas
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import fvar, ivar, vvar
# [i] Arquivo do Terminal
from pdfconverter.terminalfile import message


#region PUBLIC METHODS


def PDFTitle(filefullname_PDF):
    """Layout para exibição de conteúdo em forma de texto. \n\nRealiza a exibição do cabeçalho do PDF que está sendo lido. Necessário informar o nome do PDF para que o layout seja disponibilizado.

    Args:
        filefullname_PDF ([type]): [description]
    """

    # [>] Cria o título para leitura do arquivo no terminal
    message.Show(
        filefullname_PDF + vvar.GiantLine + "\n" +
        vvar.GiantLine + "\n\n\n\n" +
        vvar.BlankSpaces + "                          ----- + -----\n\n" +
        vvar.BlankSpaces + "         LEITURA DE ARQUIVO - NÚMERO " + str(ivar.PdfFile) + ", '" + filefullname_PDF + "'\n" +
        vvar.BlankSpaces + "   O arquivo '" + fvar.filename_PDF + "' foi lido e está pronto pra ser convertido\n\n" +
        vvar.BlankSpaces + "                          ----- + -----\n\n\n\n"
    )


def CloseLayout(LastLayout):
    """Fecha o leiaute referente ao arquivo anterior.
    """

    # [>] Design de fechamento de layout
    design = "\n" + vvar.GiantLine + "\n" + vvar.GiantLine

    # [>] Se não for o último layout do terminal coloca 10  espaços
    # para realizar a separação
    if (not LastLayout): design += "\n\n\n\n\n\n\n\n\n\n"

    # [>] Fecha o leiaute referente ao arquivo anterior
    message.Show(design)

def WithoutFormattingConversionTitle(ReadingMethod, TableDataFrame):
    message.Show(
            "\n\n"
            "          A tabela nº"+ str(ivar.DataFrame) + " do '" + fvar.filename_PDF + "' foi convertida usando '" + ReadingMethod + "'\n"
            "\________________________________________________________________________________/\n" +
            "Search this (Ctrl + F): '" + fvar.filename_PDF + " " + ReadingMethod + " tbl" + str(ivar.DataFrame) + "'\n"
            "\n" +
            str(pandas.DataFrame(TableDataFrame))
    )

#endregion