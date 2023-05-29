using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pdfconverter_desktop.Classes
{
	public class PDFConverterProgram
	{
		// 01 - Main Classes
		private static Messages ShowMessage = new Messages();


		// FUNÇÃO: ABRE A PASTA
		// -------------------------------------------------------------
		// Descrição:
		// Função que faz a abertura da pasta definida na TextBox.
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// Método para abrir uma pasta de importação ou exportação
		public void OpenFolderWithGivenPath(string folderPath)
		{
			try { Process.Start(folderPath); }
			catch (Win32Exception)
			{
				// MENSAGEM: ERRO DE CAMINHO DE IMPORTAÇÃO
				// -------------------------------------------------------------
				// Descrição:
				// Mensagem para quando houve erro ao tentar achar  o  diretório
				// de Importação
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				ShowMessage.Error(
					"A pasta informada não existe." + Environment.NewLine +
					Environment.NewLine +
					"Caminho: '" + folderPath + "'",

					"Pasta não Encontrada"
				);
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------
			}
			catch (Exception exceptionError)
			{
				// MENSAGEM: ERRO DESCONHECIDO
				// -------------------------------------------------------------
				// Descrição:
				// Mensagem quando ocorre um erro desconhecido ao tentar abrir a
				// pasta
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				ShowMessage.Exception(
					"Ocorreu um erro desconhecido ao tentar abrir a pasta.",

					exceptionError
				);
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------
			}
		}
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// -------------------------------------------------------------


		// FUNÇÃO: FECHA A APLICAÇÃO
		// -------------------------------------------------------------
		// Descrição:
		// Função que gerencia o fechamento da aplicação.
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		public void Exit()
		{
			// Exibe a caixa de confirmação e pega o resultado
			DialogResult dialogResult = ShowMessage.Confirmation("Tem certeza que deseja sair?");
			// Caso o usuário aperte em 'sim' na caixa de confirmação
			if (dialogResult == DialogResult.Yes) { Application.Exit(); }
		}

		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// -------------------------------------------------------------
	}
}
