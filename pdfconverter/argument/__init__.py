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
import os.path
import argparse
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import mvar, avar, fvar, pvar
# [i] Arquivo do Terminal
from pdfconverter.terminalfile.message import error
# [i] Conversão
from pdfconverter import conversion
# [i] Formatação de String
from pdfconverter.stringformat import stringformat
# [i] Programa
from pdfconverter.program import utilities


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
        "ValorMedio"  # [i] Valor Médio
    )

    
    # [>] Valida os argumentos
    __ValidateArgs()

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
    
    # [>] Para cada argumento passado no parâmetro do método
    for arg in args:
        # VALORES PADRÃO
        # -------------------------------------------------------------
        # Descrição: Aqui estão os valores que são  definidos  por  pa-
        # drão.
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # [i] Nome do argumento
        # [>] Adiciona o prefixo no argumento
        argName = "--" + arg
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
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -------------------------------------------------------------

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
            argName,
            default = defaultValue,
            nargs = nargsValue,
            type = contentType,
            # [i] Valores Padrão
            required = False
        )
    
    try:
        avar.parser_ArgsMain = avar.parser_Main.parse_args()
    except Exception as ExceptionError:
        # [>] Exibe mensagem de erro caso não tenha sido informado  um
        # caminho de importação
        error.Show(
            "Ocorreu um erro desconhecido ao tentar adicionar os argumentos"
            " ao parse args.",
            
            ExceptionError = ExceptionError,
            ExitProgram = True
        )

    # [>] Atualiza a variável que segura a lista com os  argumentos
    # relacionados ao campos de colunas que foram  preenchidos  com
    # algum valor
    __StoreArgs()

def __StoreArgs():
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
            else: pvar.list_columnFieldsToChange[listCounter].append(argValue)


            # [>] Adiciona +1 ao contador da lista
            listCounter += 1
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------

#region VALIDATION

def __ValidateArgs():
    """
    ---
    ---
    ---
    
    ## __ValidateArgs (Private)
    ---
    ---
    Método que chama outros métodos que realizam validação de argu-
    mentos.
    
    ---
    ---
    ---
    """

    __ValidateImportPath()
    __ValidateExportPath()
    __ValidatePageNumberArg()

#region SPECIFIC VALIDATIONS

def __ValidateImportPath():
    try:
        # [>] Pega dos argumentos o caminho de importação
        ImportPath = avar.parser_ArgsMain.ImportPath

        if (ImportPath == None):
            # [i] Exibe uma mensagem de erro mostrando que é obrigatório  a
            # inserção do caminho de importação
            error.Show(
                "É necessário colocar um valor para o caminho  de  importação,"
                "'--ImportPath <caminho_de_exportação>'.",
                
                ExitProgram = True
            )
        elif (os.path.isfile(ImportPath)):
            if (utilities.IsPDF(ImportPath)):
                fvar.path_Import = ImportPath
                # [>] Lá na frente, vai executar a função que realizará a  con-
                # versão do arquivo individual que foi indicado
                functionName = "IndividualConversion"
            else:
                error.Show("O arquivo informado no argumento de importação, precisa ser uma pasta ou um arquivo PDF.", ExitProgram = True)
        elif (os.path.isdir(ImportPath)):
            fvar.path_Import = ImportPath
            # [>] Lá na frente, vai executar a função que realizará  a  con-
            # versão de todos os PDFs indicados na pasta de importação
            functionName = "MultipleConversion"
        else:
            error.Show("O argumento ('" + ImportPath + "') passado como caminho de importação não é válido.", ExitProgram = True)

        # [>] Atribui o objeto que referencia a função com  o  nome  da
        # função passada nas validações acima
        mvar.ConversionStart = getattr(conversion, functionName)
    except Exception as ExceptionError:
        # [>] Exibe uma mensagem de erro
        error.Show(
            "Ocorreu um erro desconhecido ao tentar receber os  argumentos"
            "dos caminhos de importação.",

            ExceptionError = ExceptionError,
            ExitProgram = True
        )

def __ValidateExportPath():
    try:
        # [>] Pega dos argumentos o caminho de importação
        ExportPath = avar.parser_ArgsMain.ExportPath

        if (ExportPath == None):
            # [i] Recebe o caminho da pasta de importação  como  referência
            # para o caminho de exportação
            fvar.path_Export = fvar.path_Import
        # [>] Se o caminho fornecido for um diretório,  passa  para  as
        # variáveis globais de acordo com a ação realizada
        elif (os.path.isdir(ExportPath)): fvar.path_Export = ExportPath
        # [>] Usuário não informou valor para o caminho de exportação
        # Caso a pasta de acordo com a ação realizada não exista
        else: error.Show("A pasta de exportação ('" + ExportPath + "') informada não existe.", ExitProgram = True)
    except Exception as ExceptionError:
        # [>] Exibe uma mensagem de erro
        error.Show(
            "Ocorreu um erro desconhecido ao tentar receber os  argumentos"
            "dos caminhos de exportação.",

            ExceptionError = ExceptionError,
            ExitProgram = True
        )

def __ValidatePageNumberArg():
    """
    ---
    ---
    ---
    
    ## __ValidatePageNumberArg (Private)
    ---
    ---
    Método que valida o número de página, ou  números  de  páginas,
    passados no argumentos.
    
    ---
    ---
    ---
    """

    try:
        # [>] Recebe o número de página passado no argumento
        argPageNumber = stringformat(avar.parser_ArgsMain.PageNumber)
        # [>] Se o valor digitado como número de página é valido
        if (argPageNumber.ValidatePageNumber()):
            # [>] Passa o valor para uma variável
            fvar.readPDFPages = avar.parser_ArgsMain.PageNumber
        # [>] Se é inválido
        else:
            # [>] Exibe uma mensagem de erro
            error.Show(
                "O valor '" + avar.parser_ArgsMain.PageNumber + "' não é um va"
                "lor de número de página válido para --PageNumber.",
                
                ExitProgram = True
            )
    # [>] Quando ocorre erro desconhecido
    except Exception as ExceptionError:
        # [>] Exibe uma mensagem de erro
        error.Show(
            "Ocorreu um erro desconhecido ao validar o número de páginas.\n"
            "\n" +
            str(argPageNumber),

            ExceptionError = ExceptionError,
            ExitProgram = True
        )

#endregion

#endregion

#endregion