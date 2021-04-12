
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
            this.img_pdf = new System.Windows.Forms.PictureBox();
            this.img_csv = new System.Windows.Forms.PictureBox();
            this.pnl_whitebackground = new System.Windows.Forms.Panel();
            this.prg_pdfConversion = new System.Windows.Forms.ProgressBar();
            this.lbl_warningDesc = new System.Windows.Forms.Label();
            this.lbl_PDFConverter = new System.Windows.Forms.Label();
            this.pnl_pinkbackground = new System.Windows.Forms.Panel();
            this.lbl_warningTitle = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.img_pdf)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.img_csv)).BeginInit();
            this.pnl_whitebackground.SuspendLayout();
            this.pnl_pinkbackground.SuspendLayout();
            this.SuspendLayout();
            // 
            // btn_Convert
            // 
            this.btn_Convert.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(245)))), ((int)(((byte)(15)))), ((int)(((byte)(5)))));
            this.btn_Convert.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_Convert.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn_Convert.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.btn_Convert.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(230)))), ((int)(((byte)(230)))), ((int)(((byte)(230)))));
            this.btn_Convert.Location = new System.Drawing.Point(27, 301);
            this.btn_Convert.Name = "btn_Convert";
            this.btn_Convert.Size = new System.Drawing.Size(285, 40);
            this.btn_Convert.TabIndex = 0;
            this.btn_Convert.Text = "Converter";
            this.btn_Convert.UseVisualStyleBackColor = false;
            this.btn_Convert.Click += new System.EventHandler(this.btn_Converter_Click);
            // 
            // img_pdf
            // 
            this.img_pdf.Image = global::pdfconverter_csharp.Properties.Resources.pdf_icon;
            this.img_pdf.Location = new System.Drawing.Point(375, 46);
            this.img_pdf.Name = "img_pdf";
            this.img_pdf.Size = new System.Drawing.Size(80, 80);
            this.img_pdf.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.img_pdf.TabIndex = 4;
            this.img_pdf.TabStop = false;
            // 
            // img_csv
            // 
            this.img_csv.Image = ((System.Drawing.Image)(resources.GetObject("img_csv.Image")));
            this.img_csv.Location = new System.Drawing.Point(571, 46);
            this.img_csv.Name = "img_csv";
            this.img_csv.Size = new System.Drawing.Size(80, 80);
            this.img_csv.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.img_csv.TabIndex = 5;
            this.img_csv.TabStop = false;
            // 
            // pnl_whitebackground
            // 
            this.pnl_whitebackground.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(230)))), ((int)(((byte)(230)))), ((int)(((byte)(230)))));
            this.pnl_whitebackground.Controls.Add(this.prg_pdfConversion);
            this.pnl_whitebackground.Controls.Add(this.lbl_warningDesc);
            this.pnl_whitebackground.Controls.Add(this.lbl_PDFConverter);
            this.pnl_whitebackground.Controls.Add(this.img_csv);
            this.pnl_whitebackground.Controls.Add(this.img_pdf);
            this.pnl_whitebackground.Controls.Add(this.pnl_pinkbackground);
            this.pnl_whitebackground.Location = new System.Drawing.Point(-3, -4);
            this.pnl_whitebackground.Name = "pnl_whitebackground";
            this.pnl_whitebackground.Size = new System.Drawing.Size(787, 199);
            this.pnl_whitebackground.TabIndex = 6;
            // 
            // prg_pdfConversion
            // 
            this.prg_pdfConversion.Location = new System.Drawing.Point(461, 72);
            this.prg_pdfConversion.Name = "prg_pdfConversion";
            this.prg_pdfConversion.Size = new System.Drawing.Size(104, 29);
            this.prg_pdfConversion.TabIndex = 7;
            // 
            // lbl_warningDesc
            // 
            this.lbl_warningDesc.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(125)))), ((int)(((byte)(120)))));
            this.lbl_warningDesc.Font = new System.Drawing.Font("Arial Narrow", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.lbl_warningDesc.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(230)))), ((int)(((byte)(230)))), ((int)(((byte)(230)))));
            this.lbl_warningDesc.Location = new System.Drawing.Point(36, 131);
            this.lbl_warningDesc.Name = "lbl_warningDesc";
            this.lbl_warningDesc.Size = new System.Drawing.Size(333, 54);
            this.lbl_warningDesc.TabIndex = 10;
            this.lbl_warningDesc.Text = "Description";
            this.lbl_warningDesc.Visible = false;
            // 
            // lbl_PDFConverter
            // 
            this.lbl_PDFConverter.AutoSize = true;
            this.lbl_PDFConverter.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(190)))), ((int)(((byte)(20)))), ((int)(((byte)(10)))));
            this.lbl_PDFConverter.Font = new System.Drawing.Font("Arial", 28.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.lbl_PDFConverter.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(235)))), ((int)(((byte)(175)))), ((int)(((byte)(175)))));
            this.lbl_PDFConverter.Location = new System.Drawing.Point(30, 46);
            this.lbl_PDFConverter.Name = "lbl_PDFConverter";
            this.lbl_PDFConverter.Size = new System.Drawing.Size(339, 55);
            this.lbl_PDFConverter.TabIndex = 8;
            this.lbl_PDFConverter.Text = "PDFConverter";
            this.lbl_PDFConverter.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // pnl_pinkbackground
            // 
            this.pnl_pinkbackground.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(125)))), ((int)(((byte)(120)))));
            this.pnl_pinkbackground.Controls.Add(this.lbl_warningTitle);
            this.pnl_pinkbackground.Location = new System.Drawing.Point(30, 101);
            this.pnl_pinkbackground.Name = "pnl_pinkbackground";
            this.pnl_pinkbackground.Size = new System.Drawing.Size(339, 84);
            this.pnl_pinkbackground.TabIndex = 12;
            this.pnl_pinkbackground.Visible = false;
            // 
            // lbl_warningTitle
            // 
            this.lbl_warningTitle.AutoSize = true;
            this.lbl_warningTitle.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(125)))), ((int)(((byte)(120)))));
            this.lbl_warningTitle.Font = new System.Drawing.Font("Arial", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.lbl_warningTitle.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(190)))), ((int)(((byte)(20)))), ((int)(((byte)(10)))));
            this.lbl_warningTitle.Location = new System.Drawing.Point(5, 11);
            this.lbl_warningTitle.Name = "lbl_warningTitle";
            this.lbl_warningTitle.Size = new System.Drawing.Size(54, 19);
            this.lbl_warningTitle.TabIndex = 11;
            this.lbl_warningTitle.Text = "TITLE";
            this.lbl_warningTitle.Visible = false;
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(190)))), ((int)(((byte)(20)))), ((int)(((byte)(10)))));
            this.ClientSize = new System.Drawing.Size(782, 353);
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
            this.pnl_pinkbackground.ResumeLayout(false);
            this.pnl_pinkbackground.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btn_Convert;
        private System.Windows.Forms.PictureBox img_pdf;
        private System.Windows.Forms.PictureBox img_csv;
        private System.Windows.Forms.Panel pnl_whitebackground;
        private System.Windows.Forms.Label lbl_PDFConverter;
        private System.Windows.Forms.Label lbl_warningDesc;
        private System.Windows.Forms.Label lbl_warningTitle;
        private System.Windows.Forms.Panel pnl_pinkbackground;
        private System.Windows.Forms.ProgressBar prg_pdfConversion;
    }
}

