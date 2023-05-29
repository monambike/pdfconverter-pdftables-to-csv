import csv
import sys

import tabula
import pandas
from pandas.core.frame import DataFrame

from pdfconverter import util
from pdfconverter.__variables__ import Var
from pdfconverter.output_info import errors


# region Fields


LIBRARY: str = "tabula"


# endregion

# region Public Methods


def make_file(
    file_full_name_pdf: str,
    reading_method: str
) -> None:
    try:
        with open(
            file = util.get_current_file_path_export(),
            mode = "w",
            encoding = "UTF-8"
        ) as text_file:
            # Realiza a leitura e limpa os DataFrames que estiverem vazios, quando feito, passa para uma variável
            Var.CurrentConvertedFileInfo.list_dataframe = [
                dataframe for dataframe in read_pdf(
                    reading_method = reading_method,
                    file_full_name_pdf = file_full_name_pdf
                ) if not dataframe.empty
            ]

            # Caso a lista de DataFrames vier vazia
            if(
                Var.CurrentConvertedFileInfo.list_dataframe is None
                or len(Var.CurrentConvertedFileInfo.list_dataframe) <= 0
            ):
                # Dispara um erro no arquivo do terminal
                errors.add_error(
                    error_description = (
                        "Não foram encontradas tabelas para realizar a conversão em {ReadingMethod}"
                        " usando o método de leitura {FileName} e a biblioteca {Library}."
                        .format(
                            FileName = file_full_name_pdf,
                            ReadingMethod = reading_method.capitalize(),
                            Library = LIBRARY.capitalize()
                        )
                    ),
                    stop_application = False
                )
                return
            text_file.write(
                build_string(
                    Var.CurrentConvertedFileInfo.list_dataframe
                )
            )
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


def read_pdf(
    reading_method: str,
    file_full_name_pdf: str
) -> list[DataFrame]:
    try:
        return tabula.read_pdf(
            input_path = Var.CurrentConvertedFileInfo.file_path_pdf,
            lattice = True if reading_method == "lattice" else False,
            pages = Var.ConversionInfo.page_numbers_to_read,
            guess = True,
            multiple_tables = True,
            pandas_options = {"dtype": "str"},
            silent = True
        )
    except Exception as exception:
        errors.add_error(
            error_description = (
                "Ocorreu um erro ao tentar realizar a leitura do arquivo '{FileName}' "
                "usando o método de leitura {ReadingMethod} e a biblioteca tabula."
                .format(
                    FileName = file_full_name_pdf,
                    ReadingMethod = reading_method
                )
            ),
            error_exception = exception,
            stop_application = False
        )


def build_string(list_dataframe) -> str:
    try:
        string: str = ""
        for dataframe in list_dataframe:
            string += format_dataframe(dataframe).to_csv(
                index = False,
                index_label = False,
                header = False,
                line_terminator = "\n",
                mode = "a",
                sep = ";",
                quoting = csv.QUOTE_ALL
            )
        return string
    except Exception as exception:
        errors.add_error(
            error_description = (
                "Ocorreu um erro, ao tentar converter o arquivo '{FileName}.pd"
                "f' usando o método de leitura {ReadingMethod} e a biblioteca "
                "tabula."
                .format(
                    FileName = Var.CurrentConvertedFileInfo.file_name_pdf,
                    ReadingMethod = Var.CurrentConvertedFileInfo.current_file_reading_library
                )
            ),
            stop_application = False,
            error_exception = exception
        )


def format_dataframe(dataframe: DataFrame) -> DataFrame | None:
    try:
        # Remove as aspas duplas do que estiverem no DataFrame para evitar possíveis erros, pois os dados
        # normalmente são separa dos por pontos e vírgulas, e aspas duplas
        new_dataframe = dataframe.replace("\"", "", regex = True)

        # Deleta todas as linhas que estão completamente vazias
        new_dataframe = new_dataframe.dropna(how = "all")
        # Deleta todas as colunas que estão completamente vazias
        new_dataframe = new_dataframe.dropna(how = "all", axis = 1)

        # Transforma o cabeçalho em uma linha comum
        new_dataframe = __convert_header_to_body_row(new_dataframe)

        # Remove quebras de linha do  DataFrame  que  acontecem
        # por conta do corpo ser muito grande
        new_dataframe.replace({r"\r": " "}, inplace = True, regex = True)
        # Troca ponto e vírgula dentro do DataFrame para evitar
        # conflitos
        new_dataframe.replace({r";": ","}, inplace = True, regex = True)

        return new_dataframe
    except Exception as exception:
        sys.exit()
        # errors.add_error_method_unknown_exception(error_exception = exception)


# endregion

# region Private Methods


def __convert_header_to_body_row(dataframe: DataFrame) -> DataFrame:
    # Pegando o cabeçalho da tabela e passando ela como lista para a temporária
    dataframe_header: list = [*dataframe]

    # Checando se a lista com o cabeçalho veio preenchida e se o cabeçalho não possui campos vazios
    if dataframe_header and "Unnamed" not in dataframe_header[0]:
        # Removendo o cabeçalho do DataFrame atual
        dataframe = dataframe.T.reset_index().T.reset_index(drop = True)

        # Adicionando a lista como primeira linha do corpo do Data-
        # Frame temporário
        dataframe_header.insert(1, dataframe_header)

        # Concatenando tabela temporária à tabela principal
        pandas.concat([pandas.DataFrame(dataframe_header), dataframe], ignore_index = True)

    return dataframe


# endregion
