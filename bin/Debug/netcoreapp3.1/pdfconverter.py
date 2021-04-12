import pandas
import tabula
import xlsxwriter
from os import chdir
from glob import glob
from pathlib import Path

# Faz caminhos baseados na onde o projeto está localizado (pdfconverter\bin\Debug\netcoreapp3.1)
folderPDFs = "../../../../PDFs"
folderResultados = "../../../../resultados"
outputFile = outputFile=open(folderResultados + "/" + "output.txt", "a")

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

def Main():
	# Faz a verificação da existência das pastas a seguir e as cria caso elas ainda não existam
	Path(folderPDFs).mkdir(parents=True, exist_ok=True)
	Path(folderResultados).mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/texto").mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/tabelas").mkdir(parents=True, exist_ok=True)

	# Pega todos os PDFs
	chdir(folderPDFs)
	
	# Pega todos os PDFs dentro da pasta
	indexFile = 0
	try:
		for pdfFile in glob("*.pdf"):
			try:
				# Fazendo leitura do arquivo completo e passando para a variável
				tableListOfDataFrames = tabula.read_pdf(pdfFile, pages="all", lattice=True)

				# Indica que um arquivo completo foi lido com sucesso
				print("======================================================================\n"
					"LEITURA DE ARQUIVO - NÚMERO " + str(indexFile) + "\n"
					"O arquivo " + pdfFile + " foi lido e está pronto pra ser convertido\n",
				file=outputFile)

				# Remove extensão do arquivo, pegando apenas o nome e atribui pra variavel
				fileName = pdfFile[:-4]
				# Cria uma pasta para armazenar tabelas com o mesmo nome pra cada arquivo
				Path("../resultados/tabelas/" + fileName).mkdir(parents=True, exist_ok=True)

				# Para cada uma das tabelas 'DataFrames' contidos no arquivo csv completo 'lista de tabelas' será convertido
				indexDataFrame = 0
				for tableDataFrame in tableListOfDataFrames:
					try:
						# FAZENDO COM QUE O CABEÇALHO SE TORNE UMA LINHA COMUM
						# Cria ou limpa a lista que vai manipular o cabeçalho
						tableDataFrameHeader = []
						# Pegando o cabeçalho da tabela e passando ela como lista para a variável
						tableDataFrameHeader = [*tableDataFrame]
						# Removendo o cabeçalho da tabela atual
						tableDataFrame = tableDataFrame.T.reset_index().T.reset_index(drop=True)
						# Adicionando a lista como primeira linha do cabeçalho do DataFrame criado para manipular cabeçalho
						tableDataFrameHeader.insert(1, tableDataFrameHeader)
						# Concatenando à tabela principal
						pandas.concat([pandas.DataFrame(tableDataFrameHeader), tableDataFrame], ignore_index=True)

						# Removendo quebras de linha
						# O primeiro replace remove as que ocorrem por conta do corpo ser muito grande
						# O segundo replace remove as que acontecem por conta do ponto e vírgula
						tableDataFrame = tableDataFrame.replace({r"\r": ""}, regex=True).replace({r";": ","}, regex=True)

						tableDataFrame.to_csv(
							"../resultados/texto/"+ fileName + ".txt",
							index=False,
							index_label=False,
							header=False,
							line_terminator="\n", # Define a quebra de linha como '\n' para evitar conflito com o terminal que normalmente gera '\r' como quebra
							sep=";",
							mode="a"
						)

						excelWriter = pandas.ExcelWriter("../resultados/tabelas/" + fileName + "/" + str(indexDataFrame) + ".xlsx",
							engine='xlsxwriter'
						)
						tableDataFrame.to_excel(
							excelWriter,
							index=False,
							header=False,
							engine="xlsxwriter"
						)
						excelWriter.save()

						# Indica que uma tabela foi convertida com sucesso
						print(
							"______________________________________________________________________\n"
							"A tabela da página "+ str(indexDataFrame + 1) + " do PDF foi convertida |\n"
							"___________________________________________/\n",
							# Configurações
							file=outputFile
						)
						print(pandas.DataFrame(tableDataFrame), file=outputFile)
						indexDataFrame = indexDataFrame + 1
					except Exception as err: 
						# Fecha o design
						print("======================================================================", file=outputFile)

						print(
							"**********************************************************************\n"
							"--- ERRO ---\n"
							"\n"
							"Ocorreu um erro, ao tentar converter o arquivo\n"
							"\n"
							"Exception: " + str(err) + "\n"
							"**********************************************************************",
						file=outputFile)
						break
				print("======================================================================", file=outputFile)
				indexFile = indexFile + 1
					
			except Exception as err:
				# Fecha o design
				print("======================================================================", file=outputFile)

				print(
					"**********************************************************************\n"
					"--- ERRO ---\n"
					"Ocorreu um erro, ao tentar ler o arquivo\n"
					"\n"
					"Exception: " + str(err) + "\n"
					"**********************************************************************",
				file=outputFile)

	except Exception as err:
		# Fecha o design
		print("======================================================================", file=outputFile)

		print(
			"**********************************************************************\n"
			"--- ERRO ---\n"
			"Não há arquivos de PDF para serem convertidos\n"
			"**********************************************************************",
		file=outputFile)

Main()