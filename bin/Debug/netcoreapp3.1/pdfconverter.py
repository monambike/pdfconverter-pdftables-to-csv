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
# Fazer com que caso tenha um ';' ele não passe os dados pra outra célula
pandas.options.display.latex.multicolumn = False
#Define o padrão de codificação para UTF-8 com BOM
pandas.options.display.encoding = "utf-16"

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

				strIndexFile = str(indexFile)

				# Indica que um arquivo completo foi lido com sucesso
				print("-------------------------------------------------------------------")
				print("CONVERSÃO (" + strIndexFile + ")")
				print("O arquivo " + pdfFile + " foi lido e está pronto pra ser convertido\n")


				# Para cada uma das tabelas 'DataFrames' contidos no arquivo csv completo 'lista de tabelas' será convertido
				indexDataFrame = 0
				for df in listOfDataFrames:
					try:
						df = df.replace({r'\r': ''}, regex=True)

						fileName = pdfFile[:-4] + "-" + str(indexDataFrame)

						df.to_csv("../resultados/tabelas-csv/" + fileName + ".csv", line_terminator="\n", sep=";", index=False)
						df.to_csv("../resultados/ponto_virgula-xls/" + fileName + ".xls", line_terminator="\n", sep=";", index=False)
						df.to_csv("../resultados/ponto_virgula-txt/" + fileName + ".txt", line_terminator="\n", sep=";", index=False)

						writer = pandas.ExcelWriter("../resultados/tabelas-xlsx/" + fileName + ".xlsx", engine='xlsxwriter')
						df.to_excel(writer, engine="xlsxwriter", index=False)
						writer.save()

						# Indica que uma tabela foi convertida com sucesso
						print("- O arquivo '" + fileName + "' foi convertido")
						print(pandas.DataFrame(df))
						indexDataFrame = indexDataFrame + 1
					except Exception as err:
						print("Ocorreu um erro, ao tentar converter o arquivo")
						print(err)
						breakline = input("-- pressione enter para continuar --")
						break
				print("-------------------------------------------------------------------")
				indexFile = indexFile + 1
					
			except Exception as err:
				print("Ocorreu um erro, ao tentar ler o arquivo")
				print(err)
				breakline = input("-- pressione enter para continuar --")

	except Exception as err:
		print("Não há arquivos de PDF para serem convertidos.")
		print("Erro:")
		print(str(err))
		breakline = input("-- pressione enter para continuar --")

def criarPastas():
	# Faz a verificação da existência das pastas a seguir e as cria caso elas ainda não existam
	Path(folderPDFs).mkdir(parents=True, exist_ok=True)
	Path(folderResultados).mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/tabelas-csv").mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/tabelas-xlsx").mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/ponto_virgula-txt").mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/ponto_virgula-xls").mkdir(parents=True, exist_ok=True)

Main()