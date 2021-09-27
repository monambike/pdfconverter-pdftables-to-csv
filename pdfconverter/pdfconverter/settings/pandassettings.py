"""
---
---
---

## Package: pdfconverter >> settings
---
---
### Module Name: pandassettings
---
### path: "pdfconverter\\\\\\\\settings\\\\\\\\pandassettings.py"
---
---
Pacote e módulo que possui funções relacionadas à configurações
da biblioteca Pandas.

---
---
---
"""

# [>] Geral
import pandas


#region PRIVATE METHODS

def Set(MaxColumnWidth=None, ExpandFrameRepresentation=False, Encoding="UTF-8-sig", MultiColumn=False):
    """
    ---
    ---
    ---
    
    ## Set (Public)
    ---
    ---
    Define as configurações do Pandas. Ele já vem  configurado  por
    padrão, mas é possível alterar  os  valores  das  configurações
    passando os mesmos pelos parâmetros desse método.
    
    ### Args
    ---
    - MaxColumnWidth (int, optional, default = None):
        - Corresponde à largura máxima das colunas do pandas.
    - ExpandFrameRepresentation (bool, optional, default = False):
        - Configuração  que  evita  com  que  os  dados  acabem   sendo
        quebrados na saída do terminal durante a exibição do  DataFrame
        do Pandas.
    - Encoding (str, optional, default = "UTF-8-sig"):
        - Codificação do conteúdo interpretado pelo Pandas.
    - MultiColumn (bool, optional, default = False):
        - Configuração que faz com que caso exista um ';' com  que  ele
        não passe  os  dados para outra célula.
    
    ---
    ---
    ---
    """

    # [>] Configuração que evita com que dados sejam  quebrados  no
    # arquivo exportado
    pandas.options.display.max_colwidth = MaxColumnWidth
    # [>] Configuração que evita com que os dados acabem sendo que-
    # brados na saída do terminal
    pandas.options.display.expand_frame_repr = ExpandFrameRepresentation
    # [>] Configuração que define  o  padrão  de  codificação  para
    # UTF-8 com BOM
    pandas.options.display.encoding = Encoding
    # [>] Configuração que faz com que caso exista um ";"  ele  não
    # passe os dados pra outra célula
    pandas.options.display.latex.multicolumn = MultiColumn

#endregion