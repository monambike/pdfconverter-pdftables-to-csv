"""
---
---
---

## Package: pdfconverter >> argument
---
---
### Module Name: argument (Constructor, __init__)
---
### path: "pdfconverter\\\\\\\\argument\\\\\\\\__init__.py"
---
---
Pacote e módulo que comporta  todas  as  ações  relacionadas  à
argumentos no projeto

---
---
---
"""

# [>] Geral
import argparse
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import avar, fvar, pvar
# [i] Arquivo do Terminal
from pdfconverter.terminalfile.message import error
# [i] Program
from pdfconverter.program import utilities
# [i] Formatação de String
from pdfconverter import stringformat


#region PUBLIC METHODS

def Create():
    """
    ---
    ---
    ---

    ### Create (Public)
    ---
    Cria o ArgumentParser, que  é  uma  ferramenta  que  realiza  a
    interpretação de argumentos que são recebidos no momento em que
    a aplicação é chamada, sejam eles passados pelo usuário ou  por
    meio de algum terceiro programaticamente, para futuros usos.
    
    ---
    ---
    ---
    """

    # [>] Criando parser sem permitir abreviação
    avar.parser_Main = argparse.ArgumentParser(allow_abbrev=False)

    # [i] Adiciona os argumentos
    __AddArgs(
        # ARGUMENTOS DE CONFIGURAÇÕES INICIAIS
        "ImportPath", # [i] Argumento   que   conterá   o  caminho   de    importação
                        # (Obrigatório)
        "ExportPath", # [i] Argumento que conterá o caminho de exportação (Opcional)
        "PageNumber", # [i] Argumento que recebe o número de páginas para realizar  a
                        # leitura do arquivo PDF
        # ARGUMENTOS REFERENTES AS COLUNAS
        "Lote",       # [i] Lote
        "Ordem",      # [i] Ordem
        "Codigo",     # [i] Código
        "Produto",    # [i] Produto
        "Unidade",    # [i] Unidade
        "Quantidade", # [i] Quantidade
        "ValorMedio"  # [i] Valor Médio
    )

    
    # [>] Valida os argumentos
    __Validate()

#endregion

#region PRIVATE METHODS

def __Validate():
    """
    ---
    ---
    ---
    
    ## __Validate ([Public or Private?])
    ---
    ---
    [description]
    
    ---
    ---
    ---
    """

    # [>] Valida os caminhos de importação e exportação fornecidos
    for pathType in ("import", "export"):
        try:
            # [>] Chama a variável de argumento de acordo com a ação reali-
            # zada
            # [i] Deve ser feito desse jeito pois a variável é uma variável
            # de argumento
            pathArgValue = getattr(avar.parser_ArgsMain, pathType.capitalize() + "Path")
        except Exception as ExceptionError:
            error.Show(
                "Ocorreu um erro desconhecido relacionado ao referenciamento de"
                "variáveis através de Strings no método de validação de argumen"
                "tos.",

                ExceptionError = ExceptionError,
                ExitProgram = True
            )

        try:
            # [i] Caso a pasta de acordo com a ação realizada exista
            if (utilities.CheckIfFolderExists(pathArgValue)):
                # [>] Passa para as variáveis globais de acordo com a ação rea-
                # lizada
                setattr(fvar, "folderpath_" + pathType.capitalize(), pathArgValue)
            # [i] Caso não foram passados valores nos argumentos..
            elif (pathArgValue == None):
                # [>] ..de importação
                if (pathType == "import"):
                    # [i] Exibe uma mensagem de erro mostrando que é obrigatório  a
                    # inserção do caminho de importação
                    error.Show(
                        "É necessário colocar um valor para o caminho  de  importação,"
                        "'--ImportPath <caminho_de_exportação>'.",
                        
                        ExitProgram = True
                    )
                # [>] ..de exportação
                else:
                    # [i] Recebe o caminho do Script como referência para o caminho
                    # de exportação
                    fvar.folderpath_Export = fvar.folderpath_Script
            # Caso a pasta de acordo com a ação realizada não exista
            else:
                error.Show("A pasta de " + pathType + "ação ('" + pathArgValue + "') informada não existe.", ExitProgram = True)
        except Exception as ExceptionError:
            error.Show(
                "Ocorreu um erro desconhecido ao tentar receber os  argumentos"
                "dos caminhos de importação e exportação.",

                ExceptionError = ExceptionError,
                ExitProgram = True
            )

    try:
        argPageNumber = stringformat.ManipulateString(avar.parser_ArgsMain.PageNumber)
        # [>] Se o valor digitado como número de página é valido
        if (argPageNumber.ValidatePageNumber()):
            fvar.readPDFPages = avar.parser_ArgsMain.PageNumber
        # [>] Se é inválido
        else:
            error.Show(
                "O valor '" + avar.parser_ArgsMain.PageNumber + "' não é um va"
                "lor de número de página válido para --PageNumber.",
                
                ExitProgram = True
            )
    except Exception as ExceptionError:
        error.Show(
            "Ocorreu um erro desconhecido ao validar o número de páginas.\n"
            "\n" +
            str(argPageNumber),

            ExceptionError = ExceptionError,
            ExitProgram = True
        )

def __AddArgs(*args):
    """
    ---
    ---
    ---
    
    ## __AddArgs (Private)
    ---
    ---
    Método  que  realiza  a  adição  de  argumentos  com  os   seus
    respectivos nomes passados no argumento do método. Dentro desse
    método, é possível ainda customizar o argumento,  alterando  os
    valores padrão das variáveis.

    ### Args
    ---
    - args (str, optional):
        - Argumentos que vão ser adicionados à  variável  principal  de
        argumento, presente na classe de  variáveis  de  argumento,  no
        módulo de variáveis (avar.parser_Main).

    ---
    ---
    ---
    """
    
    # [>] Para cada argumento passado no parâmetro
    for arg in args:
        argValue = "--" + arg
        # [i] Valor do argumento que vem por padrão
        defaultValue = None
        # [i] Número de valores suportado pelo argumento
        nargsValue = '?'
        """
        # '+' == 1 or more.
        # '*' == 0 or more.
        # '?' == 0 or 1.
        """
        contentType = str

        # [i] Customização de argumentos
        # -------------------------------------------------------------
        # Descrição: Aqui dentro da condicional, podem ser alterados os
        # valores padrão caso necessário.
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        if (arg in "--PageNumber"):
            defaultValue = "all"
        if ("Path" not in arg # Se não for um
            and
            "PageNumber" != arg):
            nargsValue = '*'
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------


        # [>] Adiciona um argumento ao parser para cada String de argu-
        # mento que tiver sido passado no parâmetro.
        avar.parser_Main.add_argument(
            # [i] Valores passíveis de alteração
            argValue,
            default = defaultValue,
            nargs = nargsValue,
            type = contentType,
            # [i] Valores Padrão
            required = False
        )
    
    try:
        # [>] Adiciona os argumentos informados anteriormente na região
        # anterior ao parse args
        teste = [
            '--ImportPath',
            'C:\\users\\dvp10\\desktop',
            '--ExportPath',
            'C:\\users\\dvp10\\desktop',
            '--PageNumber',
            'all',

            '--Ordem',
            'Item',
            'Lote',
            
            '--Produto',
            'Medicamento',
            'Descrição do Item'
            
            '--ValorMedio',
            'Prev. Custo Unit. (R$)'
        ]
        avar.parser_ArgsMain = avar.parser_Main.parse_args(teste)
    except Exception as ExceptionError:
        # [>] Exibe mensagem de erro caso não tenha sido informado  um
        # caminho de importação
        error.Show(
            "Ocorreu um erro desconhecido ao tentar adicionar os argumentos"
            "ao parse args.",
            
            ExceptionError = ExceptionError,
            ExitProgram = True
        )

    # [>] Atualiza a variável que segura a lista com os  argumentos
    # relacionados ao campos de colunas que foram  preenchidos  com
    # algum valor
    __Update_argsColumnFields()

def __Update_argsColumnFields():
    """
    ### __Update_argsColumnFields (Private)
    ---
    Atualiza  a  variável  que  vai  segurar  e  possuir  todos  os
    argumentos relacionados  à  ordenação  de  colunas  que  tenham
    recebido algum valor pelo usuário.
    """


    # [>] Todos os argumentos que são  relacionados  à  alterar  as
    # colunas padrão dentro de uma array.
    patternColumnArgs = [
        "Lote",
        "Ordem",
        "Codigo",
        "Produto",
        "Unidade",
        "Quantidade",
        "ValorMedio"
    ]

    # ADICIONA OS VALORES À ARRAY
    # -------------------------------------------------------------
    # Descrição: Adiciona o nome e o valor dos argumentos do  orde-
    # nador de colunas no padrão para a array quando  eles  possuem
    # algum valor
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    listCounter = 0
    for argName in patternColumnArgs:
        # [>] Recebe o valor do argumento atual
        argValue = vars(avar.parser_ArgsMain)[argName]
        # [>] Se o argumento da lista de colunas padrão tiver algum va-
        # lor
        if (argValue != None):
            # [>] Adiciona uma nova linha na lista de colunas
            pvar.list_columnFieldsToChange.append([])

            # [>] Adiciona o nome do argumento
            pvar.list_columnFieldsToChange[listCounter].append(argName)

            if isinstance(argValue, list):
                for value in argValue:
                    # [>] Adiciona o valor do argumento
                    pvar.list_columnFieldsToChange[listCounter].append(value)
            else:
                pvar.list_columnFieldsToChange[listCounter].append(argValue)


            # [>] Adiciona +1 ao contador da lista
            listCounter += 1
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

#endregion