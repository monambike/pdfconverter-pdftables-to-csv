using System;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Management;
using System.Windows.Forms;
using pdfconverter_desktop.Classes;

// PDFConverter
// Aplicativo de Teste - Custom Software
namespace pdfconverter_desktop.Forms
{
    // FORM PRINCIPAL
    // -------------------------------------------------------------
    // Descrição:
    // Form principal.
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    public partial class frmMain : Form
    {
		// 01 - Main Classes
		private static Messages ShowMessage;
		private static PDFConverterProgram PDFConverter;
		// 02 - Stored Info
		private static StoredPaths StoredPaths;
		// 03 - Form Dependent
		private static Conversion ScriptConversion;
		private static CurrentForm.Design.Status FormStatus;
		private static CurrentForm.Design.Controls.Export ExportControls;
		private static CurrentForm.Design.Controls.Conversion ConversionControls;
		private static CurrentForm.Prompt FormPrompts;
		private static CurrentForm.Design.Controls.CustomToolTip ControlsCustomToolTip;

		#region FORM MAIN START

        // INÍCIO DA APLICAÇÃO
        // -------------------------------------------------------------
        // Descrição:
        // Função responsável pelo início da aplicação.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        public frmMain()
        {
			// 01 - Main Classes
			ShowMessage = new Messages();
			PDFConverter = new PDFConverterProgram();
			// 02 - Stored Info
			StoredPaths = new StoredPaths();
			// 03 - Form Dependent
			ScriptConversion = new Conversion(this);
			FormStatus = new CurrentForm.Design.Status(this);
			ExportControls = new CurrentForm.Design.Controls.Export(this);
			ConversionControls = new CurrentForm.Design.Controls.Conversion(this);
			FormPrompts = new CurrentForm.Prompt(this);
			ControlsCustomToolTip = new CurrentForm.Design.Controls.CustomToolTip(this);
            var tempo = DateTime.Now;

            // Inicialização
            InitializeComponent();

			ControlsCustomToolTip.SetfrmMainToolTip();

			stts_lbl_ConversionProgress.Text = "0%";

			string UserName = "";
			SelectQuery SQLQuery = new SelectQuery("SELECT FullName FROM Win32_UserAccount WHERE domain='" + Environment.UserDomainName + "' AND name='" + Environment.UserName.ToLower() + "'");
			ManagementObjectSearcher Searcher = new ManagementObjectSearcher(SQLQuery);
			foreach (ManagementBaseObject disk in Searcher.Get()) { UserName = disk["FullName"].ToString(); }
            
            if (tempo.Hour > 6 && tempo.Hour < 12) 
                lbl_UserName.Text = @"Bom dia, " + UserName.Split()[0] + @"!";
            else if (tempo.Hour >= 12 && tempo.Hour < 18)
                lbl_UserName.Text = @"Boa Tarde, " + UserName.Split()[0] + @"!";
            else 
                lbl_UserName.Text = @"Boa Noite, " + UserName.Split()[0] + @"!";
                

			try
			{
				// Muda o diretório no qual está trabalhando atual para o  mesmo
				// diretório de onde está sendo executado o Script
				Directory.SetCurrentDirectory(Path.GetDirectoryName(StoredPaths.executeScriptPath));


				// ATUALIZANDO VARIÁVEIS DE CAMINHO
				// -------------------------------------------------------------
				// Descrição:
				// Atualizando as variáveis de caminho de importação e  exporta-
				// ção.
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// Atualizando caminho de importação
				StoredPaths.importFolderPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
				// Atualizando caminho de exportação
				StoredPaths.exportFolderPath = Directory.GetCurrentDirectory();
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------
			}
			catch (DirectoryNotFoundException)
			{
				// ERRO DE CAMINHO AO TENTAR DEFINIR A SAÍDA DO TERMINAL
				// -------------------------------------------------------------
				// Descrição:
				// Exibe uma mensagem de erro quando não é possível encontrar  o
				// caminho de sáida do terminal devido ao caminho estar errado.
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				ShowMessage.Error
				(
					"Não foi possível definir o caminho de saída do terminal po" +
					"is o caminho que aponta o Script executado pela solução ap" +
					"arenta estar incorreto.",

					"Erro no Caminho do Script"
				);
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------
			}
			catch (Exception exceptionError)
			{
				// ERRO DESCONHECIDO AO TENTAR DEFINIR A SAÍDA DO TERMINAL
				// -------------------------------------------------------------
				// Descrição:
				// Exibe uma mensagem quando ocorre um erro desconhecido ao  de-
				// finir o caminho de saída do terminal.
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				ShowMessage.Exception
				(
					"Ocorreu um erro desconhecido ao tentar mudar o diretório n" +
					"o qual está sendo trabalhado atualmente para apontar a saí" +
					"da do arquivo do terminal. Por favor, contate algum desenv" +
					"olvedor para averiguar o problema.",

					exceptionError
				);
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------
			}

            // Atualiza o status de conversão no menu inferior
            FormStatus.Update("PDFConverter");

            
			// ATUALIZANDO TEXTBOX
            // -------------------------------------------------------------
            // Descrição:
            // Atualizando as TextBox mostradas para o usuário de acordo com
            // os caminhos de importação e exportação definidos anteriormen-
            // te.
            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            // Importação
            txt_PathImport.Text = StoredPaths.importFolderPath;
            // Exportação
            txt_PathExport.Text = StoredPaths.exportFolderPath;
            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            // -------------------------------------------------------------


            // Reseta o status da label possuinte da hora da última  conver-
            // são realizada
            stts_lbl_LastConversionTime.Text = "";
        }
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------

		#endregion

		#region FUNCTIONS

		// INICIA A CONVERSÃO
		// -------------------------------------------------------------
		// Descrição:
		// Função responsável por inicializar a conversão.
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		private void StartConversion()
		{
			// Desabilita os controles de conversão quando ela começar
			ConversionControls.Disable();
			lbl_PathImport.Focus();
			
			// Inicia a conversão
			ScriptConversion.Start();

			// Habilita os controles de conversão novamente quando ela acabar
			ConversionControls.Enable();
			btn_Convert.Focus();
		}
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// -------------------------------------------------------------


		// MENSAGEM DE SOBRE
		// -------------------------------------------------------------
		// Descrição:
		// Função responsável por mostrar mensagem de sobre.
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		private void ShowAbout()
		{
			// Mostra uma mensagem de sobre
			ShowMessage.Info
			(
				"Aplicativo de teste para executar o Script de conversão de Tabelas para CSV." + Environment.NewLine +
				Environment.NewLine +
				Environment.NewLine +
				"Caminho da saída do terminal:" + Environment.NewLine +
				"'" + StoredPaths.terminalFilePath + "'"
			);
		}
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// -------------------------------------------------------------


		// ABRE O ARQUIVO DE SAÍDA DO TERMINAL
		// -------------------------------------------------------------
		// Descrição:
		// Função responsável por abrir o arquivo de saída do terminal.
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		private void OpenTerminalFile()
		{
			try { Process.Start(StoredPaths.terminalFilePath); }
			catch (Win32Exception) { ShowMessage.Info("O arquivo de saída do terminal não foi criado ainda."); }
			catch (Exception exceptionError) { ShowMessage.Exception("Ocorreu um erro desconhecido ao tentar abrir o arquivo de saída do terminal", exceptionError); }
		}
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// -------------------------------------------------------------

        #endregion

        #region BUTTONS AND CHECKBOXS

        // BOTÕES GERAIS
        // -------------------------------------------------------------
        // Descrição:
        // Botão que inicia o Script pelo caminho da variável  fornecida
        // em 'executeScriptPath' na classe 'Paths.cs' e botão  de  sair
        // do aplicativo.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // Inicia a conversão
        public void btn_Execute_Click(object sender, EventArgs e)
        {
            StartConversion();
            btn_PararConversao.Enabled = true;
        }
        // Botão que fecha o aplicativo
        public void btn_Exit_Click(object sender, EventArgs e) { PDFConverter.Exit(); }
        // Botão para parar o aplicativo
        private void btn_PararConversao_Click(object sender, EventArgs e)
        {
            ScriptConversion.Stop();
            btn_PararConversao.Enabled = false;
            stts_prg_ConversionStatus.Minimum = 0;
            stts_lbl_ConversionProgress.Text = @"0%";
            FormStatus.Update("Conversão Parada!");
        }
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------

        // DEFINIÇÃO DE CAMINHOS POR BOTÃO
        // -------------------------------------------------------------
        // Descrição:
        // Botões que procuram as pastas e  depositam  os  caminhos  nas
        // TextBox
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // Botão de seleção de pasta de importação
        public void btn_ChoosePathImport_Click(object sender, EventArgs e) { txt_PathImport.Text = FormPrompts.OpenDialogPath(StoredPaths.importFolderPath); }
        // Botão de seleção de pasta de exportação
        public void btn_ChoosePathExport_Click(object sender, EventArgs e) { txt_PathExport.Text = FormPrompts.OpenDialogPath(StoredPaths.exportFolderPath); }
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------

        // ABERTURA DE PASTAS
        // -------------------------------------------------------------
        // Descrição:
        // Botões que servem  como  atalho  para  abrir  as  pastas  nas
        // textbox.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // Botão de abertura da pasta de importação
        public void btn_OpenPathImport_Click(object sender, EventArgs e) { PDFConverter.OpenFolderWithGivenPath(txt_PathImport.Text); }
        // Botão de abertura da pasta de exportação
        public void btn_OpenPathExport_Click(object sender, EventArgs e) { PDFConverter.OpenFolderWithGivenPath(txt_PathExport.Text); }
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------

        // CHECKBOX DE CAMINHO DE EXPORTAÇÃO
        // -------------------------------------------------------------
        // Descrição:
        // Checkbox que define se os comandos do referentes  ao  caminho
        // de exportação ficam habilitados ou não.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        public void chk_useExportPath_CheckedChanged(object sender, EventArgs e) { ExportControls.Switch(chk_useExportPath.Checked); }
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------

        #endregion

        #region TOP MENU BUTTONS

        // BOTÕES GERAIS
        // -------------------------------------------------------------
        // Descrição:
        // Botão que inicia o Script pelo caminho da variável  fornecida
        // em 'executeScriptPath' na classe 'Paths.cs'.
        // Também há botões que abrem uma guia de informações à respeito
        // da  aplicação ou executam ações como sair do aplicativo.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // Chama o botão que realiza o início da conversão
        public void mnu_item_Convert_Click(object sender, EventArgs e) { btn_Execute_Click(sender, e); }
        // Mostra uma mensagem de 'Sobre'
		public void mnu_item_About_Click(object sender, EventArgs e) { ShowAbout();  }
		// Abre o arquivo de saída do terminal
		public void mnu_item_OpenTerminalFile_Click(object sender, EventArgs e) { OpenTerminalFile(); }
        // Chama o botão que fecha o aplicativo
		public void mnu_item_Exit_Click(object sender, EventArgs e) { btn_Exit_Click(sender, e); }
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------


        // DEFINIÇÃO DE CAMINHOS POR BOTÃO
        // -------------------------------------------------------------
        // Descrição:
        // Botões que procuram as pastas e  depositam  os  caminhos  nas
        // TextBox.
        // Esses botões chamam os botões do frmMain.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // Botão de seleção de pasta de importação
        public void mnu_item_ChoosePathImport_Click(object sender, EventArgs e) { btn_ChoosePathImport_Click(sender, e); }
        // Botão de seleção da pasta de exportação
        public void mnu_item_ChoosePathExport_Click(object sender, EventArgs e) { btn_ChoosePathExport_Click(sender, e); }
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // -------------------------------------------------------------


		// ABERTURA DE CAMINHO DE PASTAS
		// -------------------------------------------------------------
		// Descrição:
		// Descrição:
		// Botões que abrem as pastas indicadas como caminhos de  impor-
		// tação e exportação.
		// Esses botões chamam os botões do frmMain.
        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// Botão de abertura de pasta de importação
		public void mnu_item_OpenPathImport_Click(object sender, EventArgs e) { btn_OpenPathImport_Click(sender, e); }
		// Botão de abertura de pasta de exportação
        public void mnu_item_OpenPathExport_Click(object sender, EventArgs e) { btn_OpenPathExport_Click(sender, e); }

		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// -------------------------------------------------------------

		#endregion
    }
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    // -------------------------------------------------------------
}
