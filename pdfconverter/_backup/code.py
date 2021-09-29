# [B] CHAMADA DE BIBLIOTECAS
# -------------------------------------------------------------
# Descrição:
# Chamada de todas as bibliotecas do Script.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import os
import re
import sys
import csv
import stat
import pandas
import argparse
import tabula
from glob import glob
from pathlib import Path
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# Caso tentar fazer a implementação desse tratamento de  volta,
# olhar bem se da pra encaixar ou se precisa fazer alteração, e
# não esquecer de remover o import atual

# [B] CHAMADA DA BIBLIOTECA TABULA
# -------------------------------------------------------------
# Descrição:
# Tentativa de importação da biblioteca tabula.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [>] Tentando importar a biblioteca externa Tabula
try:
    import tabula
# [i] Caso haja algum erro relacionado à importação
except ImportError as exceptionError:
    from terminalfile.message import error
    # [>] Exibe uma mensagem de erro
    error.Show(
        "Ocorreu um erro ao tentar importar a biblioteca tabula durant"
        "e a inicialização do Script.\n"
        "\n"
        "Se você está executando ou chamando o Script PDFConverter pel"
        "o executável, observe se a biblioteca tabula está em 'dist\pd"
        "fconverter'.\n"
        "Você pode copiar a pasta do tabula em:\n"
        "'C:\\Users\\<YourUser>\\AppData\\Local\\Programs\\Python\\Pyt"
        "hon39\\Lib\\site-packages'.\n"
        "\n"
        "Se você está chamando o Script diretamente pela extensão '.py"
        "', então talvez você esqueceu de fazer referência à bibliotec"
        "a ou de adicionar a mesma às variáveis ambiente?",
    
        exitProgram = True
    )
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------