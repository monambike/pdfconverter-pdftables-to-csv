# [>] Geral
import pathlib
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import mvar, fvar
# [i] Argumentos
from pdfconverter import argument
# [i] Arquivo do Terminal
from pdfconverter import terminalfile
# [i] Configurações
from pdfconverter.settings import pandassettings
# [i] Program
from pdfconverter import program


#region MAIN

# [>] Pega o caminho do Script atual e define o caminho do  ar-
# quivo de saída do terminal
# [i] Pegando o caminho até o executável ou script atual  e  a-
# tribuindo para a variável folderpath_Script
fvar.folderpath_Script = str(pathlib.Path(__file__).parent.absolute())

# [>] Passa para a variável global o caminho do arquivo de tex-
# to do terminal
fvar.filepath_TerminalFile = fvar.folderpath_Script + "\\output.txt"

# CONFIGURAÇÕES INICIAIS
# -------------------------------------------------------------
# Descrição:
# Contém todas as chamadas de funções que realizam as  configu-
# rações iniciais para o funcionamento do Script.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# [>] Recria o arquivo do terminal
terminalfile.Recreate()
# [>] Realiza as configurações da biblioteca Pandas
pandassettings.Set()
# [>] Cria o parser para manipular os argumentos
argument.Set()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------


# [>] Executa  a   função   armazenada   dentro   da   variável
# ConversionStart, a função foi atribuída no momento em que foi
# realizada a validação do argumento 'ImportPath' no módulo  de
# argumento
# Caminho onde é realizada a validação:
# "pdfconverter\\argument\\__init__.py"
# Caminho de onde são procuradas as funções:
# "pdfconverter\\conversion\\__init__.py"
mvar.ConversionStart()

# [>] Garante a finalização após a execução do Script
program.Exit()

#endregion