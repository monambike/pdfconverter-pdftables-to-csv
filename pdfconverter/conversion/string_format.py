import re
from typing import Match


# region Classes


class StringFormat:
    """
    Classe que pode armazenar uma String para que possa ser possível realizar múltiplas validações e substituições na
    mesma.
    """

    # region Constructor

    def __init__(self, string):
        self.string = string
        self.flag_config = (
            re.MULTILINE | # Faz com que os caracteres '^' e '$' respectivamente representem o início e o final da linha
            re.VERBOSE     # Permite com que o REGEX possa ser lido com maior facilidade, com comentários e separação
                           # do mesmo por seções
        )
    
    # endregion

    # region Return

    def return_string(self):
        """
        Returns:
            retorna a String que foi informada para a instância dessa classe.
        """

        return self.string

    def return_flag_config(self):
        """
        Returns:
            configurações de flag utilizadas nas expressões regulares dessa classe.
        """

        return self.flag_config

    # endregion

    # region Public Methods

    # region Regex

    def regex_match(self, regex) -> Match[str | bytes] | None:
        """
        Dada uma expressão regular, tenta procurar por ocorrências dentro da String da classe vigente.

        Args:
            regex: Expressão regular para utilizar como base para realizar a procura.

        Returns:
            Retorna o item caso tenha sido encontrado.
        """
        return re.match(
            pattern = regex,
            string = self.string,
            flags = self.flag_config
        )

    def regex_sub(self, code_regex, new_string = ""):
        """
        Realiza a substituição na String dada a expressão regular e o novo valor fornecido.

        Args:
            code_regex:
            new_string:

        Returns:

        """
        return re.sub(
            pattern = code_regex,
            repl = new_string,
            string = self.string,
            flags = self.flag_config
        )

    def regex_find_all(self, code_regex):
        """
        Procura dentro da String por todas as ocorrências dada uma expressão regular.

        Args:
            code_regex: código da expressão regular que será utilizado para realizar a busca.

        Returns:
            resultado da busca.
        """
        return re.findall(
            pattern = code_regex,
            string = self.string,
            flags = self.flag_config
        )

    # endregion

    # region Validation

    def is_page_number(self):
        """
        Tenta procurar por ocorrências de um formato de número de página dada uma string.

        Returns: Ocorrências de números de página.

        """
        return self.regex_match(
            r"""
                (?P<matchExactly>^
                    (?P<matchPageNumber>
                        (?P<singlePageNumber>\d{1,3})
                        |
                        (?P<multiplePageNumber>
                            \d{1,3}
                            -{1}
                            \d{1,3}
                        )
                        |
                        (?P<allPages>all{1})
                    )
                $)
            """
        )

    def is_small_table(self):
        """
        ---
        ---
        ---
        
        ## Check (Public/Private)
        ---
        ---
        Método que checa se o conteúdo:
        - Começa com aspas duplas e termina com aspas duplas ou termina com quebra de linha;
            - E ainda há menos que 3 aspas duplas ou menos que um ponto e vírgula
        Retorna True
        
        Se a linha possui aspas duplas no início  e  no  final  e
        ainda possui menos que duas colunas cancela o código

        ### Returns
        ---
            [type]: [description]
        
        ---
        ---
        ---
        """

        if (
            (
                (self.string.startswith("\""))
                and
                (
                    (self.string.endswith("\""))
                    or
                    (self.string.endswith("\n"))
                )
            )
            and
            (
                (self.string.count("\"") <= 3)
                and
                (self.string.count(";") <= 1)
            )
        ):
            return True

    # endregion

    # region Replacement

    # General
    def has_three_columns_or_more(self):
        """
        Só escreve a linha se tiver pelo menos mais que 3 colunas
        no arquivo fullClear
        """
        if self.string.count("\"") > 6 and self.string.count(";") > 2:
            return True
        else:
            return False

    # TableWithBlankCells
    def replace_empty_header(self, new_string = ""):
        """Detecta os dados vazios que estão presentes no  cabeçalho "Unnamed: X;"."""

        # return self.RegexSub(r"(\s?\"Unnamed:\s\d\d?\";?)", new_string)
        self.string = self.regex_sub(r"(\s?\"Unnamed:\s\d\d?\";?)", new_string)

    def replace_middle_line_break(self, new_string = ""):
        """
        Remove quebras de linha caso seja no meio dos dados, ou seja, caso não possua '"' atrás da quebra de linha e as
        substitui por um espaço para manter o padrão
        """
        self.string = self.regex_sub(r"((?<!\")\n)", new_string)

    def replace_end_line_semicolon(self, new_string = ""):
        """
        Substitui ponto e vírgula no final da linha.

        Args:
            new_string:

        Returns:

        """
        self.string = self.regex_sub(r"((?<=\");(?!.))", new_string)

    def replace_start_line_empty_space(self, new_string = ""):
        """Remove todos os espaços no início de cada linha."""
        self.string = self.regex_sub(r"(^\ *)", new_string)

    #  Main
    def replace_empty_body(self, new_string = ""):
        """Remove dados que estão vazios."""
        self.string = self.regex_sub(r"(;\"\")|(\"\";)", new_string)

    def replace_double_quotes_adjacent(self, new_string = "\n"):
        """Faz uma quebra de linha caso tenha aspas duplas adjacentes"""
        self.string = self.regex_sub(r"(?<=\")(?=\")", new_string)

    def replace_semicolon_adjacent_space(
        self,
        new_string = "\n"
    ) -> None:
        """
        Caso tenha um ponto e vírgula seguido de um espaço troca por uma quebra de linha.
        """
        self.string = self.regex_sub(r"((?<=\");\ )", new_string)

    def replace_space_between_separator_and_double_quote(self):
        """
        Caso tenha um espaço entre um separador e uma aspas dupla
        remove o conteúdo que está atrás
        """
        self.string = self.regex_sub(r"((.*\";\ )(?=\"))")
    
    # FullClear
    def replace_line_if_not_starts_with_double_quotes(self):
        """Caso a linha não comece com aspas deleta"""
        self.string = self.regex_sub(r"((^[^\"]).*)")

    def replace_line_if_not_ends_with_double_quotes(self):
        """Caso a linha não termine com aspas deleta"""
        self.string = self.regex_sub(r"(.*([^\"\n]$))")

    def replace_line_with_linebreak_or_without_double_quote(self):
        """
        Substitui linhas que não possuem quebra de linha ou aspas duplas.
        Returns:

        """
        # Remove Linhas vazias que só possuem quebra de linha  '\n'
        # ou não possuem uma aspas dupla em nenhum lugar, serão excluí-
        # das TODO: teste
        line_removed_quotes = re.sub(r"\"", "", self.string)

        # Se a temporária permanece igual, ou seja, não teve  aspas
        # duplas removidas pelo regex
        if self.string == line_removed_quotes:
            # Quer dizer que ela ta errada e vai ser apagada
            self.string = ""

    # Camelot Test

    def test_camelot_regex(self):
        self.string = self.regex_sub(r"(?<=[^\"])(\n)", " ")

    # endregion

    # endregion


# endregion
