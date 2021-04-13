import pandas
import tabula
from os import chdir
from glob import glob
from pathlib import Path

tableDataFrameHeader = []
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

	indexFile = 1
	# Pega todos os PDFs
	chdir(pathFolderPDFs)
	for pdfFile in glob("*.pdf"):
		try:
			# Remove extensão do arquivo, pegando apenas o nome e atribui pra variavel
			fileName = pdfFile[:-4]
			# Fazendo leitura do arquivo completo e passando para a variável
			tableListOfDataFrames_stream = tabula.read_pdf(pdfFile, pages="all", stream=True, multiple_tables=True, guess=False)
			tableListOfDataFrames_lattice = tabula.read_pdf(pdfFile, pages="all", lattice=True, multiple_tables=True, guess=False)
			tableListOfDataFrames_stream_guess = tabula.read_pdf(pdfFile, pages="all", stream=True, multiple_tables=True, guess=True)
			tableListOfDataFrames_lattice_guess = tabula.read_pdf(pdfFile, pages="all", lattice=True, multiple_tables=True, guess=True)

			# Indica que um arquivo completo foi lido com sucesso
			print(
				"======================================================================\n"
				"LEITURA DE ARQUIVO - NÚMERO " + str(indexFile) + " (" + pdfFile + ")\n"
				"O arquivo " + fileName + " foi lido e está pronto pra ser convertido\n",

				file=outputFile
			)

			# LATTICE
			# guess = False
			# Para cada uma das tabelas 'DataFrames' contidos no arquivo csv completo 'lista de tabelas' será convertido
			indexDataFrame = 1
			for tableDataFrame in tableListOfDataFrames_lattice:
				try:
					turnHeaderInSimpleRow(tableDataFrame)

					# Removendo quebras de linha
					# O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
					# O segundo replace remove as que acontecem por conta do ponto e vírgula
					tableDataFrame = tableDataFrame.replace({r"\r": ""}, regex=True).replace({r";": ","}, regex=True)

					# Converte para .txt no formato de um CSV
					tableDataFrame.to_csv(
						"../resultados/txt-lattice/"+ fileName + ".txt",
						index=False,
						index_label=False,
						header=False,
						line_terminator="\n", # Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
						sep=";",
						mode="a"
					)

					print(
						"______________________________________________________________________\n"
						"A tabela da página "+ str(indexDataFrame) + " do PDF foi convertida |\n"
						"___________________________________________/\n" +
						pdfFile + " lattice=True guess=False\n",

						file=outputFile
					)
					# Imprime o DataFrame
					print(pandas.DataFrame(tableDataFrame), file=outputFile)

					indexDataFrame = indexDataFrame + 1
				except Exception as err: 
					showError("Ocorreu um erro, ao tentar converter o arquivo", err)
					break

			# guess = True
			indexDataFrame = 1
			for tableDataFrame in tableListOfDataFrames_lattice_guess:
				try:
					turnHeaderInSimpleRow(tableDataFrame)

					# Removendo quebras de linha
					# O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
					# O segundo replace remove as que acontecem por conta do ponto e vírgula
					tableDataFrame = tableDataFrame.replace({r"\r": ""}, regex=True).replace({r";": ","}, regex=True)

					# Converte para .txt no formato de um CSV
					tableDataFrame.to_csv(
						"../resultados/txt-lattice/guess-"+ fileName + ".txt",
						index=False,
						index_label=False,
						header=False,
						line_terminator="\n", # Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
						sep=";",
						mode="a"
					)

					print(
						"______________________________________________________________________\n"
						"A tabela da página "+ str(indexDataFrame) + " do PDF foi convertida |\n"
						"___________________________________________/\n" +
						pdfFile + " lattice=True guess=True\n",

						file=outputFile
					)
					# Imprime o DataFrame
					print(pandas.DataFrame(tableDataFrame), file=outputFile)

					indexDataFrame = indexDataFrame + 1
				except Exception as err: 
					showError("Ocorreu um erro, ao tentar converter o arquivo", err)
					break

			print("----------------------------------------------------------------------", file=outputFile)

			# STREAM
			# guess = False
			# Para cada uma das tabelas 'DataFrames' contidos no arquivo csv completo 'lista de tabelas' será convertido
			indexDataFrame = 1
			for tableDataFrame in tableListOfDataFrames_stream:
				try:
					turnHeaderInSimpleRow(tableDataFrame)

					# Removendo quebras de linha
					# O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
					# O segundo replace remove as que acontecem por conta do ponto e vírgula
					tableDataFrame = tableDataFrame.replace({r"\r": ""}, regex=True).replace({r";": ","}, regex=True)

					# Converte para .txt no formato de um CSV
					tableDataFrame.to_csv(
						"../resultados/txt-stream/" + fileName + ".txt",
						index=False,
						index_label=False,
						header=False,
						line_terminator="\n", # Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
						sep=";",
						mode="a"
					)

					print(
						"______________________________________________________________________\n"
						"A tabela da página "+ str(indexDataFrame) + " do PDF foi convertida |\n"
						"___________________________________________/\n" +
						pdfFile + " stream=True guess=False\n",

						file=outputFile
					)
					# Imprime o DataFrame
					print(pandas.DataFrame(tableDataFrame), file=outputFile)

					indexDataFrame = indexDataFrame + 1
				except Exception as err: 
					showError("Ocorreu um erro, ao tentar converter o arquivo", err)
					break
			print("======================================================================", file=outputFile)

			# guess=True
			indexDataFrame = 1
			for tableDataFrame in tableListOfDataFrames_stream_guess:
				try:
					turnHeaderInSimpleRow(tableDataFrame)

					# Removendo quebras de linha
					# O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
					# O segundo replace remove as que acontecem por conta do ponto e vírgula
					tableDataFrame = tableDataFrame.replace({r"\r": ""}, regex=True).replace({r";": ","}, regex=True)

					# Converte para .txt no formato de um CSV
					tableDataFrame.to_csv(
						"../resultados/txt-stream/guess-" + fileName + ".txt",
						index=False,
						index_label=False,
						header=False,
						line_terminator="\n", # Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
						sep=";",
						mode="a"
					)

					print(
						"______________________________________________________________________\n"
						"A tabela da página "+ str(indexDataFrame) + " do PDF foi convertida |\n"
						"___________________________________________/\n" +
						pdfFile + " stream=True guess=True\n",

						file=outputFile
					)
					# Imprime o DataFrame
					print(pandas.DataFrame(tableDataFrame), file=outputFile)

					indexDataFrame = indexDataFrame + 1
				except Exception as err: 
					showError("Ocorreu um erro, ao tentar converter o arquivo", err)
					break

			indexFile = indexFile + 1

		except Exception as err:
			showError("Ocorreu um erro ao tentar ler o arquivo.", err)
	else:
		showError("Não há arquivos de PDF para serem convertidos", "")

def makeDirectories():
	# Faz a verificação da existência das pastas a seguir e as cria caso elas ainda não existam
	Path(pathFolderPDFs).mkdir(parents=True, exist_ok=True)
	Path(pathFolderResultados).mkdir(parents=True, exist_ok=True)
	Path(pathFolderResultados + "/txt-lattice").mkdir(parents=True, exist_ok=True)
	Path(pathFolderResultados + "/txt-stream").mkdir(parents=True, exist_ok=True)

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
		"--- MENSAGEM ---\n"
		"\n"
		"ERRO\n"
		"'" + errorMessage + "'",
		
		file=outputFile
	)

	print(str(errorErr), file=outputFile)
	if errorErr != "":
		print(str(errorErr), file=outputFile)

	print("**********************************************************************", file=outputFile)

pandaSetConfig()
Main()