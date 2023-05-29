// OuroWebPDFConverter
// Solução de Teste do Script - Custom Software
namespace pdfconverter_desktop
{
    // CLASSE DE CAMINHOS
    // -------------------------------------------------------------
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    // Descrição:
    // Classe responsável por portar e manipular os caminhos  utili-
    // zados na aplicação.
    public class StoredPaths
    {
        #region CAMINHOS DE IMPORTAÇÃO E EXPORTAÇÃO

        // CAMINHOS DE IMPORTAÇÃO E EXPORTAÇÃO
        // -------------------------------------------------------------
        // Descrição:
        // Variáveis responsáveis por manipular os caminhos de  importa-
        // ção e exportação da aplicação.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // Caminho da pasta onde serão depositadas as pasta de  exporta-
        // ção
        public string exportFolderPath = "";
        // Caminho da pasta de importação de onde serão puxados  os  ar-
        // quivos em PDF
        public string importFolderPath = "";
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------

        #endregion

        #region CAMINHOS DO TERMINAL E DO EXECUTÁVEL

        // CAMINHOS DO TERMINAL E DO EXECUTÁVEL
        // -------------------------------------------------------------
        // Descrição:
        // Variáveis responsáveis por manipular os caminhos do  terminal
        // (que já vem com um valor predefinido por padrão  pelo  desen-
        // volvedor) e o caminho do arquivo de texto do terminal.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // Variável que contém o caminho do arquivo de texto do terminal
        // (por padrão o caminho vai ser o mesmo na onde está localizado
        // o Script)
        public string terminalFilePath = "";
        // Variável contendo caminho do executável do Script
        public string executeScriptPath = @"C:\DvpLocal\WorkspaceTFS\OuroWebPDFConverter\Scc\1.0\OuroWebPDFConverter\pdfconverter_script\exe\dist\pdfconverter\pdfconverter.exe";
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------

        #endregion
    }
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    // -------------------------------------------------------------
}
