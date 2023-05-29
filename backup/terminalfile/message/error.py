# """
# ---
# ---
# ---

# ## Package: pdfconverter >> terminalfile >> message
# ---
# ---
# ### Module Name: error
# ---
# ### path: "pdfconverter\\\\\\\\terminalfile\\\\\\\\message\\\\\\\\error.py"
# ---
# ---
# Módulo responsável por comportar funções que  mandam  relatório
# de erros formatados para o terminal.

# ---
# ---
# ---
# """
# # [>] PDFConverter
# # [i] Arquivo do Terminal
# from pdfconverter import terminalfile
# from pdfconverter.terminalfile import message
# # [i] Program
# from pdfconverter import program
# from pdfconverter.program import util


# #region PUBLIC METHODS

# def Show(ErrorMessage, ExceptionError = "", ExitProgram = True, RecreateTerminalFile = True):
#     # [>] Caso solicitado, recria o arquivo de saída do terminal
#     if (RecreateTerminalFile): terminalfile.Recreate()

#     # [>] Justifica o conteúdo da mensagem corretamente
#     ErrorMessage = util.JustifyText(ErrorMessage, 58)
#     # [>] Justifica o conteúdo da mensagem de exceção corretamente
#     ExceptionError = util.JustifyText(ExceptionError, 58)

#     # [>] Exibe a mensagem
#     message.Show(
#         "=============================================================\n"
#         "                                                             \n"
#         "                                                             \n"
#         "MENSAGEM DE RETORNO                                          \n"
#         "-------------------------------------------------------------\n"
#         "<d>" + ErrorMessage + "</d>\n"
#         ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
#         "<e>" + ExceptionError + "</e>\n"
#         ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
#         "-------------------------------------------------------------\n"
#         "                                                             \n"
#         "                                                             \n"
#         "=============================================================\n"
#     )

#     # [>] Caso solicitado, após exibir o erro para  a  execução  do
#     # programa
#     if (ExitProgram): program.Exit()

# #endregion