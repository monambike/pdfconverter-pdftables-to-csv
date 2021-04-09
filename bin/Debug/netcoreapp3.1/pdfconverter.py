import pandas
import tabula
import xlsxwriter
from os import chdir
from glob import glob
from pathlib import Path

folderPDFs = "../../../../PDFs"
folderResultados = "../../../../resultados"

# CONFIGURAÇÕES DO PANDAS
# Evita com que os dados acabem sendo quebrados
pandas.options.display.expand_frame_repr = False
# Define o padrão de codificação para UTF-8 com BOM
pandas.options.display.encoding = "utf-8-sig"
# Mostra o dia primeiro quando encontrar data
pandas.options.display.date_dayfirst = True
# Fazer com que caso tenha um ';' ele não passe os dados pra outra célula
pandas.options.display.latex.multicolumn = False

def Main():
	criarPastas()
	#definirConfiguracoesPanda()

	# Pega todos os PDFs
	chdir(folderPDFs)
	
	# Pega todos os PDFs dentro da pasta
	indexFile = 0
	try:
		for pdfFile in glob("*.pdf"):
			try:
				# Fazendo leitura do arquivo completo e passando para a variável
				listOfDataFrames = tabula.read_pdf(pdfFile, pages="all", lattice=True)

				# Indica que um arquivo completo foi lido com sucesso
				print("======================================================================\n"
					"LEITURA DE ARQUIVO - NÚMERO " + str(indexFile) + "\n"
					"O arquivo " + pdfFile + " foi lido e está pronto pra ser convertido\n"
				)


				# Para cada uma das tabelas 'DataFrames' contidos no arquivo csv completo 'lista de tabelas' será convertido
				indexDataFrame = 0
				for df in listOfDataFrames:
					try:
						# Removendo quebras de linha
						df = df.replace({r'\r': ''}, regex=True)

						fileName = pdfFile[:-4] + "-" + str(indexDataFrame)

						df.to_csv("../resultados/texto/" + fileName + ".txt", index=False, line_terminator="\n", sep=";")
						df.to_csv("../resultados/teste.txt", index=False, line_terminator="\n", sep=";", mode="a")

						writer = pandas.ExcelWriter("../resultados/tabelas/" + fileName + ".xlsx", engine='xlsxwriter')
						df.to_excel(writer, index=False, engine="xlsxwriter")
						writer.save()

						# Indica que uma tabela foi convertida com sucesso
						print(
							"______________________________________________________________________\n"
							"A tabela da página "+ str(indexDataFrame + 1) + " do PDF foi convertida |\n"
							"___________________________________________/\n"
						)
						print(pandas.DataFrame(df))
						indexDataFrame = indexDataFrame + 1
					except Exception as err: 
						# Fecha o design
						print("======================================================================")

						print(
							"**********************************************************************\n"
							"--- ERRO ---\n"
							"\n"
							"Ocorreu um erro, ao tentar converter o arquivo\n"
							"\n"
							"Exception: " + str(err) + "\n"
							"**********************************************************************"
						)
						breakline = input("-- pressione enter para continuar --")
						break
				print("======================================================================")
				indexFile = indexFile + 1
				breakline = input("-- pressione enter para continuar --")
					
			except Exception as err:
				# Fecha o design
				print("======================================================================")

				print(
					"**********************************************************************\n"
					"--- ERRO ---\n"
					"Ocorreu um erro, ao tentar ler o arquivo\n"
					"\n"
					"Exception: " + str(err) + "\n"
					"**********************************************************************"
				)
				breakline = input("-- pressione enter para continuar --")

	except Exception as err:
		# Fecha o design
		print("======================================================================")

		print(
			"**********************************************************************\n"
			"--- ERRO ---\n"
			"Não há arquivos de PDF para serem convertidos\n"
			"**********************************************************************"
		)
		breakline = input("-- pressione enter para continuar --")

def criarPastas():
	# Faz a verificação da existência das pastas a seguir e as cria caso elas ainda não existam
	Path(folderPDFs).mkdir(parents=True, exist_ok=True)
	Path(folderResultados).mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/texto").mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/tabelas").mkdir(parents=True, exist_ok=True)

Main()