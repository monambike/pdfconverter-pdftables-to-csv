"""
---
---
---

## Package: pdfconverter >> program >> utilities
---
---
### Module Name: utilities (Constructor, __init__)
---
### path: "pdfconverter\\\\\\\\program\\\\\\\\utilities\\\\\\\\__init__.py"
---
---
Pacote e módulo que possui algumas funções  utilitárias  feitas
para o projeto.

---
---
---
"""


# [>] Geral
import re
import os.path


#region PUBLIC METHODS

def IsPDF(File):
    """
    ---
    ---
    ---
    
    ## IsPDF (Public)
    ---
    ---
    Método que valida se o arquivo indicado é um arquivo PDF.
    
    ### Args
    ---
    - File ([bool]):
        - Arquivo que será conferido no método.
    
    ### Returns
    ---
        [bool]: Se o item indicado na variável for um arquivo e tiver a
        extensão ".pdf" retorna True, caso contrário retorna False
    
    ---
    ---
    ---
    """

    return True if(os.path.isfile(File) and (str(File[-4:]).lower() == ".pdf")) else False

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