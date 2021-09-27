"""
---
---
---

## Package: pdfconverter >> regex
---
---
### Module Name: regex (Constructor, __init__)
---
### path: "pdfconverter\\\\\\\\regex\\\\\\\\__init__.py"
---
---
Pacote e  módulo  que  guarda  algumas  funções  de  Expressões
Regulares consigo.

---
---
---
"""

# [>] Geral
import re


#region PUBLIC METHODS

class ManipulateString:
    """Classe que manipula uma string."""
    def __init__(self, String):
        self.String = String
        """Alterar Depois"""
        self.FlagConfig = (
            re.MULTILINE | # Faz com que os caracteres '^' e '$'  represen-
                        # tem o início e o final da linha respectivamen-
                        # te
            re.VERBOSE     # Permite com que o REGEX possa ser lido com ma-
                        # ior facilidade, com  comentários  e  separação
                        # do mesmo por seções
        )
        """Configurações padrão de flag de Regex."""
    
    #region RETURN

    def ReturnString(self):
        return self.String

    def ReturnFlagConfig(self):
        return self.FlagConfig
    
    #endregion

    #region <RENAMELATER>

    def RegexMatch(self, RegexPattern):
        """
        ---
        ---
        ---

        ### DoRegex (Private)
        ---
        Faz o REGEX com as configurações padrão.

        Args:
            Regex ([str]): Regex recebido a partir do método pai.
            Value ([str]): Valor recebido a partir do método pai.

        Returns:
            [bool]: Retorna se foi encontrado alguma ocorrência ou não.
        
        ---
        ---
        ---
        """
        return re.match(RegexPattern, self.String, flags = self.FlagConfig)

    def RegexSub(self, RegexPattern, NewStringValue = ""):
        return re.sub(RegexPattern, NewStringValue, self.String, flags = self.FlagConfig)

    def RegexFindall(self, RegexPattern):
        return re.findall(RegexPattern, self.String, flags = self.FlagConfig)

    #endregion

    #region VALIDATE

    def ValidatePageNumber(self):
        """
        ---
        ---
        ---

        ### ValidatePageNumber (Public)
        ---
        Realiza a validação do valor como número de página.
        
        ---
        ---
        ---
        """
        return self.RegexMatch(
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

    def IsSmallTable(self):
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

        if(
            (
                (
                    self.String.startswith("\"")
                )
                and 
                (
                    self.String.endswith("\"") or self.String.endswith("\n")
                )
            )
            and
            (self.String.count("\"") < 3 and self.String.count(";") < 1)
        ):
            return True

    #endregion

    #region <RENAMELATER>

    #[!!!!!]
    # TABLEWITHBLANKCELLS
    def EmptyHeader(self, NewStringValue = ""):
        """Detecta os dados vazios que estão presentes no  cabeçalho "Unnamed: X;"."""

        # return self.RegexSub(r"(\s?\"Unnamed:\s\d\d?\";?)", NewStringValue)
        self.String = self.RegexSub(r"(\s?\"Unnamed:\s\d\d?\";?)", NewStringValue)

    def MiddleLineBreak(self, NewStringValue = ""):
        """
            Remove quebras de linha caso seja no meio dos  dados,  ou
            seja, caso não possua '"' atrás da quebra de linha e as subs-
            titui por um espaço para manter o padrão
        """
        self.String = self.RegexSub(r"((?<!\")\n)", NewStringValue)

    def EndLineSemicolon(self, NewStringValue = ""):
        """Remove ponto e vírgula no final da linha."""
        self.String = self.RegexSub(r"((?<=\");(?!.))", NewStringValue)

    def StartLineEmptySpace(self, NewStringValue = ""):
        """Remove todos os espaços no início de cada linha."""
        self.String = self.RegexSub(r"(^\ *)", NewStringValue)

    #  MAIN
    def EmptyBody(self, NewStringValue = ""):
        """Remove dados que estão vazios."""
        self.String = self.RegexSub(r"(;\"\")|(\"\";)", NewStringValue)

    def DoubleQuotesAdjacent(self, NewStringValue = ""):
        """Faz uma quebra de linha caso tenha aspas duplas adjacentes"""
        self.String = self.RegexSub(r"(?<=\")(?=\")", NewStringValue)

    def SemicolonAdjacentSpace(self, NewStringValue = ""):
        """
            Caso tenha um ponto e vírgula seguido de um espaço  troca
            por uma quebra de linha
        """
        self.String = self.RegexSub(r"((?<=\");\ )", NewStringValue)

    def SpaceBetweenSeparatorAndDoubleQuote(self):
        """
            Caso tenha um espaço entre um separador e uma aspas dupla
            remove o conteúdo que está atrás
        """
        self.String = self.RegexSub(r"((.*\";\ )(?=\"))")
    
    # REPLACE FULLCLEAR
    def LineNotStartsWithDoubleQuotes(self):
        """Caso a linha não comece com aspas deleta"""
        self.String = self.RegexSub(r"((^[^\"]).*)")

    def LineNotEndsWithDoubleQuotes(self):
        """Caso a linha não termine com aspas deleta"""
        self.String = self.RegexSub(r"(.*([^\"\n]$))")

    def LineWithLinebreakOrWithoutDoubleQuote(self):
        # [>] Remove Linhas vazias que só possuem quebra de linha  '\n'
        # ou não possuem uma aspas dupla em nenhum lugar, serão excluí-
        # das 
        lineRemovedQuotes = ""
        lineRemovedQuotes = re.sub(r"\"", "", self.String)

        # [i] Se a temporária permanece igual, ou seja, não teve  aspas
        # duplas removidas pelo regex
        if (self.String == lineRemovedQuotes):
            # Quer dizer que ela ta errada e vai ser apagada
            self.String = ""


    def Has3ColumnsOrMore(self):
        """
            Só escreve a linha se tiver pelo menos mais que 3 colunas
            no arquivo fullClear
        """
        if (self.String.count("\"") > 6 and
            self.String.count(";") > 2):
            return True

    #endregion

#endregion