using System;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;

namespace pdfconverter_csharp
{
    public partial class Main : Form
    {
        public Main()
        {
            InitializeComponent();
        }

        private void btn_Converter_Click(object sender, EventArgs e)
        {
            lbl_warningTitle.Visible = true;
            lbl_warningDesc.Visible = true;

            try
            {
                Process process = new Process();

                process = Process.Start(new ProcessStartInfo(@"..\..\..\exe\dist\pdfconverter\pdfconverter.exe")
                {
                    WindowStyle = ProcessWindowStyle.Normal,
                    CreateNoWindow = true,
                    UseShellExecute = false,
                    RedirectStandardError = true
                });


            }
            catch(Exception err)
            {
                MessageBox.Show("Não foi possível executar o programa devido à um errro.\n\n" + err.ToString());
            }
        }
    }
}
