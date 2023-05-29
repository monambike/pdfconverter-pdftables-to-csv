import argparse
from argparse import ArgumentParser

from pdfconverter.__variables__ import Var
from pdfconverter.argument.validate_arguments import ValidateArguments
from pdfconverter.output_info import errors


# region Public Methods

def set_arguments():
    # Criando e instanciando um novo parser e atribuindo para a variável sem permitir reconhecimento de abreviação
    # automático de argumentos
    Var.Arguments.parser_editable_main = argparse.ArgumentParser(allow_abbrev = False)

    # Adiciona os argumentos
    add_arguments_to_argument_parser(
        # PARA A ONDE IRÃO SER DIRECIONADOS OS ARGUMENTOS
        Var.Arguments.parser_editable_main,
        # ARGUMENTOS DE CONFIGURAÇÕES INICIAIS
        "ImportPath", # Argumento que conterá o caminho de importação (Obrigatório)
        "ExportPath", # Argumento que conterá o caminho de exportação (Opcional)
        "PageNumber", # Argumento que recebe o número de páginas para realizar a leitura do arquivo PDF
        # ARGUMENTOS REFERENTES AS COLUNAS
        "Lote",
        "Ordem",
        "Codigo",
        "Produto",
        "Unidade",
        "Quantidade",
        "ValorMedio",
        # ARGUMENTOS ADICIONAIS DE CONFIGURAÇÃO
        "MakeMappingColumnsFile", # Switch: Cria arquivo do terminal
        "MakeConversionDetailsFile", # Switch: Cria o arquivo contendo detalhes da conversão
        "MakeInfoFile" # Switch: Cria o arquivo de saída de informações
    )

    try:
        # Passa os argumentos após interpretados para uma nova variável.
        Var.Arguments.parser_main = Var.Arguments.parser_editable_main.parse_args(
            [
                "--ImportPath",
                "C:\\users\\dvp10\\desktop\\EDITAL (2).pdf",
                "--ExportPath",
                "C:\\users\\dvp10\\desktop",
                "--PageNumber",
                "all"
            ]
        )
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)

    # Valida os argumentos adicionados nas variáveis da classe de variáveis de argumentos
    ValidateArguments().validate_all()


def add_arguments_to_argument_parser(
    argument_parse_object: ArgumentParser,
    *arguments: str,
) -> None:
    try:
        for argument in arguments:
            argument_name: str = "--" + argument
            argument_quantity_value: str = "?"
            """Tipagem do argumento."""

            argument_parse_object.add_argument(
                # Valores passíveis de alteração
                argument_name,
                # Valores Inalteráveis
                nargs = argument_quantity_value, # Variável que define o número de valores suportados pelo argumento,
                                                 # além disso, é possível definir:
                                                 # - "+" = 1 ou mais, retorna uma lista;
                                                 # - "*" = 0 ou mais, retorna uma lista;
                                                 # - "?" = 0 ou 1, retorna uma string;
                                                 # - "[number]" = retorna uma lista;
                type = str,
                default = None,
                required = False
            )
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)

# endregion
