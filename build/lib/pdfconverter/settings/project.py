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
import os.path
import pathlib
# [>] PDFConverter
from pdfconverter.__variables__ import avar, fvar


#region PUBLIC METHODS

def SetFolderStructure():
    """Define a estrutura atual do projeto."""

    # [>] Cria uma nova pasta, caso já tenha uma chamada resultados
    int_indexFolderCreation = 0
    FolderSufix = ""
    # [>] Caminho da pasta de resultados sem o sufixo
    fvar.folderpath_Result = fvar.folderpath_Export + "\\" + fvar.foldername_Results
    # [i] Enquanto houver uma pasta de resultados existente
    while (os.path.isdir(fvar.folderpath_Result)):
        int_indexFolderCreation += 1
        # [>] Atualiza a pasta de resultados com o novo índice
        FolderSufix = " (" + str(int_indexFolderCreation) + ")"
        # [>] Passa o caminho da pasta de resultados, onde serão expor-
        # tados os arquivos com um novo sufixo
        fvar.folderpath_Result = fvar.folderpath_Export + "\\" + fvar.foldername_Results + FolderSufix

    # [>] Criando pasta raíz
    pathlib.Path(fvar.folderpath_Result).mkdir(parents = True, exist_ok = True)
    # [i] Para cada método de leitura, presente na lista de métodos
    # de leitura
    for methodPath in fvar.list_ReadingPaths:
        # [>] Cria uma pasta
        pathlib.Path(fvar.folderpath_Result + "\\" + methodPath).mkdir(parents = True, exist_ok = True)
        # [i] Para cada método de formatação, presente na lista de  mé-
        # todos de formatação
        for outputTypePath in fvar.list_FormattingPaths:
            # [>] Cria uma pasta
            pathlib.Path(fvar.folderpath_Result + "\\" + methodPath + "\\" + outputTypePath).mkdir(parents = True, exist_ok = True)

#endregion