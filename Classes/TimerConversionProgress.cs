//using System;
//using System.IO;
//using System.Windows.Forms;

//// PDFConverter
//// Aplicativo de Teste - Custom Software
//namespace pdfconverter_desktop
//{
//    // TIMER DA CONVERSÃO
//    // -------------------------------------------------------------
//    // Descrição:
//    // Classe responsável pelo gerenciamento do timer que atualiza o
//    // status da conversão.
//    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//    public class TimerConversionProgress
//    {

//        #region GLOBAL VARIABLES

//        // CHAMANDO CLASSES
//        // -------------------------------------------------------------
//        // Descrição:
//        // Fazendo a chamada de algumas classes.
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        // Importando classe de caminhos
//        StoredPaths classPaths = new StoredPaths();
//        // Importando classe de exibição de mensagens
//        Messages classMessages = new Messages();
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        // -------------------------------------------------------------


//        // RESULTADO
//        // -------------------------------------------------------------
//        // Descrição:
//        // Resultado em porcentagem do cálculo realizado.
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        public double dblConversionProgressInPercent = 0;
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        // -------------------------------------------------------------


//        // CONTADOR
//        // -------------------------------------------------------------
//        // Descrição:
//        // Criando o contador.
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        Timer timerConversionProgress = new Timer();
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        // -------------------------------------------------------------
//        // FUNÇÃO: INICIA CONTADOR DA CONVERSÃO
//        // -------------------------------------------------------------
//        // Descrição:
//        // Função que inicia o contador que trabalha em conjunto com  a
//        // função que monitora o progresso de conversão.
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        public void startTimerGetConversionProgress()
//        {
//            timerConversionProgress.Tick += new EventHandler(getConversionProgress);
//            timerConversionProgress.Interval = 500;
//            timerConversionProgress.Start();
//        }
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        // -------------------------------------------------------------

//        // FUNÇÃO: PARA CONTADOR DA CONVERSÃO
//        // -------------------------------------------------------------
//        // Descrição:
//        // Função que para o contador que trabalha  em  conjunto  com  a
//        // função que monitora o progresso de conversão.
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        public void stopTimerGetConversionProgress()
//        {
//            return;
//        }
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        // -------------------------------------------------------------

//        #endregion

//        #region FUNCTIONS

//        // FUNÇÃO: INICIA CONTADOR DA CONVERSÃO
//        // -------------------------------------------------------------
//        // Descrição:
//        // Função que inicia o contador que trabalha em conjunto com  a
//        // função que monitora o progresso de conversão.
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        public void startTimerGetConversionProgress()
//        {
//            timerConversionProgress.Tick += new EventHandler(getConversionProgress);
//            timerConversionProgress.Interval = 500;
//            timerConversionProgress.Start();
//        }
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        // -------------------------------------------------------------

//        // FUNÇÃO: PARA CONTADOR DA CONVERSÃO
//        // -------------------------------------------------------------
//        // Descrição:
//        // Função que para o contador que trabalha  em  conjunto  com  a
//        // função que monitora o progresso de conversão.
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        public void stopTimerGetConversionProgress()
//        {
//            return;
//        }
//        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//        // -------------------------------------------------------------

//        #endregion
//    }
//    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//    // -------------------------------------------------------------
//}
