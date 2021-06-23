import re
import csv
import pandas
import tabula
from os import chdir
from glob import glob
from pathlib import Path










# _____________________________________________________________





# LEGENDA
# -------------------------------------------------------------
# Descrição:
# Legenda que contém informações relacionadas à documentação do
# Script.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#region



# -------------------------------------------------------------


# Grupos:
# [C] - Conglomerado pequeno de variáveis 
# [F] - Função
# [G] - Grupo de funções (é delimitado por uma "region")
# [L] - Grupo que contém a legenda (é delimitado por uma "regi-
# on")
# [V] - Grupo  de  variáveis  (pode  ser  delimitado  por   uma
# "region" ou não)

# Dicas:
# [i] Informação ampla
# [>] Execução de uma tarefa ou uma  informação  relacionada  à
# ela


# -------------------------------------------------------------



#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------





# _____________________________________________________________










# _____________________________________________________________





# [V] VARIÁVEIS
# -------------------------------------------------------------
# Descrição:
# Grupo que contém todas as  variáveis  globais  utilizadas  no
# Script.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#region



# [C] NOMES
# -------------------------------------------------------------
# Descrição:
# Variáveis que possuem informações relacionadas à nomes de ar-
# quivos ou pastas.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Nome do arquivo PDF que vai ser convertido  (sem a exten-
# são)
fileName = ""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------


# [C] CAMINHOS
# -------------------------------------------------------------
# Descrição:
# Variáveis que armazenam caminhos.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Caminho atual para a raiz do projeto (os outros  caminhos
# vão se basear nele)
currentPath = ""
# [i] Caminho para o arquivo do terminal
txtOutputFilePath = ""
# [i] Caminho do arquivo PDF que vai ser convertido
txtFilePath = ""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------


# [C] ARQUIVOS
# -------------------------------------------------------------
# Descrição:
# Variáveis que manipulam arquivos.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Variável que armazena o arquivo de saída do Terminal
txtOutputFile = ""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------


# [C] CONTADORES
# -------------------------------------------------------------
# Descrição:
# Variáveis auxiliares que atuam como contadores.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Índice do 'For' que manipula o Data Frame
indexDataFrame = 0
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------


# [C] VISUAL
# -------------------------------------------------------------
# Descrição:
# Variáveis relacionadas ao visual de alguma parte do Script.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Linha gigante que vai ficar disposta  em  alguns  lugares
# como divisão no terminal
strGiantLine = (
    "_________________________________________"
    "_________________________________________"
    "_________________________________________"
    "_________________________________________"
    "_________________________________________"
    "_________________________________________"
    "_________________________________________"
    "_________________________________________"
    "_________________________________________"
    "_________________________________"
)
# [i] Variável que contém um espaço gigante usado em alguns la-
# youts
str150BlankSpaces = (
    "                                         "
    "                                         "
    "                                         "
    "                                         "
    "    "
)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------


# [C] OUTROS
# -------------------------------------------------------------
# Descrição:
# Variáveis que não se encaixam em outras categorias.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Variável que vai conter a lista de DataFrames de  um  de-
# terminado arquivo PDF baseado em um método de leitura,  pode-
# ndo ser lattice ou stream
tableListOfDataFrames = []
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------



#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------





# _____________________________________________________________










# _____________________________________________________________





# [G] FUNÇÃO PRINCIPAL
# -------------------------------------------------------------
# Descrição:
# Grupo que executa a função principal que faz operações  bási-
# cas realiza a chamada de outras funções.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#region

# [F] FUNÇÃO PRINCIPAL
# -------------------------------------------------------------
# Descrição:
# Função que executa funcionalidades principais e chama  outras
# funções
def Main():
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.



    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global fileName
    global indexDataFrame
    global tableListOfDataFrames
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    # [C] CONTADORES
    # -------------------------------------------------------------
    # Descrição:
    # Variáveis auxiliares que atuam como contadores.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # [i] Índice do 'For' que manipula os arquivos PDF
    indexFile = 1
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------



    # -------------------------------------------------------------



    # CONFIGURAÇÕES INICIAIS
    # -------------------------------------------------------------
    # Desc:
    # Contém todas as chamadas de funções que realizam as  configu-
    # rações iniciais para o funcionamento do Script.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    setCurrentPath()
    setPandasSettings()
    setProjectStructure()
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------



    # [>] Direciona o sistema para a pasta indicada
    chdir(currentPath + "\\PDFs")

    # [>] Filtra pelos PDFs na pasta onde foi indicada para o  sis-
    # tema pelo "chdir"
    for pdfFile in glob("*.pdf"):
        # [i] Se já não é mais o primeiro arquivo
        if (indexFile > 1):
            # [>] Fecha o leiaute referente ao arquivo anterior
            setTerminalFile("open")
            print(
                "\n" +
                strGiantLine + "\n" +
                strGiantLine + "\n"
                "\n\n\n\n\n\n\n\n\n"
            
                , file = txtOutputFile
            )
            setTerminalFile("closed")

        # [>] Remove extensão do arquivo  (pegando  apenas  o  nome)  e
        # atribui para a temporária
        fileName = pdfFile[:-4]

        # [>] Cria o título para leitura do arquivo no terminal
        setTerminalFile("open")
        print(
            pdfFile + strGiantLine + "\n" +
            strGiantLine + "\n\n\n\n"
            + str150BlankSpaces + "                          ----- + -----\n\n"
            + str150BlankSpaces + "         LEITURA DE ARQUIVO - NÚMERO " + str(indexFile) + ", '" + pdfFile + "'\n"
            + str150BlankSpaces + "   O arquivo '" + fileName + "' foi lido e está pronto pra ser convertido\n\n"
            + str150BlankSpaces + "                          ----- + -----\n\n\n\n"
            
            , file = txtOutputFile
        )
        setTerminalFile("closed")



        # MÉTODOS DE LEITURA E CONVERSÃO
        # -------------------------------------------------------------
        # Descrição:
        # Primeiro faz a leitura e conversão pra Lattice e após  faz  o
        # mesmo para o Stream
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        for method in range(2):
            # [i] Define o método de leitura Lattice
            if (method == 0):
                boolLattice = True
                conversionMethod = "lattice"
            # [i] Define o método de leitura Stream
            elif (method == 1):
                boolLattice = False
                conversionMethod = "stream"

            # LEITURA
            # -------------------------------------------------------------
            # Descrição:
            # Realiza a leitura.
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            try:
                # [>] Realiza a leitura usando um método de  leitura  fornecido
                # pelo "For"
                tableListOfDataFrames = tabula.read_pdf(
                    pdfFile,
                    guess = True,
                    lattice = boolLattice,
                    multiple_tables = True,
                    pages = "all",
                    pandas_options = {"dtype": "str"},
                    silent = True
                )
            except Exception as err:
                # [>] Exibe um erro quando ocorre um problema na hora de reali-
                # zar a leitura
                showError(
                    "Arquivo: " + pdfFile + "\n"
                    "Método de Conversão: " + conversionMethod + "\n"
                    "\n"
                    "Descrição: Ocorreu um erro ao tentar realizar a leitura do arquivo '" + pdfFile +  "' "
                    "usando o método '" + conversionMethod + "'."
                
                    , err
                )
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # -------------------------------------------------------------


            # CONVERSÃO
            # -------------------------------------------------------------
            # Descrição:
            # Realizando a conversão com o método indicado.
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # [>] Reseta a variável
            indexDataFrame = 1
            # [>] Itera os DataFrames contidos na lista de  DataFrames  gerados
            # pela leitura do tabula
            for tableDataFrame in tableListOfDataFrames:
                # [>] Remove as aspas duplas do que estiverem no DataFrame para
                # evitar possíveis erros pois os dados normalmente são  separa-
                # dos por pontos e vírgula e aspas duplas
                tableDataFrame = tableDataFrame.replace("\"", "", regex = True)

                # [>] Inicia a função que realiza a conversão com o método  in-
                # dicado
                conversionStart(conversionMethod, tableDataFrame)
            # [>] Chama a função que formata o arquivo de texto gerado pela
            # conversão
            formatTextFile(conversionMethod)
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # -------------------------------------------------------------
        # -------------------------------------------------------------
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        # [>] Atribuindo mais um ao índice para indicar que  o  arquivo
        # PDF foi convertido
        indexFile = indexFile + 1
    else:
        # [i] Se até o término da operação algum  PDF  foi  convertido,
        # fecha o leiaute do terminal
        if (indexFile > 1):
            # [>] Fecha o leiaute e pula 5 linhas
            setTerminalFile("open")
            print(
                "\n" +
                strGiantLine + "\n" +
                strGiantLine,
            
                file = txtOutputFile
            )
            setTerminalFile("closed")
        # [i] Se ainda até o término da operação nenhum PDF foi conver-
        # tido exibe um erro
        else:
            # [>] Exibe o erro
            showError("Descrição: Não há arquivos de PDF para serem convertidos.", "")
# -------------------------------------------------------------

#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------



# [G] CONFIGURAÇÕES INICIAIS
# -------------------------------------------------------------
# Descrição:
# Grupo que executa as configurações iniciais e ao decorrer  do
# exercício das tarefas do Script.
# Há funções com diversos objetivos, dentre eles,  encontrar  o
# caminho do arquivo de onde está sendo executado o Script, de-
# finir o caminho onde será utilizado para criar a estrutura de
# pastas, criar a estrutura de pastas onde serão  colocados  os
# arquivos PDF e onde serão gerados os arquivos  exportados
# e configurações adicionais da biblioteca Pandas
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#region

# [F] FUNÇÃO QUE DEFINE O LOCAL DA RAÍZ DO PROJETO
# -------------------------------------------------------------
# Descrição:
# Define o local da raíz do projeto, onde  os  outros  caminhos
# irão se basear
def setCurrentPath():
    try:
        # [V] VARIÁVEIS
        # -------------------------------------------------------------
        # Descrição:
        # Grupo contendo variáveis utilizadas na função atual.



        # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
        # -------------------------------------------------------------
        # Descrição:
        # Referenciamento de variáveis globais (suas  descrições  estão
        # no grupo de variáveis globais localizadas no escopo do início
        # do Script).
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        global currentPath
        global txtOutputFilePath
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------



        # -------------------------------------------------------------
        


        # [i] Pegando o caminho até o executável ou script atual  e  a-
        # tribuindo para a variável currentPath
        currentPath = Path(__file__).parent.absolute()
        #                           ____[o script está dentro da pasta 'netcoreapp3.1']
        #                          /
        # (pdfconverter\bin\Debug\netcoreapp3.1)

        # [i] Removendo caracteres até voltar para a localização à  se-
        # guir
        currentPath = str(currentPath)[:-37]
        # (pdfconverter\bin\Debug\netcoreapp3.1)
        #    \___[a diminuição de caracteres faz voltar  até  raiz da  pasta "pdfconverter"]

        # [>] Passa para a variável global o caminho do arquivo de tex-
        # to do terminal
        txtOutputFilePath = currentPath + "\\resultados\\output.txt"
    except Exception as err:
        # [>] Exibe um erro quando há problemas em achar o diretório a-
        # tual
        showError(
            "Descrição: Não foi possível achar o diretório atual. Prov"
            "ável problema na hora de encurtar o caminho, verifique se"
            " o caminho passado na variável 'currentPath' dentro do mé"
            "todo 'setCurrentPath' está correto."
        
            , err
        )
# -------------------------------------------------------------

# [F] FUNÇÃO QUE DEFINE A ESTRUTURA DE PASTAS DO PROJETO
# -------------------------------------------------------------
# Descrição:
# Faz a verificação da existência das pastas a seguir e as cria
# caso elas ainda não existam.
def setProjectStructure():    
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.



    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Listas que possuem os caminhos das pastas que vão  ser  gera-
    # das.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    # [C] CAMINHOS
    # [i] Caminhos que indicam a localização das  pastas  raíz  que
    # irão ser geradas futuramente.
    rootPaths = [
        "\\PDFs",
        "\\resultados"
    ]
    # [i] Caminhos que indicam a localização das pastas dos métodos
    # de leitura que vão ser geradas futuramente.
    methodPaths = [
        "\\lattice",
        "\\stream"
    ]
    # [i] Caminhos que indicam a localização das pastas dos métodos
    # de formatação que vão ser geradas futuramente.
    outputTypePaths = [
        "\\main",
        "\\fullClear",
        "\\tableWithBlankCells",
        "\\withoutFormatting"
    ]

    # ---------------------------------------------------------------------- #


    # [i] Para cada pasta raíz, presente na lista de pastas raíz
    for rootPath in rootPaths:
        # [>] Criando pastas raíz
        Path(
            currentPath +
            rootPath
        ).mkdir(parents = True, exist_ok = True)

        # [>] Dentro da pasta de resultados
        if (rootPath == "\\resultados"):
            # [i] Para cada método, presente na lista de métodos
            for methodPath in methodPaths:
                # [>] Cria uma pasta
                Path(
                    currentPath +
                    rootPath +
                    methodPath
                ).mkdir(parents = True, exist_ok = True)

                # [>] Criando pastas para métodos de formatação
                for outputTypePath in outputTypePaths:
                    Path(
                        currentPath +
                        rootPath +
                        methodPath +
                        outputTypePath
                    ).mkdir(parents = True, exist_ok = True)


    # [>] Cria arquivo para exibir a saída do terminal, se já exis-
    # tir o arquivo, limpa o mesmo
    open(txtOutputFilePath, "w").close()
# -------------------------------------------------------------

# [F] FUNÇÃO QUE DEFINE E EXECUTA CONFIGURAÇÕES DO PANDAS
# -------------------------------------------------------------
# Descrição:
# Configurações do Pandas que afetam o DataFrame e a  conversão
# para texto.
def setPandasSettings():
    # [>] Configuração que evita com que dados sejam  quebrados  no
    # arquivo exportado
    pandas.options.display.max_colwidth = None
    # [>] Configuração que evita com que os dados acabem sendo que-
    # brados na saída do terminal
    pandas.options.display.expand_frame_repr = False
    # [>] Configuração que define  o  padrão  de  codificação  para
    # UTF-8 com BOM
    pandas.options.display.encoding = "UTF-8-sig"
    # [>] Configuração que faz com que caso exista um ";"  ele  não
    # passe os dados pra outra célula
    pandas.options.display.latex.multicolumn = False
# -------------------------------------------------------------

#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------



# [G] SAÍDAS DE AVISOS
# -------------------------------------------------------------
# Descrição:
# Grupo o que contém funções que executam a exibição de  avisos
# relacionados ao arquivo que é gerado contendo informações que
# são mostradas no terminal.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#region

# [F] DEFINE O ESTADO DO TERMINAL
# -------------------------------------------------------------
# Descrição:
# Define quando o terminal vai ser aberto ou quando vai ser fe-
# chado.
def setTerminalFile(setState):
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.



    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global txtOutputFile
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



    # ---------------------------------------------------------------------- #



    # [i] Caso o programador defina a função como "open"
    if (setState == "open"):
        # [>] Abre o arquivo de saída do terminal com "append"
        txtOutputFile = open(txtOutputFilePath, "a", encoding="UTF-8")
    # [i] Caso o programador defina a função como "close"
    elif (setState == "closed"):
        # [>] Fecha o arquivo de saída do terminal
        txtOutputFile.close()
    #
    # [i] Caso o programador coloque um texto não tratado, exibe um
    # erro
    else:
        # [>] Exibe o erro
        showError(
            "O terminal só pode ser aberto ou fechado. Tenha certeza que "
            "atribuiu 'open' para aberto ou 'close' para fechado pro "
            "método 'terminal'."
        
            , ""
        )
        # [>] Fecha o aplicativo
        exit()
# -------------------------------------------------------------

# [F] EXIBE UMA MENSAGEM DE ERRO
# -------------------------------------------------------------
# Descrição:
# Função responsável por exibir mensagens de erros  disponíveis
# nas Exceptions.
def showError(errorMessage, err):
    # [>] Abre o layout com a mensagem e o arquivo
    txtOutputFile = open(txtOutputFilePath, "a", encoding="UTF-8")
    print(
        "======================================================================\n"
        "\n"
        "[ MENSAGEM ]\n"
        "\n"
        "ERRO\n"
        "\n" +
        errorMessage + "\n",
        
        file = txtOutputFile
    )

    # [i] Caso tenha uma exception ele exibe ela
    if (err != ""):
        # [>] Exibe a exception
        print(
            "\n"
            "Exception Log:"
            
            , file = txtOutputFile
        )
        print(str(err), file = txtOutputFile)
    
    # [>] Fecha o layout e o arquivo
    print(
        "\n"
        "======================================================================",
        
        file = txtOutputFile
    )
    txtOutputFile.close()
# -------------------------------------------------------------

#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------



# [G] CONVERSÃO
# -------------------------------------------------------------
# Descrição:
# Grupo que contém funções que realizam a conversão dos  arqui-
# vos PDF e toda a formatação necessária.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#region

# TORNANDO O CABEÇALHO EM UMA LINHA COMUM
# -------------------------------------------------------------
# Descrição:
# Isso é necessário para fazer com que não haja quebra de linha
# onde o DataFrame identifica como cabeçalho (título) da tabela
# caso o conteúdo delas seja muito grande.
# Isso acontece porque o título tem uma formatação gerada  pelo
# DataFrame que difere-se do corpo, o que acaba permitindo  que
# isso ocorra. O trabalho dessa função é transformar o  cabeça-
# lho em um texto de campo comum.
def turnHeaderInSimpleRow(tableDataFrame):
    # [>] Cria e limpa uma lista que vai ser usada para manipular o
    # cabeçalho no DataFrame
    tableDataFrameHeader = []

    # [>] Pegando o cabeçalho da tabela e passando ela  como  lista
    # para a temporária
    tableDataFrameHeader = [*tableDataFrame]

    # [i] Checando se a lista com o cabeçalho veio preenchida e  se
    # o cabeçalho não possui campos vazios
    if (tableDataFrameHeader and not "Unnamed" in tableDataFrameHeader[0]):
        # [>] Removendo o cabeçalho do DataFrame atual
        tableDataFrame = tableDataFrame.T.reset_index().T.reset_index(drop=True)

        # [>] Adicionando a lista como primeira linha do corpo do Data-
        # Frame temporário
        tableDataFrameHeader.insert(1, tableDataFrameHeader)

        # [>] Concatenando tabela temporária à tabela principal
        pandas.concat([pandas.DataFrame(tableDataFrameHeader), tableDataFrame], ignore_index=True)
# -------------------------------------------------------------

# [F] REALIZA A CONVERSÃO DO ARQUIVO
# -------------------------------------------------------------
# Descrição:
# Realiza a conversão do arquivo PDF para CSV como  arquivo  de
# texto.
def conversionStart(conversionMethod, tableDataFrame):
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.



    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global txtFilePath
    global indexDataFrame
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



    # ---------------------------------------------------------------------- #



    try:
        # [>] Deleta todas as linhas que estão completamente vazias
        tableDataFrame = tableDataFrame.dropna(how="all")
        
        # [>] Deleta todas as colunas que estão  completamente  va-
        # zias
        tableDataFrame = tableDataFrame.dropna(how="all", axis=1)

        # [>] Chama a função que transforma o cabeçalho em  uma li-
        # nha comum
        turnHeaderInSimpleRow(tableDataFrame)

        # [>] Remove quebras de linha do  DataFrame  que  acontecem
        # por conta do corpo ser muito grande
        tableDataFrame.replace({r"\r": " "}, inplace=True, regex=True)

        # [>] Troca ponto e vírgula dentro do DataFrame para evitar
        # conflitos
        tableDataFrame.replace({r";": ","}, inplace=True, regex=True)

        # [>] Define o caminho do arquivo  atual  para  a  variável
        # global txtFilePath
        txtFilePath = currentPath + "\\resultados\\" + conversionMethod + "\\withoutFormatting\\" + fileName + ".txt"

        # [>] Converte o arquivo para .txt no formato de um CSV
        tableDataFrame.to_csv(
            txtFilePath,
            index = False,
            index_label = False,
            header = True,
            line_terminator = "\n", # [i] Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
            mode = "a",
            sep = ";",
            quoting = csv.QUOTE_ALL
        )

        # [>] Indica ao terminal que uma tabela foi convertida  com
        # sucesso
        setTerminalFile("open")
        print(
            "\n\n"
            "          A tabela nº"+ str(indexDataFrame) + " do '" + fileName + "' foi convertida usando '" + conversionMethod + "'\n"
            "\________________________________________________________________________________/\n" +
            "Search this (Ctrl + F): '" + fileName + " " + conversionMethod + " tbl" + str(indexDataFrame) + "'\n"

            , file = txtOutputFile
        )

        # [>] Imprime o DataFrame
        print(pandas.DataFrame(tableDataFrame), file = txtOutputFile)
        setTerminalFile("closed")

        indexDataFrame = indexDataFrame + 1
    except Exception as err:
        showError(
            "Arquivo: " + fileName + "\n"
            "Método de Conversão: " + conversionMethod + "\n"
            "\n"
            "Descrição: Ocorreu um erro, ao tentar converter o "
            "arquivo '" + fileName + ".pdf' usando o "
            "método " + conversionMethod + "."
            
            , err
        )
        return
# -------------------------------------------------------------

# [F] LIMPA O ARQUIVO DE TEXTO CONVERTIDO
# -------------------------------------------------------------
# Descrição:
# Limpa o arquivo de texto removendo todas as  linhas  que  não
# contenham um separador (;), ou seja,  linhas  que  não  fazem
# parte de uma tabela.
def formatTextFile(conversionMethod):
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.



    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global txtFilePath
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    # [C] CAMINHOS
    # -------------------------------------------------------------
    # Descrição:
    # Variáveis que armazenam caminhos dos tipos de formatação.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # [i] Formatação padrão, apenas exibindo caso e caso  tenha pe-
    # lo menos um separador ";" na linha e removendo campos vazios
    txtMainPath = currentPath + "\\resultados\\" + conversionMethod + "\\main\\" + fileName + ".txt"
    # [i] Formatação padrão, porém mantendo campos vazios
    txtReturnBlankCellsPath = currentPath + "\\resultados\\" + conversionMethod + "\\tableWithBlankCells\\" + fileName + ".txt"
    # [i] Full Clear, formatação mais robusta
    txtFullClearPath = currentPath + "\\resultados\\" + conversionMethod + "\\fullClear\\" + fileName + ".txt"
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



    # -------------------------------------------------------------



    # [i] Abre o arquivo original presente na pasta 'withoutFormat-
    # ting' para criar formatações baseadas nele
    with open(txtFilePath, "r", encoding="UTF-8") as txtFile:
        # ARQUIVOS
        # -------------------------------------------------------------
        # Desc:
        # Arquivo para caso a tabela possua itens vazios  que  precisam
        # ser computados (esse arquivo apenas não terá o regex que apa-
        # ga dados vazios e similares)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # [>] Abre o arquivo de texto "tableWithBlankCells"
        txtTableWithBlankCells = open(txtReturnBlankCellsPath, "a", encoding="UTF-8")
        # [>] Abre o arquivo principal (ainda não totalmente pronto pa-
        # ra ser jogado em uma tabela possui mais dados, porém estrutu-
        # ra ainda não tão idealizada)
        txtMainFile = open(txtMainPath, "a", encoding="UTF-8")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------

        # [i] Navega por cada linha do documento de texto
        for lineCurrent in txtFile:
            # [>] Detecta os dados vazios que estão presentes no  cabeçalho
            # "Unnamed: X;"
            lineCurrent = re.sub(r"(\s?\"Unnamed:\s\d\d?\";?)", "", lineCurrent)

            # [>] Remove quebras de linha caso seja no meio dos  dados,  ou
            # seja, caso não possua '"' atrás da quebra de linha e as subs-
            # titui por um espaço para manter o padrão
            lineCurrent = re.sub(r"((?<!\")\n)", " ", lineCurrent)

            # Condicional que impede o continuamento do processo caso a va-
            # riável esteja vazia, ou seja, caso tenha  sido  apagada  pelo
            # processo anterior de limpeza
            if (lineCurrent != ""):
                # [>] Remove ponto e vírgula no final da linha
                lineCurrent = re.sub(r"((?<=\");(?!.))", "", lineCurrent)
                
                # [>] Remove todos os espaços no início de cada linha
                lineCurrent = re.sub(r"(^\ *)", "", lineCurrent)

                # [i] Se a linha possui aspas duplas no início  e  no  final  e
                # ainda possui menos que duas colunas cancela o código
                if (
                    (
                        (
                            lineCurrent.startswith("\"")
                        )
                        and 
                        (
                            lineCurrent.endswith("\"") or lineCurrent.endswith("\n")
                        )
                    )
                    and
                    (lineCurrent.count("\"") < 3 and lineCurrent.count(";") < 1)
                ):
                    # [>] Não executa o código seguinte
                    continue

                # [ EXPORTAÇÃO ]
                # Pasta: \\tableWithBlankCells  
                txtTableWithBlankCells.write(lineCurrent)
                
                # [>] Remove dados que estão vazios
                lineCurrent = re.sub(r"(;\"\")|(\"\";)", "", lineCurrent)

                # [>] Faz uma quebra de linha caso tenha aspas duplas  adjacen-
                # tes
                lineCurrent = re.sub(r"(?<=\")(?=\")", "\n", lineCurrent)

                # [>] Caso tenha um ponto e vírgula seguido de um espaço  troca
                # por uma quebra de linha
                lineCurrent = re.sub(r"((?<=\");\ )", "\n", lineCurrent)

                # [>] Caso tenha um espaço entre um separador e uma aspas dupla
                # remove o conteúdo que está atrás
                lineCurrent = re.sub(r"((.*\";\ )(?=\"))", "", lineCurrent)

                # [i] Se a linha possui aspas duplas no início  e  no  final  e
                # ainda possui menos que duas colunas cancela o código
                if (
                    (
                        (
                            lineCurrent.startswith("\"")
                        )
                        and 
                        (
                            lineCurrent.endswith("\"") or lineCurrent.endswith("\n")
                        )
                    )
                    and
                    (lineCurrent.count("\"") < 3 and lineCurrent.count(";") < 1)
                ):
                    # [>] Não executa o código seguinte
                    continue

                # [ EXPORTAÇÃO ]
                # Pasta: \\main
                txtMainFile.write(lineCurrent)
    
    # [>] Fecha o arquivo 'tableWithBlankCells'
    txtTableWithBlankCells.close()
    # [>] Fecha o arquivo 'main'
    txtMainFile.close()

    # [>] Abre o arquivo principal presente na  pasta  'main'  para
    # criar formatações baseadas nele
    with open(txtMainPath, "r", encoding="UTF-8") as txtFile:
        # [>] Abre o arquivo de texto para  realizar  a  exportação
        # fullClear
        txtFullClearFile = open(txtFullClearPath, "a", encoding="UTF-8")

        # [i] Navega por cada linha do documento de texto
        for lineCurrent in txtFile:
            # [>] Caso a linha não comece com aspas deleta
            lineCurrent = re.sub(r"((^[^\"]).*)", "", lineCurrent)
            
            # [>] Caso a linha não termine com aspas deleta
            lineCurrent = re.sub('"(.*([^"\n]$))', "", lineCurrent)

            # [>] Remove Linhas vazias que só possuem quebra de linha  '\n'
            # ou não possuem uma aspas dupla em nenhum lugar, serão excluí-
            # das 
            lineRemovedQuotes = ""
            lineRemovedQuotes = re.sub(r"\"", "", lineCurrent)

            # [i] Se a temporária permanece igual, ou seja, não teve  aspas
            # duplas removidas pelo regex
            if (lineCurrent == lineRemovedQuotes):
                # Quer dizer que ela ta errada e vai ser apagada
                lineCurrent = ""
            
            # [i] Só escreve a linha se tiver pelo menos mais que 3 colunas
            # no arquivo fullClear
            if (lineCurrent.count("\"") > 6 and
                lineCurrent.count(";") > 2):
                # [ EXPORTAÇÃO ]
                # Pasta: \\fullClear
                txtFullClearFile.write(lineCurrent)
# -------------------------------------------------------------

#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------





# _____________________________________________________________










# >>> Executa o Script
Main()