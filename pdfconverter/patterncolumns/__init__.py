"""
---
---
---

## Package: pdfconverter >> patterncolumns
---
---
### Module Name: patterncolumns (Constructor, __init__)
---
### path: "pdfconverter\\\\\\\\patterncolumns\\\\\\\\__init__.py"
---
---
Pacote e módulo comportando funções relacionadas à padronização
de arquivos resultantes da conversão.

---
---
---
"""


# [>] Geral
import re
import json
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import fvar, pvar
# [i] Programa
from pdfconverter.program.utilities.temporaryfile import temporaryfile


#region GLOBAL VARIABLES

# [C] PATTERN COLUMNS
# -------------------------------------------------------------
# Descrição:
# Variáveis que possuem relações com a definição de padrões nas
# colunas
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
list_textFileTSC = []
"""teste"""
tableIndex = -1
"""teste 2"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

#endregion

#region PUBLIC METHODS

def SetHeaderToPattern(String):
    newString = ""

    # [i] Regex que faz a verificação se o conteúdo da  li-
    # nha é um cabeçalho
    headerMatch = re.match(r"(^\"[a-zA-Z].*)", String)

    # [>] Se a linha for um cabeçalho
    if headerMatch is not None:
        # [>] Enxerga cada item do cabeçalho de cada tabela utilizando-
        # se de  uma  expressão regular e passa para uma lista
        list_CSVColumns = re.findall(
            r"""
            (?<=\")
            ([^\;]*?)
            (?=\")
            """,
            String,
            flags = re.MULTILINE | re.VERBOSE
        )


        columnIterator = 0
        # [>] Para cada coluna da linha vinda do  cabeçalho  encontrado
        # no arquivo CSV
        for column in list_CSVColumns:
            # [i] Variável que vai dizer se a coluna foi mencionada pelo u-
            # suário
            foundInArg = False
            # [i] Contador das colunas do CSV
            argContainerIterator = 0
            # [>] Ele olha cada container de argumentos na lista  de  argu-
            # mentos que o usuário forneceu, contendo os valores de colunas
            # que ele quer alterar
            for argContainer in pvar.list_columnFieldsToChange:
                # [>] Verifica se a coluna atual do CSV ta dentro do container
                if (column in argContainer):
                    # [>] Se estiver, olha cada valor do container atual
                    for lineitem in range(len(pvar.list_columnFieldsToChange[argContainerIterator])):
                        # [>] Caso seja o primeiro index
                        if lineitem == 0:
                            # [>] Pega como nome do argumento
                            argName = argContainer[lineitem]
                        # [>] Caso não seja o primeiro index
                        else:
                            # [>] Pega como valor do argumento
                            argValue = argContainer[lineitem]
                            # [>] E verifica se é igual o da coluna e se for
                            if (column == argValue):
                                # [>] Substitui o nome da coluna pelo que tá no argmento
                                newString += '"' + argName + '"'
                                # [>] Avisa a variável que foi encontrado  uma  correspondência
                                # de argumento para a coluna atual
                                foundInArg = True
                                # [>] Para o for
                                break
                            # [>] Se não for igual da coluna
                            else:
                                # [>] Parte para o próximo item da array até achar
                                continue
                # [>] Se a linha atual nao tiver dentro do container
                else:
                    # [>] Passa pro proximo container
                    continue
                argContainerIterator += 1
                # [>] Caso a linha tenha sua correspondência encontrada  dentro
                # do container atual
                if foundInArg is True:
                    # [>] Para a operação e parte para a próxima coluna
                    break
            # [>] Se ao término da operação
            else:
                # [>] For percebido que a coluna não foi mencionada pelo  usuá-
                # rio
                if not foundInArg:
                    # [i] Adiciona ela na String do jeito que ela tá
                    newString += '"' + column + '"'
            columnIterator += 1

            # [>] Pra cada coluna que for adicionada, se não for  a  última
            # coluna bota ';' na frente e se for coloca um '\n'
            newString += ';' if columnIterator < len(list_CSVColumns) else '\n'
    # [>] Se a linha não for um cabeçalho
    else:
        # [>] Devolve a String como estava
        newString = String

    return newString

def RecognizePattern(FileToReadPath):
    patterncolumnspath = fvar.path_Export + fvar.rootPath + "\pattercolumns.txt"
    LogDict = {
        'info': {
            'export_path': FileToReadPath,
            'pattern_path': patterncolumnspath 
        }
    }

    with open(FileToReadPath, "r", encoding = "UTF-8") as FileToRead:
        for line in FileToRead:
            # [i] Regex que faz a verificação se o conteúdo da  li-
            # nha é um cabeçalho
            headerMatch = re.match(r"(^\"[a-zA-Z].*)", line)

            # [>] Se a linha for um cabeçalho
            if headerMatch is not None:
                # [>] Enxerga cada item do cabeçalho de cada tabela utilizando-
                # se de  uma  expressão regular e passa para uma lista
                TextFile_CSVColumns = re.findall(
                    r"""
                    (?<=\")
                    ([^\;]*?)
                    (?=\")
                    """,
                    line,
                    flags = re.MULTILINE | re.VERBOSE
                )


                # [>] Para cada coluna da linha vinda do  cabeçalho  encontrado
                # no arquivo CSV
                for column in TextFile_CSVColumns:
                    # [>] Dentro da variável que armazena todas  as  recomendações,
                    # de todas as colunas, olha cada container (um container repre-
                    # senta o nome padrão e recomendações de uma colnua)
                    for container in pvar.StoredColumns:
                        # [>] Verifica se a coluna foi encontrada como recomendação  no
                        # container atual
                        if str(column).lower() in container:
                            LogDict[str(container[0]).replace("--","")] = column
                        # [>] Se não foi
                        else:
                            # [>] Passa para o próximo container
                            continue
                # [>] Para a operação
                break
            else:
                continue

        # [>] O arquivo com as colunas padrão está sendo atualmente ge-
        # rado na pasta de resultados
        with open(patterncolumnspath, mode = "w", encoding = "UTF-8") as TextFile:
            # [>] Transforma o dicionário de log em um JSON e escreve  den-
            # tro do arquivo
            TextFile.write(json.dumps(LogDict, indent = 4))

#endregion