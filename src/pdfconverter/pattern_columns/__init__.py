import json
import re

from pdfconverter.__variables__ import Var
from pdfconverter.output_info import errors


# region Fields


log_dict: dict = {}


# endregion

# region Public Methods


def make_file(file_path: str) -> None:
    try:

        # Se o parâmetro de caminho do método for preenchido utiliza-o, caso não, usa o argumento passado pelo usuário,
        # se o usuário não informou um valor usa o valor padrão
        path = file_path if file_path != "" else Var.ConversionInfo.folder_path_export

        # O arquivo com as colunas padrão está sendo atualmente ge-
        # rado na pasta de resultados
        with open(
            file = path + "\\pattern_columns.txt",
            mode = "w",
            encoding = "UTF-8"
        ) as TextFile:
            # Transforma o dicionário de log em um JSON e escreve  dentro do arquivo
            TextFile.write(json.dumps(log_dict, indent = 4))
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


def test(file_to_read_path: str) -> None:
    with open(
        file = file_to_read_path,
        mode = "r",
        encoding = "UTF-8"
    ) as file_to_read:
        for line in file_to_read:
            # Regex que faz a verificação se o conteúdo da  linha é um cabeçalho
            header_match = re.match(r"(^\"[a-zA-Z].*)", line)

            # Se a linha for um cabeçalho
            if header_match is not None:
                # Enxerga cada item do cabeçalho de cada tabela utilizando se de  uma  expressão regular e passa para
                # uma lista
                text_file_csv_columns = re.findall(
                    r"""
                    (?<=\")
                    ([^;]*?)
                    (?=\")
                    """,
                    line,
                    flags = re.MULTILINE | re.VERBOSE
                )

                # Para cada coluna da linha vinda do  cabeçalho  encontrado
                # no arquivo CSV
                for column in text_file_csv_columns:
                    # Dentro da variável que armazena todas as recomendações, de todas as colunas, olha cada container
                    # (um container representa o nome padrão e recomendações de uma colnua)
                    for container in pvar.StoredColumns:
                        # Verifica se a coluna foi encontrada como recomendação no container atual
                        if str(column).lower() in container:
                            log_dict[str(container[0]).replace("--", "")] = column
                # Para a operação
                break


def update():
    return


# endregion

# region Private Methods


def is_a_header(string):
    return True if re.match(r"(^\"[a-zA-Z].*)", string) is not None else False


# endregion
