from setuptools import setup
from setuptools import find_packages

# region Public Methods

setup(
    # region Descrição
    name = "pdfconverter",
    description = "Projeto que tem como objetivo realizar a leitura (utilizando-"
                  "se de bibliotecas externas) de arquivos PDF, identificar tabe"
                  "las e realizar a conversão para um arquivo CSV formatado.",
    # endregion
    # region Autoria
    author = "Vinícius Gabriel Marques de Melo",
    author_email = "vinicius_gabriel258@hotmail.com",
    url = "https://github.com/monambike",
    
    # endregion
    # region Descrição Técnica e Detalhes
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
        "camelot-py~=0.9.0",
        "numpy~=1.20.2",
        "pandas~=1.2.3",
        "pdfminer.six~=20211012",
        "tabula-py~=2.3.0"
    ]

    # endregion
)

# endregion
