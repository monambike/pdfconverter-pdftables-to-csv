# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import fvar
# [i] Colunas no Padrão
from pdfconverter import patterncolumns
# [>] Conversão
from pdfconverter.conversion.format import tablewithblankcells
# [i] Formatação de String
from pdfconverter.stringformat import ManipulateString

def MakeFile(ReadingMethod):
    txtMainPath = fvar.folderpath_Export + fvar.rootPath + "\\" + ReadingMethod + "\\main\\" + fvar.filename_PDF + ".txt"
    
    with open(fvar.filepath_ExportTxt, "r", encoding="UTF-8") as txtFile:
        # [>] Abre o arquivo principal (ainda não totalmente pronto pa-
        # ra ser jogado em uma tabela possui mais dados, porém estrutu-
        # ra ainda não tão idealizada)
        txtMainFile = open(txtMainPath, "a", encoding="UTF-8")

        # [i] Navega por cada linha do documento de texto
        for line in txtFile:
            # [>] Realiza as formatações já existentes em tableWithBlankCells
            line = tablewithblankcells.Format(line)
            
            # [>] Realiza a formatação atual do Main, e caso não  haja  ne-
            # nhuma divergência
            line = Format(line)

            line = patterncolumns.SetHeaderToPattern(line)

            if line != "":
                # [e] Exporta a linha para a pasta: \\main
                txtMainFile.write(line)

def Format(String):
    """Caso retorne None não escreve a linha, caso contrário retorna como uma variável normalmente."""

    # [i]    
    formatString = ManipulateString(String)

    # [i]
    formatString.String = tablewithblankcells.Format(formatString.String)

    if (formatString.String == ""):
        return ""

    # [>] Remove dados que estão vazios
    formatString.EmptyBody()

    # [>] Faz uma quebra de linha caso tenha aspas duplas  adjacen-
    # tes
    formatString.DoubleQuotesAdjacent("\n")

    # [>] Caso tenha um ponto e vírgula seguido de um espaço  troca
    # por uma quebra de linha
    formatString.SemicolonAdjacentSpace("\n")

    # [>] Caso tenha um espaço entre um separador e uma aspas dupla
    # remove o conteúdo que está atrás
    formatString.SpaceBetweenSeparatorAndDoubleQuote()

    # [i] Se a linha possui aspas duplas no início  e  no  final  e
    # ainda possui menos que duas colunas cancela o código
    if (formatString.IsSmallTable()):
        # [>] Não executa o código seguinte
        return ""

    return formatString.ReturnString()