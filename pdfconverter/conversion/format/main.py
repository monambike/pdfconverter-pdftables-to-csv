"""
---
---
---

## Package: pdfconverter >> conversion >> format
---
---
### Module Name: main
---
### path: "pdfconverter\\\\\\\\conversion\\\\\\\\format\\\\\\\\main.py"
---
---
Módulo relacionado à formatação Main.

---
---
---
"""


# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import fvar
# [>] Conversão
from pdfconverter.conversion.format import tablewithblankcells
# [i] Formatação de String
from pdfconverter.stringformat import stringformat


#region PUBLIC METHODS

def MakeFile(ReadingMethod):
    """
    ---
    ---
    ---
    
    ## MakeFile (Public)
    ---
    ---
    Método gera o arquivo com as formatações  realizadas  referente
    ao módulo vigente.
    
    ### Args
    ---
    - ReadingMethod ([str]):
        - Método de leitura utilizado para fazer a geração do arquivo.
    
    ---
    ---
    ---
    """

    fvar.main_OutputTxt = fvar.path_Export + fvar.rootPath + "\\" + ReadingMethod + "\\main\\" + fvar.filename_PDF + ".txt"
    # [>] Abre o arquivo principal (ainda não totalmente pronto pa-
    # ra ser jogado em uma tabela possui mais dados, porém estrutu-
    # ra ainda não tão idealizada)
    with open(fvar.main_OutputTxt, "a", encoding="UTF-8") as TextFile:
        # [>] Formata o arquivo e escreve um novo arquivo de saída
        TextFile.write(FormatTextFile(fvar.filepath_ExportTxt))
    
def FormatTextFile(TextFilePath):
    """
    ---
    ---
    ---
    
    ## FormatStart (Public)
    ---
    ---
    Método faz todo esse processo para ficar mais fácil de  decidir
    quando será gerado um novo arquivo.
    
    ### Returns
    ---
        [str]: Nova String com as formatações realizadas do módulo presente.
    
    ---
    ---
    ---
    """
    
    newString = ""
    # [i] Abre o arquivo original presente na pasta 'withoutFormat-
    # ting' para criar formatações baseadas nele
    with open(TextFilePath, "r", encoding="UTF-8") as TextFile:
        # [i] Navega por cada linha do documento de texto
        for line in TextFile:
            # [>] Realiza as formatações já existentes em tableWithBlankCells
            line = tablewithblankcells.FormatString(line)
            # [>] Realiza a formatação do módulo vigente
            line = FormatString(line)

            # [>] Adiciona à nova String
            newString += line
    # [>] Devolve pro método a nova String                
    return newString

def FormatString(String):
    """
    ---
    ---
    ---
    
    ## FormatString (Public)
    ---
    ---
    Método que realiza a formatação de acordo com o módulo vigente.
    
    ### Args
    ---
    - String ([str]):
        - String que será utilizada para realizar a formatação.
    
    ### Returns
    ---
        [str]: Retorna a nova String formatada.
    
    ---
    ---
    ---
    """

    # [>] Cria um novo objeto para manipular a String
    formatString = stringformat(String)

    if (formatString.String == ""): return ""

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
    if (formatString.IsSmallTable()): return ""

    return formatString.ReturnString()

#endregion