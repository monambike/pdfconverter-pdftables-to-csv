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

        private void llbl_Path_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            string path = llbl_pathLink.Text;
            Process.Start("explorer.exe", path);
        }

        private void btn_Converter_Click(object sender, EventArgs e)
        {
            lbl_warningTitle.Visible = true;
            lbl_warningDesc.Visible = true;

            try
            {
                Process process = new Process();

                process = Process.Start(new ProcessStartInfo(@"..\..\..\pdfconverter-python\pdfconverter.exe")
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
