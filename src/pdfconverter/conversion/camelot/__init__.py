import csv

import camelot.core
from camelot.core import TableList

from pdfconverter import util
from pdfconverter.__variables__ import Var
from pdfconverter.output_info import errors


# region Fields


LIBRARY: str = "camelot"


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
        ) as TextFile:
            TextFile.write(
                build_string(
                    read_pdf(
                        file_full_name_pdf = file_full_name_pdf,
                        reading_method = reading_method
                    )
                )
            )
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


def read_pdf(
    file_full_name_pdf: str,
    reading_method: str
) -> TableList:
    """
    Realiza a leitura das tabelas de um arquivo PDF, dado o caminho do arquivo.

    Args:
        file_full_name_pdf: Caminho do arquivo PDF.
        reading_method: Método de leitura que será utilizado para ler o PDF.

    Returns:
        Resultado da leitura realizada em um TableList.
    """

    try:
        return camelot.read_pdf(
            filepath = file_full_name_pdf,
            flavor = reading_method,
            pages = Var.ConversionInfo.page_numbers_to_read
        )
    except Exception as exception:
        errors.add_error(
            error_description = (
                "Ocorreu um erro ao tentar realizar a leitura do arquivo '{FileName}' "
                "usando o método '{ReadingMethod}' e a biblioteca {Library}."
                .format(
                    FileName = file_full_name_pdf,
                    ReadingMethod = reading_method,
                    Library = LIBRARY
                )
            ),
            stop_application = False,
            error_exception = exception
        )
        

def build_string(
    table_list: TableList
) -> str:
    string = ""

    try:
        for table in table_list:
            string += table.to_csv(
                index = False,
                index_label = False,
                header = False,
                mode = "a",
                sep = ";",
                quoting = csv.QUOTE_ALL
            )
    except Exception as exception:
        errors.add_error(
            error_description = (
                "Ocorreu um erro, ao tentar converter o arquivo '{FileName}.pd"
                "f' usando o método de leitura {ReadingMethod} e a biblioteca "
                "{Library}."
                .format(
                    FileName = Var.CurrentConvertedFileInfo.file_name_pdf,
                    ReadingMethod = Var.CurrentConvertedFileInfo.current_file_reading_library,
                    Library = LIBRARY
                )
            ),
            stop_application = False,
            error_exception = exception
        )

    return string


# endregion
