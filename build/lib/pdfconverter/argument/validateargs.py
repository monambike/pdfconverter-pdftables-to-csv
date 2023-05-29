# [>] Geral
import os.path
# [>] PDFConverter
# [i] Variáveis
from pdfconverter.__variables__ import mvar, avar, fvar
# [i] Arquivo do Terminal
from pdfconverter.terminalfile.message import error
# [i] Conversão
from pdfconverter import conversion
# [i] Formatação de String
from pdfconverter.stringformat import stringformat
# [i] Programa
from pdfconverter.program import utilities


#region VALIDATE ARGS

class validateargs:
    """Classe que realiza algumas validações de argumentos."""

    #region CONSTRUCTOR

    def __init__(self): pass

    #endregion

    #region PUBLIC METHODS

    def All(self):
        self.ImportPath()
        self.ExportPath()
        self.PageNumber()

    @staticmethod
    def ImportPath():
        try:
            # [>] Pega dos argumentos o caminho de importação
            ImportPathArg = avar.parser_ArgsMain.ImportPath

            # [i] Caso o usuário não tenha preenchido o caminho de importa-
            # ção, exibe uma mensagem de erro mostrando que  é  obrigatório
            # a inserção do caminho de importação
            if (ImportPathArg == None): error.Show("É necessário colocar um valor para o caminho de importação, '--ImportPath <caminho_de_exportação>'.")
            # [i] Caso seja percebido que o valor do argumento de  importa-
            # ção se refere à um arquivo
            elif (os.path.isfile(ImportPathArg)):
                # [i] E esse arquivo referido seja um PDF
                if (utilities.IsPDF(ImportPathArg)):
                    # [>] Passa o valor para a classe de variáveis
                    avar.path_ImportArg = ImportPathArg
                    fvar.folderpath_Import = os.path.dirname(ImportPathArg)
                    # [>] Lá na frente, vai executar a função que realizará a  con-
                    # versão do arquivo individual que foi indicado
                    functionName = "IndividualConversion"
                # [i] Caso tenha sido indicado um arquivo que não seja  um  PDF
                # exibe uma mensagem de erro
                else: error.Show("O arquivo informado no argumento de importação, precisa ser uma pasta ou um arquivo PDF.")
            # [i] Caso seja percebido que o valor do argumento de  importa-
            # ção se refere à uma pasta
            elif (os.path.isdir(ImportPathArg)):
                # [>] Passa o valor para a classe de variáveis
                avar.path_ImportArg = ImportPathArg
                fvar.folderpath_Import = ImportPathArg
                # [>] Lá na frente, vai executar a função que realizará  a  con-
                # versão de todos os PDFs indicados na pasta
                functionName = "MultipleConversion"
            # [i] Exibe um erro caso o argument o não tenha passado nas va-
            # lidações
            else: error.Show("O argumento ('" + ImportPathArg + "') passado como caminho de importação não é válido.")

            # [>] Atribui o objeto que referencia a função com  o  nome  da
            # função passada nas validações acima
            mvar.ConversionStart = getattr(conversion, functionName)
        # [>] Caso ocorra um erro desconhecido exibe uma mensagem
        except Exception as ExceptionError:
            error.Show("Ocorreu um erro desconhecido ao tentar receber os argumentos dos caminhos de importação.", ExceptionError)

    @staticmethod
    def ExportPath():
        try:
            # [>] Pega dos argumentos o caminho de importação
            ExportPath = avar.parser_ArgsMain.ExportPath

            # [i] Caso o caminho de exportação não tenha sido informado pe-
            # lo usuário, informa o caminho da pasta de importação como re-
            # ferência para o caminho de exportação
            if (ExportPath == None): fvar.folderpath_Export = fvar.folderpath_Import
            # [i] Se o caminho fornecido for um diretório,  passa  para  as
            # variáveis globais o valor fornecido no argumento
            elif (os.path.isdir(ExportPath)): fvar.folderpath_Export = ExportPath
            # [i] Caso a pasta de acordo com a ação realizada não exista
            else: error.Show("A pasta de exportação ('" + ExportPath + "') informada não existe.")
        # [>] Caso ocorra um erro desconhecido exibe uma mensagem
        except Exception as ExceptionError:
            error.Show("Ocorreu um erro desconhecido ao tentar receber os  argumentos dos caminhos de exportação.", ExceptionError)

    @staticmethod
    def PageNumber():
        """
        ---
        ---
        ---
        
        ## __ValidatePageNumberArg (Private)
        ---
        ---
        Método que valida o número de página, ou  números  de  páginas,
        passados no argumentos.
        
        ---
        ---
        ---
        """


        try:
            # [i] Se o valor digitado é válido como número de página  passa
            # o número de páginas do argumento para uma variável dentro  da
            # classe de variáveis
            if (stringformat(avar.parser_ArgsMain.PageNumber).ValidatePageNumber()): avar.readPDFPagesArg = avar.parser_ArgsMain.PageNumber
            # [i] Se o número de páginas é inválido, exibe uma mensagem  de
            # erro
            else: error.Show("O valor '" + avar.parser_ArgsMain.PageNumber + "' não é um valor de número de página válido para --PageNumber.")
        # [>] Caso ocorra um erro desconhecido exibe uma mensagem
        except Exception as ExceptionError:
            error.Show("Ocorreu um erro desconhecido ao validar o número de páginas.\n", ExceptionError)

    #endregion

#endregion