"""
---
---
---

## Package: pdfconverter >> conversion
---
---
### Module Name: withoutformatting
---
### path: "pdfconverter\\\\\\\\conversion\\\\\\\\withoutformatting.py"
---
---
Módulo com itens relacionados à geração do arquivo sem formatação.

---
---
---
"""


# [>] Geral
import csv
import pandas
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import fvar
# [i] Arquivo do Terminal
from pdfconverter.terminalfile.message import design, error


#region PUBLIC METHODS

def AppendToFile(ReadingMethod, TableDataFrame):
    """
    ---
    ---
    ---

    ### Start (Public)
    ---
    Inicia a conversão e gera um arquivo sem formatação.
    
    Args:
        ReadingMethod ([type]): Método de leitura.
        TableDataFrame ([type]): DataFrame atual para gerar o arquivo.
 
    ---
    ---
    ---
    """

    try:
        # [>] Chama a função que  realiza  algumas  formatações  no
        # DataFrame
        TableDataFrame = FormatDataFrame(TableDataFrame)

        # [>] Define o caminho do arquivo  atual  para  a  variável
        # global filepath_ExportTxt
        fvar.filepath_WithoutFormatting = fvar.folderpath_Result + "\\" +  ReadingMethod + "\\withoutFormatting\\" + fvar.filename_PDF + ".txt"

        # [>] Converte o arquivo para .txt no formato de um CSV
        TableDataFrame.to_csv(
            fvar.filepath_WithoutFormatting,
            index = False,
            index_label = False,
            header = False,
            line_terminator = "\n", # [i] Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
            mode = "a",
            sep = ";",
            quoting = csv.QUOTE_ALL
        )

        # [>] Indica ao terminal que uma tabela foi convertida  com
        # sucesso e imprime o DataFrame
        design.WithoutFormattingConversionTitle(ReadingMethod, TableDataFrame)
    # [>] Caso haja um erro desconhecido na hora de realizar a con-
    # versão
    except Exception as ExceptionError:
        # [>] Exibe uma mensagem de erro
        error.Show(
            "Arquivo: " + fvar.filename_PDF + "\n"
            "Método de Conversão: " + ReadingMethod + "\n"
            "\n"
            "Ocorreu um erro, ao tentar converter o "
            "arquivo '" + fvar.filename_PDF + ".pdf' usando o "
            "método " + ReadingMethod + ".",
            
            ExceptionError = ExceptionError,
            ExitProgram = False,
            RecreateTerminalFile = False
        )
        return

def FormatDataFrame(TableDataFrame):
    # [>] Remove as aspas duplas do que estiverem no DataFrame para
    # evitar possíveis erros pois os dados normalmente são  separa-
    # dos por pontos e vírgula e aspas duplas
    TableDataFrame = TableDataFrame.replace("\"", "", regex = True)
    # [>] Deleta todas as linhas que estão completamente vazias
    TableDataFrame = TableDataFrame.dropna(how="all")  
    # [>] Deleta todas as colunas que estão  completamente  va-
    # zias
    TableDataFrame = TableDataFrame.dropna(how="all", axis=1)

    # [>] Transforma o cabeçalho em uma linha comum
    TableDataFrame = __TurnHeaderInSimpleRow(TableDataFrame)

    # [>] Remove quebras de linha do  DataFrame  que  acontecem
    # por conta do corpo ser muito grande
    TableDataFrame.replace({r"\r": " "}, inplace=True, regex=True)
    # [>] Troca ponto e vírgula dentro do DataFrame para evitar
    # conflitos
    TableDataFrame.replace({r";": ","}, inplace=True, regex=True)

    return TableDataFrame

#endregion

#region PRIVATE METHODS

def __TurnHeaderInSimpleRow(TableDataFrame):
    """
    ---
    ---
    ---

    ### TurnHeaderInSimpleRow (Private)
    ---
    Transforma o cabeçalho do DataFrame em  uma  linha  comum  para
    padronizar a formatação.

    Args:
        TableDataFrame ([type]): [description]
 
    ---
    ---
    ---
    """

    # [>] Cria e limpa uma lista que vai ser usada para manipular o
    # cabeçalho no DataFrame
    TableDataFrameHeader = []

    # [>] Pegando o cabeçalho da tabela e passando ela  como  lista
    # para a temporária
    TableDataFrameHeader = [*TableDataFrame]

    # [i] Checando se a lista com o cabeçalho veio preenchida e  se
    # o cabeçalho não possui campos vazios
    if (TableDataFrameHeader and not "Unnamed" in TableDataFrameHeader[0]):
        # [>] Removendo o cabeçalho do DataFrame atual
        TableDataFrame = TableDataFrame.T.reset_index().T.reset_index(drop=True)

        # [>] Adicionando a lista como primeira linha do corpo do Data-
        # Frame temporário
        TableDataFrameHeader.insert(1, TableDataFrameHeader)

        # [>] Concatenando tabela temporária à tabela principal
        pandas.concat([pandas.DataFrame(TableDataFrameHeader), TableDataFrame], ignore_index=True)

    return TableDataFrame

#endregion