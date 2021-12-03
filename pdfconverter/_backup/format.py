# """
# ---
# ---
# ---

# ## Package: pdfconverter >> conversion
# ---
# ---
# ### Module Name: format
# ---
# ### path: "pdfconverter\\\\\\\\conversion\\\\\\\\format.py"
# ---
# ---
# Módulo comportando funções relacionadas à formatação.

# ---
# ---
# ---
# """

# # [>] Geral
# import re
# # [>] PDFConverter
# # [i] Variáveis
# from pdfconverter.__variables__ import fvar


# #region PUBLIC METHODS

# # [>] Inicia a formatação dos arquivos de texto
# def Start(ReadingMethod):
#     """
#     ---
#     ---
#     ---

#     ### Start (Public)
#     ---
#     Inicia a formatação dos arquivos de texto.

#     Args:
#         ReadingMethod ([type]): [description]
 
#     ---
#     ---
#     ---
#     """

#     # [C] CAMINHOS
#     # -------------------------------------------------------------
#     # Descrição:
#     # Variáveis que armazenam caminhos dos tipos de formatação.
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # [i] Formatação padrão, apenas exibindo caso e caso  tenha pe-
#     # lo menos um separador ";" na linha e removendo campos vazios
#     txtMainPath = fvar.folderpath_Export + fvar.rootPath + "\\" + ReadingMethod + "\\main\\" + fvar.filename_PDF + ".txt"
#     # [i] Formatação padrão, porém mantendo campos vazios
#     txtReturnBlankCellsPath = fvar.folderpath_Export + fvar.rootPath + "\\" + ReadingMethod + "\\tableWithBlankCells\\" + fvar.filename_PDF + ".txt"
#     # [i] Full Clear, formatação mais robusta
#     txtFullClearPath = fvar.folderpath_Export + fvar.rootPath + "\\" + ReadingMethod + "\\fullClear\\" + fvar.filename_PDF + ".txt"
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------

#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     # -------------------------------------------------------------


#     # [i] Abre o arquivo original presente na pasta 'withoutFormat-
#     # ting' para criar formatações baseadas nele
#     with open(fvar.filepath_ExportTxt, "r", encoding="UTF-8") as txtFile:
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

# #endregion