import os
from setuptools import setup, find_packages

def read(FileName):
    """
    ---
    ---
    ---
    
    ## read (Public)
    ---
    ---
    Método que retorna a leitura de um arquivo.
    
    ### Args
    ---
    - FileName (str):
        - Nome do arquivo que irá ser lido.
    
    ### Returns
    ---
        [type]: [description]
    
    ---
    ---
    ---
    """
    return open(os.path.join(os.path.dirname(__file__), FileName)).read()

setup(
    #region DESCRIÇÃO
    name = "pdfconverter",
    description = "Projeto que tem como objetivo realizar a leitura (utilizando-"
                  "se de bibliotecas externas) de arquivos PDF, identificar tabe"
                  "las e realizar a conversão para um arquivo CSV formatado.",
    #endregion
    #region AUTORIA
    author = "Vinícius Gabriel Marques de Melo",
    author_email = "vinicius_gabriel258@hotmail.com",
    url = "https://github.com/monambike",
    
    #endregion
    #region DESCRIÇÃO TÉCNICA E REQUERIMENTOS
    version = "1.0",
    license = "CC0",
    packages = find_packages(include=["pdfconverter", "pdfconverter.*"]),
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Customer Service",
        "License :: Free for non-commercial use",
        "Natural Language :: Portuguese (Brazilian)",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities"
    ],
    install_requires = [
        "numpy==1.20.2",
        "pandas==1.2.3",
        "pdfminer.six==20201018",
        "tabula-py==2.3.0"
    ]
    #endregion
)