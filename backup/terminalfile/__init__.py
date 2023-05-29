# """
# ---
# ---
# ---

# ## Package: pdfconverter >> terminalfile
# ---
# ---
# ### Module Name: terminalfile (Constructor, __init__)
# ---
# ### path: "pdfconverter\\\\\\\\terminalfile\\\\\\\\__init__.py"
# ---
# ---
# Pacote e módulo responsável por realizar ações relacionadas  ao
# arquivo do terminal.

# ---
# ---
# ---
# """


# # [>] Geral
# import os
# import stat
# # [>] PDFConverter
# # [>] Variáveis
# from pdfconverter.__variables__ import fvar
# # [>] Arquivo do Terminal
# from pdfconverter.terminalfile.message import error


# #region PUBLIC METHODS

# def Open():
#     """Abre o arquivo do terminal dentro de uma variável global."""

#     fvar.file_TerminalFile = open(
#         fvar.filepath_TerminalFile,  # [i] Caminho do arquivo de saída do terminal
#         "a",                        # [i] Realiza uma adição de texto
#         encoding="UTF-8"            # [i] Codificação UTF-8
#     )

# def Close():
#     """
#     Realiza o fechamento do arquivo de saída do terminal. Caso ele
#     não tenha sido aberto ainda, dispara um erro pro terminal e
#     para a aplicação.
#     """

#     try:
#         # [>] Tenta fechar o arquivo do terminal
#         fvar.file_TerminalFile.close()
#     except AttributeError:
#         error.Show("O arquivo do terminal não pode ser fechado pois ele não foi aberto ainda.")
#     except Exception as ExceptionError:
#         error.Show("Ocorreu um erro desconhecido ao tentar realizar o  fechamento do arquivo do terminal.", ExceptionError = ExceptionError,)

# def Recreate():
#     """Método que recria o arquivo de saída do terminal do zero."""

#     try:
#         # [>] Cria e/ou limpa o arquivo de texto contendo  a  saída  do
#         # terminal
#         fvar.file_TerminalFile = open(
#             fvar.filepath_TerminalFile, # [i] Caminho do arquivo de saída do terminal
#             "w",                        # [i] Realiza uma sobrescrita de texto
#             encoding="UTF-8"            # [i] Codificação UTF-8
#         )
#     except PermissionError:
#         # [>] Caso esteja como READONLY, remove a propriedade
#         os.chmod(fvar.filepath_TerminalFile, stat.S_IWRITE)

#         # [>] Cria e/ou limpa o arquivo de texto contendo  a  saída  do
#         # terminal
#         fvar.file_TerminalFile = open(
#             fvar.filepath_TerminalFile, # [i] Caminho do arquivo de saída do terminal
#             "w",                        # [i] Realiza uma sobrescrita de texto
#             encoding="UTF-8"            # [i] Codificação UTF-8
#         )
#     except Exception as ExceptionError:
#         # [>] Retorna o erro
#         error.Show(
#             "Ocorreu um erro desconhecido ao tentar realizar a abertura do"
#             "arquivo de saída do terminal",
            
#             ExceptionError = ExceptionError
#         )

# #endregion