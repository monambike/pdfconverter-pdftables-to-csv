# [>] Geral
import pathlib
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import fvar
# [i] Argumentos
from pdfconverter import argument
# [i] Arquivo do Terminal
from pdfconverter import terminalfile
# [i] Configurações
from pdfconverter.settings import pandassettings
# [i] Conversão
from pdfconverter import conversion
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

# [>] Roda a aplicação
def Run():
    """Método que roda a aplicação PDFConverter."""

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
    argument.Create()
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------


    conversion.Start()


# [>] Roda a aplicação
Run()

# [>] Garante a finalização após a execução do Script
program.Exit()

#endregion