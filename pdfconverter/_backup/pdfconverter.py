# # Sumário
# # _____________________________________________________________

# # [L] LEGENDA
# # -------------------------------------------------------------
# # Descrição:
# # Legenda que contém informações relacionadas à documentação do
# # Script.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #region

# # -------------------------------------------------------------
# # Grupos:
# # -------------------------------------------------------------
# # - REGIONS -
# # [G] - Grupo de funções (é delimitado por uma "region")
# # [L] - Grupo que contém a legenda (é delimitado por uma "regi-
# # on")
# # [V] - Grupo  de  variáveis  (pode  ser  delimitado  por   uma
# # "region" ou não)
# # - NÃO REGIONS -
# # [B] - Importação de bibliotecas
# # [C] - Conglomerado pequeno de variáveis 
# # [F] - Função
# # -------------------------------------------------------------
# #
# # -------------------------------------------------------------
# # Dicas:
# # -------------------------------------------------------------
# # [i] - Informação ou descrição abrangente
# # [>] - Execução de uma tarefa ou uma informação relacionada  à
# # ela
# # [e] - Exportação de um arquivo PDF convertido para CSV
# # -------------------------------------------------------------

# #endregion
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # _____________________________________________________________





# # Escopo
# # _____________________________________________________________

# # [V] VARIÁVEIS
# # -------------------------------------------------------------
# # Descrição:
# # Grupo que contém todas as  variáveis  globais  utilizadas  no
# # Script.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #region

# # [C] ARQUIVOS
# # -------------------------------------------------------------
# # Descrição:
# # Variáveis que armazenam possuem realações com arquivos direta
# # e indiretamente.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # [i] Nome do arquivo PDF que vai ser convertido  (sem a exten-
# # são)
# filename_PDF = ""
# # [i] Caminho atual para a raiz do projeto (os outros  caminhos
# # vão se basear nele)
# folderpath_Script = ""
# # [i] Caminho da pasta de importação onde os arquivos  PDF  vão
# # ser alocados
# folderpath_Import = ""
# # [i] Caminho da pasta onde os arquivos exportação vão ser alo-
# # cados
# folderpath_Export = ""
# # [i] Caminho para o arquivo do terminal
# filepath_TerminalFile = ""
# # [i] Caminho do arquivo de texto que vai ser gerado  pelo  PDF
# # que vai ser convertido
# filepath_ExportTxt = ""
# # [i] Variável que armazena o arquivo de saída do Terminal
# file_TerminalFile = ""
# # [i] Páginas que vão ser lidas para realizar a conversão
# readPDFPages = ""
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [C] CONTADORES
# # -------------------------------------------------------------
# # Descrição:
# # Variáveis auxiliares que atuam como contadores.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # [i] Índice do 'For' que manipula o Data Frame
# index_DataFrame = 0
# # [i] Índice do 'For' que manipula os arquivos PDF
# index_PdfFile = 1
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [C] VISUAL DO TERMINAL
# # -------------------------------------------------------------
# # Descrição:
# # Variáveis relacionadas ao visual de alguma parte  do  Script,
# # normalmente essas partes visuais estão diretamente relaciona-
# # das com a saída do terminal.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # [i] Linha gigante que vai ficar disposta  em  alguns  lugares
# # como divisão no terminal
# visual_GiantLine = (
#     "_________________________________________"
#     "_________________________________________"
#     "_________________________________________"
#     "_________________________________________"
#     "_________________________________________"
#     "_________________________________________"
#     "_________________________________________"
#     "_________________________________________"
#     "_________________________________________"
#     "_________________________________"
# )
# # [i] Variável que contém um espaço gigante usado em alguns la-
# # youts
# visual_BlankSpaces = (
#     "                                         "
#     "                                         "
#     "                                         "
#     "                                         "
#     "    "
# )
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [C] ARGUMENTOS
# # -------------------------------------------------------------
# # Descrição:
# # Variáveis relacionadas à alguma ação ou função relacionada  à
# # argumentos
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # [i] Variável que vai ser responsável por criar o parser.
# parser_Main = None
# # [i] Variável que vai ser responsável por fazer a  manipulação
# # dos argumentos dados.
# parser_ArgsMain = None
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [C] LISTAS
# # -------------------------------------------------------------
# # Descrição:
# # Variáveis que fazem gerenciamento de listas.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # [i] Variável que vai conter a lista de DataFrames de  um  de-
# # terminado arquivo PDF baseado em um método de leitura,  pode-
# # ndo ser lattice ou stream
# list_DataFrames = []
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# #endregion
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # _____________________________________________________________





# # Funções
# # _____________________________________________________________

# # [G] FUNÇÃO PRINCIPAL
# # -------------------------------------------------------------
# # Descrição:
# # Grupo que executa a função principal que faz operações  bási-
# # cas realiza a chamada de outras funções.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #region

# # [F] FUNÇÃO PRINCIPAL
# # -------------------------------------------------------------
# # Descrição:
# # Função que executa funcionalidades principais e chama  outras
# # funções
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def Main():
#     # [V] VARIÁVEIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Grupo contendo variáveis utilizadas na função atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
#     # -------------------------------------------------------------
#     # Descrição:
#     # Referenciamento de variáveis globais (suas  descrições  estão
#     # no grupo de variáveis globais localizadas no escopo do início
#     # do Script).
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     global filename_PDF
#     global index_DataFrame
#     global list_DataFrames
#     global folderpath_Import
#     global folderpath_Export
#     global index_PdfFile
#     global readPDFPages
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------


#     # CONFIGURAÇÕES INICIAIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Contém todas as chamadas de funções que realizam as  configu-
#     # rações iniciais para o funcionamento do Script.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # [>] Realiza as configurações da biblioteca Pandas
#     SetPandasSettings()
#     # [>] Cria o parser para manipular os argumentos
#     CreateParser()
#     # [>] Valida os argumentos
#     ValidateArguments()
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------
    

#     if (folderpath_Import != ""):
#         # [>] Direciona o sistema para a pasta indicada
#         os.chdir(folderpath_Import)
#         # [>] Filtra pelos PDFs na pasta onde foi indicada para o  sis-
#         # tema pelo "chdir"
#         for str_PdfFileFullName in glob("*.pdf"):
#             # [i] Se já não é mais o primeiro arquivo
#             if (index_PdfFile > 1):
#                 # [>] Fecha o leiaute referente ao arquivo anterior
#                 SetTerminalFile(True)
#                 print(
#                     "\n" +
#                     visual_GiantLine + "\n" +
#                     visual_GiantLine + "\n"
#                     "\n\n\n\n\n\n\n\n\n",
                    
#                     file = file_TerminalFile
#                 )
#                 SetTerminalFile(False)
#             # [>] Se é o primeiro arquivo ainda
#             else:
#                 # [>] Define a estrutura inicial do projeto
#                 SetProjectStructure()
                

#             # [>] Remove extensão do arquivo  (pegando  apenas  o  nome)  e
#             # atribui para a temporária
#             filename_PDF = str_PdfFileFullName[:-4]

#             # [>] Cria o título para leitura do arquivo no terminal
#             SetTerminalFile(True)
#             print(
#                 str_PdfFileFullName + visual_GiantLine + "\n" +
#                 visual_GiantLine + "\n\n\n\n" +
#                 visual_BlankSpaces + "                          ----- + -----\n\n" +
#                 visual_BlankSpaces + "         LEITURA DE ARQUIVO - NÚMERO " + str(index_PdfFile) + ", '" + str_PdfFileFullName + "'\n" +
#                 visual_BlankSpaces + "   O arquivo '" + filename_PDF + "' foi lido e está pronto pra ser convertido\n\n" +
#                 visual_BlankSpaces + "                          ----- + -----\n\n\n\n",
                
#                 file = file_TerminalFile
#             )
#             SetTerminalFile(False)



#             # MÉTODOS DE LEITURA E CONVERSÃO
#             # -------------------------------------------------------------
#             # Descrição:
#             # Primeiro faz a leitura e conversão pra Lattice e após  faz  o
#             # mesmo para o Stream
#             # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#             for method in range(2):
#                 # [i] Define o método de leitura Lattice
#                 if (method == 0):
#                     boolLattice = True
#                     conversionMethod = "lattice"
#                 # [i] Define o método de leitura Stream
#                 elif (method == 1):
#                     boolLattice = False
#                     conversionMethod = "stream"

#                 # LEITURA
#                 # -------------------------------------------------------------
#                 # Descrição:
#                 # Realiza a leitura.
#                 # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#                 try:
#                     # [>] Realiza a leitura usando um método de  leitura  fornecido
#                     # pelo "For"
#                     list_DataFrames = tabula.read_pdf(
#                         str_PdfFileFullName,
#                         guess = True,
#                         lattice = boolLattice,
#                         multiple_tables = True,
#                         pages = readPDFPages,
#                         pandas_options = {"dtype": "str"},
#                         silent = True
#                     )
#                 # [i] Quando ocorre um problema desconhecido na hora de  reali-
#                 # zar a leitura
#                 except Exception as exceptionError:
#                     # [>] Exibe a mensagem de erro
#                     ShowError(
#                         "Arquivo: " + str_PdfFileFullName + "\n"
#                         "Método de Conversão: " + conversionMethod + "\n"
#                         "\n"
#                         "Ocorreu um erro ao tentar realizar a leitura do arquivo '" + str_PdfFileFullName +  "' "
#                         "usando o método '" + conversionMethod + "'.",
                        
#                         exceptionError
#                     )
#                 # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#                 # -------------------------------------------------------------


#                 # CONVERSÃO
#                 # -------------------------------------------------------------
#                 # Descrição:
#                 # Realizando a conversão com o método indicado.
#                 # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#                 # [>] Reseta a variável
#                 index_DataFrame = 1
#                 # [>] Itera os DataFrames contidos na lista de  DataFrames  gerados
#                 # pela leitura do tabula
#                 for tableDataFrame in list_DataFrames:
#                     # [>] Remove as aspas duplas do que estiverem no DataFrame para
#                     # evitar possíveis erros pois os dados normalmente são  separa-
#                     # dos por pontos e vírgula e aspas duplas
#                     tableDataFrame = tableDataFrame.replace("\"", "", regex = True)

#                     # [>] Inicia a função que realiza a conversão com o método  in-
#                     # dicado
#                     ConversionStart(conversionMethod, tableDataFrame)
#                 try:
#                     # [>] Chama a função que formata o arquivo de texto gerado pela
#                     # conversão
#                     FormatTextFile(conversionMethod)
#                 except FileNotFoundError:
#                     ShowError(
#                         "A pasta de resultados foi apagada durante a conversão, a mesm"
#                         "a será encerrada.",
                    
#                         exitProgram = True,
#                         recreateTerminalFile = True
#                     )
#                 except Exception as exceptionError:
#                     ShowError (
#                         "Ocorreu um erro desconhecido ao tentar realizar a formatação "
#                         "da conversão, a mesma será encerrada.",
                        
#                         exceptionError,
#                         exitProgram = True
#                     )
#                 # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#                 # -------------------------------------------------------------
#             # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#             # -------------------------------------------------------------

#             # [>] Atribuindo mais um ao índice para indicar que  o  arquivo
#             # PDF foi convertido
#             index_PdfFile += 1
#         else:
#             # [i] Se até o término da operação algum  PDF  foi  convertido,
#             # fecha o leiaute do terminal
#             if (index_PdfFile > 1):
#                 # [>] Fecha o leiaute e pula 5 linhas
#                 SetTerminalFile(True)
#                 print(
#                     "\n" +
#                     visual_GiantLine + "\n" +
#                     visual_GiantLine,
                
#                     file = file_TerminalFile
#                 )
#                 SetTerminalFile(False)
#             # [i] Se ainda até o término da operação nenhum PDF foi conver-
#             # tido exibe um erro
#             else:
#                 # [>] Exibe o erro
#                 ShowError("Não há arquivos de PDF para serem convertidos.")
#     else:
#         ShowError("É necessário indicar um caminho de importação")
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# #endregion
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [G] CONFIGURAÇÕES INICIAIS
# # -------------------------------------------------------------
# # Descrição:
# # Grupo que executa as configurações iniciais e ao decorrer  do
# # exercício das tarefas do Script.
# # Há funções com diversos objetivos, dentre eles,  encontrar  o
# # caminho do arquivo de onde está sendo executado o Script, de-
# # finir o caminho onde será utilizado para criar a estrutura de
# # pastas, criar a estrutura de pastas onde serão  colocados  os
# # arquivos PDF e onde serão gerados os arquivos  exportados
# # e configurações adicionais da biblioteca Pandas
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #region

# # [F] FUNÇÃO QUE DEFINE O LOCAL DA RAÍZ DO PROJETO
# # -------------------------------------------------------------
# # Descrição:
# # Define o local da raíz do projeto, onde  os  outros  caminhos
# # irão se basear
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def SetCurrentPath():
#     # [V] VARIÁVEIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Grupo contendo variáveis utilizadas na função atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
#     # -------------------------------------------------------------
#     # Descrição:
#     # Referenciamento de variáveis globais (suas  descrições  estão
#     # no grupo de variáveis globais localizadas no escopo do início
#     # do Script).
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     global filepath_TerminalFile
#     global folderpath_Script
#     global file_TerminalFile
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------
    

#     # [i] Pegando o caminho até o executável ou script atual  e  a-
#     # tribuindo para a variável folderpath_Script
#     folderpath_Script = str(Path(__file__).parent.absolute())

#     # [>] Passa para a variável global o caminho do arquivo de tex-
#     # to do terminal
#     filepath_TerminalFile = folderpath_Script + "\\output.txt"

#     RecreateTerminalFile()
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [F] FUNÇÃO QUE CRIA O ARQUIVO DE SAÍDA DO TERMINAL
# # -------------------------------------------------------------
# # Descrição:
# # Função responsável por limpar ou criar o arquivo de saída  do
# # terminal.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def RecreateTerminalFile():
#     # [V] VARIÁVEIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Grupo contendo variáveis utilizadas na função atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
#     # -------------------------------------------------------------
#     # Descrição:
#     # Referenciamento de variáveis globais (suas  descrições  estão
#     # no grupo de variáveis globais localizadas no escopo do início
#     # do Script).
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     global file_TerminalFile
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------


#     try:
#         # [>] Cria e/ou limpa o arquivo de texto contendo  a  saída  do
#         # terminal
#         file_TerminalFile = open(filepath_TerminalFile, "w", encoding="UTF-8")
#     except PermissionError:
#         # [>] Caso esteja como READONLY, remove a propriedade
#         os.chmod(filepath_TerminalFile, stat.S_IWRITE)

#         # [>] Cria e/ou limpa o arquivo de texto contendo  a  saída  do
#         # terminal
#         file_TerminalFile = open(filepath_TerminalFile, "w", encoding="UTF-8")
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [F] FUNÇÃO QUE DEFINE A ESTRUTURA DE PASTAS DO PROJETO
# # -------------------------------------------------------------
# # Descrição:
# # Faz a verificação da existência das pastas a seguir e as cria
# # caso elas ainda não existam.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def SetProjectStructure():
#     # [V] VARIÁVEIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Grupo contendo variáveis utilizadas na função atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
#     # -------------------------------------------------------------
#     # Descrição:
#     # Listas que possuem os caminhos das pastas que vão  ser  gera-
#     # das.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # [C] CAMINHOS
#     # [i] Caminhos que indicam a localização das  pastas  raíz  que
#     # irão ser geradas futuramente.
#     rootPath = "\\resultados"
#     # [i] Caminhos que indicam a localização das pastas dos métodos
#     # de leitura que vão ser geradas futuramente dentro da pasta de
#     # exportação.
#     list_readingPaths = [
#         "\\lattice",
#         "\\stream"
#     ]
#     # [i] Caminhos que indicam a localização das pastas dos métodos
#     # de formatação que vão ser geradas futuramente dentro das pas-
#     # tas de métodos de leitura, que estão dentro da pasta  de  ex-
#     # portação.
#     list_formattingPaths = [
#         "\\main",
#         "\\fullClear",
#         "\\tableWithBlankCells",
#         "\\withoutFormatting"
#     ]
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

    
#     # [>] Cria uma nova pasta, caso já tenha uma chamada resultados
#     int_indexFolderCreation = 0
#     folderSufix = ""
#     # [i] Enquanto houver uma pasta de resultados existente
#     while (os.path.isdir(folderpath_Export + rootPath + folderSufix)):
#         # [>] Adiciona +1 ao contador
#         int_indexFolderCreation += 1
#         # [>] Arruma o nome do arquivo com o valor do contador
#         folderSufix = " (" + str(int_indexFolderCreation) + ")"
#     # [>] Atualiza o nome da pasta
#     rootPath = rootPath + folderSufix


#     # [>] Criando pasta raíz
#     Path(
#         folderpath_Export +
#         rootPath
#     ).mkdir(parents = True, exist_ok = True)

#     # [i] Para cada método, presente na lista de métodos
#     for methodPath in list_readingPaths:
#         # [>] Cria uma pasta
#         Path(
#             folderpath_Export +
#             rootPath +
#             methodPath
#         ).mkdir(parents = True, exist_ok = True)

#         # [>] Criando pastas para métodos de formatação
#         for outputTypePath in list_formattingPaths:
#             Path(
#                 folderpath_Export +
#                 rootPath +
#                 methodPath +
#                 outputTypePath
#             ).mkdir(parents = True, exist_ok = True)


#     # [>] Cria arquivo para exibir a saída do terminal, se já exis-
#     # tir o arquivo, limpa o mesmo
#     open(filepath_TerminalFile, "w").close()
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [F] FUNÇÃO QUE DEFINE E EXECUTA CONFIGURAÇÕES DO PANDAS
# # -------------------------------------------------------------
# # Descrição:
# # Configurações do Pandas que afetam o DataFrame e a  conversão
# # para texto.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def SetPandasSettings():
#     # [>] Configuração que evita com que dados sejam  quebrados  no
#     # arquivo exportado
#     pandas.options.display.max_colwidth = None
#     # [>] Configuração que evita com que os dados acabem sendo que-
#     # brados na saída do terminal
#     pandas.options.display.expand_frame_repr = False
#     # [>] Configuração que define  o  padrão  de  codificação  para
#     # UTF-8 com BOM
#     pandas.options.display.encoding = "UTF-8-sig"
#     # [>] Configuração que faz com que caso exista um ";"  ele  não
#     # passe os dados pra outra célula
#     pandas.options.display.latex.multicolumn = False
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# #endregion
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [G] SAÍDAS DE AVISOS
# # -------------------------------------------------------------
# # Descrição:
# # Grupo o que contém funções que executam a exibição de  avisos
# # relacionados ao arquivo que é gerado contendo informações que
# # são mostradas no terminal.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #region

# # [F] DEFINE O ESTADO DO TERMINAL
# # -------------------------------------------------------------
# # Descrição:
# # Define quando o terminal vai ser aberto ou quando vai ser fe-
# # chado.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def SetTerminalFile(asOpen = True):
#     # [V] VARIÁVEIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Grupo contendo variáveis utilizadas na função atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
#     # -------------------------------------------------------------
#     # Descrição:
#     # Referenciamento de variáveis globais (suas  descrições  estão
#     # no grupo de variáveis globais localizadas no escopo do início
#     # do Script).
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     global file_TerminalFile
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------


#     # [i] Caso o programador decida abrir o arquivo
#     if (asOpen):
#         # [>] Abre o arquivo de saída do terminal com "append"
#         file_TerminalFile = open(filepath_TerminalFile, "a", encoding="UTF-8")
#     # [i] Caso o programador decida fechar o arquivo
#     else:
#         # [>] Fecha o arquivo de saída do terminal
#         file_TerminalFile.close()
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [F] EXIBE UMA MENSAGEM DE ERRO
# # -------------------------------------------------------------
# # Descrição:
# # Função responsável por exibir mensagens de erros  disponíveis
# # nas Exceptions.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def ShowError(errorMessage, exceptionError = "", exitProgram = False, recreateTerminalFile = False):
#     # [>] Se desejado, recriar o arquivo de saída do terminal
#     if (recreateTerminalFile):
#         # [>] Recria o arquivo de saída do terminal
#         RecreateTerminalFile()
    
#     # [>] Justifica o conteúdo da mensagem corretamente
#     errorMessage = '\n'.join(re.findall('.{1,%i}' % 58, errorMessage))
#     # [>] Justifica a Exception corretamente
#     exceptionError = '\n'.join(re.findall('.{1,%i}' % 58, str(exceptionError)))

#     # [>] Abre o arquivo de saída do terminal
#     SetTerminalFile(asOpen = True)
#     # [>] Monta a caixa de mensagem
#     print(
#         "=============================================================\n"
#         "                                                             \n"
#         "                                                             \n"
#         "MENSAGEM DE RETORNO                                          \n"
#         "-------------------------------------------------------------\n"
#         "<d>" + errorMessage + "</d>\n"
#         ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
#         "<e>" + str(exceptionError) + "</e>\n"
#         ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
#         "-------------------------------------------------------------\n"
#         "                                                             \n"
#         "                                                             \n"
#         "=============================================================\n",
        
#         file = file_TerminalFile
#     )
#     # [>] Fecha o arquivo de saída do terminal
#     SetTerminalFile(asOpen = False)

#     # [>] Se desejado sair do programa
#     if (exitProgram):
#         # [>] Para o programa ao exibir o erro
#         sys.exit()
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# #endregion
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [G] CONVERSÃO
# # -------------------------------------------------------------
# # Descrição:
# # Grupo que contém funções que realizam a conversão dos  arqui-
# # vos PDF e toda a formatação necessária.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #region

# # TORNANDO O CABEÇALHO EM UMA LINHA COMUM
# # -------------------------------------------------------------
# # Descrição:
# # Isso é necessário para fazer com que não haja quebra de linha
# # onde o DataFrame identifica como cabeçalho (título) da tabela
# # caso o conteúdo delas seja muito grande.
# # Isso acontece porque o título tem uma formatação gerada  pelo
# # DataFrame que difere-se do corpo, o que acaba permitindo  que
# # isso ocorra. O trabalho dessa função é transformar o  cabeça-
# # lho em um texto de campo comum.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def TurnHeaderInSimpleRow(tableDataFrame):
#     # [>] Cria e limpa uma lista que vai ser usada para manipular o
#     # cabeçalho no DataFrame
#     tableDataFrameHeader = []

#     # [>] Pegando o cabeçalho da tabela e passando ela  como  lista
#     # para a temporária
#     tableDataFrameHeader = [*tableDataFrame]

#     # [i] Checando se a lista com o cabeçalho veio preenchida e  se
#     # o cabeçalho não possui campos vazios
#     if (tableDataFrameHeader and not "Unnamed" in tableDataFrameHeader[0]):
#         # [>] Removendo o cabeçalho do DataFrame atual
#         tableDataFrame = tableDataFrame.T.reset_index().T.reset_index(drop=True)

#         # [>] Adicionando a lista como primeira linha do corpo do Data-
#         # Frame temporário
#         tableDataFrameHeader.insert(1, tableDataFrameHeader)

#         # [>] Concatenando tabela temporária à tabela principal
#         pandas.concat([pandas.DataFrame(tableDataFrameHeader), tableDataFrame], ignore_index=True)
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [F] REALIZA A CONVERSÃO DO ARQUIVO
# # -------------------------------------------------------------
# # Descrição:
# # Realiza a conversão do arquivo PDF para CSV como  arquivo  de
# # texto.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def ConversionStart(conversionMethod, tableDataFrame):
#     # [V] VARIÁVEIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Grupo contendo variáveis utilizadas na função atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
#     # -------------------------------------------------------------
#     # Descrição:
#     # Referenciamento de variáveis globais (suas  descrições  estão
#     # no grupo de variáveis globais localizadas no escopo do início
#     # do Script).
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     global filepath_ExportTxt
#     global index_DataFrame
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------


#     try:
#         # [>] Deleta todas as linhas que estão completamente vazias
#         tableDataFrame = tableDataFrame.dropna(how="all")
        
#         # [>] Deleta todas as colunas que estão  completamente  va-
#         # zias
#         tableDataFrame = tableDataFrame.dropna(how="all", axis=1)

#         # [>] Chama a função que transforma o cabeçalho em  uma li-
#         # nha comum
#         TurnHeaderInSimpleRow(tableDataFrame)

#         # [>] Remove quebras de linha do  DataFrame  que  acontecem
#         # por conta do corpo ser muito grande
#         tableDataFrame.replace({r"\r": " "}, inplace=True, regex=True)

#         # [>] Troca ponto e vírgula dentro do DataFrame para evitar
#         # conflitos
#         tableDataFrame.replace({r";": ","}, inplace=True, regex=True)

#         # [>] Define o caminho do arquivo  atual  para  a  variável
#         # global filepath_ExportTxt
#         filepath_ExportTxt = folderpath_Export + "\\resultados\\" + conversionMethod + "\\withoutFormatting\\" + filename_PDF + ".txt"

#         # [>] Converte o arquivo para .txt no formato de um CSV
#         tableDataFrame.to_csv(
#             filepath_ExportTxt,
#             index = False,
#             index_label = False,
#             header = True,
#             line_terminator = "\n", # [i] Define a quebra de linha como '\n' para evitar conflito com o terminal que gera \r
#             mode = "a",
#             sep = ";",
#             quoting = csv.QUOTE_ALL
#         )

#         # [>] Indica ao terminal que uma tabela foi convertida  com
#         # sucesso
#         SetTerminalFile(True)
#         print(
#             "\n\n"
#             "          A tabela nº"+ str(index_DataFrame) + " do '" + filename_PDF + "' foi convertida usando '" + conversionMethod + "'\n"
#             "\________________________________________________________________________________/\n" +
#             "Search this (Ctrl + F): '" + filename_PDF + " " + conversionMethod + " tbl" + str(index_DataFrame) + "'\n",
            
#             file = file_TerminalFile
#         )

#         # [>] Imprime o DataFrame
#         print(pandas.DataFrame(tableDataFrame), file = file_TerminalFile)
#         SetTerminalFile(False)

#         index_DataFrame += 1
#     # [>] Caso haja um erro desconhecido na hora de realizar a con-
#     # versão
#     except Exception as exceptionError:
#         # [>] Exibe uma mensagem de erro
#         ShowError(
#             "Arquivo: " + filename_PDF + "\n"
#             "Método de Conversão: " + conversionMethod + "\n"
#             "\n"
#             "Ocorreu um erro, ao tentar converter o "
#             "arquivo '" + filename_PDF + ".pdf' usando o "
#             "método " + conversionMethod + ".",
            
#             exceptionError
#         )
#         return
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [F] LIMPA O ARQUIVO DE TEXTO CONVERTIDO
# # -------------------------------------------------------------
# # Descrição:
# # Limpa o arquivo de texto removendo todas as  linhas  que  não
# # contenham um separador (;), ou seja,  linhas  que  não  fazem
# # parte de uma tabela.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def FormatTextFile(conversionMethod):
#     # [V] VARIÁVEIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Grupo contendo variáveis utilizadas na função atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
#     # -------------------------------------------------------------
#     # Descrição:
#     # Referenciamento de variáveis globais (suas  descrições  estão
#     # no grupo de variáveis globais localizadas no escopo do início
#     # do Script).
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     global filepath_ExportTxt
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # [C] CAMINHOS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Variáveis que armazenam caminhos dos tipos de formatação.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # [i] Formatação padrão, apenas exibindo caso e caso  tenha pe-
#     # lo menos um separador ";" na linha e removendo campos vazios
#     txtMainPath = folderpath_Export + "\\resultados\\" + conversionMethod + "\\main\\" + filename_PDF + ".txt"
#     # [i] Formatação padrão, porém mantendo campos vazios
#     txtReturnBlankCellsPath = folderpath_Export + "\\resultados\\" + conversionMethod + "\\tableWithBlankCells\\" + filename_PDF + ".txt"
#     # [i] Full Clear, formatação mais robusta
#     txtFullClearPath = folderpath_Export + "\\resultados\\" + conversionMethod + "\\fullClear\\" + filename_PDF + ".txt"
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------


#     # [i] Abre o arquivo original presente na pasta 'withoutFormat-
#     # ting' para criar formatações baseadas nele
#     with open(filepath_ExportTxt, "r", encoding="UTF-8") as txtFile:
#         # ARQUIVOS
#         # -------------------------------------------------------------
#         # Descrição:
#         # Arquivo para caso a tabela possua itens vazios  que  precisam
#         # ser computados (esse arquivo apenas não terá o regex que apa-
#         # ga dados vazios e similares)
#         # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#         # [>] Abre o arquivo de texto "tableWithBlankCells"
#         txtTableWithBlankCells = open(txtReturnBlankCellsPath, "a", encoding="UTF-8")
#         # [>] Abre o arquivo principal (ainda não totalmente pronto pa-
#         # ra ser jogado em uma tabela possui mais dados, porém estrutu-
#         # ra ainda não tão idealizada)
#         txtMainFile = open(txtMainPath, "a", encoding="UTF-8")
#         # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#         # -------------------------------------------------------------

#         # [i] Navega por cada linha do documento de texto
#         for line in txtFile:
#             # [>] Detecta os dados vazios que estão presentes no  cabeçalho
#             # "Unnamed: X;"
#             line = re.sub(r"(\s?\"Unnamed:\s\d\d?\";?)", "", line)

#             # [>] Remove quebras de linha caso seja no meio dos  dados,  ou
#             # seja, caso não possua '"' atrás da quebra de linha e as subs-
#             # titui por um espaço para manter o padrão
#             line = re.sub(r"((?<!\")\n)", " ", line)

#             # Condicional que impede o continuamento do processo caso a va-
#             # riável esteja vazia, ou seja, caso tenha  sido  apagada  pelo
#             # processo anterior de limpeza
#             if (line != ""):
#                 # [>] Remove ponto e vírgula no final da linha
#                 line = re.sub(r"((?<=\");(?!.))", "", line)
                
#                 # [>] Remove todos os espaços no início de cada linha
#                 line = re.sub(r"(^\ *)", "", line)

#                 # [i] Se a linha possui aspas duplas no início  e  no  final  e
#                 # ainda possui menos que duas colunas cancela o código
#                 if (
#                     (
#                         (
#                             line.startswith("\"")
#                         )
#                         and 
#                         (
#                             line.endswith("\"") or line.endswith("\n")
#                         )
#                     )
#                     and
#                     (line.count("\"") < 3 and line.count(";") < 1)
#                 ):
#                     # [>] Não executa o código seguinte
#                     continue

#                 # [e] Exportação para a pasta: \\tableWithBlankCells
#                 txtTableWithBlankCells.write(line)
                
#                 # [>] Remove dados que estão vazios
#                 line = re.sub(r"(;\"\")|(\"\";)", "", line)

#                 # [>] Faz uma quebra de linha caso tenha aspas duplas  adjacen-
#                 # tes
#                 line = re.sub(r"(?<=\")(?=\")", "\n", line)

#                 # [>] Caso tenha um ponto e vírgula seguido de um espaço  troca
#                 # por uma quebra de linha
#                 line = re.sub(r"((?<=\");\ )", "\n", line)

#                 # [>] Caso tenha um espaço entre um separador e uma aspas dupla
#                 # remove o conteúdo que está atrás
#                 line = re.sub(r"((.*\";\ )(?=\"))", "", line)

#                 # [i] Se a linha possui aspas duplas no início  e  no  final  e
#                 # ainda possui menos que duas colunas cancela o código
#                 if (
#                     (
#                         (
#                             line.startswith("\"")
#                         )
#                         and 
#                         (
#                             line.endswith("\"") or line.endswith("\n")
#                         )
#                     )
#                     and
#                     (line.count("\"") < 3 and line.count(";") < 1)
#                 ):
#                     # [>] Não executa o código seguinte
#                     continue

#                 # [e] Exportação para a pasta: \\main
#                 txtMainFile.write(line)
    
#     # [>] Fecha o arquivo 'tableWithBlankCells'
#     txtTableWithBlankCells.close()
#     # [>] Fecha o arquivo 'main'
#     txtMainFile.close()

#     # [>] Abre o arquivo principal presente na  pasta  'main'  para
#     # criar formatações baseadas nele
#     with open(txtMainPath, "r", encoding="UTF-8") as txtFile:
#         # [>] Abre o arquivo de texto para  realizar  a  exportação
#         # fullClear
#         txtFullClearFile = open(txtFullClearPath, "a", encoding="UTF-8")

#         # [i] Navega por cada linha do documento de texto
#         for line in txtFile:
#             # [>] Caso a linha não comece com aspas deleta
#             line = re.sub(r"((^[^\"]).*)", "", line)
            
#             # [>] Caso a linha não termine com aspas deleta
#             line = re.sub('"(.*([^"\n]$))', "", line)

#             # [>] Remove Linhas vazias que só possuem quebra de linha  '\n'
#             # ou não possuem uma aspas dupla em nenhum lugar, serão excluí-
#             # das 
#             lineRemovedQuotes = ""
#             lineRemovedQuotes = re.sub(r"\"", "", line)

#             # [i] Se a temporária permanece igual, ou seja, não teve  aspas
#             # duplas removidas pelo regex
#             if (line == lineRemovedQuotes):
#                 # Quer dizer que ela ta errada e vai ser apagada
#                 line = ""
            
#             # [i] Só escreve a linha se tiver pelo menos mais que 3 colunas
#             # no arquivo fullClear
#             if (line.count("\"") > 6 and
#                 line.count(";") > 2):
#                 # [e] Exportação para a pasta: \\fullClear
#                 txtFullClearFile.write(line)
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# #endregion
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------


# # [G] MANIPULAÇÃO DE ARGUMENTOS
# # -------------------------------------------------------------
# # Descrição:
# # Grupo que contém funções que realizam a manipulação da bibli-
# # oteca que manipula argumentos, a 'argparse'.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #region

# # [F] CRIA O PARSER
# # -------------------------------------------------------------
# # Descrição:
# # Função que cria o parser que vai manipular os argumentos for-
# # necidos pelo usuário.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def CreateParser():
#     # [V] VARIÁVEIS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Grupo contendo variáveis utilizadas na função atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     # [C] REFERENCIAMENTO DE VARIÁVEIS GLOBAIS    
#     # -------------------------------------------------------------
#     # Descrição:
#     # Referenciamento de variáveis globais (suas  descrições  estão
#     # no grupo de variáveis globais localizadas no escopo do início
#     # do Script).
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     global parser_Main
#     global parser_ArgsMain
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------


#     # [>] Criando parser sem permitir abreviação
#     parser_Main = argparse.ArgumentParser(allow_abbrev=False)


#     # ARGUMENTOS UTILIZADOS NO PARSER
#     # -------------------------------------------------------------
#     # Descrição:
#     # Aqui estão dispostos os argumentos que vão ser passados  para
#     # o parser mais tarde.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # [i] Argumento   que   conterá   o  caminho   de    importação
#     # (Obrigatório)
#     parser_Main.add_argument(
#         "--importPath",
#         required = False,
#         default = "C:\\users\\dvp10\\desktop",
#         type = str
#     )
#     # [i] Argumento que conterá o caminho de exportação (Opcional)
#     parser_Main.add_argument(
#         "--exportPath",
#         required = False,
#         default = "C:\\users\\dvp10\\desktop",
#         type = str
#     )
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------


#     try:
#         # [>] Adiciona os argumentos informados anteriormente na região
#         # anterior ao parser
#         parser_ArgsMain = parser_Main.parse_args()
#     except:
#         # [>] Exibe mensagem de erro caso não tenha sido informado  um
#         # caminho de importação
#         ShowError("É necessário informar um caminho de importação.")
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [F] CHECA SE A PASTA PASSADA NO PARÂMETRO EXISTE
# # -------------------------------------------------------------
# # Descrição:
# # Função que faz uma validação de existência de uma pasta  pas-
# # sada como argumento.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def CheckIfFolderExists(folderThatWillBeChecked = ""):
#     # [>] Instancia a variável como não existente
#     currentFolderExists = False
#     # [i] Se a pasta fornecida existe
#     if (os.path.isdir(str(folderThatWillBeChecked))):
#         # [>] Define a mesma como existente na variável
#         currentFolderExists = True
#     # [>] Retorna pra função
#     return currentFolderExists
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# def ValidateArguments():
#     global folderpath_Import
#     global folderpath_Export
#     global readPDFPages

    
#     # Abre o arquivo de saída do terminal
#     SetTerminalFile(True)


#     # Se for recebido dois valores
#     if("frstPage" == "isNumberAndNotEmpty" and "scndPage" == "isNumberAndNotEmpty"):
#         # Procura no intervalo de páginas
#         readPDFPages = "frstPage" + "-" + "scndPage"
#     # Se for recebido um valor apenas
#     elif("frstPage" == "isNumberAndNotEmpty"):
#         # Procura na página solicitada
#         return
#     # Se não for recebido nenhum valor
#     elif("frstPage" == "empty" and "scndPage" == "empty"):
#         # Procura todas as páginas
#         return
#     # Se não encaixar nas outras condicionais
#     else:
#         print("erro")
#         # Retorna erro
#         return

#     readPDFPages = "all"


    

#     # VALIDAÇÃO DO CAMINHO DA PASTA DE IMPORTAÇÃO
#     # -------------------------------------------------------------
#     # Descrição:
#     # Faz a validação da existência do caminho que leva  as  pastas
#     # de importação. É obrigatória a inserção desse campo pelo usu-
#     # ário.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # [IMPORTAÇÃO - Obrigatório]
#     try:
#         # [i] Caso a pasta de importação exista
#         if (CheckIfFolderExists(parser_ArgsMain.importPath)):
#             # [>] Leva o caminho para a variável que segura os caminhos  de
#             # importação
#             folderpath_Import = parser_ArgsMain.importPath
#         # [i] Caso o usuário não tenha informado o caminho da pasta  de
#         # importação
#         elif (parser_ArgsMain.importPath == None):
#             # [>] Exibe uma mensagem de erro
#             ShowError("É necessário informar um caminho de importação com '--importPath <caminho>'.")
#             # [>] Encerra a operação
#             return
#         # [i] Caso a pasta de importação não exista
#         elif (CheckIfFolderExists(parser_ArgsMain.importPath) == False):
#             # [>] Exibe uma mensagem de erro
#             ShowError("O caminho de importação informado não existe.")
#             return
#         # [i] Caso apareça um erro não tratado
#         else:
#             # [>] Exibe uma mensagem de erro
#             ShowError("Ocorreu um erro desconhecido na hora de receber o caminho de importação.")
#     except Exception as exceptionError:
#         # [>] Exibe uma mensagem de erro
#         ShowError("O caminho de importação não pode ficar vazio.")
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#     # -------------------------------------------------------------
#     # VALIDAÇÃO DO CAMINHO DA PASTA DE EXPORTAÇÃO
#     # -------------------------------------------------------------
#     # Descrição:
#     # Faz a validação da existência do caminho que leva  as  pastas
#     # de exportação. A inserção desse caminho não é obrigatória,  e
#     # caso não seja preenchida, escolhe a mesma pasta na qual  está
#     # localizada o Script atual.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     try:
#         # [i] Caso o usuário tenha fornecido  o  caminho  da  pasta  de
#         # exportação faz a verificação.
#         if (CheckIfFolderExists(parser_ArgsMain.exportPath)):
#             # [i] Caso a verificação seja um sucesso, ou seja, e caso o ca-
#             # minho exista, atribui o caminho para a variável.
#             folderpath_Export = parser_ArgsMain.exportPath
#         # [i] Caso o usuário não tenha fornecido o caminho da pasta  de
#         # exportação, escolhe a pasta do Script como local para  alocar
#         # a pasta
#         elif (parser_ArgsMain.exportPath == None):
#             folderpath_Export = folderpath_Script
#         # [i] Caso o caminho não exista
#         elif (CheckIfFolderExists(parser_ArgsMain.exportPath) == False):
#             # [>] Exibe uma mensagem de erro
#             ShowError("O caminho de exportação informado não existe.")
#             # [>] Informa que o caminho de exportação não existe
#             exportFolderDoesntExist = True
#             return
#         # [i] Caso apareça um erro não tratado
#         else:
#             # [>] Exibe uma mensagem de erro
#             ShowError("Ocorreu um erro desconhecido na hora de receber o caminho de exportação.")
#     except:
#         # [i] Caso o usuário não tenha fornecido o caminho da pasta  de
#         # exportação, escolhe a pasta do Script como local para  alocar
#         # a pasta
#         folderpath_Export = folderpath_Script    
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # Fecha o arquivo de saída do terminal
#     SetTerminalFile(False)
#     return

# #endregion
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # _____________________________________________________________





# # Início do Script
# # _____________________________________________________________

# # [G] INÍCIO DO SCRIPT
# # -------------------------------------------------------------
# # Descrição:
# # Início da aplicação.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #region

# # [B] CHAMADA DE BIBLIOTECAS
# # -------------------------------------------------------------
# # Descrição:
# # Chamada de todas as bibliotecas do Script.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # [>] Importando bibliotecas
# import os
# import re
# import sys
# import csv
# import stat
# import pandas
# import argparse
# from glob import glob
# from pathlib import Path
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------


# # [>] Pega o caminho do Script atual e define o caminho do  ar-
# # quivo de saída do terminal
# SetCurrentPath()


# # [B] CHAMADA DA BIBLIOTECA TABULA
# # -------------------------------------------------------------
# # Descrição:
# # Tentativa de importação da biblioteca tabula.
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # [>] Tentando importar a biblioteca externa Tabula
# try:
#     import tabula
# # [i] Caso haja algum erro relacionado à importação
# except ImportError as exceptionError:
#     # [>] Exibe uma mensagem de erro
#     ShowError(
#         "Ocorreu um erro ao tentar importar a biblioteca tabula durant"
#         "e a inicialização do Script.\n"
#         "\n"
#         "Se você está executando ou chamando o Script PDFConverter pel"
#         "o executável, observe se a biblioteca tabula está em 'dist\pd"
#         "fconverter'.\n"
#         "Você pode copiar a pasta do tabula em:\n"
#         "'C:\\Users\\<YourUser>\\AppData\\Local\\Programs\\Python\\Pyt"
#         "hon39\\Lib\\site-packages'.\n"
#         "\n"
#         "Se você está chamando o Script diretamente pela extensão '.py"
#         "', então talvez você esqueceu de fazer referência à bibliotec"
#         "a ou de adicionar a mesma às variáveis ambiente?",
    
#         exitProgram = True
#     )
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # [>] Executa o Script
# Main()
# # [>] Garante a finalização da execução do Script
# sys.exit()

# #endregion
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # -------------------------------------------------------------

# # _____________________________________________________________