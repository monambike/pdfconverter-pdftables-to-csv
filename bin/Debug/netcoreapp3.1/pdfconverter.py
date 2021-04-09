import pandas
import tabula
from os import chdir
from glob import glob
from pathlib import Path

folderPDFs = "../../../../PDFs"
folderResultados = "../../../../resultados"

# CONFIGURAÇÕES
# Evita com que os dados acabem sendo quebrados
pandas.options.display.expand_frame_repr = False
# Fazer com que caso tenha um ';' ele não passe os dados pra outra célula
pandas.options.display.latex.multicolumn = False
#Define o padrão de codificação para UTF-8 com BOM
pandas.options.display.encoding = "utf-8-sig"

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
					df = df.replace({r'\r': ''}, regex=True)

					fileName = pdfFile[:-4] + "-" + str(indexDataFrame)

					df.to_csv("../resultados/tabelas/" + fileName + ".xls", line_terminator="\n", sep=";", index=False)
					df.to_csv("../resultados/csv/" + fileName + ".csv", line_terminator="\n", sep=";", index=False)
					df.to_csv("../resultados/texto/" + fileName + ".txt", line_terminator="\n", sep=";", index=False)

					# Indica que uma tabela foi convertida com sucesso
					print("- O arquivo '" + fileName + "' foi convertido")
					print(pandas.DataFrame(df))

					indexDataFrame = indexDataFrame + 1

				print("-------------------------------------------------------------------")
				indexFile = indexFile + 1
					
			except Exception as err:
				print("Ocorreu um erro, ao tentar converter o arquivo")
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
	Path(folderResultados + "/texto").mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/tabelas").mkdir(parents=True, exist_ok=True)
	Path(folderResultados + "/csv").mkdir(parents=True, exist_ok=True)


#def definirConfiguracoesPanda():

Main()