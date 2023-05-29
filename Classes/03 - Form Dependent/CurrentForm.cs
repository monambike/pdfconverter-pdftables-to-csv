using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using pdfconverter_desktop.Forms;

namespace pdfconverter_desktop.Classes
{
	public class CurrentForm
	{
		public class Design
		{
			public class Controls
			{
				public class Export
				{
					// Pega a instância do frmMain
					private static frmMain _frmMainInstance;

					public Export(frmMain frmMainInstance) { _frmMainInstance = frmMainInstance; }


					// FUNÇÃO: FAZ O CONTROLE DOS CONTROLES DE EXPORTAÇÃO
					// -------------------------------------------------------------
					// Descrição:
					// Função que gerencia a habilitação e desabilitação dos contro-
					// les de exportação  de  acordo  com  o  que  está  marcado  na
					// checkbox.
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					public void Switch(bool enableControls = true)
					{
						// DESABILITANDO CONTROLES
						// -------------------------------------------------------------
						// Descrição:
						// Desabilitando controles.
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						// Rótulos
						_frmMainInstance.lbl_PathExport.Enabled = enableControls;
						// Caixas de Texto
						_frmMainInstance.txt_PathExport.Enabled = enableControls;
						// Botões
						_frmMainInstance.btn_ChoosePathExport.Enabled = enableControls;
						_frmMainInstance.btn_OpenPathExport.Enabled = enableControls;
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						// -------------------------------------------------------------
					}
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------
				}

				public class Conversion
				{
					// Pega a instância do frmMain
					private static frmMain _frmMainInstance;

					public Conversion(frmMain frmMainInstance) { _frmMainInstance = frmMainInstance; }
					

					// FUNÇÃO: HABILITA OS CONTROLES RELACIONADOS À CONVERSÃO
					// -------------------------------------------------------------
					// Descrição:
					// Função responsável por habilitar os controles relacionados  à
					// conversão.
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					public void Enable()
					{
						// Controles do Formulários
						// Botão de conversão
						_frmMainInstance.btn_Convert.Enabled = true;
						// Controles relacionados à escolha de caminhos
						_frmMainInstance.btn_ChoosePathImport.Enabled = true;
						_frmMainInstance.btn_ChoosePathExport.Enabled = true;

						// Controles do Menu Superior
						// Botão de Conversão
						_frmMainInstance.mnu_item_Convert.Enabled = true;
						// Controle relacionado à escolha de caminho
						_frmMainInstance.mnu_item_ChoosePath.Enabled = true;
					}
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------

					
					// FUNÇÃO: HABILITA OS CONTROLES RELACIONADOS À CONVERSÃO
					// -------------------------------------------------------------
					// Descrição:
					// Função responsável por habilitar os controles relacionados  à
					// conversão.
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					public void Disable()
					{
						// Controles do Formulários
						// Botão de conversão
						_frmMainInstance.btn_Convert.Enabled = false;
						// Controles relacionados à escolha de caminhos
						_frmMainInstance.btn_ChoosePathImport.Enabled = false;
						_frmMainInstance.btn_ChoosePathExport.Enabled = false;

						// Controles do Menu Superior
						// Botão de Conversão
						_frmMainInstance.mnu_item_Convert.Enabled = false;
						// Controle relacionado à escolha de caminho
						_frmMainInstance.mnu_item_ChoosePath.Enabled = false;
					}
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------
				}

				public class CustomToolTip
				{
					// Pega a instância do frmMain
					private static frmMain _frmMainInstance;

					public CustomToolTip(frmMain frmMainInstance) { _frmMainInstance = frmMainInstance; }
					

					// FUNÇÃO: DEFINE O TOOLTIP
					// -------------------------------------------------------------
					// Descrição:
					// Função responsável definir o ToolTip para  os  controles  que
					// foram passados.
					// [AVISO]
					// Método ruim, recomenda-se melhoria utilizando-se de  recursão
					// ou similares.
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					public void SetfrmMainToolTip(params Control[] ToolTipReceiverControls)
					{
						// Criando a ToolTip customizada
						ToolTip ToolTip = new ToolTip()
						{
							// Propriedades Principais
							ToolTipIcon = System.Windows.Forms.ToolTipIcon.Info,
							ToolTipTitle = "INFO",
							// Definindo os Delays
							AutoPopDelay = 5000,
							InitialDelay = 1000,
							ReshowDelay = 500,
							// Força a ToolTip a aparecer, independente do form  estar  ativo
							// ou não
							ShowAlways = true
						};

						ToolTip.SetToolTip(_frmMainInstance.btn_OpenPathImport, "Botão para abrir a pasta onde está apontado o caminho de importação.");
						ToolTip.SetToolTip(_frmMainInstance.btn_OpenPathExport, "Botão para abrir a pasta onde está apontado o caminho de exportação.");

						ToolTip.SetToolTip(_frmMainInstance.btn_ChoosePathImport, "Botão para escolher o caminho de importação.");
						ToolTip.SetToolTip(_frmMainInstance.btn_ChoosePathExport, "Botão para escolher o caminho de exportação.");

						ToolTip.SetToolTip(_frmMainInstance.txt_PathImport, "Caminho de importação utilizado na conversão.");
						ToolTip.SetToolTip(_frmMainInstance.txt_PathExport, "Caminho de exportação utilizado na conversão.");

						ToolTip.SetToolTip(
							_frmMainInstance.chk_useExportPath,
							
							"Ao marcar a CheckBox, o programa utilizará o caminho de expor-" + Environment.NewLine +
							"tação padrão definido no código dentro do  Script,  atualmente" + Environment.NewLine +
							"sendo, a pasta onde está localizado o executável do Script."
						);
					}
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------
				}
			}

			public class Status
			{
				// Pega a instância do frmMain
				private static frmMain _frmMainInstance;

				public Status(frmMain frmMainInstance) { _frmMainInstance = frmMainInstance; }


				// FUNÇÃO: ATUALIZA STATUS DA APLICAÇÃO
				// -------------------------------------------------------------
				// Descrição:
				// Atualiza o status da aplicação na parte inferior  da  aplica-
				// ção.
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				public void Update(string applicationCurrentStatus, int progressBarValue = 0)
				{
					// Atualiza o rótulo
					_frmMainInstance.stts_lbl_ConversionStatus.Text = applicationCurrentStatus;
					// Atualiza a progress bar
					_frmMainInstance.stts_prg_ConversionStatus.Value = progressBarValue;
				}
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------
			}

			public class Errors
			{
				// Pega a instância do frmMain
				private static frmMain _frmMainInstance;

				public Errors(frmMain frmMainInstance) { _frmMainInstance = frmMainInstance; }


				// FUNÇÃO: ATUALIZA O DESIGN DE ACORDO COM OS ERROS RETORNADOS
				// -------------------------------------------------------------
				// Descrição:
				// Função que atualiza o design, ou seja, o painel de erros, com
				// os erros retornados pelo arquivo do terminal.
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				public void Update(List<StoredTerminalErrors> lstErrors)
				{
					// Itera de acordo com o número de erros dispostos na lista
					int numberOfOcurrences = 0;
					while (numberOfOcurrences < lstErrors.Count)
					{
						// Cria a variável que vai manipular o conteúdo da label
						string labelContent = "";

						// While que itera em 3, criando 3 labels
						int labelCounter = 0;
						while (labelCounter < 3)
						{
							// Atribui o valor da label de acordo com a posição do contador
							switch (labelCounter)
							{
								// Primeira label
								case 0:
									// Recebe o número da hora no índex do erro
									labelContent = DateTime.Now.ToString();
									break;
								// Segunda label
								case 1:
									// Recebe a descrição do erro vinda do terminal
									labelContent = lstErrors[numberOfOcurrences].errorDescription.ToString();
									break;
								// Terceira label
								case 2:
									// Recebe a descrição da exceção vinda do terminal
									labelContent = lstErrors[numberOfOcurrences].errorException.ToString();
									break;
								default:
									break;
							}

							// Adiciona uma nova label
							_frmMainInstance.tbl_ErrorList.Controls.Add(
								new Label()
								{
									// Ajustes visuais
									BackColor = Color.FromArgb(250, 220, 220),
									BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle,
									Dock = DockStyle.Fill,
									// Conteúdo da Mensagem
									Text = labelContent
								},
								// Posição da label na coluna do tableLayout
								labelCounter,
								// Modelo de linha que vai ser pego como referência pelo tableLayout
								_frmMainInstance.tbl_ErrorList.RowCount - 1
							);

							// Adiciona +1 ao contador para ir para a próxima label
							labelCounter++;
						}

						// Pega um ponto de referência da linha anterior
						RowStyle previousRowReference = _frmMainInstance.tbl_ErrorList.RowStyles[_frmMainInstance.tbl_ErrorList.RowCount - 1];

						// Aumenta o contador de linhas do painel em um
						_frmMainInstance.tbl_ErrorList.RowCount++;

						// Adiciona uma nova linha como cópia da linha anterior
						_frmMainInstance.tbl_ErrorList.RowStyles.Add(new RowStyle(previousRowReference.SizeType, previousRowReference.Height));

						// Adiciona +1 ao contador para ir para o próximo erro
						numberOfOcurrences++;
					}
				}
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------
			}
		}
	
		public class Prompt
		{
			// Pega a instância do frmMain
			private static frmMain _frmMainInstance;

			public Prompt(frmMain frmMainInstance) { _frmMainInstance = frmMainInstance; }


			// FUNÇÃO: ATUALIZA AS VARIÁVEIS COM CAMINHO
			// -------------------------------------------------------------
			// Descrição:
			// Função para atualizar as variáveis que possuem  o  caminho  e
			// retorna o caminho para o método.
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			public string OpenDialogPath(string pathStoreVariable = "")
			{
				// Abre a caixa de diálogo com base no caminho da TextBox
				if (_frmMainInstance.folderbd_PDFFolder.ShowDialog() == DialogResult.OK) { pathStoreVariable = _frmMainInstance.folderbd_PDFFolder.SelectedPath; }
				// Retorna o caminho para o método
				return pathStoreVariable;
			}
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// -------------------------------------------------------------
		}
	}
}