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

# - CAMINHOS
# Caminho atual
currentPath = ""
# Caminhos baseados no currentPath
pathOutputFile = ""
# Arquivo raíz exportado
txtFilePath = ""

# - ARQUIVOS DE SAÍDA
# Saída do Terminal
outputFile = ""

# - CONTADORES
# Índice do Data Frame
indexDataFrame = 0


# Linha gigante que vai ficar disposta em
# alguns lugares como divisão no terminal
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



# REGION
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÃO PRINCIPAL - INÍCIO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def Main():
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - GLOBAIS
    global fileName
    global indexDataFrame

    # - CONTADORES
    # Índice do arquivo
    indexFile = 1

    # ---------------------------------------------------------------------- #

    # >> CONFIGURAÇÕES INICIAIS <<
    setCurrentPath()
    pandaSetConfig()
    setProjectStructure()

    # Direciona o sistema para a pasta indicada
    chdir(currentPath + "\\PDFs")
    # Filtra pelos PDFs na onde foi indicado pro sistema
    for pdfFile in glob("*.pdf"):
        # Se já não é mais o primeiro arquivo
        if (indexFile > 1):
            # Fecha o leiaute
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

            # Abre o leiaute para o terminal
            setTerminalFile("open")
            print(
                pdfFile + strGiantLine + "\n" +
                strGiantLine + "\n\n\n\n"
                "                                              										                                                                                                    ----- + -----\n\n"
                "                                              							                                                                                                    	     LEITURA DE ARQUIVO - NÚMERO " + str(indexFile) + ", '" + pdfFile + "'\n"
                "                                              							                                                                                                    O arquivo '" + fileName + "' foi lido e está pronto pra ser convertido\n\n"
                "                                              										                                                                                                    ----- + -----\n\n\n\n",
                
                file = outputFile
            )
            setTerminalFile("closed")


            # >> MÉTODOS DE LEITURA E CONVERSÃO <<
            # Desc:
            # Primeiro faz a leitura e conversão pra Lattice e após faz o mesmo
            # para o Stream
            for method in range(2):
                # Lattice
                if (method == 0):
                    boolLattice = True
                    conversionMethod = "lattice"
                # Stream
                elif (method == 1):
                    boolLattice = False
                    conversionMethod = "stream"

                # >> LEITURA <<
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

                # >> CONVERSÃO <<
                # Desc:
                # Realizando a conversão com o método indicado
                indexDataFrame = 1
                for tableDataFrame in tableListOfDataFrames:
                    # Remove as aspas duplas do que estiverem no DataFrame para evitar possíveis erros,
                    # porque os dados normalmente são separados por pontos e vírgula e aspas duplas
                    tableDataFrame = tableDataFrame.replace("\"", "", regex = True)

                    conversionStart(conversionMethod, tableDataFrame)
                formatTextFile(conversionMethod)

            # Atribuindo mais um ao índice para indicar que os arquivos foram convertidos
            indexFile = indexFile + 1

        except Exception as err:
            showError("Ocorreu um erro ao tentar realizar a leitura do arquivo '" + pdfFile +  "'.", err)
            break 
    else:
        # Se até o término da operação algum PDF foi convertido, fecha o
        # leiaute do terminal
        if (indexFile > 1):
            # Fecha o leiaute e pula 5 linhas
            setTerminalFile("open")
            print(
                "\n" +
                strGiantLine + "\n" +
                strGiantLine,
            
                file = outputFile
            )
            setTerminalFile("closed")
        # Se até o término da operação nenhum PDF foi convertido ainda
        # exibe um erro
        else:
            showError("Não há arquivos de PDF para serem convertidos.", "")
            break

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÃO PRINCIPAL - FIM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# REGION
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CONFIGURAÇÕES INICIAIS - INÍCIO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >> DEFINE O LOCAL DA RAÍZ DO PROJETO <<
# Desc:
# Define o local da raíz do projeto, onde os outros caminhos irão se basear
def setCurrentPath():
    try:
        # ---------------------------------------------------------------------- #

        # >> VARIÁVEIS <<

        # - Globais
        global currentPath
        global pathOutputFile

        # ---------------------------------------------------------------------- #

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
        showError(
            "Não foi possível achar o diretório atual. Provável problema na hora de encurtar o "
            "caminho, verifique se o caminho passado na variável 'currentPath' dentro do método "
            "'setCurrentPath' está correto."
        
        , err)

# >> DEFINE A ESTRUTURA DE PASTAS DO PROJETO <<
# Desc:
# Faz a verificação da existência das pastas a seguir e as cria caso elas ainda não existam.
def setProjectStructure():
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - CAMINHOS
    # Raíz
    rootPaths = [
        "\\PDFs",
        "\\resultados"
    ]
    # Métodos de Leitura
    methodPaths = [
        "\\lattice",
        "\\stream"
    ]
    # Métodos de Formatação
    outputTypePaths = [
        "\\main",
        "\\fullClear",
        "\\tableWithBlankCells",
        "\\withoutFormatting"
    ]

    # ---------------------------------------------------------------------- #

    # Criando pastas raíz
    for rootPath in rootPaths:
        Path(
            currentPath +
            rootPath
        ).mkdir(parents = True, exist_ok = True)

        # Criando pastas para métodos de leitura dentro de resultados
        if (rootPath == "\\resultados"):
            for methodPath in methodPaths:
                Path(
                    currentPath +
                    rootPath +
                    methodPath
                ).mkdir(parents = True, exist_ok = True)
                # Criando pastas para métodos de formatação
                for outputTypePath in outputTypePaths:
                    Path(
                        currentPath +
                        rootPath +
                        methodPath +
                        outputTypePath
                    ).mkdir(parents = True, exist_ok = True)


    # Cria arquivo para exibir a saída do terminal,
    # se já existir o arquivo, limpa o mesmo
    outputClear = open(pathOutputFile, "w", encoding="UTF-8")
    outputClear.close()

# >> CONFIGURAÇÕES DO PANDAS <<
# Desc:
# Configurações do Pandas que afetam o DataFrame e a conversão para texto.
def pandaSetConfig():
    # Evita com que dados sejam quebrados no arquivo exportado
    pandas.options.display.max_colwidth = None
    # Evita com que os dados acabem sendo quebrados na saída do terminal
    pandas.options.display.expand_frame_repr = False
    # Define o padrão de codificação para UTF-8 com BOM
    pandas.options.display.encoding = "UTF-8-sig"
    # Fazer com que caso tenha um ';' ele não passe os dados pra outra célula
    pandas.options.display.latex.multicolumn = False

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CONFIGURAÇÕES INICIAIS - FIM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# REGION
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SAÍDAS DE AVISOS - INÍCIO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >> DEFINE O ESTADO DO TERMINAL <<
# Desc:
# Define quando o terminal vai ser aberto ou quando vai ser fechado.
def setTerminalFile(setState):
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - GLOBAIS
    global outputFile

    # ---------------------------------------------------------------------- #

    if (setState == "open"):
        outputFile = open(pathOutputFile, "a", encoding="UTF-8")
    elif (setState == "closed"):
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
    if (err != ""):
        print("EXCEPTION", file = outputFile)
        print(str(err), file = outputFile)
    
    # Fecha o layout
    print(
        "**********************************************************************",
        
        file = outputFile
    )
    outputFile.close()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SAÍDAS DE AVISOS - FIM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# REGION
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CONVERSÃO - INÍCIO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

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

    # Checando se a lista com o cabeçalho veio preenchida ou se o cabeçalho não possui
    # campos vazios
    if (tableDataFrameHeader and not "Unnamed" in tableDataFrameHeader[0]):
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
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - GLOBAIS
    global txtFilePath
    global indexDataFrame

    # ---------------------------------------------------------------------- #

    try:
        # Deleta todas as linhas que estão completamente vazias
        tableDataFrame = tableDataFrame.dropna(how="all")
        # Deleta todas as colunas que estão completamente vazias
        tableDataFrame = tableDataFrame.dropna(how="all", axis=1)

        turnHeaderInSimpleRow(tableDataFrame)
        
        # Removendo quebras de linha
        # O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
        # O segundo replace remove as que acontecem por conta do ponto e vírgula
        tableDataFrame = tableDataFrame.replace({r"\r": " "}, regex=True).replace({r";": ","}, regex=True)

        # Define o caminho do arquivo atual para a variável global txtFilePath
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
    
    # - GLOBAIS
    global txtFilePath

    # - CAMINHOS
    # Formatação padrão, apenas exibindo caso e caso tenha pelo menos um separados (;) na linha
    # e removendo campos vazios
    txtMainPath = currentPath + "\\resultados\\" + conversionMethod + "\\main\\" + fileName + ".txt"
    # Formatação padrão, porém mantendo campos vazios
    txtReturnBlankCellsPath = currentPath + "\\resultados\\" + conversionMethod + "\\tableWithBlankCells\\" + fileName + ".txt"
    # Full CLear
    txtFullClearPath = currentPath + "\\resultados\\" + conversionMethod + "\\fullClear\\" + fileName + ".txt"

    # - MANIPULAÇÃO DE LINHAS
    # ÚLTIMA LINHA
    # A variável recebe esse valor de início para indicar que ainda nenhum
    # arquivo passou pela verificação ainda
    # Isso deve ser desse jeito porque quando algum arquivo passa pela verificação
    # essa variável recebe vazio ("")
    lineLastHistory = "<thisMeansThatItHasNoValueYet>"

    # - EXPRESSÕES REGULARES (REGEX)
    # Detecta dados que estão vazios
    # Respectivamente detecta:
    # ;""
    # "";
    regexDetectEmptyDataInBody = re.compile(
        r"""
        (;\"\")|
        (\"\";)|
        """,

        re.VERBOSE|re.MULTILINE
    )
    # Remove todo ponto e vírgula presente no final da linha
    # Respectivamente detecta:
    # ; 
    detectFinalLineSemicolon = re.compile(r"((?<=\");(?!.))")
    
    # ---------------------------------------------------------------------- #

    # >> ABRINDO ARQUIVOS <<
    # Desc:
    # Abrindo os arquivos que serão utilizados depois na hora de realizar a exportação
    # com formatação.

    # - ARQUIVOS
    # Arquivo para caso a tabela possua itens vazios que precisam ser computados
    # (esse arquivo apenas não terá o 'regexDetectEmptyDataInBody' e similares)
    txtReturnBlankCellsFile = open(txtReturnBlankCellsPath, "a", encoding="UTF-8")
    # Arquivo principal, ainda não totalmente pronto para ser jogado em uma tabela
    # (possui mais dados, porém estrutura ainda não tão idealizada)
    txtMainFile = open(txtMainPath, "a", encoding="UTF-8")
    # O arquivo já pronto e estruturado para ser jogado em uma tabela
    # (alguns dados podem vir faltando)
    txtFullClearFile = open(txtFullClearPath, "a", encoding="UTF-8")

    # ---------------------------------------------------------------------- #

    # Abre o arquivo original presente na pasta 'withoutFormatting'
    # para criar formatações baseadas nele
    with open(txtFilePath, "r", encoding="UTF-8") as txtFile:
        # Navega por cada linha do documento de texto
        for lineCurrent in txtFile:
            # >> REMOVE LINHAS SEM ASPAS DUPLAS <<
            # Desc:
            # Linhas vazias que só possuem quebra de linha '\n' ou não possuem
            # uma aspas dupla no início OU final, serão excluídas 
            lineRemovedQuotes = ""
            lineRemovedQuotes = re.sub(r"\"", "", lineCurrent)                
            # Se essa permanece igual, ou seja, não teve aspas duplas removidas
            if (lineCurrent == lineRemovedQuotes):
                # Tá errada e vai ser apagada
                lineCurrent = ""

            # Condicional que impede o continuamento do processo caso a variável
            # esteja vazia, ou seja, caso tenha sido apagada pelo processo
            # anterior de limpeza
            if (lineCurrent != ""):
                    # FORMATAÇÃO (tableBlankCells)
                    # ---------------------------------------------------------------------- #

                    # Repete a formatação do arquivo duas vezes para garantir
                    # for formatFile in range(2):
                    # Detecta os dados vazios que estão presentes no cabeçalho
                    # "Unnamed: X;"
                    lineCurrent = re.sub(r"(\s?\"Unnamed:\s\d\d?\";?)", "", lineCurrent)

                    # Remove quebras de linha caso seja no meio dos dados,
                    # ou seja, caso não possua " atrás da quebra de linha
                    # e as substitui por um espaço para manter o padrão
                    lineCurrent = re.sub(r"((?<!\")\n)", " ", lineCurrent)

                    # Remove ponto e vírgula no final da linha
                    lineCurrent = detectFinalLineSemicolon.sub("", lineCurrent)
                  
                    # Só escreve a linha se tiver pelo menos mais que 2 colunas
                    # no arquivo fullClear
                    if (lineCurrent.count("\"") > 4
                        and lineCurrent.count(";") > 1):
                        # [ EXPORTAÇÃO ]
                        # Pasta: \\txtReturnBlankCellsFile  
                        txtReturnBlankCellsFile.write(lineCurrent)

                    # ---------------------------------------------------------------------- #


                    # FORMATAÇÃO (main)
                    # ---------------------------------------------------------------------- #

                    # Remove campos vazios no corpo
                    lineCurrent = regexDetectEmptyDataInBody.sub("", lineCurrent)
                    # Remove ponto e vírgula no final da linha novamente após tirar campos vazios
                    lineCurrent = detectFinalLineSemicolon.sub("", lineCurrent)

                    # Faz uma quebra de linha caso tenha duas aspas duplas uma do lado
                    # da outra
                    lineCurrent = re.sub(r"(?<=\")(?=\")", "\n", lineCurrent)
                    
                    # Remove todos os espaços no início de cada linha
                    lineCurrent = re.sub(r"(^\ *)", "", lineCurrent)

                    # Remove os dados caso tenha espaço entre os separadores e aspas
                    lineCurrent = re.sub(r"((.*\"; )(?=\"))", "", lineCurrent)

                    # Pega os dados que possuem espaços entre o separadores e uma aspas
                    # dupla e coloca uma quebra de linha
                    lineCurrent = re.sub(r"(;\ )", "\n", lineCurrent)

                    if (not lineCurrent.startswith('"') or
                        lineCurrent.startswith('"') and
                        ";" in lineCurrent
                        or lineCurrent == "\n"):
                        
                        # [ EXPORTAÇÃO ]
                        # Pasta: \\main
                        txtMainFile.write(lineCurrent)

                    # Coloca essa linha no histórico
                    lineLastHistory = lineCurrent

                    # ---------------------------------------------------------------------- #

        # Fecha os arquivos de exportação
        txtMainFile.close()
        txtReturnBlankCellsFile.close()

    # FORMATAÇÃO (fullCleaned)
    # ---------------------------------------------------------------------- #
    
    # Abre o arquivo principal presente na pasta 'main' para
    # criar formatações baseadas nele
    with open(txtMainPath, "r", encoding="UTF-8") as txtFile:
        # Navega por cada linha do documento de texto
        for lineCurrent in txtFile:
            # Caso a linha não comece com aspas deleta
            lineCurrent = re.sub(r"((^[^\"]).*)", "", lineCurrent)
            
            # Caso a linha não termine com aspas deleta
            lineCurrent = re.sub('"(.*([^"\n]$))', "", lineCurrent)

            # >> SEGUNDA VERIFICAÇÃO <<
            # Desc:
            # Linhas vazias que só possuem uma quebra de linha '\n' como conteúdo ou
            # não possuem uma aspas dupla no início ou no final (segunda verificação),
            # serão excluídas 
            # - Limpa variável
            lineRemovedQuotes = ""
            lineRemovedQuotes = re.sub(r"\"", "", lineCurrent)
                       
            # Se a temporária permanece igual, ou seja, não teve aspas duplas
            # removidas pelo regex
            if (lineCurrent == lineRemovedQuotes):
                # Quer dizer que ela ta errada e vai ser apagada
                lineCurrent = ""
            
            # Só escreve a linha se tiver pelo menos mais que 3 colunas
            # no arquivo fullClear
            if (lineCurrent.count("\"") > 6
                and lineCurrent.count(";") > 2):
                # [ EXPORTAÇÃO ]
                # Pasta: \\fullClear
                txtFullClearFile.write(lineCurrent)
        
        # Fecha os arquivos de exportação
        txtFullClearFile.close()
    
    # ---------------------------------------------------------------------- #

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CONVERSÃO - FIM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



Main()