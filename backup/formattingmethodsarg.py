# @staticmethod
# def FormattingMethod():
#     FormattingMethod = avar.parser_ArgsMain.FormattingMethod

#     try:
#         for letter in FormattingMethod:
#             # [i] Verifica se há letras repetidas no argumento que  informa
#             # os métodos de formatação
#             if (str(FormattingMethod).count(letter)) > 1: raise RepeatedFormattingType
            
#             # [i] Verifica se há alguma letra que não faz parte dos métodos
#             # de formatação existentes
#             if (letter != "T" and letter != "M" and letter != "F"): raise InvalidFormattingType
#     except InvalidFormattingType as ExceptionError:
#         error.Show("Ocorreu um erro na hora de realizar as formatações em 'ConversionStart()'.", ExceptionError)
#     except RepeatedFormattingType as ExceptionError:
#         error.Show("O tipo de formatação '" + letter + "' foi repetido mais de uma vez em '" + FormattingMethod + "'.", ExceptionError)
#     except Exception as ExceptionError:
#         error.Show("Ocorreu um erro desconhecido ao tentar realizar as formatações requisitadas em 'ConversionStart()'.", ExceptionError)

#     # [>] Após a validação, traz para a variável os métodos de for-
#     # matação que serão realizados
#     avar.FormattingMethodArg = FormattingMethod

#     # [>] Traz para a variável a quantidade de arquivos  que  serão
#     # exportados
#     fvar.quantity_ExportedFiles = len(FormattingMethod)