from pdfconverter import util
from pdfconverter.conversion.string_format import StringFormat
from pdfconverter.output_info import errors


# region Public Methods


def make_file():
    try:
        with open(
            file = util.get_current_file_path_export(),
            mode = "a",
            encoding="UTF-8"
        ) as TextFile:
            # Formata o arquivo e escreve um novo arquivo de saída
            TextFile.write(format_text_file("<conversion_path>"))
    except Exception as exception:
        errors.add_error_method_unknown_exception(exception)


def format_text_file(file_path_text_file):
    try:
        string: str = ""

        # [i] Abre o arquivo original presente na pasta 'withoutFormat-
        # ting' para criar formatações baseadas nele
        with open(
            file = file_path_text_file,
            mode = "r",
            encoding="UTF-8"
        ) as text_file:
            # [i] Navega por cada linha do documento de texto
            for line in text_file:
                # Realiza a formatação do módulo vigente
                line = format_string(line)
                if line == ("" or None):
                    continue

                # Adiciona à nova String
                string += line

        return string
    except Exception as exception:
        errors.add_error_method_unknown_exception(exception)


def format_string(string):
    try:
        # Cria um novo objeto para manipular a String
        string_formatting = StringFormat(string)

        if string_formatting.string == "":
            return ""

        # Detecta os dados vazios que estão presentes no  cabeçalho
        # "Unnamed: X;"
        string_formatting.replace_empty_header()

        # Remove ponto e vírgula no final da linha
        string_formatting.replace_end_line_semicolon()

        # Remove quebras de linha caso seja no meio dos  dados,  ou
        # seja, caso não possua '"' atrás da quebra de linha e as substitui
        # por um espaço para manter o padrão
        string_formatting.replace_middle_line_break(" ")

        # Condicional que impede a continuação do processo caso a variável
        # esteja vazia, ou seja, caso tenha  sido  apagada  pelo
        # processo anterior de limpeza
        if string_formatting.string == "":
            return ""

        # Remove ponto e vírgula no final da linha
        string_formatting.replace_end_line_semicolon()

        # Remove todos os espaços no início de cada linha
        string_formatting.replace_start_line_empty_space()

        # Se a linha possui aspas duplas no início  e  no  final  e
        # ainda possui menos que duas colunas cancela o código
        if string_formatting.is_small_table():
            return ""

        return string_formatting.return_string()
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


# endregion
