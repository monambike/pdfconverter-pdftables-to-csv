# @staticmethod
# def GetUserGivenPatternColumnsArgs():
#     """
#     ---
#     ---
#     ---
    
#     ## __StoreArgs (Private)
#     ---
#     ---
#     Método que atualiza a  variável  que  vai  armazenar  todos  os
#     argumentos relacionados  à  ordenação  de  colunas  que  tenham
#     recebido algum valor pelo usuário.
    
#     ---
#     ---
#     ---
#     """

#     counter_ArgListIterator = 0
#     for argName in avar.patternColumnArgs:
#         # [>] Recebe o valor do argumento atual baseado  na  lista  que
#         # possui as colunas padrão
#         argValue = vars(avar.parser_ArgsMain)[argName]
#         # [>] Se o argumento da lista de colunas padrão tiver algum va-
#         # lor
#         if (argValue != None):
#             # [>] Adiciona um novo container na lista de colunas
#             pvar.list_UserGivenColumnToChange.append([])
#             # [>] Adiciona o título do argumento
#             pvar.list_UserGivenColumnToChange[counter_ArgListIterator].append(argName)

#             # [i] Caso tenha vindo uma lista de valores
#             if isinstance(argValue, list):
#                 # [>] Para cada valor na lista de valores passados na variável,
#                 # adiciona o valor na lista
#                 for value in argValue: pvar.list_UserGivenColumnToChange[counter_ArgListIterator].append(value)
#             # [i] Caso contrário, adiciona o valor do argumento  direto  na
#             # lista
#             else: pvar.list_UserGivenColumnToChange[counter_ArgListIterator].append(argValue)

#             # [>] Adiciona +1 ao contador da lista
#             counter_ArgListIterator += 1