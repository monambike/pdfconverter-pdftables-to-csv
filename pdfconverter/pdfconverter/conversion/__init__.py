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
from pdfconverter import patterncolumns
import tabula
from glob import glob
import os
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import cvar, fvar, ivar
# [i] Arquivo do Terminal
from pdfconverter.terminalfile.message import error
from pdfconverter.terminalfile.message import design
# [i]
from pdfconverter.settings import project
# [i]
from pdfconverter.conversion import withoutformatting
from pdfconverter.conversion.format import main, fullclear, tablewithblankcells


#region PUBLIC METHODS

def Start():
    # [>] Direciona o sistema para a pasta de importação
    os.chdir(fvar.folderpath_Import)
    # [>] Filtra pelos PDFs na pasta onde foi indicada para o  sis-
    # tema pelo "chdir"
    for filefullname_PDF in glob("*.pdf"):
        # [>] Configura o terminal ou o projeto de acordo com a  situa-
        # ção
        # [i] Se não é o primeiro arquivo
        if (ivar.PdfFile > 1):
            # [>] Fecha o layout pulando algumas linhas
            design.CloseLayout(LastLayout = False)
        # [i] Se é o primeiro arquivo ainda
        else:
            # [>] Define a estrutura inicial do projeto
            project.SetStructure()
        # [>] Atribuindo mais um ao índice para indicar  que  um  certo
        # arquivo PDF está sendo convertido
        ivar.PdfFile += 1

        # [>] Remove extensão do arquivo  (pegando  apenas  o  nome)  e
        # atribui para a variável
        fvar.filename_PDF = filefullname_PDF[:-4]

        # [>] Exibe o título ao terminal contendo o nome do  arquivo  e
        # outras informações complementares
        design.PDFTitle(filefullname_PDF)

        # MÉTODOS DE LEITURA E CONVERSÃO
        # -------------------------------------------------------------
        # Descrição:
        # Primeiro faz a leitura e conversão pra Lattice e após  faz  o
        # mesmo para o Stream
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        for ReadingMethod in ("lattice", "stream"):
            # [>] Realiza a leitura do arquivo PDF
            cvar.list_DataFrames = ReadPDF(ReadingMethod, filefullname_PDF)

            # [>] Limpa a lista de DataFrames removendo os DataFrames vazi-
            # os
            cvar.list_DataFrames = [DataFrame for DataFrame in cvar.list_DataFrames if not DataFrame.empty]

            # [>] Caso a lista de DataFrames vier vazia
            if (len(cvar.list_DataFrames) <= 0):
                # [>] Dispara um erro no arquivo do terminal
                error.Show("Não foram encontradas tabelas para realizar a conversão.")

                # [>] Passa para o próximo arquivo sem continuar  os  processos
                # posteriores
                continue


            # [>] Reseta a variável
            ivar.DataFrame = 1
            # [>] Itera os DataFrames contidos na lista de  DataFrames  gerados
            # pela leitura do tabula
            for TableDataFrame in cvar.list_DataFrames:
                # [>] Inicia a função que realiza a conversão com o método  in-
                # dicado
                withoutformatting.MakeFile(ReadingMethod, TableDataFrame)

                # [>] Avança o contador de DataFrames em um
                ivar.DataFrame += 1

            main.MakeFile(ReadingMethod)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------
    else:
        # [i] Se até o término da operação algum  PDF  foi  convertido
        if (ivar.PdfFile > 1):
            # [>] Fecha o layout do terminal
            design.CloseLayout(LastLayout = True)
        # [i] Se ainda até o término da operação nenhum PDF foi conver-
        # tido
        else:
            # [>] Exibe erro mostrando que não há arquivos para serem  con-
            # vertidos
            error.Show("Não há arquivos de PDF para serem convertidos.")

def ReadPDF(ReadingMethod, filefullname_PDF):
    """
    ---
    ---
    ---

    ### ReadPDF
    ---
    Realiza a leitura do PDF utilizando-se da biblioteca tabula com
    o método de leitura proveniente. Depois de  realizada,  retorna
    as tabelas reconhecidas para uma lista de DataFrames.

    Args:
        ReadingMethod ([str]): Tipo de leitura a ser realizada (Stream ou Lattice).
 
    ---
    ---
    ---
    """

    # LEITURA
    # -------------------------------------------------------------
    # Descrição:
    # Realiza a leitura.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    try:
        # [>] Realiza a leitura usando um método de  leitura  fornecido
        # pelo "For" e retorna uma lista de DataFrames
        return tabula.read_pdf(
            filefullname_PDF,
            guess = True,
            lattice = True if (ReadingMethod == "lattice") else False, # [>] Define como True caso o método de conversão  esteja  como
                                                                       # lattice, caso contrário define como False
            multiple_tables = True,
            pages = fvar.readPDFPages,
            pandas_options = {"dtype": "str"},
            silent = True
        )
    # [i] Quando ocorre um problema desconhecido na hora de  reali-
    # zar a leitura
    except Exception as ExceptionError:
        # [>] Exibe a mensagem de erro
        error.Show(
            "Arquivo: " + filefullname_PDF + "\n"
            "Método de Conversão: " + ReadingMethod + "\n"
            "\n"
            "Ocorreu um erro ao tentar realizar a leitura do arquivo '" + filefullname_PDF +  "' "
            "usando o método '" + ReadingMethod + "'.",
            
            ExceptionError = ExceptionError
        )
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

#endregion