"""
---
---
---

## Package: pdfconverter >> patterncolumns
---
---
### Module Name: patterncolumns
---
### path: "pdfconverter\\\\\\\\patterncolumns\\\\\\\\__init__.py"
---
---
Módulo  comportando  funções  relacionadas  à  padronização  de
arquivos resultantes da conversão.

---
---
---
"""

# [>] Geral
import re
import pathlib
# [>] PDFConverter
# [>] Variables
from pdfconverter.__variables__ import pvar
# [>] Terminal File
from pdfconverter.terminalfile import error

#region GLOBAL VARIABLES

# [C] PATTERN COLUMNS
# -------------------------------------------------------------
# Descrição:
# Variáveis que possuem relações com a definição de padrões nas
# colunas
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
list_textFileTSC = []
"""teste"""
tableIndex = -1
"""teste 2"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

#endregion

#region PUBLIC METHODS

def GenerateTextFile(BasedFilePath, NewFolderPath):
    """
    ---
    ---
    ---
    
    ## GenerateTextFile ([Public or Private?])
    ---
    ---
    Gera um novo arquivo de texto, baseado em um antigo.
    
    ### Args
    ---
    - BasedFilePath ([type], [optional], default = ):
        - [description]
    - NewFolderPath ([type], [optional], default = ):
        - [description]
    
    ---
    ---
    ---
    """

    __SeparateFileInTables(BasedFilePath)

    pathlib.Path(NewFolderPath).mkdir(parents = True, exist_ok = True)

    # [>] Gera um arquivo de texto com o conteúdo separado por tabelas
    # -------------------------------------------------------------
    index = 0
    for table in list_textFileTSC:
        FileInPattern = open(NewFolderPath + "\\arquivoColunaPadronizado (" + str(index) + ").txt", "a", encoding = "UTF-8")
        for line in table:
            # [>] Aqui vai ser escrito o conteúdo da variável
            FileInPattern.write(line)
        FileInPattern.close()

        index += 1
    # -------------------------------------------------------------
    
    __SetTableColumnsToPattern()

    # [>] Gera um arquivo de texto com o conteúdo do título alterado
    # -------------------------------------------------------------
    # -------------------------------------------------------------

def __SeparateFileInTables(BasedFilePath):
    """
    ---
    ---
    ---
    ---

    ### __SeparateFileInTables (Private)
    ---
    Função responsável por fazer o reconhecimento e a separação  do
    conteúdo do arquivo de texto em tabelas.

    Ela pega todas as linhas que iniciam com aspas e  uma  letra  e
    para de pegar quando encontra outro cabeçalho.

    ---
    ---
    ---
    """


    # Referenciamento de variáveis globais
    global tableIndex
    global list_textFileTSC


    textFilePath = BasedFilePath
    # [>] Com o arquivo de texto no qual vai ser feito  a  checagem
    # aberto
    with open(textFilePath, "r", encoding="UTF-8") as textFile:
        # [>] Para cada linha no arquivo de texto
        for line in textFile:            
            # [i] Regex que faz a verificação se o conteúdo da  li-
            # nha é um cabeçalho
            tableHeaderMatch = re.match(r"(^\"[a-zA-Z].*)", line)

            # [>] Se a linha for um cabeçalho
            if tableHeaderMatch is not None:
                # [>] Cria-se mais um espaço na array, que representa uma tabe-
                # la.
                list_textFileTSC.append([])

                # [>] Adiciona mais um ao contador de tabelas, para  se  inici-
                # ar a criação de mais uma.
                # [i] Observação, adições posteriores  serão  realizadas  nessa
                # nova tabela.
                tableIndex += 1
            # [>] Adiciona o conteúdo da linha na representação  da  tabela
            # atual dentro da array que segura todo o conteúdo  do  arquivo
            # de texto
            list_textFileTSC[tableIndex].append(line)

def __SetTableColumnsToPattern():
    """
    ---
    ---
    ---
    ---

    ### SetTableColumnsToPattern (Public)
    ---
    Função responsável por definir os valores das novas colunas
    baseado nos valores  fornecidos  do  conteúdo  das  colunas
    antigas, e das novas.

    Os novos valores atribuidos serão passados para uma  array,
    e apartir  dessa  array  um  novo  arquivo  de  texto  será
    montado.

    ---
    ---
    ---
    """

    i = 0
    newString = ""
    # [>] Para cada tabela presente na array que segmenta o conteú-
    # do do arquivo de texto (que é resultado da conversão)
    for table in list_textFileTSC:
        # [>] Enxerga cada item do cabeçalho de cada tabela utilizando-
        # se de  uma  expressão regular
        list_AllColumns = re.findall(
            r"""
            (?<=\")
            ([^\;]*?)
            (?=\")
            """,
            list_textFileTSC[i][0],
            flags = re.MULTILINE | re.VERBOSE
        )

        index = 0
        # [>] Para cada encontro que houve
        for argument in pvar.argsColumnFields:
            argName = argument[0]
            argValue = argument[1]
            
            # [>] Adiciona +1 ao contador
            index += 1

            # [>] Verifica se o encontro foi passado como argumento
            if (argValue in list_AllColumns):
                # [>] Agora precisa criar uma nova linha de uma array contendo os valores e substituir na antiga
                newString += '"' + argName + '"'
                newString += ';' if index < len(pvar.argsColumnFields) else '\n'
            else:
                error.Show("Não foi possível encontrar " + argument[1] + " no arquivo PDF.", ExitProgram = True, RecreateTerminalFile = True)

        list_textFileTSC[i][0] = newString

        novoarquivo = open("C:\\users\\dvp10\\desktop" + "\\novoarquivocolunas (" + str(i) + ").txt", "a", encoding="UTF-8")
        for table in list_textFileTSC:
            for line in table:
                print(line)
                novoarquivo.write(line)
        novoarquivo.close()

        # [>] Adiciona mais um ao contador de tabelas
        i += 1

def __RecognizePatternInTableColumns():
    """
    ---
    ---
    ---
    
    ### RecognizePatternInTableColumns
    ---
    Função responsável por fazer o  reconhecimento  automático  das
    colunas  existentes,  identificando  onde  elas   poderiam   se
    encaixar no padrão atual

    O reconhecimento vai ser realizado com base no primeiro item de
    cada tabela, que é onde localiza-se o cabeçalho.
    Esse reconhecimento só vai servir como sugestão   pro   usuário
    não precisar ficar digitando toda vez,  mesmo  que  o  item  se
    repita pra quase todo PDF.
    
    ---
    ---
    ---

    ### Padrão Atual
    ---
    - Lote: coluna referente ao Lote do produto;
    - Ordem(seq): Coluna referente ao identificador do produto;
    - Codigo: Coluna referente ao código do produto;
    - Produto: Coluna referente à descrição do produto;
    - Unidade: Coluna referente ao tipo de unidade do produto;
    - Quantidade:  Coluna  referente  à  quantidade  disponível  do
    produto;
    - Vlr Medio: Coluna referente ao valor médio do produto.

    ---
    ---
    ---
    """

    tablesQuantity = len(list_textFileTSC)
    index_tableCounter = 0
    # [>] Para cada tabela na lista de tabelas
    for index_tableCounter in range(tablesQuantity):
        # [>] Converte o cabeçalho da array para string
        ListHeader = ''.join(list_textFileTSC[index_tableCounter][0])


        # [>] Localiza e segmenta todas as colunas do cabeçalho
        list_separatedColumns = re.findall(
            r"""
            (?<=\")                # 2. Que inicie com aspas duplas
            ([^\;\n].*?)           # 1. Procura por todo conteúdo que não seja 'ponto e vírgula' e quebra de linha
            (?=\")                 # 3. Que termine com aspas duplas
            """,
            ListHeader,            # Lista retornada
            flags = re.MULTILINE | # Configuração multilinha
                    re.VERBOSE     # Configuração verbose
        )

#endregion

#region SINGLE FILE TEST

def SetHeaderToPattern(String):
    newString = ""

    # [i] Regex que faz a verificação se o conteúdo da  li-
    # nha é um cabeçalho
    headerMatch = re.match(r"(^\"[a-zA-Z].*)", String)

    # [>] Se a linha for um cabeçalho
    if headerMatch is not None:
        # [>] Enxerga cada item do cabeçalho de cada tabela utilizando-
        # se de  uma  expressão regular e passa para uma lista
        list_CSVColumns = re.findall(
            r"""
            (?<=\")
            ([^\;]*?)
            (?=\")
            """,
            String,
            flags = re.MULTILINE | re.VERBOSE
        )


        columnIterator = 0
        # [>] Para cada coluna da linha vinda do  cabeçalho  encontrado
        # no arquivo CSV
        for column in list_CSVColumns:
            # [i] Variável que vai dizer se a coluna foi mencionada pelo u-
            # suário
            foundInArg = False
            # [i] Contador das colunas do CSV
            argContainerIterator = 0
            # [>] Ele olha cada container de argumentos na lista  de  argu-
            # mentos que o usuário forneceu, contendo os valores de colunas
            # que ele quer alterar
            for argContainer in pvar.list_columnFieldsToChange:
                # [>] Verifica se a coluna atual do CSV ta dentro do container
                if (column in argContainer):
                    # [>] Se estiver, olha cada valor do container atual
                    for lineitem in range(len(pvar.list_columnFieldsToChange[argContainerIterator])):
                        # [>] Caso seja o primeiro index
                        if lineitem == 0:
                            # [>] Pega como nome do argumento
                            argName = argContainer[lineitem]
                        # [>] Caso não seja o primeiro index
                        else:
                            # [>] Pega como valor do argumento
                            argValue = argContainer[lineitem]
                            # [>] E verifica se é igual o da coluna e se for
                            if (column == argValue):
                                # [>] Substitui o nome da coluna pelo que tá no argmento
                                newString += '"' + argName + '"'
                                # [>] Avisa a variável que foi encontrado  uma  correspondência
                                # de argumento para a coluna atual
                                foundInArg = True
                                # [>] Para o for
                                break
                            # [>] Se não for igual da coluna
                            else:
                                # [>] Parte para o próximo item da array até achar
                                continue
                # [>] Se a linha atual nao tiver dentro do container
                else:
                    # [>] Passa pro proximo container
                    continue
                argContainerIterator += 1
                # [>] Caso a linha tenha sua correspondência encontrada  dentro
                # do container atual
                if foundInArg is True:
                    # [>] Para a operação e parte para a próxima coluna
                    break
            # [>] Se ao término da operação
            else:
                # [>] For percebido que a coluna não foi mencionada pelo  usuá-
                # rio
                if not foundInArg:
                    # [i] Adiciona ela na String do jeito que ela tá
                    newString += '"' + column + '"'
            columnIterator += 1

            # [>] Pra cada coluna que for adicionada, se não for  a  última
            # coluna bota ';' na frente e se for coloca um '\n'
            newString += ';' if columnIterator < len(list_CSVColumns) else '\n'
    # [>] Se a linha não for um cabeçalho
    else:
        # [>] Devolve a String como estava
        newString = String

    return newString

#endregion

#region TEMP TEST

# [WARNING] You must comment items in this region  if  u  wanna
# make an import at another place or the methods will be called
# at import
# -------------------------------------------------------------

# SeparateByTableColumns("C:\\Users\\dvp10\\Desktop\\resultados (1)\\lattice\\main\\EDITAL (1).txt")
# breakpoint=""
# SetTableColumnsToPattern()

#endregion