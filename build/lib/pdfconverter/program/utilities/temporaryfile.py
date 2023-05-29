"""
---
---
---

## Package: pdfconverter >> program >> utilities
---
---
### Module Name: temporaryfile
---
### path: "pdfconverter\\\\\\\\program\\\\\\\\utilities\\\\\\\\temporaryfile.py"
---
---
Módulo  responsável  por  fazer  a  manipulação   de   arquivos
temporários.

---
---
---
"""


# [>] Geral
import tempfile
# [i] Programa
from pdfconverter.program.utilities import time


#region GLOBAL VARIABLES

File = ""
"""Variável que armazena o objeto do arquivo temporário."""

#endregion

#region TEMPORARY FILE

class temporaryfile():
    def __init__(self, FilePrefix, FileSuffix = "", DeleteAfterFileClose = True):
        """
        ---
        ---
        ---
        
        ## __init__ (ifpublicmethod{Public}{ÒR}ifprivatemethod{ifPrivate}{OR}ifconstructor{Constructor, __init__})
        ---
        ---
        Método construtor responsável por realizar a criação do arquivo
        com algumas predefinições,  e  alguns  valores  que  podem  ser
        alterados por quem vai instanciar o objeto.
        
        ### Args
        ---
        - FilePrefix (str):
            - Prefixo do nome do arquivo.
        - FileSuffix (str, optional, default = ""):
            - Sufixo do nome do arquivo.
        - DeleteAfterFileClose (bool, optional, default = True):
            - Se deseja que o arquivo seja deletado após  o  fechamento  do
            mesmo via código ou ao término da execução do aplicativo.
        
        ---
        ---
        ---
        """

        global File
        File = tempfile.NamedTemporaryFile(
            mode = "w+",
            prefix = "PDFConverter_" + FilePrefix + "_" + time.GetDateAndTime(),
            suffix = FileSuffix + "_.tmp",
            delete = DeleteAfterFileClose
        )

    def Write(self, String):
        # [i] Escrita
        # [>] Escreve a linha
        File.write(String)

    def ReadAllLines(self):
        # [i] Leitura
        # [>] Move o cursor para o início do arquivo
        File.seek(0,0)
        # [>] Escreve a linha
        return File.readlines()

    def Close(self):
        # [>] Fecha o arquivo, e deleta caso tenha não tenha sido  con-
        # figurado 'DeleteAfterFileClose' como 'False'
        # -------------------------------------------------------------
        File.close()


#endregion