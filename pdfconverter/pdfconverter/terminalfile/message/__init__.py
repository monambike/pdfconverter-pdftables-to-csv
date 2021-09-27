"""
---
---
---

## Package: pdfconverter >> terminalfile >> message
---
---
### Module Name: message (Constructor, __init__)
---
### path: "pdfconverter\\\\\\\\terminalfile\\\\\\\\message\\\\\\\\__init__.py"
---
---
Pacote e módulo responsável pelo envio de mensagens ao terminal.

---
---
---
"""

# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import fvar
# [i] Arquivo do Terminal
from pdfconverter import terminalfile


#region PUBLIC METHODS

# [>] Joga a mensagem para o arquivo de saída do terminal
def Show(Message):
    # [>] Abre o arquivo de saída do terminal
    terminalfile.Open()

    # [>] Exibe a mensagem pro arquivo do terminal
    print(Message, file = fvar.file_TerminalFile)

    # [>] Fecha o arquivo de saída do terminal
    terminalfile.Close()

#endregion