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
		// Pasta na onde se localiza o executável do Script
        public static string scriptExeFileFolderPath = @"C:\DvpLocal\WorkSpaceTFS\OuroWebPDFConverter\Scc\1.0\OuroWebPDFConverter\pdfconverter_script\exe\dist\pdfconverter";


		// CAMINHOS DO TERMINAL E DO EXECUTÁVEL
		// -------------------------------------------------------------
		// Descrição:
		// Variáveis responsáveis por manipular os caminhos do  terminal
		// (que já vem com um valor predefinido por padrão  pelo  desen-
		// volvedor) e o caminho do arquivo de texto do terminal.
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		public static string
			// Variável que contém o caminho do arquivo de texto do terminal
			// (por padrão o caminho vai ser o mesmo na onde está localizado
			// o Script)
			terminalFilePath = scriptExeFileFolderPath + @"\output.txt",
			// Variável contendo caminho do executável do Script
			executeScriptPath = scriptExeFileFolderPath + @"\pdfconverter.exe";
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// -------------------------------------------------------------

		
		// CAMINHOS DE IMPORTAÇÃO E EXPORTAÇÃO
        // -------------------------------------------------------------
        // Descrição:
        // Variáveis responsáveis por manipular os caminhos de  importa-
        // ção e exportação da aplicação.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        public string
			// Caminho da pasta onde serão depositadas as pasta de  exporta-
			// ção
			exportFolderPath = "",
			// Caminho da pasta de importação de onde serão puxados  os  ar-
			// quivos em PDF
			importFolderPath = "";
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------
    }
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    // -------------------------------------------------------------
}