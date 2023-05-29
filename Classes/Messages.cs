using System;
using System.Windows.Forms;

// OuroWebPDFConverter
// Solução de Teste do Script - Custom Software
namespace pdfconverter_desktop
{
    // CLASSE DE MENSAGENS
    // -------------------------------------------------------------
    // Descrição:
    // Classe responsável pelo retorno de mensagens para o usuário.
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    public class Messages
    {
        public DialogResult Info(string messageContent)
        {
            return MessageBox.Show
            (
                messageContent,

                "Mensagem de Aviso",
                MessageBoxButtons.OK,
                MessageBoxIcon.Asterisk
            );
        }

        public DialogResult Confirmation(string messageContent)
        {
            return MessageBox.Show
            (
                messageContent,

                "Caixa de Confirmação",
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Question
            );
        }

        public DialogResult Error(string messageContent, string messageTitle)
        {
            return MessageBox.Show
            (
                messageContent,

                "Erro: " + messageTitle,
                MessageBoxButtons.OK,
                MessageBoxIcon.Error
            );
        }

        public DialogResult Exception(string messageContent, Exception exceptionError)
        {
            // Concatena a Exception na variável de exibição da mensagem
            return MessageBox.Show
            (
                messageContent + "\n" +
                "\n" +
                "[Por favor, contate o desenvolvedor e mostre essa mensagem de " +
                "erro.]\n" +
                "--------------- + ---------------\n" +
                "\n" +
                "EXCEPTION LOG\n" +
                "\n" +
                exceptionError.ToString(),

                "Erro",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error
            );
        }
    }
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    // -------------------------------------------------------------
}
