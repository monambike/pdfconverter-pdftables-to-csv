# Bibliotecas
# _____________________________________________________________
import os
import re
import csv
import pandas
import tabula
import argparse
from glob import glob
from pathlib import Path
# _____________________________________________________________





# Sumário
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
# -------------------------------------------------------------
# [C] - Conglomerado pequeno de variáveis 
# [F] - Função
# [G] - Grupo de funções (é delimitado por uma "region")
# [L] - Grupo que contém a legenda (é delimitado por uma "regi-
# on")
# [V] - Grupo  de  variáveis  (pode  ser  delimitado  por   uma
# "region" ou não)
# -------------------------------------------------------------
#
# -------------------------------------------------------------
# Dicas:
# -------------------------------------------------------------
# [i] - Informação ampla
# [>] - Execução de uma tarefa ou uma informação relacionada  à
# ela
# [e] - Exportação de um arquivo PDF convertido para CSV
# -------------------------------------------------------------

#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# _____________________________________________________________





# Escopo
# _____________________________________________________________

# [V] VARIÁVEIS
# -------------------------------------------------------------
# Descrição:
# Grupo que contém todas as  variáveis  globais  utilizadas  no
# Script.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#region

# [C] ARQUIVOS
# -------------------------------------------------------------
# Descrição:
# Variáveis que armazenam possuem realações com arquivos direta
# e indiretamente.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Nome do arquivo PDF que vai ser convertido  (sem a exten-
# são)
str_fileName = ""
# [i] Caminho atual para a raiz do projeto (os outros  caminhos
# vão se basear nele)
folderPath_script = ""
# [i] Caminho para o arquivo do terminal
filePath_outputTxt = ""
# [i] Caminho do arquivo PDF que vai ser convertido
filePath_exportTxt = ""
# [i] Variável que armazena o arquivo de saída do Terminal
file_outputTxt = ""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [C] CONTADORES
# -------------------------------------------------------------
# Descrição:
# Variáveis auxiliares que atuam como contadores.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Índice do 'For' que manipula o Data Frame
index_dataFrame = 0
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [C] VISUAL DO TERMINAL
# -------------------------------------------------------------
# Descrição:
# Variáveis relacionadas ao visual de alguma parte  do  Script,
# normalmente essas partes visuais estão diretamente relaciona-
# das com a saída do terminal.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Linha gigante que vai ficar disposta  em  alguns  lugares
# como divisão no terminal
visual_giantLine = (
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
visual_blankSpaces = (
    "                                         "
    "                                         "
    "                                         "
    "                                         "
    "    "
)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [C] ARGUMENTOS
# -------------------------------------------------------------
# Descrição:
# Variáveis relacionadas à alguma ação ou função relacionada  à
# argumentos
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Variável que vai ser responsável por criar o parser.
parser_main = None
# [i] Variável que vai ser responsável por fazer a  manipulação
# dos argumentos dados.
parserArgs_main = None
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [C] LISTAS
# -------------------------------------------------------------
# Descrição:
# Variáveis que fazem gerenciamento de listas.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [i] Variável que vai conter a lista de DataFrames de  um  de-
# terminado arquivo PDF baseado em um método de leitura,  pode-
# ndo ser lattice ou stream
list_dataFrames = []
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# _____________________________________________________________





# Funções
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def Main():
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global str_fileName
    global index_dataFrame
    global list_dataFrames
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # [C] CONTADORES
    # -------------------------------------------------------------
    # Descrição:
    # Variáveis auxiliares que atuam como contadores.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # [i] Índice do 'For' que manipula os arquivos PDF
    index_file = 1
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    # CONFIGURAÇÕES INICIAIS
    # -------------------------------------------------------------
    # Descrição:
    # Contém todas as chamadas de funções que realizam as  configu-
    # rações iniciais para o funcionamento do Script.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    setCurrentPath()
    setPandasSettings()
    setProjectStructure()
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    # Cria o parser para manipular os argumentos
    createParser()


    # VALIDAÇÃO PASTAS DE IMPORTAÇÃO E EXPORTAÇÃO
    # -------------------------------------------------------------
    # Descrição:
    # Faz a validação da existência pastas de importação (obrigató-
    # rio) e  exportação (opcional) providenciadas através de argu-
    # mentos.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    setTerminalFileAsOpen(True)
    # [i] [Obrigatório] Caso a pasta de importação não exista
    if(not checkIfFolderExists(parserArgs_main.importPath)):
        # [>] Exibe uma mensagem de erro
        print(
            "O caminho de importação informado não existe.",

            file = file_outputTxt
        )
        # [>] E para a aplicação
        return
    # [i] [Opcional] Caso o usuário tenha fornecido  o  caminho  da
    # pasta de exportação e caso a pasta de exportação não exista
    if((parserArgs_main.exportPath != None) and (checkIfFolderExists(parserArgs_main.exportPath))):
        # [>] Exibe uma mensagem de erro
        print(
            "O caminho de exportação informado não existe.",
            
            file = file_outputTxt
        )
        # [>] E para a aplicação
        return
    setTerminalFileAsOpen(False)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # [>] Direciona o sistema para a pasta indicada
    os.chdir(folderPath_script + "\\PDFs")
    # [>] Filtra pelos PDFs na pasta onde foi indicada para o  sis-
    # tema pelo "chdir"
    for pdfFile in glob("*.pdf"):
        # [i] Se já não é mais o primeiro arquivo
        if (index_file > 1):
            # [>] Fecha o leiaute referente ao arquivo anterior
            setTerminalFileAsOpen(True)
            print(
                "\n" +
                visual_giantLine + "\n" +
                visual_giantLine + "\n"
                "\n\n\n\n\n\n\n\n\n",
                
                file = file_outputTxt
            )
            setTerminalFileAsOpen(False)

        # [>] Remove extensão do arquivo  (pegando  apenas  o  nome)  e
        # atribui para a temporária
        str_fileName = pdfFile[:-4]

        # [>] Cria o título para leitura do arquivo no terminal
        setTerminalFileAsOpen(True)
        print(
            pdfFile + visual_giantLine + "\n" +
            visual_giantLine + "\n\n\n\n" +
            visual_blankSpaces + "                          ----- + -----\n\n" +
            visual_blankSpaces + "         LEITURA DE ARQUIVO - NÚMERO " + str(index_file) + ", '" + pdfFile + "'\n" +
            visual_blankSpaces + "   O arquivo '" + str_fileName + "' foi lido e está pronto pra ser convertido\n\n" +
            visual_blankSpaces + "                          ----- + -----\n\n\n\n",
            
            file = file_outputTxt
        )
        setTerminalFileAsOpen(False)



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
                list_dataFrames = tabula.read_pdf(
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
                    "usando o método '" + conversionMethod + "'.",
                    
                    err
                )
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # -------------------------------------------------------------


            # CONVERSÃO
            # -------------------------------------------------------------
            # Descrição:
            # Realizando a conversão com o método indicado.
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # [>] Reseta a variável
            index_dataFrame = 1
            # [>] Itera os DataFrames contidos na lista de  DataFrames  gerados
            # pela leitura do tabula
            for tableDataFrame in list_dataFrames:
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
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------

        # [>] Atribuindo mais um ao índice para indicar que  o  arquivo
        # PDF foi convertido
        index_file = index_file + 1
    else:
        # [i] Se até o término da operação algum  PDF  foi  convertido,
        # fecha o leiaute do terminal
        if (index_file > 1):
            # [>] Fecha o leiaute e pula 5 linhas
            setTerminalFileAsOpen(True)
            print(
                "\n" +
                visual_giantLine + "\n" +
                visual_giantLine,
            
                file = file_outputTxt
            )
            setTerminalFileAsOpen(False)
        # [i] Se ainda até o término da operação nenhum PDF foi conver-
        # tido exibe um erro
        else:
            # [>] Exibe o erro
            showError("Descrição: Não há arquivos de PDF para serem convertidos.", "")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def setCurrentPath():
    try:
        # [V] VARIÁVEIS
        # -------------------------------------------------------------
        # Descrição:
        # Grupo contendo variáveis utilizadas na função atual.
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
        # -------------------------------------------------------------
        # Descrição:
        # Referenciamento de variáveis globais (suas  descrições  estão
        # no grupo de variáveis globais localizadas no escopo do início
        # do Script).
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        global folderPath_script
        global filePath_outputTxt
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------
        

        # [i] Pegando o caminho até o executável ou script atual  e  a-
        # tribuindo para a variável folderPath_script
        folderPath_script = Path(__file__).parent.absolute()
        #                           ____[o script está dentro da pasta 'netcoreapp3.1']
        #                          /
        # (pdfconverter\bin\Debug\netcoreapp3.1)
        
        folderPath_script = str(folderPath_script)

        # [>] Passa para a variável global o caminho do arquivo de tex-
        # to do terminal
        filePath_outputTxt = folderPath_script + "\\resultados\\output.txt"
    except Exception as err:
        # [>] Exibe um erro quando há problemas em achar o diretório a-
        # tual
        showError(
            "Descrição: Não foi possível achar o diretório atual. Prov"
            "ável problema na hora de encurtar o caminho, verifique se"
            " o caminho passado na variável 'folderPath_script' dentro do mé"
            "todo 'setCurrentPath' está correto."
        
            , err
        )
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# [F] FUNÇÃO QUE DEFINE A ESTRUTURA DE PASTAS DO PROJETO
# -------------------------------------------------------------
# Descrição:
# Faz a verificação da existência das pastas a seguir e as cria
# caso elas ainda não existam.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def setProjectStructure():    
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Listas que possuem os caminhos das pastas que vão  ser  gera-
    # das.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # [C] CAMINHOS
    # [i] Caminhos que indicam a localização das  pastas  raíz  que
    # irão ser geradas futuramente.
    list_rootPaths = [
        "\\PDFs",
        "\\resultados"
    ]
    # [i] Caminhos que indicam a localização das pastas dos métodos
    # de leitura que vão ser geradas futuramente dentro da pasta de
    # exportação.
    list_readingPaths = [
        "\\lattice",
        "\\stream"
    ]
    # [i] Caminhos que indicam a localização das pastas dos métodos
    # de formatação que vão ser geradas futuramente dentro das pas-
    # tas de métodos de leitura, que estão dentro da pasta  de  ex-
    # portação.
    list_formattingPaths = [
        "\\main",
        "\\fullClear",
        "\\tableWithBlankCells",
        "\\withoutFormatting"
    ]
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    # [i] Para cada pasta raíz, presente na lista de pastas raíz
    for rootPath in list_rootPaths:
        # [>] Criando pastas raíz
        Path(
            folderPath_script +
            rootPath
        ).mkdir(parents = True, exist_ok = True)

        # [>] Dentro da pasta de resultados
        if (rootPath == "\\resultados"):
            # [i] Para cada método, presente na lista de métodos
            for methodPath in list_readingPaths:
                # [>] Cria uma pasta
                Path(
                    folderPath_script +
                    rootPath +
                    methodPath
                ).mkdir(parents = True, exist_ok = True)

                # [>] Criando pastas para métodos de formatação
                for outputTypePath in list_formattingPaths:
                    Path(
                        folderPath_script +
                        rootPath +
                        methodPath +
                        outputTypePath
                    ).mkdir(parents = True, exist_ok = True)


    # [>] Cria arquivo para exibir a saída do terminal, se já exis-
    # tir o arquivo, limpa o mesmo
    open(filePath_outputTxt, "w").close()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [F] FUNÇÃO QUE DEFINE E EXECUTA CONFIGURAÇÕES DO PANDAS
# -------------------------------------------------------------
# Descrição:
# Configurações do Pandas que afetam o DataFrame e a  conversão
# para texto.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def setTerminalFileAsOpen(openingState):
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global file_outputTxt
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    # [i] Caso o programador decida abrir o arquivo
    if (openingState):
        # [>] Abre o arquivo de saída do terminal com "append"
        file_outputTxt = open(filePath_outputTxt, "a", encoding="UTF-8")
    # [i] Caso o programador decida fechar o arquivo
    else:
        # [>] Fecha o arquivo de saída do terminal
        file_outputTxt.close()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [F] EXIBE UMA MENSAGEM DE ERRO
# -------------------------------------------------------------
# Descrição:
# Função responsável por exibir mensagens de erros  disponíveis
# nas Exceptions.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def showError(errorMessage, err):
    # [>] Abre o layout com a mensagem e o arquivo
    file_outputTxt = open(filePath_outputTxt, "a", encoding="UTF-8")
    print(
        "======================================================================\n"
        "\n"
        "[ MENSAGEM ]\n"
        "\n"
        "ERRO\n"
        "\n" +
        errorMessage + "\n",
        
        file = file_outputTxt
    )

    # [i] Caso tenha uma exception ele exibe ela
    if (err != ""):
        # [>] Exibe a exception
        print(
            "\n"
            "Exception Log:",
            
            file = file_outputTxt
        )
        print(str(err), file = file_outputTxt)
    
    # [>] Fecha o layout e o arquivo
    print(
        "\n"
        "======================================================================",
        
        file = file_outputTxt
    )
    file_outputTxt.close()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [F] REALIZA A CONVERSÃO DO ARQUIVO
# -------------------------------------------------------------
# Descrição:
# Realiza a conversão do arquivo PDF para CSV como  arquivo  de
# texto.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def conversionStart(conversionMethod, tableDataFrame):
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global filePath_exportTxt
    global index_dataFrame
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


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
        # global filePath_exportTxt
        filePath_exportTxt = folderPath_script + "\\resultados\\" + conversionMethod + "\\withoutFormatting\\" + str_fileName + ".txt"

        # [>] Converte o arquivo para .txt no formato de um CSV
        tableDataFrame.to_csv(
            filePath_exportTxt,
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
        setTerminalFileAsOpen(True)
        print(
            "\n\n"
            "          A tabela nº"+ str(index_dataFrame) + " do '" + str_fileName + "' foi convertida usando '" + conversionMethod + "'\n"
            "\________________________________________________________________________________/\n" +
            "Search this (Ctrl + F): '" + str_fileName + " " + conversionMethod + " tbl" + str(index_dataFrame) + "'\n",
            
            file = file_outputTxt
        )

        # [>] Imprime o DataFrame
        print(pandas.DataFrame(tableDataFrame), file = file_outputTxt)
        setTerminalFileAsOpen(False)

        index_dataFrame = index_dataFrame + 1
    except Exception as err:
        # [>] Exibe um erro de conversão caso haja um erro não tra-
        # tado
        showError(
            "Arquivo: " + str_fileName + "\n"
            "Método de Conversão: " + conversionMethod + "\n"
            "\n"
            "Descrição: Ocorreu um erro, ao tentar converter o "
            "arquivo '" + str_fileName + ".pdf' usando o "
            "método " + conversionMethod + ".",
            
            err
        )
        return
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [F] LIMPA O ARQUIVO DE TEXTO CONVERTIDO
# -------------------------------------------------------------
# Descrição:
# Limpa o arquivo de texto removendo todas as  linhas  que  não
# contenham um separador (;), ou seja,  linhas  que  não  fazem
# parte de uma tabela.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def formatTextFile(conversionMethod):
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global filePath_exportTxt
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # [C] CAMINHOS
    # -------------------------------------------------------------
    # Descrição:
    # Variáveis que armazenam caminhos dos tipos de formatação.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # [i] Formatação padrão, apenas exibindo caso e caso  tenha pe-
    # lo menos um separador ";" na linha e removendo campos vazios
    txtMainPath = folderPath_script + "\\resultados\\" + conversionMethod + "\\main\\" + str_fileName + ".txt"
    # [i] Formatação padrão, porém mantendo campos vazios
    txtReturnBlankCellsPath = folderPath_script + "\\resultados\\" + conversionMethod + "\\tableWithBlankCells\\" + str_fileName + ".txt"
    # [i] Full Clear, formatação mais robusta
    txtFullClearPath = folderPath_script + "\\resultados\\" + conversionMethod + "\\fullClear\\" + str_fileName + ".txt"
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    # [i] Abre o arquivo original presente na pasta 'withoutFormat-
    # ting' para criar formatações baseadas nele
    with open(filePath_exportTxt, "r", encoding="UTF-8") as txtFile:
        # ARQUIVOS
        # -------------------------------------------------------------
        # Descrição:
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
        for line in txtFile:
            # [>] Detecta os dados vazios que estão presentes no  cabeçalho
            # "Unnamed: X;"
            line = re.sub(r"(\s?\"Unnamed:\s\d\d?\";?)", "", line)

            # [>] Remove quebras de linha caso seja no meio dos  dados,  ou
            # seja, caso não possua '"' atrás da quebra de linha e as subs-
            # titui por um espaço para manter o padrão
            line = re.sub(r"((?<!\")\n)", " ", line)

            # Condicional que impede o continuamento do processo caso a va-
            # riável esteja vazia, ou seja, caso tenha  sido  apagada  pelo
            # processo anterior de limpeza
            if (line != ""):
                # [>] Remove ponto e vírgula no final da linha
                line = re.sub(r"((?<=\");(?!.))", "", line)
                
                # [>] Remove todos os espaços no início de cada linha
                line = re.sub(r"(^\ *)", "", line)

                # [i] Se a linha possui aspas duplas no início  e  no  final  e
                # ainda possui menos que duas colunas cancela o código
                if (
                    (
                        (
                            line.startswith("\"")
                        )
                        and 
                        (
                            line.endswith("\"") or line.endswith("\n")
                        )
                    )
                    and
                    (line.count("\"") < 3 and line.count(";") < 1)
                ):
                    # [>] Não executa o código seguinte
                    continue

                # [e] Exportação para a pasta: \\tableWithBlankCells
                txtTableWithBlankCells.write(line)
                
                # [>] Remove dados que estão vazios
                line = re.sub(r"(;\"\")|(\"\";)", "", line)

                # [>] Faz uma quebra de linha caso tenha aspas duplas  adjacen-
                # tes
                line = re.sub(r"(?<=\")(?=\")", "\n", line)

                # [>] Caso tenha um ponto e vírgula seguido de um espaço  troca
                # por uma quebra de linha
                line = re.sub(r"((?<=\");\ )", "\n", line)

                # [>] Caso tenha um espaço entre um separador e uma aspas dupla
                # remove o conteúdo que está atrás
                line = re.sub(r"((.*\";\ )(?=\"))", "", line)

                # [i] Se a linha possui aspas duplas no início  e  no  final  e
                # ainda possui menos que duas colunas cancela o código
                if (
                    (
                        (
                            line.startswith("\"")
                        )
                        and 
                        (
                            line.endswith("\"") or line.endswith("\n")
                        )
                    )
                    and
                    (line.count("\"") < 3 and line.count(";") < 1)
                ):
                    # [>] Não executa o código seguinte
                    continue

                # [e] Exportação para a pasta: \\main
                txtMainFile.write(line)
    
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
        for line in txtFile:
            # [>] Caso a linha não comece com aspas deleta
            line = re.sub(r"((^[^\"]).*)", "", line)
            
            # [>] Caso a linha não termine com aspas deleta
            line = re.sub('"(.*([^"\n]$))', "", line)

            # [>] Remove Linhas vazias que só possuem quebra de linha  '\n'
            # ou não possuem uma aspas dupla em nenhum lugar, serão excluí-
            # das 
            lineRemovedQuotes = ""
            lineRemovedQuotes = re.sub(r"\"", "", line)

            # [i] Se a temporária permanece igual, ou seja, não teve  aspas
            # duplas removidas pelo regex
            if (line == lineRemovedQuotes):
                # Quer dizer que ela ta errada e vai ser apagada
                line = ""
            
            # [i] Só escreve a linha se tiver pelo menos mais que 3 colunas
            # no arquivo fullClear
            if (line.count("\"") > 6 and
                line.count(";") > 2):
                # [e] Exportação para a pasta: \\fullClear
                txtFullClearFile.write(line)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------


# [G] MANIPULAÇÃO DE ARGUMENTOS
# -------------------------------------------------------------
# Descrição:
# Grupo que contém funções que realizam a manipulação da bibli-
# oteca que manipula argumentos, a 'argparse'.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#region

# [F] CRIA O PARSER
# -------------------------------------------------------------
# Descrição:
# Função que cria o parser que vai manipular os argumentos for-
# necidos pelo usuário.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def createParser():
    # [V] VARIÁVEIS
    # -------------------------------------------------------------
    # Descrição:
    # Grupo contendo variáveis utilizadas na função atual.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
    # -------------------------------------------------------------
    # Descrição:
    # Referenciamento de variáveis globais (suas  descrições  estão
    # no grupo de variáveis globais localizadas no escopo do início
    # do Script).
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global parser_main
    global parserArgs_main
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    # [>] Criando parser
    parser_main = argparse.ArgumentParser(allow_abbrev=False)


    # ARGUMENTOS UTILIZADOS NO PARSER
    # -------------------------------------------------------------
    # Descrição:
    # Aqui estão dispostos os argumentos que vão ser passados  para
    # o parser mais tarde.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # [i] Argumento   que   conterá   o  caminho   de    importação
    # (Obrigatório)
    parser_main.add_argument(
        "--importPath",
        required = True,
        type = str
    )
    # [i] Argumento que conterá o caminho de exportação (Opcional)
    parser_main.add_argument(
        "--exportPath",
        required = False,
        type = str
    )
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    # [>] Adiciona os argumentos informados anteriormente na região
    # anterior ao parser
    parserArgs_main = parser_main.parse_args()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# [F] CHECA SE A PASTA PASSADA NO PARÂMETRO EXISTE
# -------------------------------------------------------------
# Descrição:
# Função que faz uma validação de existência de uma pasta  pas-
# sada como argumento.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def checkIfFolderExists(folderThatWillBeChecked):
    # [>] Instancia a variável como não existente
    currentFolderExists = False
    # [i] Se a pasta fornecida existe
    if (os.path.isdir(folderThatWillBeChecked)):
        # [>] Define a mesma como existente na variável
        currentFolderExists = True
    # [>] Retorna pra função
    return currentFolderExists
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

#endregion
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# _____________________________________________________________





# [>] Executa o Script
# _____________________________________________________________
Main()