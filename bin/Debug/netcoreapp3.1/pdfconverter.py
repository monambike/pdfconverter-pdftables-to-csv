import re
import csv
import pandas
import tabula
from os import chdir
from glob import glob
from pathlib import Path
from PyPDF2 import PdfFileReader

# ---------------------------------------------------------------------- #

# >> VARIÁVEIS <<

# - NOMES DE ARQUIVOS -
# Nome do arquivo em PDF formatado sem a extensão
fileName = ""

# - ARQUIVOS DE SAÍDA -
# Saída do Terminal
outputFile = ""
# Saída do arquivo exportado
txtFilePath = ""

# - CAMINHOS -
# Caminho atual
currentPath = ""
# Caminhos baseados no currentPath
pathOutputFile = ""

# - CONTADORES -
# Índice do Data Frame
indexDataFrame = 0

strGiantLine = (
                    "_____________________________________________________________"
                    "_____________________________________________________________"
                    "_____________________________________________________________"
                    "_____________________________________________________________"
                    "_____________________________________________________________"
                    "_____________________________________________________________"
                    "____________________________________"
               )

# ---------------------------------------------------------------------- #



#    >>>>>>>>>> FUNÇÃO PRINCIPAL - INÍCIO <<<<<<<<<<

def Main():
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - GLOBAIS -
    global fileName
    global indexDataFrame

    # - CONTADORES -
    # Índice do arquivo
    indexFile = 1

    # ---------------------------------------------------------------------- #

    # - CONFIGURAÇÕES INICIAIS -
    setCurrentPath()
    pandaSetConfig()
    setProjectStructure()

    chdir(currentPath + "\\PDFs")
    # Filtra pelos PDFs
    for pdfFile in glob("*.pdf"):
        # Se já não é mais o primeira arquivo
        if indexFile > 1:
            # Fecha o leiaute e pula 5 linhas
            setTerminalFile("open")
            print(
                "\n" +
                strGiantLine + "\n" +
                strGiantLine + "\n"
                "\n\n\n\n\n\n\n\n\n",
            
                file = outputFile
            )
            setTerminalFile("closed")

        try:
            # Remove extensão do arquivo, pegando apenas o nome e atribui para a temporária
            fileName = pdfFile[:-4]

            # Pega o número de páginas que o PDF contém
            pdf = PdfFileReader(open(pdfFile, "rb"))
            pdfNumberOfPages = pdf.getNumPages()

            # - TERMINAL -
            setTerminalFile("open")
            print(
                pdfFile + strGiantLine + "\n" +
                strGiantLine + "\n\n\n\n"
                "                                              										----- + -----\n\n"
                "                                              								LEITURA DE ARQUIVO - NÚMERO " + str(indexFile) + ", '" + pdfFile + "'\n"
                "                                              							O arquivo '" + fileName + "' foi lido e está pronto pra ser convertido\n\n"
                "                                              										----- + -----\n\n\n\n",
                
                file = outputFile
            )
            setTerminalFile("closed")


            # - MÉTODOS DE LEITURA E CONVERSÃO -
            # Desc:
            # Primeiro faz a leitura e conversão pra Lattice e após faz o mesmo para o Stream
            # Legenda
            #  - boolLattice = True, em outras palavras, 0 é Lattice
            #  - boolLattice = False, em outras palavras, 1 é Stream
            for method in range(2):

                if method == 0:
                    boolLattice = True
                    conversionMethod = "lattice"
                elif method == 1:
                    boolLattice = False
                    conversionMethod = "stream"

                # - LEITURA -
                # Desc:
                # Fazendo leitura do arquivo completo e passando como lista de DataFrames
                # para a variável
                tableListOfDataFrames = tabula.read_pdf(
                    pdfFile,
                    guess = True,
                    multiple_tables = True,
                    pages = "all",
                    silent = True,
                    lattice = boolLattice,
                    pandas_options = {"dtype": "str"}
                )

                # - CONVERSÃO -
                # Desc:
                # Realizando a conversão com o método indicado
                indexDataFrame = 1
                for tableDataFrame in tableListOfDataFrames:
                    conversionStart(conversionMethod, tableDataFrame)
                formatTextFile(conversionMethod)

            # Atribuindo mais um ao índice para indicar que os arquivos foram convertidos
            indexFile = indexFile + 1

        except Exception as err:
            showError("Ocorreu um erro ao tentar realizar a leitura do arquivo '" + pdfFile +  "'.", err)
            break 
    else:
        showError("Não há arquivos de PDF para serem convertidos.", "")

#    >>>>>>>>>> FUNÇÃO PRINCIPAL - FIM <<<<<<<<<<



#    >>>>>>>>>> CONFIGURAÇÕES INICIAIS - INÍCIO <<<<<<<<<<

# >> DEFINE O LOCAL DA RAÍZ DO PROJETO <<
# Desc:
# Define o local da raíz do projeto, onde os outros caminhos irão se basear
def setCurrentPath():
    try:
        global currentPath
        global pathOutputFile

        # Pegando o caminho até o executável ou script atual e atribuindo para a variável currentPath
        currentPath = Path(__file__).parent.absolute()
        #                           ____[o script está dentro da pasta 'netcoreapp3.1']
        #                          /
        # (pdfconverter\bin\Debug\netcoreapp3.1)

        # Removendo caracteres até voltar para a localização à seguir
        currentPath = str(currentPath)[:-37]
        # (pdfconverter\bin\Debug\netcoreapp3.1)
        #    \___[a diminuição de caracteres faz voltar até a pasta 'pdfconverter']

        pathOutputFile = currentPath + "\\resultados\\output.txt"
    except Exception as err:
        showError("Não foi possível achar o diretório atual. Provável problema na hora de encurtar "
        "o caminho, verifique se o caminho passado na variável 'currentPath' dentro do método "
        "'setCurrentPath' está correto.", err)

# >> DEFINE A ESTRUTURA DE PASTAS DO PROJETO <<
# Desc:
# Faz a verificação da existência das pastas a seguir e as cria caso elas ainda não existam.
def setProjectStructure():
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - CAMINHOS -
    # Pastas Raíz
    rootPaths = [
        "\\PDFs",
        "\\resultados"
    ]
    # Métodos
    methodPaths = [
        "\\lattice",
        "\\stream"
    ]
    # Tipos de Saída
    outputTypePaths = [
        "\\main",
        "\\tableWithBlankCells",
        "\\withoutFormatting"
    ]

    # ---------------------------------------------------------------------- #

    for rootPath in rootPaths:
        Path(
            currentPath +
            rootPath
        ).mkdir(parents = True, exist_ok = True)

        if rootPath == "\\resultados":
            for methodPath in methodPaths:
                Path(
                    currentPath +
                    rootPath +
                    methodPath
                ).mkdir(parents = True, exist_ok = True)

                for outputTypePath in outputTypePaths:
                    Path(
                        currentPath +
                        rootPath +
                        methodPath +
                        outputTypePath
                    ).mkdir(parents = True, exist_ok = True)


    # Cria arquivo para exibir a saída do terminal, se já tiver limpa
    outputClear = open(pathOutputFile, "w", encoding="UTF-8")
    outputClear.close()

# >> CONFIGURAÇÕES DO PANDAS <<
# Desc:
# Configurações do Pandas que afetam o DataFrame e a conversão para texto.
def pandaSetConfig():
    # Evita com que os dados acabem sendo quebrados na saída do terminal e no arquivo exportado
    pandas.options.display.max_colwidth = None
    pandas.options.display.expand_frame_repr = False

    # Define o padrão de codificação para UTF-8 com BOM
    pandas.options.display.encoding = "UTF-8-sig"
    
    # Mostra o dia primeiro quando encontrar data
    pandas.options.display.date_dayfirst = True
    
    # Fazer com que caso tenha um ';' ele não passe os dados pra outra célula
    pandas.options.display.latex.multicolumn = False

#    >>>>>>>>>> CONFIGURAÇÕES INICIAIS - FIM <<<<<<<<<<



# >>>>>>>>>> SAÍDAS DE AVISOS - INÍCIO <<<<<<<<<<

# >> DEFINE O ESTADO DO TERMINAL <<
# Desc:
# Define quando o terminal vai ser aberto ou quando vai ser fechado.
def setTerminalFile(setState):
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - GLOBAIS -
    global outputFile

    # ---------------------------------------------------------------------- #

    if setState == "open":
        outputFile = open(pathOutputFile, "a", encoding="UTF-8")
    elif setState == "closed":
        outputFile.close()
    else:
        showError("O terminal só pode ser aberto ou fechado. Tenha certeza que atribuiu 'open' para aberto ou 'close' para fechado pro método 'terminal'.", "")
        exit()

# >> EXIBE UMA MENSAGEM DE ERRO <<
# Desc:
# Função responsável por exibir mensagens de erros disponíveis nas Exceptions.
def showError(errorMessage, err):
    # Limpa o terminal para exibir melhor o erro
    open(pathOutputFile, "w").close()

    outputFile = open(pathOutputFile, "a", encoding="UTF-8")
    print(
        "**********************************************************************\n"
        "--- MENSAGEM ---\n"
        "\n"
        "ERRO\n"
        "Descrição: " + errorMessage + "\n",
        
        file = outputFile
    )

    # Caso tenha uma exception, ele exibe
    if err != "":
        print("EXCEPTION", file = outputFile)
        print(str(err), file = outputFile)
    
    # Fecha o layout e o arquivo
    print(
        "**********************************************************************",
        
        file = outputFile
    )
    outputFile.close()

# >>>>>>>>>> SAÍDAS DE AVISOS - FIM <<<<<<<<<<



# >>>>>>>>>> CONVERSÃO - INÍCIO <<<<<<<<<<

# >> FAZENDO COM QUE O CABEÇALHO SE TORNE UMA LINHA COMUM <<
# Desc:
# Isso é necessário para fazer com que não haja quebra de linha onde o DataFrame identifica
# como cabeçalho (título) da tabela caso o conteúdo delas seja muito grande.
# Isso acontece porque o título tem uma formatação gerada pelo DataFrame que difere-se do corpo,
# o que acaba permitindo que isso ocorra.
def turnHeaderInSimpleRow(tableDataFrame):
    # Limpa a lista que vai ser usada para manipular o cabeçalho no DataFrame
    tableDataFrameHeader = []

    # Pegando o cabeçalho da tabela e passando ela como lista para a temporária
    tableDataFrameHeader = [*tableDataFrame]

    # Checando se a lista veio vazia ou se o cabeçalho possui campos vazios
    if tableDataFrameHeader and not "Unnamed" in tableDataFrameHeader[0]:
        # Removendo o cabeçalho do DataFrame atual
        tableDataFrame = tableDataFrame.T.reset_index().T.reset_index(drop=True)


        # Adicionando a lista como primeira linha do DataFrame temporário
        tableDataFrameHeader.insert(1, tableDataFrameHeader)

        # Concatenando tabela temporária à tabela principal
        pandas.concat([pandas.DataFrame(tableDataFrameHeader), tableDataFrame], ignore_index=True)

# >> REALIZA A CONVERSÃO DO ARQUIVO <<
# Desc:
# Realiza a conversão do arquivo PDF para texto.
def conversionStart(conversionMethod, tableDataFrame):
    global txtFilePath
    global indexDataFrame

    try:
        # Deleta todas as linhas que estão completamente vazias
        tableDataFrame = tableDataFrame.dropna(how="all")
        # Deleta todas as colunas que estão completamente vazias
        tableDataFrame = tableDataFrame.dropna(how="all", axis=1)

        turnHeaderInSimpleRow(tableDataFrame)

        # Transforma todo o conteúdo do DataFrame em string
        #tableDataFrame = tableDataFrame.astype(str)
        
        # TESTE
        #verifyCellsValue(tableDataFrame)
        
        # Removendo quebras de linha
        # O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
        # O segundo replace remove as que acontecem por conta do ponto e vírgula
        tableDataFrame = tableDataFrame.replace({r"\r": " "}, regex=True).replace({r";": ","}, regex=True)

        txtFilePath = currentPath + "\\resultados\\" + conversionMethod + "\\withoutFormatting\\" + fileName + ".txt"
        
        # Converte para .txt no formato de um CSV
        tableDataFrame.to_csv(
            txtFilePath,
            index = False,
            index_label = False,
            header = True,
            line_terminator = "\n", # Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
            mode = "a",
            sep = ";",
            quoting = csv.QUOTE_ALL
        )

        # Indica ao terminal que uma tabela foi convertida com sucesso
        setTerminalFile("open")
        print(
            "\n\n"
            "          A tabela nº"+ str(indexDataFrame) + " do '" + fileName + "' foi convertida usando '" + conversionMethod + "'\n"
            "\________________________________________________________________________________/\n" +
            "Search this (Ctrl + F): '" + fileName + " " + conversionMethod + " tbl" + str(indexDataFrame) + "'\n",

            file = outputFile
        )
        # Imprime o DataFrame
        print(pandas.DataFrame(tableDataFrame), file = outputFile)
        setTerminalFile("closed")

        indexDataFrame = indexDataFrame + 1
    except Exception as err:
        showError("Ocorreu um erro, ao tentar converter o arquivo '" + fileName + ".pdf' usando o método " + conversionMethod + ".", err)

        return

# >> LIMPA O ARQUIVO DE TEXTO CONVERTIDO <<
# Desc:
# Limpa o arquivo de texto removendo todas as linhas que não contenham um
# separador (;), ou seja, linhas que não fazem parte de uma tabela.
def formatTextFile(conversionMethod):
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - GLOBAIS -
    global txtFilePath

    # - EXPRESSÕES REGULARES -
    # Procura no geral por similares à 'Unnamed: 1;' e '"";'
    #reReturnBlankCells = "(\s?\"Unnamed:\s\d\d?\";?)|(;\"\")|(\"\";)|((?<=\");(?!.))|((?<!\")\n)"
    # Retorna todos os ponto e vírgula que estão no final da linha
    #reReturnAllLineEndingSemicolon = ""
    # Procura por quebras de linha inadequadas (quebras que ocorrem no meio dos dados)
    #reReturnWrongLineBreaks = ""

    # - CAMINHOS -
    # Formatação padrão, apenas exibindo caso e caso tenha pelo menos um separados (;) na linha
    # e removendo campos vazios
    txtMainPath = currentPath + "\\resultados\\" + conversionMethod + "\\main\\" + fileName + ".txt"
    # Formatação padrão, porém mantendo campos vazios
    txtReturnBlankCellsPath = currentPath + "\\resultados\\" + conversionMethod + "\\tableWithBlankCells\\" + fileName + ".txt"

    # ---------------------------------------------------------------------- #
    
    # - RESULTADO -
    # Desc:
    # Novos arquivos gerados com a limpeza
    # Arquivo principal, com toda a limpeza definida
    txtMainFile = open(txtMainPath, "a", encoding="UTF-8")
    # Arquivo para caso a tabela tenha itens vazios que precisam ser computados
    txtReturnBlankCellsFile = open(txtReturnBlankCellsPath, "a", encoding="UTF-8")

    regexSearch = re.compile(
        r"""

        (\s?\"Unnamed:\s\d\d?\";?)| # Remove os Unnamed
        (;\"\")|                    # Remove (;"")
        (\"\";)|                    # Remove ("";)
        ((?<=\");(?!.))|            # Remove pontos e vírgulas que estão no final da linha
        ((?<!\")\n)                # Remove quebras de linha caso seja no meio dos dados,
                                    # ou seja, caso não possua " atrás da quebra de linha

        """,
        
        re.VERBOSE|re.MULTILINE
    )

    # Abre o arquivo original
    with open(txtFilePath, "r", encoding="UTF-8") as txtDoc:
        # Navega por cada linha do documento de texto
        for line in txtDoc:
            # Se a linha não começa com '"' (indicando que o dado
            # foi quebrado na metade) ou caso a linha possua ponto
            # e vírgula também escreve
            if not line.startswith('"') or line.startswith('"') and ";" in line or line != "\n":
                txtReturnBlankCellsFile.write(line)

                # Repete a limpeza duas vezes para garantir
                for i in range(2):
                    # Substitui por nada os itens que ele encontrar com regexSearch
                    line = regexSearch.sub("", line)

                if not line.startswith('"') or line.startswith('"') and ";" in line or line == "\n":
                    txtMainFile.write(line)

    txtMainFile.close()
    txtReturnBlankCellsFile.close()

# >>>>>>>>>> CONVERSÃO - FIM <<<<<<<<<<



Main()