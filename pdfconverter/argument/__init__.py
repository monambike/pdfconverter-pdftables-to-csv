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
from pdfconverter.__variables__ import avar, pvar
# [i] Argumentos
from pdfconverter.argument.validateargs import validateargs
# [i] Arquivo do Terminal
from pdfconverter.terminalfile.message import error


#region PUBLIC METHODS

def Set():
    """
    ---
    ---
    ---

    ### Create (Public)
    ---
    Método que cria o ArgumentParser, que é uma ferramenta que rea-
    liza a interpretação de argumentos que são recebidos no momento
    em que a aplicação é chamada, sejam eles passados pelo  usuário
    ou por meio de algum terceiro programaticamente,  para  futuros
    usos.
    
    ---
    ---
    ---
    """

    # [>] Criando e instanciando um novo parser e atribuindo para a
    # variável sem permitir reconhecimento de abreviação automático
    # de argumentos
    avar.parser_Main = argparse.ArgumentParser(allow_abbrev = False)

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
        "ValorMedio", # [i] Valor Médio
        # ARGUMENTOS ADICIONAIS DE CONFIGURAÇÃO
        "FormattingMethod"
    )

    # [>] Valida os argumentos adicionados
    validateargs().All()

#endregion

#region PRIVATE METHODS

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
    
    # [>] Para cada argumento passado no parâmetro do  método  para
    # ser adicionado a variável principal de argumentos
    for arg in args:
        # VALORES PADRÃO
        # -------------------------------------------------------------
        # Descrição: Aqui estão os valores que são  definidos  por  pa-
        # drão.
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # [i] Nome do argumento
        # [>] Adiciona o prefixo no argumento
        avar.argName = "--" + arg
        # [i] Valor do argumento que vem por padrão
        avar.defaultValue = None
        # [i] Número de valores suportado pelo argumento
        avar.nargsValue = '?'
        """
        '+' == 1 or more.
        '*' == 0 or more.
        '?' == 0 or 1.
        """
        avar.contentType = str
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------

        # [i] Customização de argumentos
        # -------------------------------------------------------------
        # Descrição: Aqui dentro da condicional, podem ser alterados os
        # valores padrão caso necessário.
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        if (avar.argName == "--PageNumber"): avar.defaultValue = "all"
        elif (avar.argName in avar.patternColumnArgs): avar.nargsValue = '*'
        elif (avar.argName == "--FormattingMethod"): avar.defaultValue = "MFT"
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------


        # [>] Adiciona um argumento ao parser para cada String de argu-
        # mento que tiver sido passado no parâmetro.
        avar.parser_Main.add_argument(
            # [i] Valores passíveis de alteração
            avar.argName,
            default = avar.defaultValue,
            nargs = avar.nargsValue,
            type = avar.contentType,
            # [i] Valores Padrão
            required = False
        )
    
    try:
        # [>] Passa os argumentos depois de interpretados para uma nova
        # variável
        avar.parser_ArgsMain = avar.parser_Main.parse_args(_ParseArgsProgramatically())
    except Exception as ExceptionError:
        # [>] Exibe mensagem de erro caso não tenha sido informado  um
        # caminho de importação
        error.Show("Ocorreu um erro desconhecido ao tentar adicionar os argumentos ao parse args.", ExceptionError)

    # [>] Atualiza a variável que segura a lista com os  argumentos
    # relacionados ao campos de colunas que foram  preenchidos  com
    # algum valor
    __GetUserGivenPatternColumnsArgs()

def __GetUserGivenPatternColumnsArgs():
    """
    ---
    ---
    ---
    
    ## __StoreArgs (Private)
    ---
    ---
    Método que atualiza a  variável  que  vai  armazenar  todos  os
    argumentos relacionados  à  ordenação  de  colunas  que  tenham
    recebido algum valor pelo usuário.
    
    ---
    ---
    ---
    """

    counter_ArgListIterator = 0
    for argName in avar.patternColumnArgs:
        # [>] Recebe o valor do argumento atual baseado  na  lista  que
        # possui as colunas padrão
        argValue = vars(avar.parser_ArgsMain)[argName]
        # [>] Se o argumento da lista de colunas padrão tiver algum va-
        # lor
        if (argValue != None):
            # [>] Adiciona um novo container na lista de colunas
            pvar.list_UserGivenColumnToChange.append([])
            # [>] Adiciona o título do argumento
            pvar.list_UserGivenColumnToChange[counter_ArgListIterator].append(argName)

            # [i] Caso tenha vindo uma lista de valores
            if isinstance(argValue, list):
                # [>] Para cada valor na lista de valores passados na variável,
                # adiciona o valor na lista
                for value in argValue: pvar.list_UserGivenColumnToChange[counter_ArgListIterator].append(value)
            # [i] Caso contrário, adiciona o valor do argumento  direto  na
            # lista
            else: pvar.list_UserGivenColumnToChange[counter_ArgListIterator].append(argValue)

            # [>] Adiciona +1 ao contador da lista
            counter_ArgListIterator += 1

#endregion

#region METHODS FOR TESTING

def _ParseArgsProgramatically():
    """
    ---
    ---
    ---
    
    ## ParseArgsProgramatically Public
    ---
    ---
    Método que passa os argumentos que normalmente são passados pe-
    lo terminal programaticamente. O método deve ser colocado  den-
    tro da variável avar.parser_Main.parse_args.
    
    ### Returns
    ---
        list: Variável que segura os valores da lista de argumentos.
    
    ---
    ---
    ---
    """
    
    ArgsList = ["--ImportPath", "C:\\users\\dvp10\\desktop\\EDITAL (2).pdf"]
    ArgsList = [""]
    ArgsList = ["--ImportPath", "C:\\users\\dvp10\\desktop\\", "--ExportPath", "C:\\users\\dvp10\\desktop"]
    ArgsList = ["--ImportPath", "C:\\users\\dvp10\\desktop\\EDITAL (2).pdf", "--ExportPath", "C:\\users\\dvp10\\desktop", "--FormattingMethod", "F"]
    return ArgsList

#endregion