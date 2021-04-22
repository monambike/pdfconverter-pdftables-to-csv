import pandas
import tabula
import csv
from os import chdir
from glob import glob
from pathlib import Path
from PyPDF2 import PdfFileReader

# ---------------------------------------------------------------------- #

# >> VARIÁVEIS <<

# - ARQUIVOS DE SAÍDA -
# Saída do Terminal
outputFile = ""
# Saída do arquivo exportado
txtFilePath = ""

# - CAMINHOS -
# Definindo o caminho do projeto atual e atribuindo para a variável
currentPath = Path(__file__).parent.absolute()
currentPath = str(currentPath)[:-37]
# (pdfconverter\bin\Debug\netcoreapp3.1)
#    \___[ volta até essa pasta (pdfconverter) ]
# Caminhos baseados no currentPath
pathFolderPDFs = currentPath + "\\PDFs"
pathFolderResultados = currentPath + "\\resultados"
pathOutputFile = currentPath + "\\resultados\\output.txt"

# - CONTADORES -
# Índice do Data Frame
indexDataFrame = 0

# ---------------------------------------------------------------------- #

def Main():
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - GLOBAIS -
    global indexDataFrame

    # - CONTADORES -
    # Índice do arquivo
    indexFile = 1

    # ---------------------------------------------------------------------- #

    setProjectStructure()

    # Pega todos os arquivos
    chdir(pathFolderPDFs)
    # Filtra pelos PDFs
    for pdfFile in glob("*.pdf"):
        try:
            # Remove extensão do arquivo, pegando apenas o nome e atribui para a temporária
            fileName = pdfFile[:-4]

            # Pega o número de páginas que o PDF contém
            pdf = PdfFileReader(open(pdfFile, "rb"))
            pdfNumberOfPages = pdf.getNumPages()

            # - LEITURA -
            # Desc: Fazendo leitura do arquivo completo e passando como lista de DataFrames
            # para a variável
            # Método de leitura usando Lattice
            tableListOfDataFrames_lattice = tabula.read_pdf(
                pdfFile,
                pages="all",
                lattice=True,
                multiple_tables=True,
                guess=True,
                silent=True
            )
            # Método de leitura usando Stream
            tableListOfDataFrames_stream = tabula.read_pdf(
                pdfFile,
                pages="all",
                stream=True,
                multiple_tables=True,
                guess=True,
                silent=True
            )

            # Indica ao terminal que um arquivo completo foi lido com sucesso
            setTerminalFile("open")
            print(
                "======================================================================\n"
                "LEITURA DE ARQUIVO - NÚMERO " + str(indexFile) + " (" + pdfFile + ")\n"
                "O arquivo " + fileName + " foi lido e está pronto pra ser convertido\n",

                file=outputFile
            )
            setTerminalFile("closed")

            # - CONVERSÃO -
            # Lattice
            # Desc: Realizando a conversão com o que foi dado na leitura com o lattice
            indexDataFrame = 1
            conversionMethod = "lattice"
            for tableDataFrame in tableListOfDataFrames_lattice:
                # Passando os parâmetro do Lattice para a função
                conversionStart(fileName, conversionMethod, tableDataFrame, tableListOfDataFrames_lattice)
            cleanTextFile(fileName, conversionMethod)
            # Stream
            # Desc: Realizando a conversão com o que foi dado na leitura com o stream
            indexDataFrame = 1
            conversionMethod = "stream"
            for tableDataFrame in tableListOfDataFrames_stream:
                # Passando os parâmetro do Stream para a função
                conversionStart(fileName, conversionMethod, tableDataFrame, tableListOfDataFrames_stream)
            cleanTextFile(fileName, conversionMethod)
            
            # Atribuindo mais um ao índice para indicar que os arquivos foram convertidos
            indexFile = indexFile + 1
        except Exception as err:
            showError("Ocorreu um erro ao tentar realizar a leitura do arquivo '" + pdfFile +  "'.", err)
            break 
    else:
        showError("Não há arquivos de PDF para serem convertidos", "")

# >> DEFINE A ESTRUTURA DO PROJETO <<
def setProjectStructure():
    # Limpa o arquivo da saída do terminal
    outputClear = open(pathOutputFile, "w", encoding="UTF-8")
    outputClear.close()
    
    # Faz a verificação da existência das pastas a seguir e as cria caso elas ainda não existam
    Path(pathFolderPDFs).mkdir(parents=True, exist_ok=True)
    Path(pathFolderResultados).mkdir(parents=True, exist_ok=True)
    Path(pathFolderResultados + "\\lattice").mkdir(parents=True, exist_ok=True)
    Path(pathFolderResultados + "\\stream").mkdir(parents=True, exist_ok=True)
    Path(pathFolderResultados + "\\test").mkdir(parents=True, exist_ok=True)
    Path(pathFolderResultados + "\\test\\lattice").mkdir(parents=True, exist_ok=True)
    Path(pathFolderResultados + "\\test\\stream").mkdir(parents=True, exist_ok=True)

# >> CONFIGURAÇÕES DO PANDAS <<
# Desc: Configurações do Pandas que afetam o DataFrame e a conversão para texto.
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

# >> FAZENDO COM QUE O CABEÇALHO SE TORNE UMA LINHA COMUM <<
# Desc: Isso é necessário para fazer com que não haja quebra de linha onde o DataFrame identifica
# como cabeçalho (título) da tabela caso o conteúdo delas seja muito grande.
# Isso acontece porque o título tem uma formatação gerada pelo DataFrame que difere-se do corpo,
# o que acaba permitindo que isso ocorra.
def turnHeaderInSimpleRow(tableDataFrame):
    # Limpa a lista que vai ser usada para manipular o cabeçalho no DataFrame
    tableDataFrameHeader = []

    # Pegando o cabeçalho da tabela e passando ela como lista para a temporária
    tableDataFrameHeader = [*tableDataFrame]

    # Removendo o cabeçalho do DataFrame atual
    tableDataFrame = tableDataFrame.T.reset_index().T.reset_index(drop=True)

    # Adicionando a lista como primeira linha do DataFrame temporário
    tableDataFrameHeader.insert(1, tableDataFrameHeader)

    # Concatenando tabela temporária à tabela principal
    pandas.concat([pandas.DataFrame(tableDataFrameHeader), tableDataFrame], ignore_index=True)

def conversionStart(fileName, conversionMethod, tableDataFrame, tableListOfDataFrames):
    global txtFilePath
    global indexDataFrame

    try:
        # Deleta todas as linhas que estão completamente vazias
        tableDataFrame = tableDataFrame.dropna(how="all")
        tableDataFrame = tableDataFrame.dropna(how="all", axis=1)

        turnHeaderInSimpleRow(tableDataFrame)

        # Transforma todo o conteúdo do DataFrame em string
        #tableDataFrame = tableDataFrame.astype(str)
        
        # TESTE
        #verifyCellsValue(tableDataFrame)
        
        # Removendo quebras de linha
        # O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
        # O segundo replace remove as que acontecem por conta do ponto e vírgula
        tableDataFrame = tableDataFrame.replace({r"\r": ""}, regex=True).replace({r";": ","}, regex=True)

        txtFilePath = pathFolderResultados + "\\" + conversionMethod + "\\" + fileName + ".txt"
        
        # Converte para .txt no formato de um CSV
        tableDataFrame.to_csv(
            txtFilePath,
            index=False,
            index_label=False,
            header=True,
            line_terminator="\n", # Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
            sep=";",
            mode="a",
            quoting=csv.QUOTE_ALL
        )
        
        setTerminalFile("open")
        print(
            "______________________________________________________________________\n"
            "A tabela da página "+ str(indexDataFrame) + " do PDF foi convertida |\n"
            "___________________________________________/\n" +
            fileName + " " + conversionMethod + " pg" + str(indexDataFrame) + "\n",

            file=outputFile
        )
        # Imprime o DataFrame
        print(pandas.DataFrame(tableDataFrame), file=outputFile)
        setTerminalFile("closed")

        indexDataFrame = indexDataFrame + 1
    except Exception as err:
        showError("Ocorreu um erro, ao tentar converter o arquivo '" + fileName + ".pdf' usando o método " + conversionMethod + ".", err)

        return

def cleanTextFile(fileName, conversionMethod):
    # ---------------------------------------------------------------------- #

    # >> VARIÁVEIS <<
    
    # - GLOBAIS -
    global txtFilePath

    # ---------------------------------------------------------------------- #

    txtFileCleanedPath = pathFolderResultados + "\\test\\" + conversionMethod + "\\" + fileName + ".txt"
    
    # Esse loop por toda linha e vai encontrando caracteres iguais, quando ele encontrar algum caractere diferente na mesma linha ele para e retorna falso
    txtFileCleaned = open(txtFileCleanedPath, "a", encoding="UTF-8")
    with open(txtFilePath, "r", encoding="UTF-8") as txtDoc:
        # Navega por cada linha do documento de texto
        for line in txtDoc:
            # Escreve um novo documento
            # Só escreve a linha se ela tiver com pelo menos um ';'
            if ";" in line:
                txtFileCleaned.write(line)
    txtFileCleaned.close()
    
    return True

# DEFINE O ESTADO DO TERMINAL
# Define quando o terminal vai ser aberto ou quando vai ser fechado
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

# FUNÇÃO PARA VERIFICAR ONDE COMEÇA E ONDE TERMINA AS TABELAS
#def verifyCellsValue(tableDataFrame):
    #cellValueFirstDigit = ""
    #outputTest = open(currentPath + "\\resultados\\funcTest.txt", "a")
    # Navega por cada linha do DataFrame
    #pandas.display(tableDataFrame)
    
    #print(display.iloc[0])
    #for rowIndex, row in tableDataFrame.iterrows():
    #    teste_1 = str(row)

        # Caso o primeiro caractere comece com letras
        # e não tenha "nan" (similar ao "None" porém exibido em strings vazias dentro do corpo do DataFrame)
        # é o título
    #    if str(row)[:1].isdigit():
    #        print("")
        # Caso contrário é o corpo
    #    else:
    #        print("Pode ser um titulo: " + str(row), file=outputTest)
    #    break

# EXIBE UMA MENSAGEM DE ERRO
def showError(errorMessage, err):
    setTerminalFile("open")
    print(
        "======================================================================\n"
        "**********************************************************************\n"
        "--- MENSAGEM ---\n"
        "\n"
        "ERRO\n"
        "Descrição: " + errorMessage + "\n",
        
        file=outputFile
    )

    # Caso tenha uma exception, ele exibe
    if err != "":
        print("EXCEPTION")
        print(str(err), file=outputFile)
    
    print(
        "**********************************************************************",
        
        file=outputFile
    )
    setTerminalFile("closed")
    
    outputTest.close()

pandaSetConfig()
Main()