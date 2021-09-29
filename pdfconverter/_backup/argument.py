from terminalfile.message import error
from program import utilities
from __variables__ import fvar


def __ValidateImpExpPathsArgs():
    """
    ---
    ---
    ---
    
    ## __ValidateImpExpPathsArgs (Private)
    ---
    ---
    Método que valida os caminhos de importação e exportação passa-
    dos nos argumentos.
    
    ---
    ---
    ---
    """

    # [>] Valida os caminhos de importação e exportação fornecidos
    for pathType in ("import", "export"):
        # [>] Chama a variável de argumento de acordo com a ação reali-
        # zada
        # [i] Deve ser feito desse jeito pois a variável é uma variável
        # de argumento
        pathArgValue = getattr(avar.parser_ArgsMain, pathType.capitalize() + "Path")

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
                    # [i] Recebe o caminho da pasta de importação  como  referência
                    # para o caminho de exportação
                    fvar.folderpath_Export = fvar.folderpath_Import
            # Caso a pasta de acordo com a ação realizada não exista
            else:
                error.Show("A pasta de " + pathType + "ação ('" + pathArgValue + "') informada não existe.", ExitProgram = True)
        # [>] Quando ocorre erro desconhecido
        except Exception as ExceptionError:
            # [>] Exibe uma mensagem de erro
            error.Show(
                "Ocorreu um erro desconhecido ao tentar receber os argumentos "
                "dos caminhos de importação e exportação.",

                ExceptionError = ExceptionError,
                ExitProgram = True
            )