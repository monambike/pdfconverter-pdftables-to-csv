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
from pdfconverter.__variables__ import cvar, fvar, ivar
# [i] Arquivo do Terminal
from pdfconverter.terminalfile.message import design, error
# [i] Projeto
from pdfconverter.settings import project
# [>] Conversão
from pdfconverter.conversion import withoutformatting
# [i] Formatações
from pdfconverter.conversion.format import main


#region PUBLIC METHODS

def Start():
    """
    ---
    ---
    ---
    
    ## Start (Private)
    ---
    ---
    Método que dá início à conversão.
    
    ---
    ---
    ---
    """

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
            project.SetFolderStructure()
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

            # [>] Caso a lista de DataFrames vier vazia
            if (len(cvar.list_DataFrames) <= 0):
                # [>] Dispara um erro no arquivo do terminal
                error.Show("Não foram encontradas tabelas para realizar a conversão.")

                # [>] Passa para o próximo arquivo sem continuar  os  processos
                # posteriores
                continue

            # [>] Limpa a lista de DataFrames removendo os DataFrames vazi-
            # os
            cvar.list_DataFrames = [DataFrame for DataFrame in cvar.list_DataFrames if not DataFrame.empty]

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
            pages = fvar.readPDFPages,                                 # [i] Páginas do arquivo PDF a serem lidas
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
            
            ExceptionError = ExceptionError
        )
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

#endregion