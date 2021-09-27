"""
---
---
---

## Package: pdfconverter >> terminalfile >> message
---
---
### Module Name: error
---
### path: "pdfconverter\\\\\\\\terminalfile\\\\\\\\message\\\\\\\\error.py"
---
---
Módulo responsável por comportar funções que  mandam  relatório
de erros formatados para o terminal.

---
---
---
"""
# [>] PDFConverter
# [i] Arquivo do Terminal
from pdfconverter import terminalfile
from pdfconverter.terminalfile import message
# [i] Program
from pdfconverter import program
from pdfconverter.program import utilities


#region PUBLIC METHODS

def Show(ErrorMessage, ExceptionError = "", ExitProgram = False, RecreateTerminalFile = False):
    # [>] Se desejado, recriar o arquivo de saída do terminal
    if (RecreateTerminalFile):
        # [>] Recria o arquivo de saída do terminal
        terminalfile.Recreate()

    # [>] Justifica o conteúdo da mensagem corretamente
    ErrorMessage = utilities.JustifyText(ErrorMessage, 58)
    # [>] Justifica o conteúdo da mensagem de exceção corretamente
    ExceptionError = utilities.JustifyText(ExceptionError, 58)

    # [>] Conteúdo da mensagem de erro
    Message = (
        "=============================================================\n"
        "                                                             \n"
        "                                                             \n"
        "MENSAGEM DE RETORNO                                          \n"
        "-------------------------------------------------------------\n"
        "<d>" + ErrorMessage + "</d>\n"
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
        "<e>" + ExceptionError + "</e>\n"
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
        "-------------------------------------------------------------\n"
        "                                                             \n"
        "                                                             \n"
        "=============================================================\n"
    )

    # [>] Exibe a mensagem
    message.Show(Message)

    # [>] Se desejado sair do programa
    if (ExitProgram):
        # [>] Para o programa ao exibir o erro
        program.Exit()

#endregion