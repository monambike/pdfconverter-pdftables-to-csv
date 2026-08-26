from pdfconverter import util
from pdfconverter.conversion.string_format import StringFormat
from pdfconverter.conversion.tabula.formatting import tablewithblankcells
from pdfconverter.output_info import errors


# region Public Methods


def make_file() -> None:
    try:
        with open(
            file = util.get_current_file_path_export(),
            mode = "a",
            encoding = "UTF-8"
        ) as TextFile:
            # Formata o arquivo e escreve um novo arquivo de saída
            TextFile.write(format_text_file("<file_path>"))
    except Exception as exception:
        errors.add_error_method_unknown_exception(exception)


def format_text_file(file_path_text_file: str) -> str:
    try:
        string: str = ""

        # Abre o arquivo original presente na pasta 'withoutFormat-
        # ting' para criar formatações baseadas nele
        with open(file_path_text_file, "r", encoding="UTF-8") as TextFile:
            # Navega por cada linha do documento de texto
            for line in TextFile:
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

        return string
    except Exception as exception:
        errors.add_error_method_unknown_exception(exception)


def format_string_line(string: str) -> str:
    try:
        # Cria um novo objeto para manipular a String
        string_formatting: StringFormat = StringFormat(string)

        if string_formatting.string == "":
            return ""

        # Remove dados que estão vazios
        string_formatting.replace_empty_body()

        # Faz uma quebra de linha caso tenha aspas duplas
        # adjacentes
        string_formatting.replace_double_quotes_adjacent("\n")

        # Caso tenha um ponto e vírgula seguido de um espaço  troca
        # por uma quebra de linha
        string_formatting.replace_semicolon_adjacent_space("\n")

        # Caso tenha um espaço entre um separador e uma aspas dupla
        # remove o conteúdo que está atrás
        string_formatting.replace_space_between_separator_and_double_quote()

        # Se a linha possui aspas duplas no início  e  no  final  e
        # ainda possui menos que duas colunas cancela o código
        if string_formatting.is_small_table():
            return ""

        return string_formatting.return_string()
    except Exception as exception:
        errors.add_error_method_unknown_exception(exception)


# endregion
