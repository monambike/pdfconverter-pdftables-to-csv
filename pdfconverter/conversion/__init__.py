"""
---
---
---

## Package: pdfconverter >> conversion
---
---
### Module Name: conversion (Constructor, __init__)
---
### path: "pdfconverter\\\\\\\\conversion\\\\\\\\__init__.py"
---
---
Pacote e módulo comportando funções relacionadas à conversão.

---
---
---
"""


# [>] Geral
import os
import tabula
from glob import glob
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import avar, cvar, fvar
# [i] Arquivo do Terminal
from pdfconverter.terminalfile.message import design, error
# [i] Configurações
from pdfconverter.settings import project
# [i] Conversão
from pdfconverter.conversion import withoutformatting
from pdfconverter.conversion.format import tablewithblankcells, main, fullclear
# [i] Programa
from pdfconverter.program.exceptions import InvalidFormattingType, RepeatedFormattingType


#region PUBLIC METHODS

def IndividualConversion():
    # [>] Como a modalidade de conversão será  individual,  informa
    # que apenas um PDF será convertido
    fvar.quantity_ImportedFiles = 1

    # [>] Inicia a conversão
    ConversionStart(avar.path_ImportArg)
    
    # [>] Fecha o layout do terminal quando a conversão é finaliza-
    # da
    design.CloseLayout(LastLayout = True)

def MultipleConversion():
    # [>] Recebe um caminho que à frente será usado para obter  in-
    # formação referente à todos os arquivos PDFs presentes na pas-
    # ta de importação
    referencepath_AllPDFFiles = fvar.folderpath_Import + "\\*.pdf"

    # [>] Recebe a quantidade de arquivos que serão importados
    fvar.quantity_ImportedFiles = len(glob(referencepath_AllPDFFiles))

    # [>] Filtra pelos PDFs na pasta onde foi indicada para o  sis-
    # tema pelo "chdir"
    for PDF in glob(referencepath_AllPDFFiles):
        # [>] Inicia a conversão
        ConversionStart(PDF)
    else:
        # [i] Se até o término da operação algum  PDF  foi  convertido,
        # fecha o layout do terminal
        if (fvar.counter_PdfFile > 0): design.CloseLayout(LastLayout = True)
        # [i] Se ainda até o término da operação nenhum PDF foi conver-
        # tido, exibe erro mostrando que não  há  arquivos  para  serem
        # convertidos
        else: error.Show("Não há arquivos de PDF para serem convertidos.")

def ConversionStart(fullfilepath_PDF):
    """
    ---
    ---
    ---
    
    ## ConversionStart (Public)
    ---
    ---
    Método que realiza a conversão dado um caminho  de  um  arquivo
    PDF.
    Pode ser feita a escolha de um  método  de  formatação  e  caso
    feita, serão criadas as pastas e os arquivos  necessários  para
    # -------------------------------------------------------------
    gerar os arquivos.
    
    ### Args
    ---
    - fullfilepath_PDF ([str],):
        - Caminho do arquivo PDF que vai ser utilizado para realizar  a
        conversão.
    - Formatting (str, optional, default = ""):
        - Com esse parâmetro, é possível escolher um tipo de formatação
        para ser realizada.
        T = tableWithBlankCells
        M = Main
        F = FullClear
    
    ---
    ---
    ---
    """

    # [>] Recebe somente o nome completo do arquivo PDF dado o caminho de importação dele
    filefullname_PDF = os.path.basename(fullfilepath_PDF)

    # [>] Configura o terminal ou o projeto de acordo com a  situa-
    # ção
    # [i] Se não é o primeiro arquivo fecha o layout pulando  algu-
    # mas linhas
    if (fvar.counter_PdfFile >= 1): design.CloseLayout(LastLayout = False)
    # [i] Se é o primeiro arquivo ainda define a estrutura  inicial
    # do projeto
    else:
        project.SetFolderStructure()
        def MakeRelatoryFile():
            import json
            from pdfconverter.terminalfile import error


            # [>] Configura o caminho para o relatório
            fvar.filepath_RelatoryFile = fvar.folderpath_Result + "\\startreport.txt"


            try:
                with open(fvar.filepath_RelatoryFile, mode = "w", encoding = "UTF-8") as TextFile:
                    TextFile.write(
                        json.dumps(
                        {
                            "resultsFolder": {
                                "nameResultsFolder": fvar.foldername_Result,
                                "pathResultsFolder": fvar.folderpath_Result
                            },
                            "quantityImportedFiles": fvar.quantity_ImportedFiles,
                            "quantityExportedFiles": fvar.quantity_ExportedFiles
                        },
                        
                        indent = 4
                        )
                    )
            except Exception as ExceptionError:
                error.Show("Ocorreu um erro desconhecido ao tentar gerar o arquivo com as informações preliminares da conversão.", ExceptionError)
        MakeRelatoryFile()
    # [>] Atribuindo mais um ao índice para indicar  que  um  certo
    # arquivo PDF está sendo convertido
    fvar.counter_PdfFile += 1

    # [>] Remove extensão do arquivo  (pegando  apenas  o  nome)  e
    # atribui para a variável
    fvar.filename_PDF = filefullname_PDF[:-4]

    # [>] Exibe o título ao terminal contendo o nome do  arquivo  e
    # outras informações complementares
    design.PDFTitle(filefullname_PDF)

    # MÉTODOS DE LEITURA E CONVERSÃO
    # -------------------------------------------------------------
    # Descrição:
    # [i] Primeiro faz a leitura e conversão pra Lattice e após faz
    # o mesmo para o Stream
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    for ReadingMethod in ("lattice", "stream"):
        # [>] Realiza a leitura do arquivo PDF
        cvar.list_DataFrames = ReadPDF(ReadingMethod, fullfilepath_PDF)

        # [>] Caso a lista de DataFrames vier vazia
        if (cvar.list_DataFrames == None or len(cvar.list_DataFrames) <= 0):
            # [>] Dispara um erro no arquivo do terminal
            error.Show("Não foram encontradas tabelas para realizar a conversão.", ExitProgram = False, RecreateTerminalFile = False)
            # [>] Passa para o próximo arquivo sem continuar  os  processos
            # posteriores
            continue

        # [>] Limpa a lista de DataFrames removendo os DataFrames vazi-
        # os
        cvar.list_DataFrames = [DataFrame for DataFrame in cvar.list_DataFrames if not DataFrame.empty]

        # [>] Reseta a variável
        fvar.counter_DataFrame = 1
        # [>] Itera os DataFrames contidos na lista de  DataFrames  gerados
        # pela leitura do tabula
        for TableDataFrame in cvar.list_DataFrames:
            # [>] Inicia a função que realiza a conversão com o método  in-
            # dicado
            withoutformatting.AppendToFile(ReadingMethod, TableDataFrame)
            # [>] Avança o contador de DataFrames em um
            fvar.counter_DataFrame += 1
        # [>]
        __MakeFormattedFiles(ReadingMethod, avar.FormattingMethodArg)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

def ReadPDF(ReadingMethod, filefullname_PDF):
    """
    ---
    ---
    ---
    
    ## ReadPDF (Public)
    ---
    ---
    Método que realiza a leitura do PDF utilizando-se da biblioteca
    tabula com o método de leitura proveniente. Depois de  realiza-
    da, retorna as tabelas reconhecidas para uma lista de  DataFra-
    mes.
    
    ### Args
    ---
    - ReadingMethod ([str]):
        - Tipo de leitura a ser realizada pela biblioteca Tabula (Stream ou Lattice).
    - filefullname_PDF ([str]):
        - Caminho do arquivo PDF que vai ser lido.
    
    ### Returns
    ---
        [list]: Retorna uma lista  de  DataFrames  com  o  conteúdo  do
        arquivo PDF lido.
    
    ---
    ---
    ---
    """

    try:
        # [>] Realiza a leitura do arquivo PDF
        return tabula.read_pdf(
            # VALORES ALTERÁVEIS
            filefullname_PDF,                                          # [i] Caminho do arquivo PDF
            lattice = True if (ReadingMethod == "lattice") else False, # [>] Define como True caso o método de conversão  esteja  como
                                                                       # lattice, caso contrário define como False
            pages = avar.readPDFPagesArg,                              # [i] Páginas do arquivo PDF a serem lidas
            # VALORES PADRÃO
            guess = True,                                              # [i] Tenta adivinhar uma porção da página para ler
            multiple_tables = True,                                    # [i] Se o arquivo PDF tem mais de uma tabela
            pandas_options = {"dtype": "str"},                         # [i] Tipo de dados do DataFrame
            silent = True                                              # [i] Não exibe erros da biblioteca Tabula ao terminal, cmd
        )
    # [i] Quando ocorre um problema desconhecido na hora de  reali-
    # zar a leitura
    except Exception as ExceptionError:
        # [>] Exibe uma mensagem de erro
        error.Show(
            "Arquivo: " + filefullname_PDF + "\n"
            "Método de Conversão: " + ReadingMethod + "\n"
            "\n"
            "Ocorreu um erro ao tentar realizar a leitura do arquivo '" + filefullname_PDF +  "' "
            "usando o método '" + ReadingMethod + "'.",
            
            ExceptionError = ExceptionError,
            ExitProgram = False,
            RecreateTerminalFile = False
        )
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

#endregion

#region PRIVATE METHODS

def __MakeFormattedFiles(ReadingMethod, Formatting):
    try:
        for letter in Formatting:
            if (str(Formatting).count(letter)) > 1: raise RepeatedFormattingType

            if (letter == "T"): tablewithblankcells.MakeFile(ReadingMethod)
            elif (letter == "M"): main.MakeFile(ReadingMethod)
            elif (letter == "F"): fullclear.MakeFile(ReadingMethod)
            else: raise InvalidFormattingType
    except InvalidFormattingType as ExceptionError:
        error.Show("Ocorreu um erro na hora de realizar as formatações em 'ConversionStart()'.", ExceptionError)
    except RepeatedFormattingType as ExceptionError:
        error.Show("O tipo de formatação '" + letter + "' foi repetido mais de uma vez em '" + Formatting + "'.", ExceptionError)
    except Exception as ExceptionError:
        error.Show("Ocorreu um erro desconhecido ao tentar realizar as formatações requisitadas em 'ConversionStart()'.", ExceptionError)

#endregion