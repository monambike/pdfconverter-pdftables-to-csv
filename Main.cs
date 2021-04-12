using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace pdfconverter_csharp
{
    public partial class Main : Form
    {
        public Main()
        {
            InitializeComponent();
        }

        public void btn_Converter_Click(object sender, EventArgs e)
        {
            prg_pdfConversion.Style = ProgressBarStyle.Marquee;
            prg_pdfConversion.Value = 0;
            lbl_warningTitle.Text = "POR FAVOR AGUARDE...";
            lbl_warningDesc.Text = "Seus PDF's estão sendo convertidos nesse momento.";

            pnl_pinkbackground.Visible = true;
            lbl_warningTitle.Visible = true;
            lbl_warningDesc.Visible = true;

            try
            {
                using (System.Diagnostics.Process execute = new System.Diagnostics.Process())
                {
                    Process cmdProcess = new Process()
                    {
                        StartInfo = new ProcessStartInfo
                        {
                            FileName = @"..\..\..\exe\dist\pdfconverter\pdfconverter.exe",
                            CreateNoWindow = true,
                            UseShellExecute = false,
                            RedirectStandardError = true,
                        }
                    };

                    cmdProcess.EnableRaisingEvents = true;

                    cmdProcess.Start();

                    cmdProcess.WaitForExit();

                    prg_pdfConversion.Style = ProgressBarStyle.Continuous;
                    prg_pdfConversion.Value = 100;
                    lbl_warningTitle.Text = "CONCLUÍDO!";
                    lbl_warningDesc.Text = "A conversão foi realizada com sucesso!";
                }
            }
            catch (Exception err)
            {
                MessageBox.Show("Não foi possível executar o programa devido à um errro.\n\n" + err.ToString());
            }
        }
    }
}
