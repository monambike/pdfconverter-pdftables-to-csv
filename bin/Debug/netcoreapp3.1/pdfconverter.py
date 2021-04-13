import pandas
import tabula
import xlsxwriter
from os import chdir
from glob import glob
from pathlib import Path

tableDataFrame = None
tableDataFrameHeader = []
tableListOfDataFrames_stream = None
tableListOfDataFrames_lattice = None
err = None
# Caminhos baseados na onde o executável fonte do projeto está localizado
# (pdfconverter\bin\Debug\netcoreapp3.1)
pathFolderPDFs = "../../../../PDFs"
pathFolderResultados = "../../../../resultados"
pathOutputFile = pathFolderResultados + "/output.txt"
# Arquivo output
outputFile = open(pathOutputFile, "a")

def Main():
	# Limpa o arquivo de saída do terminal
	outputClear = open(pathOutputFile,"w")
	outputClear.close()

	makeDirectories()

	indexFile = 0
	try:
		# Pega todos os PDFs
		chdir(pathFolderPDFs)
		for pdfFile in glob("*.pdf"):
			try:
				# Fazendo leitura do arquivo completo e passando para a variável
				tableListOfDataFrames_stream = tabula.read_pdf(pdfFile, pages="all", stream=True, multiple_tables=True, guess=True)
				tableListOfDataFrames_lattice = tabula.read_pdf(pdfFile, pages="all", lattice=True, multiple_tables=True, guess=True)

				# Indica que um arquivo completo foi lido com sucesso
				print(
					"======================================================================\n"
					"LEITURA DE ARQUIVO - NÚMERO " + str(indexFile) + "\n"
					"O arquivo " + pdfFile + " foi lido e está pronto pra ser convertido\n",

					file=outputFile
				)

				# Remove extensão do arquivo, pegando apenas o nome e atribui pra variavel
				fileName = pdfFile[:-4]
				# Cria uma pasta para armazenar tabelas com o mesmo nome pra cada arquivo
				Path("../resultados/tabelas/" + fileName).mkdir(parents=True, exist_ok=True)

				# LATTICE
				# Para cada uma das tabelas 'DataFrames' contidos no arquivo csv completo 'lista de tabelas' será convertido
				indexDataFrame = 0
				for tableDataFrame in tableListOfDataFrames_lattice:
					try:
						turnHeaderInSimpleRow(tableDataFrame)

						# Removendo quebras de linha
						# O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
						# O segundo replace remove as que acontecem por conta do ponto e vírgula
						tableDataFrame = tableDataFrame.replace({r"\r": ""}, regex=True).replace({r";": ","}, regex=True)

						# Converte para .txt no formato de um CSV
						tableDataFrame.to_csv(
							"../resultados/texto/"+ fileName + ".txt",
							index=False,
							index_label=False,
							header=False,
							line_terminator="\n", # Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
							sep=";",
							mode="a"
						)

						# Converte para excel
						excelWriter = pandas.ExcelWriter(
							"../resultados/tabelas/" + fileName + "/" + str(indexDataFrame) + ".xlsx",
							engine="xlsxwriter"
						)
						tableDataFrame.to_excel(
							excelWriter,
							index=False,
							header=False,
							engine="xlsxwriter"
						)
						excelWriter.save()

						print(
							"______________________________________________________________________\n"
							"A tabela da página "+ str(indexDataFrame + 1) + " do PDF foi convertida |\n"
							"___________________________________________/\n",

							file=outputFile
						)
						# Imprime o DataFrame
						print(pandas.DataFrame(tableDataFrame), file=outputFile)

						indexDataFrame = indexDataFrame + 1
					except Exception as err: 
						showError("Ocorreu um erro, ao tentar converter o arquivo", err)
						break
				print("======================================================================", file=outputFile)

				# STREAM
				# espaço reservado

				indexFile = indexFile + 1

			except Exception as err:
				showError("Ocorreu um erro ao tentar ler o arquivo.", err)

		else:
			showError("Não há arquivos de PDF para serem convertidos", err)

	except Exception as err:
		showError("Ocorreu um erro desconhecido.", err)

def makeDirectories():
	# Faz a verificação da existência das pastas a seguir e as cria caso elas ainda não existam
	Path(pathFolderPDFs).mkdir(parents=True, exist_ok=True)
	Path(pathFolderResultados).mkdir(parents=True, exist_ok=True)
	Path(pathFolderResultados + "/texto").mkdir(parents=True, exist_ok=True)
	Path(pathFolderResultados + "/tabelas").mkdir(parents=True, exist_ok=True)

def pandaSetConfig():
	# CONFIGURAÇÕES DO PANDAS

	# Evita com que os dados acabem sendo quebrados na saída do terminal e no arquivo exportado
	pandas.options.display.max_colwidth = None
	pandas.options.display.expand_frame_repr = False
	# Define o padrão de codificação para UTF-8 com BOM
	pandas.options.display.encoding = "utf-8-sig"
	# Mostra o dia primeiro quando encontrar data
	pandas.options.display.date_dayfirst = True
	# Fazer com que caso tenha um ';' ele não passe os dados pra outra célula
	pandas.options.display.latex.multicolumn = False

def turnHeaderInSimpleRow(tableDataFrame):
	# FAZENDO COM QUE O CABEÇALHO SE TORNE UMA LINHA COMUM
	# Isso é necessário para fazer com que não haja quebra nas linhas onde ele identifica
	# como título caso o conteúdo delas seja muito grande, isso acontece porque o título
	# tem uma formatação gerada pelo dataframe que pelo jeito faz com que isso ocorra.
	
	# Limpa a lista que vai manipular o cabeçalho
	tableDataFrameHeader = []
	# Pegando o cabeçalho da tabela e passando ela como lista para a variável
	tableDataFrameHeader = [*tableDataFrame]
	# Removendo o cabeçalho da tabela atual
	tableDataFrame = tableDataFrame.T.reset_index().T.reset_index(drop=True)
	# Adicionando a lista como primeira linha do cabeçalho do DataFrame criado para manipular cabeçalho
	tableDataFrameHeader.insert(1, tableDataFrameHeader)
	# Concatenando à tabela principal
	pandas.concat([pandas.DataFrame(tableDataFrameHeader), tableDataFrame], ignore_index=True)

def showError(errorMessage, errorErr):
	print(
		"======================================================================\n"
		"**********************************************************************\n"
		"--- ERRO ---\n"
		"\n"
		"'" + errorMessage + "'",
		
		file=outputFile
	)

	print(str(errorErr), file=outputFile)
	#if err is not None:
	#	print(str(errorErr), file=outputFile)

	print("**********************************************************************", file=outputFile)

pandaSetConfig()
Main()