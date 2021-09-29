"""
---
---
---

## Package: pdfconverter >> settings
---
---
### Module Name: project
---
### path: "pdfconverter\\\\\\\\settings\\\\\\\\project.py"
---
---
Módulo  responsável  por  definir   configurações   diretamente
relacionadas a montagem e execução do projeto.

---
---
---
"""


# [>] Geral
import os
import pathlib
# [>] PDFConverter
from pdfconverter.__variables__ import fvar


#region PUBLIC METHODS

def SetFolderStructure():
    """Define a estrutura atual do projeto."""

    # [>] Cria uma nova pasta, caso já tenha uma chamada resultados
    int_indexFolderCreation = 0
    folderSufix = ""
    # [i] Enquanto houver uma pasta de resultados existente
    while (os.path.isdir(fvar.path_Export + fvar.rootPath + folderSufix)):
        # [>] Adiciona +1 ao contador
        int_indexFolderCreation += 1
        # [>] Arruma o nome do arquivo com o valor do contador
        folderSufix = " (" + str(int_indexFolderCreation) + ")"
    # [>] Atualiza o nome da pasta com o sufixo
    fvar.rootPath += folderSufix


    # [>] Criando pasta raíz
    pathlib.Path(
        fvar.path_Export +
        fvar.rootPath
    ).mkdir(parents = True, exist_ok = True)

    # [i] Para cada método, presente na lista de métodos
    for methodPath in fvar.list_readingPaths:
        # [>] Cria uma pasta
        pathlib.Path(
            fvar.path_Export +
            fvar.rootPath +
            methodPath
        ).mkdir(parents = True, exist_ok = True)

        # [>] Criando pastas para métodos de formatação
        for outputTypePath in fvar.list_formattingPaths:
            pathlib.Path(
                fvar.path_Export +
                fvar.rootPath +
                methodPath +
                outputTypePath
            ).mkdir(parents = True, exist_ok = True)

#endregion