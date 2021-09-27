# [>] PDFConverter
from pdfconverter.stringformat import ManipulateString
# [i] Variáveis
from pdfconverter.__variables__ import fvar

def MakeFile(ReadingMethod):
    txtTableWithBlankCellsPath = fvar.folderpath_Export + fvar.rootPath + "\\" + ReadingMethod + "\\tableWithBlankCells\\" + fvar.filename_PDF + ".txt"

    # [i] Abre o arquivo original presente na pasta 'withoutFormat-
    # ting' para criar formatações baseadas nele
    with open(fvar.filepath_ExportTxt, "r", encoding="UTF-8") as txtFile:
        # [>] Abre o arquivo de texto "tableWithBlankCells"
        tableWithBlankCellsFile = open(txtTableWithBlankCellsPath, "a", encoding="UTF-8")

        # [i] Navega por cada linha do documento de texto
        for line in txtFile:
            # [>] Realiza a formatação atual do TableWithBlankCells, e caso
            # não  haja  nenhuma divergência
            line = Format(line)

            if line != "":
                # [e] Exporta a linha para a pasta: \\tableWithBlankCells
                tableWithBlankCellsFile.write(Format(line))
            
def Format(String):
    """Caso retorne None não escreve a linha, caso contrário retorna como uma variável normalmente."""

    formatString = ManipulateString(String)

    # [>] Detecta os dados vazios que estão presentes no  cabeçalho
    # "Unnamed: X;"
    formatString.EmptyHeader()

    # [>] Remove ponto e vírgula no final da linha
    formatString.EndLineSemicolon()
    
    # [>] Remove quebras de linha caso seja no meio dos  dados,  ou
    # seja, caso não possua '"' atrás da quebra de linha e as subs-
    # titui por um espaço para manter o padrão
    formatString.MiddleLineBreak(" ")

    # Condicional que impede o continuamento do processo caso a va-
    # riável esteja vazia, ou seja, caso tenha  sido  apagada  pelo
    # processo anterior de limpeza
    if (formatString.String == ""):
        return ""

    # [>] Remove ponto e vírgula no final da linha
    formatString.EndLineSemicolon()
    
    # [>] Remove todos os espaços no início de cada linha
    formatString.StartLineEmptySpace()

    # [i] Se a linha possui aspas duplas no início  e  no  final  e
    # ainda possui menos que duas colunas cancela o código
    if (formatString.IsSmallTable()):
        # [>] Não executa o código seguinte
        return ""

    return formatString.ReturnString()