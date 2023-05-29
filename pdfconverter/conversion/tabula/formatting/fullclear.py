from pdfconverter import util
from pdfconverter.conversion.string_format import StringFormat
from pdfconverter.conversion.tabula.formatting import main
from pdfconverter.conversion.tabula.formatting import tablewithblankcells
from pdfconverter.output_info import errors


# region Public Methods


def make_file() -> None:
    try:
        # Abre o arquivo principal (ainda não totalmente pronto para
        # ser jogado em uma tabela possui mais dados, porém estrutura
        # ainda não tão idealizada)
        with open(
            file = util.get_current_file_path_export(),
            mode = "a",
            encoding="UTF-8"
        ) as TextFile:
            # Formata o arquivo e escreve um novo arquivo de saída
            TextFile.write(
                format_text_file("Var.filepath_WithoutFormatting")
            )
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


def format_text_file(file_path_text_file: str) -> str:
    try:
        string: str = ""

        # Abre o arquivo original presente na pasta 'withoutFormat-
        # ting' para criar formatações baseadas nele
        with open(
                file = file_path_text_file,
                mode = "r",
                encoding="UTF-8"
        ) as TextFile:
            # Navega por cada linha do documento de texto
            for line in TextFile:
                # Realiza as formatações já existentes em tableWithBlankCells
                line = tablewithblankcells.format_string(line)
                if line == ("" or None):
                    continue
                # Realiza as formatações já existentes em main
                line = main.format_string_line(line)
                if line == ("" or None):
                    continue
                # Realiza a formatação do módulo vigente
                line = format_string(line)
                if line == ("" or None):
                    continue

                # Adiciona à nova String
                string += line

        return string
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


def format_string(string: str) -> str:
    try:
        # Cria um novo objeto para manipular a String
        string_formatting: StringFormat = StringFormat(string)

        if string_formatting.string == "":
            return ""

        # Caso a linha não comece com aspas deleta
        string_formatting.replace_line_if_not_starts_with_double_quotes()

        # Caso a linha não termine com aspas deleta
        string_formatting.replace_line_if_not_ends_with_double_quotes()

        # Caso a linha tenha quebra de linha sem aspas duplas
        string_formatting.replace_line_with_linebreak_or_without_double_quote()

        # Só escreve a linha se tiver pelo menos mais que 3 colunas
        # no arquivo fullClear
        if string_formatting.has_three_columns_or_more():
            return string_formatting.string
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


# endregion
