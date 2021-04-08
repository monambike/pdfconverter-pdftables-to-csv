import tabula
import pandas
from glob import glob
from os import chdir


	
def pandasTest():# CONFIGURAÇÕES
	# Evita com que os dados acabem sendo quebrados
	pandas.options.display.expand_frame_repr = False
	# Fazer com que caso tenha um ';' ele não passe os dados pra outra célula
	pandas.options.display.latex.multicolumn = False
	
	pandas.options.display.max_columns = None
	pandas.options.display.max_rows = None
	pandas.options.display.max_colwidth = None
	pandas.options.display.max_info_columns = 500
	pandas.options.display.encoding = "UTF-8"

	# Pega todos os PDFs dentro da pasta com o Script
	chdir(".")
	# Filtra por PDF
	for pdfFile in glob("*.pdf"):
		try:
			indexFile = 0

			# Fazendo leitura do arquivo completo e passando para a variável
			listOfDataFrames = tabula.read_pdf(pdfFile, pages="1", lattice=True, multiple_tables=True)

			# Indica que um arquivo completo foi lido com sucesso
			print("-------------------------------------------------------------------")
			print("CONVERSÃO (" + str(indexFile) + ")")
			print("O arquivo " + pdfFile + " foi lido e está pronto pra ser convertido\n")
			indexFile = indexFile = 1

			# CÓDIGO PRECISA SER TESTADO E IMPLEMENTADO AINDA
			# Faz a limpa de quebra de linha
			#for row_index, row in df.iterrows():
			#	if re.search(r"\\r", str(row)):
			#		print type(row)               #Return type is pandas.Series
			#		row.replace({r'\\r': ''} , regex=True)
			#		print row
			#		count += 1



			# Para cada uma das tabelas 'DataFrames' contidos no arquivo csv completo 'lista de tabelas' será convertido
			indexDataFrame = 0
			for df in listOfDataFrames:
				df.to_csv(pdfFile[:-4] + "-" + str(indexDataFrame) + ".csv")

				# Indica que uma tabela foi convertida com sucesso
				print("- O arquivo '" + pdfFile[:-4] + "-" + str(indexDataFrame) + ".csv' foi convertido")
				indexDataFrame = indexDataFrame + 1

				print(pandas.DataFrame(df))

			print("-------------------------------------------------------------------")
				
		except Exception as err:
			errorFile = open("error-file.txt", "w")
			errorFile.write("Ocorreu um erro ao tentar converter um arquivo.")

			print("Error {0}".format(str(err)))
			print("Ocorreu um erro, ao tentar converter o arquivo")
			breakline = input("-- pressione enter para continuar --")
	else:
		errorFile = open("error-file.txt", "w")
		errorFile.write("Não há arquivos de PDF para serem convertidos.")
		errorFile.close()

pandasTest()