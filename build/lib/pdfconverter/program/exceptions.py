"""
---
---
---

## Package: pdfconverter >> program
---
---
### Module Name: exceptions
---
### path: "pdfconverter\\\\\\\\program\\\\\\\\exceptions.py"
---
---
Módulo responsável por manter algumas exceções customizadas  do
programa PDFConverter.

---
---
---
"""


#region EXCEPTIONS

class InvalidFormattingType(Exception):
    """
    ---
    ---
    ---
    
    ## InvalidFormattingType
    ---
    ---
    Exceção disparada quando é passado como parâmetro, um método de
    formatação não existente ou não existente na condicional dentro
    do método que inicializa a conversão (ConversionStart).
    
    ### Default Message
    ---
    \"O  método   de   formatação   passado   como   parâmetro   em
    'ConversionStart' não existe.\"
    
    ---
    ---
    ---
    """

    def __init__(self, msg="O método de formatação passado como parâmetro em 'ConversionStart' não existe.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class RepeatedFormattingType(Exception):
    """
    ---
    ---
    ---
    
    ## InvalidFormattingType
    ---
    ---
    Exceção disparada quando é passado como parâmetro o mesmo  tipo
    de formatação mais de uma vez.
    
    ### Default Message
    ---
    \"Não se pode repetir o mesmo tipo de formatação  mais  de  uma
    vez.\"
    
    ---
    ---
    ---
    """

    def __init__(self, msg="Não se pode repetir o mesmo tipo de formatação mais de uma vez.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

#endregion