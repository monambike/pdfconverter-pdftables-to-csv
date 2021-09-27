"""
---
---
---

## Package: pdfconverter >> program
---
---
### Module Name: utilities
---
### path: "pdfconverter\\\\\\\\program\\\\\\\\utilities.py"
---
---
Módulo que possui algumas funções  utilitárias  feitas  para  o
projeto.

---
---
---
"""

# [>] Geral
import re
import os.path


#region PUBLIC METHODS

# [>] Checa se a pasta passada no parâmetro existe
def CheckIfFolderExists(Folder = ""):
    """
    ---
    ---
    ---
    
    ## CheckIfFolderExists (Public)
    ---
    ---
    Checa se a pasta passada no parâmetro existe.
    
    ### Args
    ---
    - FolderThatWillBeChecked (str, [optional], default = ""):
        - Pasta que vai ter sua existência checada pelo método.
    
    ### Returns
    ---
        [bool]: Retorna 'True' se a pasta informada existe e  caso  não
        exista retorna 'False'.
    
    ---
    ---
    ---
    """

    # return True 
    # [>] Retorna pra função
    return True if (os.path.isdir(str(Folder))) else False

# [>] Justifica o texto
def JustifyText(Text, CharQuantity):
    """
    ### JustifyText (Public)
    ---
    Realiza a justificação do texto com a quantidade de caracteres
    informada.

    Args:
        Content ([str]): Texto no qual será justificado.
        CharQuantity ([int]): Quantidade de caracteres na qual a
        justificação de texto vai se basear.

    Returns:
        [str]: Retorna a String justificada.
    """

    return '\n'.join(re.findall('.{1,%i}' % int(CharQuantity), str(Text)))

#endregion