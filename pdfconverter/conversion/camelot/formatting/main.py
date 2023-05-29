from pdfconverter import util
from pdfconverter.conversion.string_format import StringFormat
from pdfconverter.conversion.tabula.formatting import tablewithblankcells
from pdfconverter.output_info import errors


# region Public Methods


def make_file():
    try:
        with open(
            file = util.get_current_file_path_export(),
            mode = "a",
            encoding="UTF-8"
        ) as TextFile:
            TextFile.write(format_text_file("<without_formatting_variable_or_path"))
    except Exception as exception:
        errors.add_error_method_unknown_exception(exception)


def format_text_file(text_file_path: str):    
    string = ""
    # Abre o arquivo original presente na pasta 'withoutFormat-
    # ting' para criar formatações baseadas nele
    with open(
        file = text_file_path,
        mode = "r",
        encoding="UTF-8"
    ) as text_file:
        for line in text_file:
            # Realiza as formatações já existentes em tableWithBlankCells
            line = tablewithblankcells.format_string(line)
            if line == ("" or None):
                continue
            # Realiza a formatação do módulo vigente
            line = format_string_line(line)
            if line == ("" or None):
                continue

            # Adiciona à nova String
            string += line
    # Devolve pro método a nova String
    return string


def format_string_line(string):
    # Cria um novo objeto para manipular a String
    string_format = StringFormat(string)

    # Realiza a limpeza no arquivo do Camelot para melhor leitura
    string_format.test_camelot_regex()

    return string_format.return_string()


# endregion
