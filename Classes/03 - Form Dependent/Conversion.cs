using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using pdfconverter_desktop.Forms;

namespace pdfconverter_desktop.Classes
{
	public class Conversion
	{
        public static Process correctionProcess;

        // Pega a instância do frmMain
		private static frmMain _frmMainInstance;
		// 01 - Main Classes
		private static Messages ShowMessage = new Messages();
		// 02 - Stored Info
		private static StoredPaths StoredPaths = new StoredPaths();
		// 03 - Form Dependent
		private static Conversion.Tracking ConversionTracking;
		private static CurrentForm.Design.Status FormStatus;

		public Conversion(frmMain frmMainInstance) 
		{
			// Recebe a instância do form
			_frmMainInstance = frmMainInstance;
			// Recebe as classes com variáveis com parâmetros  para  classes
			// dependentes de form
			ConversionTracking = new Conversion.Tracking(frmMainInstance, StoredPaths);
			FormStatus = new CurrentForm.Design.Status(frmMainInstance);
		}

        // Parar o processo - botão ParaConversão
        public void Stop()
        {

            try
            {
                correctionProcess.Kill();
                //ShowMessage.Info(@"ATENÇÃO! A conversão foi parada.");
                MessageBox.Show(string.Format(@"        ATENÇÃO! "+ Environment.NewLine + Environment.NewLine + "A conversão foi parada."), "Parar Serviço", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            catch (Exception ex)
            {
                MessageBox.Show(string.Format("Erro:{0} {1}",ex.Message,Environment.NewLine),"Parar Serviço", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

		// FUNÇÃO: INICIA A CONVERSÃO
		// -------------------------------------------------------------
		// Descrição:
		// Função para iniciar a conversão.
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		public void Start()
		{
			// Variável responsável por armazenar o resultado de  caixas  de
			// diálogos
			DialogResult dialogResult;

			// MENSAGEM: CAIXA DE CONFIRMAÇÃO
			// -------------------------------------------------------------
			// Descrição:
			// Caixa de confirmação de inicialização de conversão.
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			dialogResult = ShowMessage.Confirmation
			(
				"Você deseja iniciar a conversão de PDFs no caminho informado?" + Environment.NewLine +
				Environment.NewLine +
				"Caminho: '" + _frmMainInstance.txt_PathExport.Text + "'"
			);
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// -------------------------------------------------------------

			// Caso o usuário aperte em 'sim' na caixa de confirmação
			if (dialogResult == DialogResult.Yes)
			{
				FormStatus.Update("Iniciando conversão...");

				// Passa os caminhos das TextBox para a classe que  manipula  os
				// caminhos para garantir que não vão ser passados  os  caminhos
				// errados
				StoredPaths.importFolderPath = _frmMainInstance.txt_PathImport.Text;
				StoredPaths.exportFolderPath = _frmMainInstance.txt_PathExport.Text;

				// Faz a validação da existência do diretório de importação
				if (Directory.Exists(StoredPaths.importFolderPath))
				{
					// Verifica se há arquivos PDF para serem convertidos
					if (Directory.GetFiles(StoredPaths.importFolderPath, "*.pdf", SearchOption.TopDirectoryOnly).Length == 0)
					{
						// MENSAGEM: ABERTURA DE PASTA
						// -------------------------------------------------------------
						// Descrição:
						// Mensagem para quando não sejam encontrados  arquivos  PDF  em
						// uma determinada pasta, para que o usuário decida se a quer a-
						// brir ou não.
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						dialogResult = ShowMessage.Confirmation
						(
							"A conversão não será realizada pois não há arquivos PDF para s" +
							"erem convertidos em:" + Environment.NewLine +
							"'" + StoredPaths.importFolderPath + Environment.NewLine +
							Environment.NewLine +
							"Deseja visualizar a pasta agora?"
						);
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						// -------------------------------------------------------------

						// Caso o usuário queira, a pasta é aberta
						if (dialogResult == DialogResult.Yes) { Process.Start(StoredPaths.importFolderPath); }

						// Para a execução do método
						return;
					}

					try
					{
						// Argumentos
						string terminalArguments = "--importPath \"" + StoredPaths.importFolderPath + "\"";
						// Se optar por escolher um caminho de exportação
						if (_frmMainInstance.chk_useExportPath.Checked)
						{
							// Faz a validação da existência do diretório de exportação
							if (Directory.Exists(StoredPaths.exportFolderPath))
							{
								// Se existe passa para os argumentos
								terminalArguments += " --exportPath \"" + StoredPaths.exportFolderPath + "\"";
							}
							else
							{
								// Atualiza o status da aplicação
								FormStatus.Update("Erro ao realizar a conversão.");

								// MENSAGEM: ERRO DE CAMINHO DE IMPORTAÇÃO
								// -------------------------------------------------------------
								// Descrição:
								// Mensagem para quando houve erro ao tentar achar  o  diretório
								// de Importação
								// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
								ShowMessage.Error(
									"O diretório de exportação informado não foi encontrado ou " +
									"não existe. Verifique o caminho do diretório e tente novam" +
									"ente.",

									"Diretório Não Encontrado"
								);
								// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
								// -------------------------------------------------------------

								// Para a execução do método
								return;
							}
						}

						// Definindo a metadata do processo do terminal
						ProcessStartInfo terminalProcess = new ProcessStartInfo
						{
							// Atributos Principais
							Arguments = terminalArguments,
							CreateNoWindow = true,
							FileName = StoredPaths.executeScriptPath,
							// Outros
							RedirectStandardError = true,
							RedirectStandardOutput = true,
							UseShellExecute = false
						};

						
						// Executa o Script e anota o progresso do processo em uma vari-
						// ável
						correctionProcess = Process.Start(terminalProcess);
						// Habilita processo disparar eventos
						correctionProcess.EnableRaisingEvents = true;
						// Trigger de evento para quando o processo é finalizado
						correctionProcess.Exited += new EventHandler(ConversionTracking.ConversionProcessExited);

						bool processIsRunning = Process.GetProcessesByName(correctionProcess.ProcessName).Any();
						// Se o processo está rodando corretamente
						if (processIsRunning)
						{
							// MENSAGEM: ÊXITO NA INICIALIZAÇÃO DO SCRIPT
							// -------------------------------------------------------------
							// Descrição:
							// O Script inicializou êxito.
							// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
							FormStatus.Update("Aguarde... A conversão foi iniciada");
							_frmMainInstance.stts_prg_ConversionStatus.Value = 0;
							ShowMessage.Info
							(
								"O Script foi inicializado com êxito, aguarde até o término" +
								" da conversão."
							);
							// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
							// -------------------------------------------------------------

							// Inicia o rastreamento da conversão
							ConversionTracking.Start();
						}
						else { ShowMessage.Info("Não foi possível realizar a conversão."); }
					}
					catch (Win32Exception exceptionError)
					{
						// Mensagem para quando não é possível achar o Script
						ShowMessage.Exception
						(
							"Não foi possível encontrar o arquivo executável para rea" +
							"lizar a execução do Script." + Environment.NewLine +
							"Contate o desenvolvedor para verificar se o caminho na c" +
							"lasse 'Paths.cs' que referencia o executável do Script e" +
							"stá correto.",

							exceptionError
						);

						// Atualiza o status da aplicação
						FormStatus.Update("Erro ao realizar a conversão.");
					}
					catch (Exception exceptionError)
					{
						// Erro não tratado
						ShowMessage.Exception("Ocorreu um erro desconhecido ao tentar criar o arquivo.",exceptionError);

						// Atualiza o status da aplicação
						FormStatus.Update("Erro ao realizar a conversão.");
					}
				}
				else
				{
					// Atualiza o status da aplicação
					FormStatus.Update("Erro ao realizar a conversão.");

					// MENSAGEM: ERRO DE CAMINHO DE EXPORTAÇÃO
					// -------------------------------------------------------------
					// Descrição:
					// Mensagem para quando houve erro ao tentar achar  o  diretório
					// de exportação
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					ShowMessage.Error
					(
						"O diretório de importação informado não foi encontrado ou " +
						"não existe. Verifique o caminho do diretório e tente novam" +
						"ente.",

						"Diretório Não Encontrado"
					);
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------
				}
			}
		}
		// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		// -------------------------------------------------------------


		private class Tracking
		{
			// Pega a instância do frmMain
			private static frmMain _frmMainInstance;
			// 01 - Main Classes
			private static Messages ShowMessage = new Messages();
			// 02 - StoredInfo
			private static StoredPaths StoredPaths;

			public Tracking(frmMain frmMainInstance, StoredPaths conversionStoredPaths)
			{
				_frmMainInstance = frmMainInstance;
				StoredPaths = conversionStoredPaths;
			}


			// VARIÁVEIS
			// -------------------------------------------------------------
			// Descrição:
			// Variáveis utilizadas nessa região.
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// GERAIS
			// Contador que faz o rastreio do progresso da conversão
			Timer timer = new Timer();
			// Resultado em porcentagem do cálculo realizado.
			double dblConversionProgressInPercent = 0;
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// -------------------------------------------------------------
			

			// FUNÇÃO: INICIA CONTADOR DA CONVERSÃO
			// -------------------------------------------------------------
			// Descrição:
			// Função que inicia o contador que trabalha em conjunto com  a
			// função que monitora o progresso de conversão.
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			public void Start()
			{
				// Criando timer
				timer.Tick += new EventHandler(TrackingConversionProgress);
				timer.Interval = 500;

				// Iniciando o timer
				timer.Start();
			}
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// -------------------------------------------------------------


			// FUNÇÃO: PARA CONTADOR DA CONVERSÃO
			// -------------------------------------------------------------
			// Descrição:
			// Função que para o contador que trabalha  em  conjunto  com  a
			// função que monitora o progresso de conversão.
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			public void Stop() { timer.Stop(); }
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// -------------------------------------------------------------


			// FUNÇÃO: PARA CONTADOR DA CONVERSÃO
			// -------------------------------------------------------------
			// Descrição:
			// Função que realiza o cálculo da conversão.
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			private void ReturnConversionProgress()
			{
				// VARIÁVEIS
				// -------------------------------------------------------------
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

				// FORMATAÇÃO
				// -------------------------------------------------------------
				// Descrição:
				// Variáveis que realizam a contagem de tipos de leitura e  for-
				// matação selecionados pelo usuário ou pré definidos.
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// Contador de tipos de leitura realizados na conversão
				int counterReadingTypes = 2;
				// Contador de tipos de formatação realizados na conversão
				int counterFormattingTypes = 4;
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------

				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------

				try
				{
					// CONTADORES DE ARQUIVOS
					// -------------------------------------------------------------
					// Descrição:
					// Variáveis que realizam a contagem de arquivos em uma determi-
					// nada pasta.
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// Contador de número de arquivos de importação
					int counterImportFiles = Directory.GetFiles
					(
						StoredPaths.importFolderPath,
						"*.pdf",
						SearchOption.TopDirectoryOnly
					).Length;
					// Contador de número de arquivos de exportação
					int counterExportFiles = Directory.GetFiles
					(
						StoredPaths.exportFolderPath + @"\\resultados",
						"*.txt",
						SearchOption.AllDirectories
					).Length;
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------


					// FÓRMULA DE CÁLCULO DE PROGRESSO
					// -------------------------------------------------------------
					// Descrição:
					// A fórmula de cálculo de progresso em porcentagem é gerada com
					// base na seguinte descrição:
					// O número de arquivos de exportação mutiplicado por  100, deve
					// ser dividido pelo número de arquivos de importação  multipli-
					// cado pelo resultado da mutiplicação do  número  de  tipos  de
					// leitura e formatação selecionados para a conversão.
					// Gerando porcentagem de progresso
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					dblConversionProgressInPercent =
					(
						(counterExportFiles * 100)
						/
						(counterImportFiles * (counterReadingTypes * counterFormattingTypes))
					);
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------
				}
				catch (DivideByZeroException) { dblConversionProgressInPercent = 0; }
				catch (ArgumentException exceptionError)
				{
					// MENSAGEM DE AVISO
					// -------------------------------------------------------------
					// Descrição:
					// Mensagem de erro caso tenha acontecido algum erro relacionado
					// aos arquivos de importação ou exportação.
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					ShowMessage.Exception
					(
						"Ocorreu um erro ao tentar achar os arquivos de importação e ex" +
						"portação." + Environment.NewLine +
						Environment.NewLine +
						"Caminho de Importação: '" + StoredPaths.importFolderPath + "'",

						exceptionError
					);
				}
				catch (Exception exceptionError)
				{
					// ERRO: DESCONHECIDO
					// -------------------------------------------------------------
					// Descrição:
					// Mensagem de erro caso tenha acontecido algum erro desconheci-
					// do ao tentar relatar o progresso de conversão.
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					ShowMessage.Exception
					(
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						"Ocorreu um erro desconhecido ao tentar realizar o cálculo de p" +
						"rogresso.",

						exceptionError
					);
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------
				}

				// Atualiza a ProgressBar
				_frmMainInstance.stts_prg_ConversionStatus.Value = (int)dblConversionProgressInPercent;
				// Atualiza a mensagem de texto com o progresso
				_frmMainInstance.stts_lbl_ConversionProgress.Text = dblConversionProgressInPercent.ToString() + "%";
			}
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// -------------------------------------------------------------


			// EVENTO: TIMER DE CONVERSÃO BATE
			// -------------------------------------------------------------
			// Descrição:
			// Evento que é disparado toda vez que o timer bate. Esse evento
			// chama o método que retorna a porcentagem do progresso da con-
			// versão baseado em um cálculo.
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			private void TrackingConversionProgress(object sender, EventArgs e) { ReturnConversionProgress(); }
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// -------------------------------------------------------------


			// EVENTO: TERMINAL FINALIZADO
			// -------------------------------------------------------------
			// Descrição:
			// Evento disparado quando o terminal é finalizado.
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			public void ConversionProcessExited(object sender, System.EventArgs e)
			{
				// Retorna as mensagens de erro de acordo com o final da operação
				//new Conversion.TerminalFile.Errors().Get();

				// Faz com que pare de ser realizada o tracking da conversão
				Stop();
				
				// Retorna o último estado da conversão
				ReturnConversionProgress();

				// Mostra mensagem de êxito
				ShowMessage.Info("A conversão foi concluída com êxito!");
			}
			// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			// -------------------------------------------------------------
		}

		public class TerminalFile
		{
			public class Errors
			{
				// 02 - Stored Info
				private static StoredPaths StoredPaths = new StoredPaths();

				// FUNÇÃO: RETORNA OS ERROS DADOS PELO TERMINAL
				// -------------------------------------------------------------
				// Descrição:
				// Função que pega os erros retornados pelo arquivo do terminal.
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				public void Get()
				{
					// REGEX
					// -------------------------------------------------------------
					// Variáveis que seguram algumas regras de expressões  regulares
					// para poder encontrar algum item posteriormente.
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// Regex que vai ser aplicado para procurar a descrição do erro
					Regex regexFindDescriptionText = new Regex
					(
						@"(?<=\<d\>)" +
						@"(.+?)" + // Conteúdo da descrição que vai ser lido
						@"(?=\<\/d\>)",

						RegexOptions.Singleline
					);
					// REGEX que vai ser aplicado para procurar a exceção do erro
					Regex regexFindExceptionText = new Regex
					(
						@"(?<=\<e\>)" +
						@"(.+?)" + // Conteúdo da descrição que vai ser lido
						@"(?=\<\/e\>)",

						RegexOptions.Singleline
					);
					// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					// -------------------------------------------------------------


					// Muda o diretório que está sendo trabalhado para a mesma pasta
					// onde está sendo executado o terminal para que direcione o ar-
					// quivo de saída para lá
					Directory.SetCurrentDirectory(Path.GetDirectoryName(StoredPaths.terminalFilePath));

					try
					{
						// Pega o conteúdo do arquivo de texto do terminal e passa  para
						// uma string
						string terminalFileContent = File.ReadAllText(StoredPaths.terminalFilePath);

						// PROCURANDO OCORRÊNCIAS COM O REGEX
						// -------------------------------------------------------------
						// Descrição:
						// Procura todas as ocorrências de acordo com o  REGEX  que  foi
						// passado   anteriormente   em   'regexFindDescriptionText'   e
						// 'regexFindExceptionText'
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						// Procura pela mensagem de descrição
						Match foundDescriptionMatch = regexFindDescriptionText.Match(terminalFileContent);
						// Procura pela mensagem de exceção
						Match foundExceptionMatch = regexFindExceptionText.Match(terminalFileContent);
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						// -------------------------------------------------------------

						List<StoredTerminalErrors> lstErrors = new List<StoredTerminalErrors>();

						// Enquanto houver descrições de erros continua passando para o próximo
						int counterErrorMatches = 0;
						while (foundDescriptionMatch.Success)
						{
							// Insere os erros na lista
							lstErrors.Insert(
								counterErrorMatches,
								new StoredTerminalErrors()
								{
									errorDescription = foundDescriptionMatch.ToString(),
									errorException = foundExceptionMatch.ToString()
								}
							);

							// AVANÇANDO PARA O PRÓXIMO ÍNDEX
							// -------------------------------------------------------------
							// Descrição:
							// Avançando para o próximo encontro da descrição e da exceção e
							// adicionando +1 ao contador.
							// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
							// Procura pela próxima descrição
							foundDescriptionMatch = foundDescriptionMatch.NextMatch();
							// Procura pela próxima exceção
							foundExceptionMatch = foundExceptionMatch.NextMatch();
							// Adiciona +1 ao contador
							counterErrorMatches++;
							// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
							// -------------------------------------------------------------
						}

						// RETORNO DE ÊXITO/ERRO
						// -------------------------------------------------------------
						// Descrição:
						// Região referente ao retorno ao  usuário  referente  caso  foi
						// captado algum erro no terminal ou caso a conversão foi reali-
						// zada com êxito sem qualquer problema.
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						if (lstErrors.Count < 1)
						{
							// Mensagem de êxito
							ShowMessage.Info("A conversão foi realizada com êxito!");

							// Atualiza o status da aplicação
							FormStatus.Update("Êxito na conversão.", 100);
						}
						else
						{
							// Mensagem de erro
							ShowMessage.Error(
								"Houve um erro (ou mais) ao tentar realizar a conversão, por favor verifique.",

								"Aviso de Erro"
							);

							// Atualiza o status da aplicação
							FormStatus.Update("Erro ao realizar a conversão.");
						}
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						// -------------------------------------------------------------

						// Atualiza o status da label com a hora da última conversão
						// realizada
						_frmMainInstance.stts_lbl_LastConversionTime.Text = DateTime.Now.ToString();

						// Chama a função que atualiza o design após inserir os erros na
						// string
						//DesignErrors.Update(lstErrors);
					}
					// Quando o arquivo do terminal não é encontrado
					catch (FileNotFoundException)
					{
						// MENSAGEM DE ERRO
						// -------------------------------------------------------------
						// Descrição:
						// Mensagem de erro para quando não é possível encontrar  o  ar-
						// quivo de saída do terminal.
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						ShowMessage.Error("O arquivo de sáida do terminal não foi encontrado.", "Arquivo de Saída do Terminal Não Encontrado");
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						// -------------------------------------------------------------
					}
					catch (Exception exceptionError)
					{
						// MENSAGEM DE ERRO
						// -------------------------------------------------------------
						// Descrição:
						// Mensagem de erro para quando ocorre um erro  desconhecido  ao
						// fazer a leitura do arquivo do terminal.
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						ShowMessage.Exception("Ocorreu um erro desconhecido ao tentar fazer a leitura do arquivo do terminal.", exceptionError);
						// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
						// -------------------------------------------------------------
					}
				}
				// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
				// -------------------------------------------------------------
			}
		}
	}
}