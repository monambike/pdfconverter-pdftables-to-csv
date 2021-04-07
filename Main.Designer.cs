
namespace pdfconverter_csharp
{
    partial class Main
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Main));
            this.btn_Convert = new System.Windows.Forms.Button();
            this.lbl_pathDesc = new System.Windows.Forms.Label();
            this.llbl_pathLink = new System.Windows.Forms.LinkLabel();
            this.img_pdf = new System.Windows.Forms.PictureBox();
            this.img_csv = new System.Windows.Forms.PictureBox();
            this.pnl_whitebackground = new System.Windows.Forms.Panel();
            this.lbl_warningTitle = new System.Windows.Forms.Label();
            this.lbl_warningDesc = new System.Windows.Forms.Label();
            this.lbl_PDFConverter = new System.Windows.Forms.Label();
            this.img_arrow = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.img_pdf)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.img_csv)).BeginInit();
            this.pnl_whitebackground.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.img_arrow)).BeginInit();
            this.SuspendLayout();
            // 
            // btn_Convert
            // 
            this.btn_Convert.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_Convert.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.btn_Convert.ForeColor = System.Drawing.Color.IndianRed;
            this.btn_Convert.Location = new System.Drawing.Point(240, 286);
            this.btn_Convert.Name = "btn_Convert";
            this.btn_Convert.Size = new System.Drawing.Size(285, 40);
            this.btn_Convert.TabIndex = 0;
            this.btn_Convert.Text = "Converter";
            this.btn_Convert.UseVisualStyleBackColor = true;
            this.btn_Convert.Click += new System.EventHandler(this.btn_Converter_Click);
            // 
            // lbl_pathDesc
            // 
            this.lbl_pathDesc.AutoSize = true;
            this.lbl_pathDesc.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.lbl_pathDesc.ForeColor = System.Drawing.Color.Snow;
            this.lbl_pathDesc.Location = new System.Drawing.Point(149, 174);
            this.lbl_pathDesc.Name = "lbl_pathDesc";
            this.lbl_pathDesc.Size = new System.Drawing.Size(441, 48);
            this.lbl_pathDesc.TabIndex = 1;
            this.lbl_pathDesc.Text = "Clique no botão abaixo para converter os arquivos em PDF\r\npara CSV que estão em:";
            this.lbl_pathDesc.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // llbl_pathLink
            // 
            this.llbl_pathLink.AutoSize = true;
            this.llbl_pathLink.Cursor = System.Windows.Forms.Cursors.Hand;
            this.llbl_pathLink.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.llbl_pathLink.LinkColor = System.Drawing.Color.Pink;
            this.llbl_pathLink.Location = new System.Drawing.Point(32, 247);
            this.llbl_pathLink.Name = "llbl_pathLink";
            this.llbl_pathLink.Size = new System.Drawing.Size(687, 24);
            this.llbl_pathLink.TabIndex = 2;
            this.llbl_pathLink.TabStop = true;
            this.llbl_pathLink.Text = "C:\\Users\\dvp10\\Desktop\\Desktop\\pdfconverter\\pdfconverter-csharp\\bin\\Debug\\netcore" +
    "app3.1";
            this.llbl_pathLink.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.llbl_Path_LinkClicked);
            // 
            // img_pdf
            // 
            this.img_pdf.Image = global::pdfconverter_csharp.Properties.Resources.pdf_icon;
            this.img_pdf.Location = new System.Drawing.Point(428, 16);
            this.img_pdf.Name = "img_pdf";
            this.img_pdf.Size = new System.Drawing.Size(115, 115);
            this.img_pdf.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.img_pdf.TabIndex = 4;
            this.img_pdf.TabStop = false;
            // 
            // img_csv
            // 
            this.img_csv.Image = global::pdfconverter_csharp.Properties.Resources.csv_icon;
            this.img_csv.Location = new System.Drawing.Point(659, 16);
            this.img_csv.Name = "img_csv";
            this.img_csv.Size = new System.Drawing.Size(115, 115);
            this.img_csv.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.img_csv.TabIndex = 5;
            this.img_csv.TabStop = false;
            // 
            // pnl_whitebackground
            // 
            this.pnl_whitebackground.BackColor = System.Drawing.Color.Snow;
            this.pnl_whitebackground.Controls.Add(this.lbl_warningTitle);
            this.pnl_whitebackground.Controls.Add(this.lbl_warningDesc);
            this.pnl_whitebackground.Controls.Add(this.lbl_PDFConverter);
            this.pnl_whitebackground.Controls.Add(this.img_arrow);
            this.pnl_whitebackground.Controls.Add(this.img_csv);
            this.pnl_whitebackground.Controls.Add(this.img_pdf);
            this.pnl_whitebackground.Location = new System.Drawing.Point(-3, -4);
            this.pnl_whitebackground.Name = "pnl_whitebackground";
            this.pnl_whitebackground.Size = new System.Drawing.Size(787, 166);
            this.pnl_whitebackground.TabIndex = 6;
            // 
            // lbl_warningTitle
            // 
            this.lbl_warningTitle.AutoSize = true;
            this.lbl_warningTitle.Font = new System.Drawing.Font("Arial", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.lbl_warningTitle.Location = new System.Drawing.Point(39, 82);
            this.lbl_warningTitle.Name = "lbl_warningTitle";
            this.lbl_warningTitle.Size = new System.Drawing.Size(176, 19);
            this.lbl_warningTitle.TabIndex = 11;
            this.lbl_warningTitle.Text = "HEY, PODE FECHAR!";
            this.lbl_warningTitle.Visible = false;
            // 
            // lbl_warningDesc
            // 
            this.lbl_warningDesc.Font = new System.Drawing.Font("Arial Narrow", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.lbl_warningDesc.Location = new System.Drawing.Point(39, 105);
            this.lbl_warningDesc.Name = "lbl_warningDesc";
            this.lbl_warningDesc.Size = new System.Drawing.Size(354, 50);
            this.lbl_warningDesc.TabIndex = 10;
            this.lbl_warningDesc.Text = "Seus arquivos estão sendo (ou já foram) convertidos, cheque o progresso no link d" +
    "a pasta.";
            this.lbl_warningDesc.Visible = false;
            // 
            // lbl_PDFConverter
            // 
            this.lbl_PDFConverter.AutoSize = true;
            this.lbl_PDFConverter.Font = new System.Drawing.Font("Arial", 28.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.lbl_PDFConverter.Location = new System.Drawing.Point(30, 16);
            this.lbl_PDFConverter.Name = "lbl_PDFConverter";
            this.lbl_PDFConverter.Size = new System.Drawing.Size(339, 55);
            this.lbl_PDFConverter.TabIndex = 8;
            this.lbl_PDFConverter.Text = "PDFConverter";
            this.lbl_PDFConverter.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // img_arrow
            // 
            this.img_arrow.Image = global::pdfconverter_csharp.Properties.Resources.arrow_icon;
            this.img_arrow.Location = new System.Drawing.Point(549, 16);
            this.img_arrow.Name = "img_arrow";
            this.img_arrow.Size = new System.Drawing.Size(104, 76);
            this.img_arrow.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.img_arrow.TabIndex = 7;
            this.img_arrow.TabStop = false;
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Firebrick;
            this.ClientSize = new System.Drawing.Size(782, 353);
            this.Controls.Add(this.llbl_pathLink);
            this.Controls.Add(this.lbl_pathDesc);
            this.Controls.Add(this.btn_Convert);
            this.Controls.Add(this.pnl_whitebackground);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "Main";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "PDFConverter";
            ((System.ComponentModel.ISupportInitialize)(this.img_pdf)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.img_csv)).EndInit();
            this.pnl_whitebackground.ResumeLayout(false);
            this.pnl_whitebackground.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.img_arrow)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_Convert;
        private System.Windows.Forms.Label lbl_pathDesc;
        private System.Windows.Forms.LinkLabel llbl_pathLink;
        private System.Windows.Forms.PictureBox img_pdf;
        private System.Windows.Forms.PictureBox img_csv;
        private System.Windows.Forms.Panel pnl_whitebackground;
        private System.Windows.Forms.PictureBox img_arrow;
        private System.Windows.Forms.Label lbl_PDFConverter;
        private System.Windows.Forms.Label lbl_warningDesc;
        private System.Windows.Forms.Label lbl_warningTitle;
    }
}

