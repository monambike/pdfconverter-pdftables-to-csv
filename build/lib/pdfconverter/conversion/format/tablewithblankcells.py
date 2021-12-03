"""
---
---
---

## Package: pdfconverter >> conversion >> format
---
---
### Module Name: tablewithblankcells
---
### path: "pdfconverter\\\\\\\\conversion\\\\\\\\format\\\\\\\\tablewithblankcells.py"
---
---
Módulo relacionado à formatação TableWithBlankCells.

---
---
---
"""


# [>] PDFConverter
from pdfconverter.stringformat import stringformat
# [i] Arquivo do terminal
from pdfconverter.terminalfile.message import error
# [i] Variáveis
from pdfconverter.__variables__ import fvar


#region PUBLIC METHODS

def MakeFile(ReadingMethod):
    try:
        fvar.filepath_TableWithBlankCells = fvar.folderpath_Result + "\\" + ReadingMethod + "\\tableWithBlankCells\\" + fvar.filename_PDF + ".txt"
        # [>] Abre o arquivo de texto "tableWithBlankCells"
        with open(fvar.filepath_TableWithBlankCells, "a", encoding="UTF-8") as TextFile:
            # [>] Formata o arquivo e escreve um novo arquivo de saída
            TextFile.write(FormatTextFile(fvar.filepath_WithoutFormatting))
    except Exception as ExceptionError:
        error.Show("Ocorreu um erro desconhecido ao criar o arquivo com formatação 'tablewithblankcells'.", ExceptionError)
            
def FormatTextFile(TextFilePath):
    newString = ""
    # [i] Abre o arquivo original presente na pasta 'withoutFormat-
    # ting' para criar formatações baseadas nele
    with open(TextFilePath, "r", encoding="UTF-8") as TextFile:
        # [i] Navega por cada linha do documento de texto
        for line in TextFile:
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
    if (formatString.String == ""): return ""

    # [>] Remove ponto e vírgula no final da linha
    formatString.EndLineSemicolon()
    
    # [>] Remove todos os espaços no início de cada linha
    formatString.StartLineEmptySpace()

    # [i] Se a linha possui aspas duplas no início  e  no  final  e
    # ainda possui menos que duas colunas cancela o código
    if (formatString.IsSmallTable()): return ""

    return formatString.ReturnString()

#endregion