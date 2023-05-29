namespace pdfconverter_desktop.Forms
{
    partial class frmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMain));
            this.lbl_TitlePDFConverter = new System.Windows.Forms.Label();
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.img_PDF = new System.Windows.Forms.PictureBox();
            this.lbl_SubtitlePDFConverter = new System.Windows.Forms.Label();
            this.folderbd_PDFFolder = new System.Windows.Forms.FolderBrowserDialog();
            this.mnu_TopMenu = new System.Windows.Forms.MenuStrip();
            this.mnu_item_Convertion = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_Convert = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_ItemSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.mnu_item_Open = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_OpenTerminalFile = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_ItemSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.mnu_item_OpenPathImport = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_OpenPathExport = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_ChoosePath = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_ChoosePathImport = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_ChoosePathExport = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_About = new System.Windows.Forms.ToolStripMenuItem();
            this.mnu_item_Exit = new System.Windows.Forms.ToolStripMenuItem();
            this.lbl_PathPDF = new System.Windows.Forms.Label();
            this.txt_PathImport = new System.Windows.Forms.TextBox();
            this.tbl_ImportPDF = new System.Windows.Forms.TableLayoutPanel();
            this.lbl_PathExport = new System.Windows.Forms.Label();
            this.btn_OpenPathImport = new System.Windows.Forms.Button();
            this.lbl_PathImport = new System.Windows.Forms.Label();
            this.txt_PathExport = new System.Windows.Forms.TextBox();
            this.btn_OpenPathExport = new System.Windows.Forms.Button();
            this.btn_ChoosePathImport = new System.Windows.Forms.Button();
            this.btn_ChoosePathExport = new System.Windows.Forms.Button();
            this.chk_useExportPath = new System.Windows.Forms.CheckBox();
            this.stts_lbl_LabelProgress = new System.Windows.Forms.ToolStripStatusLabel();
            this.stts_prg_ConversionStatus = new System.Windows.Forms.ToolStripProgressBar();
            this.stts_lbl_LabelSep2 = new System.Windows.Forms.ToolStripStatusLabel();
            this.stts_lbl_ConversionStatus = new System.Windows.Forms.ToolStripStatusLabel();
            this.stts_StripMenuStatus = new System.Windows.Forms.StatusStrip();
            this.stts_lbl_LabelStatus = new System.Windows.Forms.ToolStripStatusLabel();
            this.stts_lbl_LabelSep1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.stts_lbl_ConversionProgress = new System.Windows.Forms.ToolStripStatusLabel();
            this.stts_lbl_LabelLastConversionTime = new System.Windows.Forms.ToolStripStatusLabel();
            this.stts_lbl_LastConversionTime = new System.Windows.Forms.ToolStripStatusLabel();
            this.btn_Convert = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.btn_PararConversao = new System.Windows.Forms.Button();
            this.lbl_UserName = new System.Windows.Forms.Label();
            this.btn_Exit = new System.Windows.Forms.Button();
            this.pnl_ErrorListBackground = new System.Windows.Forms.Panel();
            this.pnl_ErrorListDataBackground = new System.Windows.Forms.Panel();
            this.tbl_ErrorList = new System.Windows.Forms.TableLayoutPanel();
            this.tableLayoutPanel2 = new System.Windows.Forms.TableLayoutPanel();
            this.lbl_ErrorListTitle = new System.Windows.Forms.Label();
            this.tbl_item_lblNumber = new System.Windows.Forms.Label();
            this.tbl_item_lblDescription = new System.Windows.Forms.Label();
            this.tbl_item_lblException = new System.Windows.Forms.Label();
            this.tableLayoutPanel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.img_PDF)).BeginInit();
            this.mnu_TopMenu.SuspendLayout();
            this.tbl_ImportPDF.SuspendLayout();
            this.stts_StripMenuStatus.SuspendLayout();
            this.panel1.SuspendLayout();
            this.pnl_ErrorListBackground.SuspendLayout();
            this.pnl_ErrorListDataBackground.SuspendLayout();
            this.tableLayoutPanel2.SuspendLayout();
            this.SuspendLayout();
            // 
            // lbl_TitlePDFConverter
            // 
            this.lbl_TitlePDFConverter.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lbl_TitlePDFConverter.AutoSize = true;
            this.lbl_TitlePDFConverter.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.lbl_TitlePDFConverter.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lbl_TitlePDFConverter.Font = new System.Drawing.Font("Microsoft Sans Serif", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_TitlePDFConverter.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.lbl_TitlePDFConverter.Location = new System.Drawing.Point(2, 0);
            this.lbl_TitlePDFConverter.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lbl_TitlePDFConverter.MinimumSize = new System.Drawing.Size(309, 56);
            this.lbl_TitlePDFConverter.Name = "lbl_TitlePDFConverter";
            this.lbl_TitlePDFConverter.Size = new System.Drawing.Size(450, 57);
            this.lbl_TitlePDFConverter.TabIndex = 4;
            this.lbl_TitlePDFConverter.Text = "PDFConverter";
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tableLayoutPanel1.AutoSize = true;
            this.tableLayoutPanel1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.tableLayoutPanel1.ColumnCount = 2;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 80F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 20F));
            this.tableLayoutPanel1.Controls.Add(this.img_PDF, 1, 0);
            this.tableLayoutPanel1.Controls.Add(this.lbl_TitlePDFConverter, 0, 0);
            this.tableLayoutPanel1.Controls.Add(this.lbl_SubtitlePDFConverter, 0, 1);
            this.tableLayoutPanel1.Location = new System.Drawing.Point(9, 40);
            this.tableLayoutPanel1.Margin = new System.Windows.Forms.Padding(2);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 2;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tableLayoutPanel1.Size = new System.Drawing.Size(568, 181);
            this.tableLayoutPanel1.TabIndex = 6;
            // 
            // img_PDF
            // 
            this.img_PDF.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.img_PDF.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.img_PDF.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.img_PDF.Image = global::pdfconverter_desktop.Properties.Resources.pdfconverter_ico_white;
            this.img_PDF.Location = new System.Drawing.Point(454, 0);
            this.img_PDF.Margin = new System.Windows.Forms.Padding(0);
            this.img_PDF.MinimumSize = new System.Drawing.Size(109, 111);
            this.img_PDF.Name = "img_PDF";
            this.tableLayoutPanel1.SetRowSpan(this.img_PDF, 2);
            this.img_PDF.Size = new System.Drawing.Size(114, 181);
            this.img_PDF.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.img_PDF.TabIndex = 7;
            this.img_PDF.TabStop = false;
            // 
            // lbl_SubtitlePDFConverter
            // 
            this.lbl_SubtitlePDFConverter.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lbl_SubtitlePDFConverter.AutoSize = true;
            this.lbl_SubtitlePDFConverter.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.lbl_SubtitlePDFConverter.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_SubtitlePDFConverter.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(25)))), ((int)(((byte)(25)))), ((int)(((byte)(25)))));
            this.lbl_SubtitlePDFConverter.Location = new System.Drawing.Point(2, 57);
            this.lbl_SubtitlePDFConverter.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lbl_SubtitlePDFConverter.Name = "lbl_SubtitlePDFConverter";
            this.lbl_SubtitlePDFConverter.Padding = new System.Windows.Forms.Padding(2);
            this.lbl_SubtitlePDFConverter.Size = new System.Drawing.Size(450, 124);
            this.lbl_SubtitlePDFConverter.TabIndex = 8;
            this.lbl_SubtitlePDFConverter.Text = resources.GetString("lbl_SubtitlePDFConverter.Text");
            // 
            // mnu_TopMenu
            // 
            this.mnu_TopMenu.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(230)))), ((int)(((byte)(230)))), ((int)(((byte)(230)))));
            this.mnu_TopMenu.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.mnu_TopMenu.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.mnu_TopMenu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnu_item_Convertion,
            this.mnu_item_About,
            this.mnu_item_Exit});
            this.mnu_TopMenu.Location = new System.Drawing.Point(0, 0);
            this.mnu_TopMenu.Name = "mnu_TopMenu";
            this.mnu_TopMenu.Padding = new System.Windows.Forms.Padding(4, 2, 0, 2);
            this.mnu_TopMenu.Size = new System.Drawing.Size(588, 28);
            this.mnu_TopMenu.TabIndex = 8;
            this.mnu_TopMenu.Text = "mnu_TopMenu";
            // 
            // mnu_item_Convertion
            // 
            this.mnu_item_Convertion.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnu_item_Convert,
            this.mnu_item_ItemSeparator1,
            this.mnu_item_Open,
            this.mnu_item_ChoosePath});
            this.mnu_item_Convertion.Font = new System.Drawing.Font("Segoe UI", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.mnu_item_Convertion.Name = "mnu_item_Convertion";
            this.mnu_item_Convertion.ShortcutKeyDisplayString = "";
            this.mnu_item_Convertion.Size = new System.Drawing.Size(90, 24);
            this.mnu_item_Convertion.Text = "&Conversão";
            // 
            // mnu_item_Convert
            // 
            this.mnu_item_Convert.Name = "mnu_item_Convert";
            this.mnu_item_Convert.ShortcutKeyDisplayString = "Ctrl+S";
            this.mnu_item_Convert.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.S)));
            this.mnu_item_Convert.Size = new System.Drawing.Size(192, 24);
            this.mnu_item_Convert.Text = "&Converter";
            this.mnu_item_Convert.Click += new System.EventHandler(this.mnu_item_Convert_Click);
            // 
            // mnu_item_ItemSeparator1
            // 
            this.mnu_item_ItemSeparator1.Name = "mnu_item_ItemSeparator1";
            this.mnu_item_ItemSeparator1.Size = new System.Drawing.Size(189, 6);
            // 
            // mnu_item_Open
            // 
            this.mnu_item_Open.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnu_item_OpenTerminalFile,
            this.mnu_item_ItemSeparator2,
            this.mnu_item_OpenPathImport,
            this.mnu_item_OpenPathExport});
            this.mnu_item_Open.Name = "mnu_item_Open";
            this.mnu_item_Open.ShortcutKeyDisplayString = "";
            this.mnu_item_Open.Size = new System.Drawing.Size(192, 24);
            this.mnu_item_Open.Text = "&Abrir";
            // 
            // mnu_item_OpenTerminalFile
            // 
            this.mnu_item_OpenTerminalFile.Name = "mnu_item_OpenTerminalFile";
            this.mnu_item_OpenTerminalFile.ShortcutKeyDisplayString = "Ctrl+Shift+O";
            this.mnu_item_OpenTerminalFile.ShortcutKeys = ((System.Windows.Forms.Keys)(((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Shift) 
            | System.Windows.Forms.Keys.O)));
            this.mnu_item_OpenTerminalFile.Size = new System.Drawing.Size(306, 24);
            this.mnu_item_OpenTerminalFile.Text = "Arquivo do &Terminal";
            this.mnu_item_OpenTerminalFile.Click += new System.EventHandler(this.mnu_item_OpenTerminalFile_Click);
            // 
            // mnu_item_ItemSeparator2
            // 
            this.mnu_item_ItemSeparator2.Name = "mnu_item_ItemSeparator2";
            this.mnu_item_ItemSeparator2.Size = new System.Drawing.Size(303, 6);
            // 
            // mnu_item_OpenPathImport
            // 
            this.mnu_item_OpenPathImport.Name = "mnu_item_OpenPathImport";
            this.mnu_item_OpenPathImport.ShortcutKeyDisplayString = "Ctrl+Shift+I";
            this.mnu_item_OpenPathImport.ShortcutKeys = ((System.Windows.Forms.Keys)(((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Shift) 
            | System.Windows.Forms.Keys.I)));
            this.mnu_item_OpenPathImport.Size = new System.Drawing.Size(306, 24);
            this.mnu_item_OpenPathImport.Text = "Pasta de &Importação";
            this.mnu_item_OpenPathImport.Click += new System.EventHandler(this.mnu_item_OpenPathImport_Click);
            // 
            // mnu_item_OpenPathExport
            // 
            this.mnu_item_OpenPathExport.Name = "mnu_item_OpenPathExport";
            this.mnu_item_OpenPathExport.ShortcutKeyDisplayString = "Ctrl+Shift+E";
            this.mnu_item_OpenPathExport.ShortcutKeys = ((System.Windows.Forms.Keys)(((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Shift) 
            | System.Windows.Forms.Keys.E)));
            this.mnu_item_OpenPathExport.Size = new System.Drawing.Size(306, 24);
            this.mnu_item_OpenPathExport.Text = "Pasta de &Exportação";
            this.mnu_item_OpenPathExport.Click += new System.EventHandler(this.mnu_item_OpenPathExport_Click);
            // 
            // mnu_item_ChoosePath
            // 
            this.mnu_item_ChoosePath.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnu_item_ChoosePathImport,
            this.mnu_item_ChoosePathExport});
            this.mnu_item_ChoosePath.Name = "mnu_item_ChoosePath";
            this.mnu_item_ChoosePath.Size = new System.Drawing.Size(192, 24);
            this.mnu_item_ChoosePath.Text = "&Selecionar";
            // 
            // mnu_item_ChoosePathImport
            // 
            this.mnu_item_ChoosePathImport.Name = "mnu_item_ChoosePathImport";
            this.mnu_item_ChoosePathImport.ShortcutKeyDisplayString = "Ctrl+Alt+I";
            this.mnu_item_ChoosePathImport.ShortcutKeys = ((System.Windows.Forms.Keys)(((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Alt) 
            | System.Windows.Forms.Keys.I)));
            this.mnu_item_ChoosePathImport.Size = new System.Drawing.Size(291, 24);
            this.mnu_item_ChoosePathImport.Text = "Pasta de &Importação";
            this.mnu_item_ChoosePathImport.Click += new System.EventHandler(this.mnu_item_ChoosePathImport_Click);
            // 
            // mnu_item_ChoosePathExport
            // 
            this.mnu_item_ChoosePathExport.Name = "mnu_item_ChoosePathExport";
            this.mnu_item_ChoosePathExport.ShortcutKeyDisplayString = "Ctrl+Alt+E";
            this.mnu_item_ChoosePathExport.ShortcutKeys = ((System.Windows.Forms.Keys)(((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Alt) 
            | System.Windows.Forms.Keys.E)));
            this.mnu_item_ChoosePathExport.Size = new System.Drawing.Size(291, 24);
            this.mnu_item_ChoosePathExport.Text = "Pasta de &Exportação";
            this.mnu_item_ChoosePathExport.Click += new System.EventHandler(this.mnu_item_ChoosePathExport_Click);
            // 
            // mnu_item_About
            // 
            this.mnu_item_About.Font = new System.Drawing.Font("Segoe UI", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.mnu_item_About.Name = "mnu_item_About";
            this.mnu_item_About.ShortcutKeyDisplayString = "Ctrl+I";
            this.mnu_item_About.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.I)));
            this.mnu_item_About.Size = new System.Drawing.Size(47, 24);
            this.mnu_item_About.Text = "&Info";
            this.mnu_item_About.Click += new System.EventHandler(this.mnu_item_About_Click);
            // 
            // mnu_item_Exit
            // 
            this.mnu_item_Exit.Font = new System.Drawing.Font("Segoe UI", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.mnu_item_Exit.Name = "mnu_item_Exit";
            this.mnu_item_Exit.ShortcutKeyDisplayString = "Ctrl+F4";
            this.mnu_item_Exit.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.F4)));
            this.mnu_item_Exit.Size = new System.Drawing.Size(46, 24);
            this.mnu_item_Exit.Text = "&Sair";
            this.mnu_item_Exit.Click += new System.EventHandler(this.mnu_item_Exit_Click);
            // 
            // lbl_PathPDF
            // 
            this.lbl_PathPDF.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lbl_PathPDF.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.tbl_ImportPDF.SetColumnSpan(this.lbl_PathPDF, 4);
            this.lbl_PathPDF.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_PathPDF.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.lbl_PathPDF.Location = new System.Drawing.Point(2, 2);
            this.lbl_PathPDF.Margin = new System.Windows.Forms.Padding(0);
            this.lbl_PathPDF.MinimumSize = new System.Drawing.Size(566, 42);
            this.lbl_PathPDF.Name = "lbl_PathPDF";
            this.lbl_PathPDF.Padding = new System.Windows.Forms.Padding(38, 0, 38, 0);
            this.lbl_PathPDF.Size = new System.Drawing.Size(566, 48);
            this.lbl_PathPDF.TabIndex = 3;
            this.lbl_PathPDF.Text = "Selecione o caminho da pasta contendo os PDF\'s para realizar a importação:";
            this.lbl_PathPDF.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // txt_PathImport
            // 
            this.txt_PathImport.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.txt_PathImport.BackColor = System.Drawing.SystemColors.Info;
            this.txt_PathImport.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txt_PathImport.Location = new System.Drawing.Point(108, 58);
            this.txt_PathImport.Margin = new System.Windows.Forms.Padding(2);
            this.txt_PathImport.Name = "txt_PathImport";
            this.txt_PathImport.Size = new System.Drawing.Size(234, 26);
            this.txt_PathImport.TabIndex = 5;
            // 
            // tbl_ImportPDF
            // 
            this.tbl_ImportPDF.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tbl_ImportPDF.AutoSize = true;
            this.tbl_ImportPDF.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.tbl_ImportPDF.ColumnCount = 4;
            this.tbl_ImportPDF.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.tbl_ImportPDF.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tbl_ImportPDF.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.tbl_ImportPDF.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.tbl_ImportPDF.Controls.Add(this.lbl_PathExport, 0, 2);
            this.tbl_ImportPDF.Controls.Add(this.btn_OpenPathImport, 3, 1);
            this.tbl_ImportPDF.Controls.Add(this.lbl_PathPDF, 0, 0);
            this.tbl_ImportPDF.Controls.Add(this.txt_PathImport, 1, 1);
            this.tbl_ImportPDF.Controls.Add(this.lbl_PathImport, 0, 1);
            this.tbl_ImportPDF.Controls.Add(this.txt_PathExport, 1, 2);
            this.tbl_ImportPDF.Controls.Add(this.btn_OpenPathExport, 3, 2);
            this.tbl_ImportPDF.Controls.Add(this.btn_ChoosePathImport, 2, 1);
            this.tbl_ImportPDF.Controls.Add(this.btn_ChoosePathExport, 2, 2);
            this.tbl_ImportPDF.Controls.Add(this.chk_useExportPath, 1, 3);
            this.tbl_ImportPDF.Location = new System.Drawing.Point(9, 223);
            this.tbl_ImportPDF.Margin = new System.Windows.Forms.Padding(2);
            this.tbl_ImportPDF.MinimumSize = new System.Drawing.Size(568, 98);
            this.tbl_ImportPDF.Name = "tbl_ImportPDF";
            this.tbl_ImportPDF.Padding = new System.Windows.Forms.Padding(2);
            this.tbl_ImportPDF.RowCount = 4;
            this.tbl_ImportPDF.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tbl_ImportPDF.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tbl_ImportPDF.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tbl_ImportPDF.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tbl_ImportPDF.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tbl_ImportPDF.Size = new System.Drawing.Size(570, 163);
            this.tbl_ImportPDF.TabIndex = 4;
            // 
            // lbl_PathExport
            // 
            this.lbl_PathExport.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.lbl_PathExport.AutoSize = true;
            this.lbl_PathExport.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lbl_PathExport.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_PathExport.Location = new System.Drawing.Point(4, 100);
            this.lbl_PathExport.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lbl_PathExport.Name = "lbl_PathExport";
            this.lbl_PathExport.Padding = new System.Windows.Forms.Padding(2);
            this.lbl_PathExport.Size = new System.Drawing.Size(100, 26);
            this.lbl_PathExport.TabIndex = 8;
            this.lbl_PathExport.Text = "Exportação:";
            this.lbl_PathExport.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // btn_OpenPathImport
            // 
            this.btn_OpenPathImport.AutoSize = true;
            this.btn_OpenPathImport.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.btn_OpenPathImport.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_OpenPathImport.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_OpenPathImport.Image = global::pdfconverter_desktop.Properties.Resources.folder;
            this.btn_OpenPathImport.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn_OpenPathImport.Location = new System.Drawing.Point(476, 52);
            this.btn_OpenPathImport.Margin = new System.Windows.Forms.Padding(2);
            this.btn_OpenPathImport.Name = "btn_OpenPathImport";
            this.btn_OpenPathImport.Padding = new System.Windows.Forms.Padding(1);
            this.btn_OpenPathImport.Size = new System.Drawing.Size(90, 38);
            this.btn_OpenPathImport.TabIndex = 6;
            this.btn_OpenPathImport.Text = "Abrir";
            this.btn_OpenPathImport.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn_OpenPathImport.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btn_OpenPathImport.UseVisualStyleBackColor = true;
            this.btn_OpenPathImport.Click += new System.EventHandler(this.btn_OpenPathImport_Click);
            // 
            // lbl_PathImport
            // 
            this.lbl_PathImport.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.lbl_PathImport.AutoSize = true;
            this.lbl_PathImport.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lbl_PathImport.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_PathImport.Location = new System.Drawing.Point(4, 58);
            this.lbl_PathImport.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lbl_PathImport.Name = "lbl_PathImport";
            this.lbl_PathImport.Padding = new System.Windows.Forms.Padding(2);
            this.lbl_PathImport.Size = new System.Drawing.Size(100, 26);
            this.lbl_PathImport.TabIndex = 4;
            this.lbl_PathImport.Text = "Importação:";
            this.lbl_PathImport.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // txt_PathExport
            // 
            this.txt_PathExport.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.txt_PathExport.BackColor = System.Drawing.SystemColors.Info;
            this.txt_PathExport.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txt_PathExport.Location = new System.Drawing.Point(108, 100);
            this.txt_PathExport.Margin = new System.Windows.Forms.Padding(2);
            this.txt_PathExport.Name = "txt_PathExport";
            this.txt_PathExport.Size = new System.Drawing.Size(234, 26);
            this.txt_PathExport.TabIndex = 7;
            // 
            // btn_OpenPathExport
            // 
            this.btn_OpenPathExport.AutoSize = true;
            this.btn_OpenPathExport.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.btn_OpenPathExport.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_OpenPathExport.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_OpenPathExport.Image = global::pdfconverter_desktop.Properties.Resources.folder;
            this.btn_OpenPathExport.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn_OpenPathExport.Location = new System.Drawing.Point(476, 94);
            this.btn_OpenPathExport.Margin = new System.Windows.Forms.Padding(2);
            this.btn_OpenPathExport.Name = "btn_OpenPathExport";
            this.btn_OpenPathExport.Padding = new System.Windows.Forms.Padding(1);
            this.btn_OpenPathExport.Size = new System.Drawing.Size(90, 38);
            this.btn_OpenPathExport.TabIndex = 9;
            this.btn_OpenPathExport.Text = "Abrir";
            this.btn_OpenPathExport.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn_OpenPathExport.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btn_OpenPathExport.UseVisualStyleBackColor = true;
            this.btn_OpenPathExport.Click += new System.EventHandler(this.btn_OpenPathExport_Click);
            // 
            // btn_ChoosePathImport
            // 
            this.btn_ChoosePathImport.AutoSize = true;
            this.btn_ChoosePathImport.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.btn_ChoosePathImport.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_ChoosePathImport.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_ChoosePathImport.Image = global::pdfconverter_desktop.Properties.Resources.folder;
            this.btn_ChoosePathImport.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn_ChoosePathImport.Location = new System.Drawing.Point(346, 52);
            this.btn_ChoosePathImport.Margin = new System.Windows.Forms.Padding(2);
            this.btn_ChoosePathImport.Name = "btn_ChoosePathImport";
            this.btn_ChoosePathImport.Padding = new System.Windows.Forms.Padding(1);
            this.btn_ChoosePathImport.Size = new System.Drawing.Size(126, 38);
            this.btn_ChoosePathImport.TabIndex = 5;
            this.btn_ChoosePathImport.Text = "Selecionar";
            this.btn_ChoosePathImport.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn_ChoosePathImport.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btn_ChoosePathImport.UseVisualStyleBackColor = true;
            this.btn_ChoosePathImport.Click += new System.EventHandler(this.btn_ChoosePathImport_Click);
            // 
            // btn_ChoosePathExport
            // 
            this.btn_ChoosePathExport.AutoSize = true;
            this.btn_ChoosePathExport.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.btn_ChoosePathExport.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_ChoosePathExport.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_ChoosePathExport.Image = global::pdfconverter_desktop.Properties.Resources.folder;
            this.btn_ChoosePathExport.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn_ChoosePathExport.Location = new System.Drawing.Point(346, 94);
            this.btn_ChoosePathExport.Margin = new System.Windows.Forms.Padding(2);
            this.btn_ChoosePathExport.Name = "btn_ChoosePathExport";
            this.btn_ChoosePathExport.Padding = new System.Windows.Forms.Padding(1);
            this.btn_ChoosePathExport.Size = new System.Drawing.Size(126, 38);
            this.btn_ChoosePathExport.TabIndex = 8;
            this.btn_ChoosePathExport.Text = "Selecionar";
            this.btn_ChoosePathExport.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn_ChoosePathExport.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btn_ChoosePathExport.UseVisualStyleBackColor = true;
            this.btn_ChoosePathExport.Click += new System.EventHandler(this.btn_ChoosePathExport_Click);
            // 
            // chk_useExportPath
            // 
            this.chk_useExportPath.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.chk_useExportPath.AutoSize = true;
            this.chk_useExportPath.Checked = true;
            this.chk_useExportPath.CheckState = System.Windows.Forms.CheckState.Checked;
            this.tbl_ImportPDF.SetColumnSpan(this.chk_useExportPath, 4);
            this.chk_useExportPath.Cursor = System.Windows.Forms.Cursors.Hand;
            this.chk_useExportPath.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.chk_useExportPath.Location = new System.Drawing.Point(4, 137);
            this.chk_useExportPath.Margin = new System.Windows.Forms.Padding(2);
            this.chk_useExportPath.Name = "chk_useExportPath";
            this.chk_useExportPath.Padding = new System.Windows.Forms.Padding(2, 0, 0, 0);
            this.chk_useExportPath.Size = new System.Drawing.Size(238, 21);
            this.chk_useExportPath.TabIndex = 10;
            this.chk_useExportPath.Text = "Escolher Caminho de Exportação";
            this.chk_useExportPath.UseVisualStyleBackColor = true;
            this.chk_useExportPath.CheckedChanged += new System.EventHandler(this.chk_useExportPath_CheckedChanged);
            // 
            // stts_lbl_LabelProgress
            // 
            this.stts_lbl_LabelProgress.BackColor = System.Drawing.SystemColors.ControlLight;
            this.stts_lbl_LabelProgress.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.stts_lbl_LabelProgress.Name = "stts_lbl_LabelProgress";
            this.stts_lbl_LabelProgress.Size = new System.Drawing.Size(65, 19);
            this.stts_lbl_LabelProgress.Text = "Progress:";
            // 
            // stts_prg_ConversionStatus
            // 
            this.stts_prg_ConversionStatus.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
            this.stts_prg_ConversionStatus.Name = "stts_prg_ConversionStatus";
            this.stts_prg_ConversionStatus.Size = new System.Drawing.Size(75, 18);
            // 
            // stts_lbl_LabelSep2
            // 
            this.stts_lbl_LabelSep2.BackColor = System.Drawing.SystemColors.ControlLight;
            this.stts_lbl_LabelSep2.Name = "stts_lbl_LabelSep2";
            this.stts_lbl_LabelSep2.Padding = new System.Windows.Forms.Padding(5, 0, 5, 0);
            this.stts_lbl_LabelSep2.Size = new System.Drawing.Size(20, 19);
            this.stts_lbl_LabelSep2.Text = "|";
            // 
            // stts_lbl_ConversionStatus
            // 
            this.stts_lbl_ConversionStatus.BackColor = System.Drawing.SystemColors.ControlLight;
            this.stts_lbl_ConversionStatus.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.stts_lbl_ConversionStatus.Name = "stts_lbl_ConversionStatus";
            this.stts_lbl_ConversionStatus.Size = new System.Drawing.Size(66, 19);
            this.stts_lbl_ConversionStatus.Text = "<status>";
            // 
            // stts_StripMenuStatus
            // 
            this.stts_StripMenuStatus.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.stts_StripMenuStatus.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.stts_lbl_LabelStatus,
            this.stts_lbl_ConversionStatus,
            this.stts_lbl_LabelSep1,
            this.stts_lbl_LabelProgress,
            this.stts_prg_ConversionStatus,
            this.stts_lbl_ConversionProgress,
            this.stts_lbl_LabelSep2,
            this.stts_lbl_LabelLastConversionTime,
            this.stts_lbl_LastConversionTime});
            this.stts_StripMenuStatus.Location = new System.Drawing.Point(0, 588);
            this.stts_StripMenuStatus.Name = "stts_StripMenuStatus";
            this.stts_StripMenuStatus.Padding = new System.Windows.Forms.Padding(1, 0, 10, 0);
            this.stts_StripMenuStatus.Size = new System.Drawing.Size(588, 24);
            this.stts_StripMenuStatus.TabIndex = 7;
            this.stts_StripMenuStatus.Text = "statusStrip1";
            // 
            // stts_lbl_LabelStatus
            // 
            this.stts_lbl_LabelStatus.BackColor = System.Drawing.SystemColors.ControlLight;
            this.stts_lbl_LabelStatus.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.stts_lbl_LabelStatus.Name = "stts_lbl_LabelStatus";
            this.stts_lbl_LabelStatus.Size = new System.Drawing.Size(50, 19);
            this.stts_lbl_LabelStatus.Text = "Status:";
            // 
            // stts_lbl_LabelSep1
            // 
            this.stts_lbl_LabelSep1.BackColor = System.Drawing.SystemColors.ControlLight;
            this.stts_lbl_LabelSep1.Name = "stts_lbl_LabelSep1";
            this.stts_lbl_LabelSep1.Padding = new System.Windows.Forms.Padding(5, 0, 5, 0);
            this.stts_lbl_LabelSep1.Size = new System.Drawing.Size(20, 19);
            this.stts_lbl_LabelSep1.Text = "|";
            // 
            // stts_lbl_ConversionProgress
            // 
            this.stts_lbl_ConversionProgress.BackColor = System.Drawing.SystemColors.ControlLight;
            this.stts_lbl_ConversionProgress.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.stts_lbl_ConversionProgress.Name = "stts_lbl_ConversionProgress";
            this.stts_lbl_ConversionProgress.Size = new System.Drawing.Size(40, 19);
            this.stts_lbl_ConversionProgress.Text = "<%>";
            // 
            // stts_lbl_LabelLastConversionTime
            // 
            this.stts_lbl_LabelLastConversionTime.BackColor = System.Drawing.SystemColors.ControlLight;
            this.stts_lbl_LabelLastConversionTime.Name = "stts_lbl_LabelLastConversionTime";
            this.stts_lbl_LabelLastConversionTime.Size = new System.Drawing.Size(104, 19);
            this.stts_lbl_LabelLastConversionTime.Text = "Última Conversão:";
            // 
            // stts_lbl_LastConversionTime
            // 
            this.stts_lbl_LastConversionTime.BackColor = System.Drawing.SystemColors.ControlLight;
            this.stts_lbl_LastConversionTime.Name = "stts_lbl_LastConversionTime";
            this.stts_lbl_LastConversionTime.Size = new System.Drawing.Size(93, 19);
            this.stts_lbl_LastConversionTime.Text = "<dd/mm/yyyy>";
            // 
            // btn_Convert
            // 
            this.btn_Convert.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btn_Convert.AutoSize = true;
            this.btn_Convert.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(250)))), ((int)(((byte)(250)))), ((int)(((byte)(250)))));
            this.btn_Convert.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_Convert.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_Convert.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(20)))), ((int)(((byte)(20)))), ((int)(((byte)(20)))));
            this.btn_Convert.Location = new System.Drawing.Point(403, 2);
            this.btn_Convert.Margin = new System.Windows.Forms.Padding(2);
            this.btn_Convert.Name = "btn_Convert";
            this.btn_Convert.Padding = new System.Windows.Forms.Padding(1);
            this.btn_Convert.Size = new System.Drawing.Size(92, 33);
            this.btn_Convert.TabIndex = 2;
            this.btn_Convert.Text = "Converter";
            this.btn_Convert.UseVisualStyleBackColor = false;
            this.btn_Convert.Click += new System.EventHandler(this.btn_Execute_Click);
            // 
            // panel1
            // 
            this.panel1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.panel1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(230)))), ((int)(((byte)(230)))), ((int)(((byte)(230)))));
            this.panel1.Controls.Add(this.btn_PararConversao);
            this.panel1.Controls.Add(this.lbl_UserName);
            this.panel1.Controls.Add(this.btn_Exit);
            this.panel1.Controls.Add(this.btn_Convert);
            this.panel1.Location = new System.Drawing.Point(9, 551);
            this.panel1.Margin = new System.Windows.Forms.Padding(2);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(570, 38);
            this.panel1.TabIndex = 1;
            // 
            // btn_PararConversao
            // 
            this.btn_PararConversao.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btn_PararConversao.AutoSize = true;
            this.btn_PararConversao.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(250)))), ((int)(((byte)(250)))), ((int)(((byte)(250)))));
            this.btn_PararConversao.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_PararConversao.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_PararConversao.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(20)))), ((int)(((byte)(20)))), ((int)(((byte)(20)))));
            this.btn_PararConversao.Location = new System.Drawing.Point(260, 2);
            this.btn_PararConversao.Margin = new System.Windows.Forms.Padding(2);
            this.btn_PararConversao.Name = "btn_PararConversao";
            this.btn_PararConversao.Padding = new System.Windows.Forms.Padding(1);
            this.btn_PararConversao.Size = new System.Drawing.Size(139, 33);
            this.btn_PararConversao.TabIndex = 5;
            this.btn_PararConversao.Text = "Parar Conversão";
            this.btn_PararConversao.UseVisualStyleBackColor = false;
            this.btn_PararConversao.Click += new System.EventHandler(this.btn_PararConversao_Click);
            // 
            // lbl_UserName
            // 
            this.lbl_UserName.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_UserName.Location = new System.Drawing.Point(2, 2);
            this.lbl_UserName.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lbl_UserName.Name = "lbl_UserName";
            this.lbl_UserName.Size = new System.Drawing.Size(250, 33);
            this.lbl_UserName.TabIndex = 4;
            this.lbl_UserName.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // btn_Exit
            // 
            this.btn_Exit.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btn_Exit.AutoSize = true;
            this.btn_Exit.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.btn_Exit.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btn_Exit.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btn_Exit.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_Exit.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.btn_Exit.Location = new System.Drawing.Point(499, 2);
            this.btn_Exit.Margin = new System.Windows.Forms.Padding(2);
            this.btn_Exit.Name = "btn_Exit";
            this.btn_Exit.Padding = new System.Windows.Forms.Padding(1);
            this.btn_Exit.Size = new System.Drawing.Size(71, 33);
            this.btn_Exit.TabIndex = 3;
            this.btn_Exit.Text = "Sair";
            this.btn_Exit.UseVisualStyleBackColor = false;
            this.btn_Exit.Click += new System.EventHandler(this.btn_Exit_Click);
            // 
            // pnl_ErrorListBackground
            // 
            this.pnl_ErrorListBackground.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pnl_ErrorListBackground.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(250)))), ((int)(((byte)(250)))), ((int)(((byte)(250)))));
            this.pnl_ErrorListBackground.Controls.Add(this.pnl_ErrorListDataBackground);
            this.pnl_ErrorListBackground.Controls.Add(this.tableLayoutPanel2);
            this.pnl_ErrorListBackground.Location = new System.Drawing.Point(9, 391);
            this.pnl_ErrorListBackground.Margin = new System.Windows.Forms.Padding(2);
            this.pnl_ErrorListBackground.Name = "pnl_ErrorListBackground";
            this.pnl_ErrorListBackground.Size = new System.Drawing.Size(570, 155);
            this.pnl_ErrorListBackground.TabIndex = 10;
            // 
            // pnl_ErrorListDataBackground
            // 
            this.pnl_ErrorListDataBackground.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pnl_ErrorListDataBackground.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.pnl_ErrorListDataBackground.Controls.Add(this.tbl_ErrorList);
            this.pnl_ErrorListDataBackground.Location = new System.Drawing.Point(4, 75);
            this.pnl_ErrorListDataBackground.Margin = new System.Windows.Forms.Padding(2);
            this.pnl_ErrorListDataBackground.Name = "pnl_ErrorListDataBackground";
            this.pnl_ErrorListDataBackground.Size = new System.Drawing.Size(564, 78);
            this.pnl_ErrorListDataBackground.TabIndex = 12;
            // 
            // tbl_ErrorList
            // 
            this.tbl_ErrorList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tbl_ErrorList.AutoScroll = true;
            this.tbl_ErrorList.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.tbl_ErrorList.ColumnCount = 3;
            this.tbl_ErrorList.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 10F));
            this.tbl_ErrorList.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 45F));
            this.tbl_ErrorList.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 45F));
            this.tbl_ErrorList.Location = new System.Drawing.Point(4, 9);
            this.tbl_ErrorList.Margin = new System.Windows.Forms.Padding(2);
            this.tbl_ErrorList.Name = "tbl_ErrorList";
            this.tbl_ErrorList.RowCount = 1;
            this.tbl_ErrorList.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 58F));
            this.tbl_ErrorList.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 58F));
            this.tbl_ErrorList.Size = new System.Drawing.Size(568, 58);
            this.tbl_ErrorList.TabIndex = 11;
            // 
            // tableLayoutPanel2
            // 
            this.tableLayoutPanel2.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tableLayoutPanel2.ColumnCount = 3;
            this.tableLayoutPanel2.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 10F));
            this.tableLayoutPanel2.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 45F));
            this.tableLayoutPanel2.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 45F));
            this.tableLayoutPanel2.Controls.Add(this.lbl_ErrorListTitle, 0, 0);
            this.tableLayoutPanel2.Controls.Add(this.tbl_item_lblNumber, 0, 1);
            this.tableLayoutPanel2.Controls.Add(this.tbl_item_lblDescription, 1, 1);
            this.tableLayoutPanel2.Controls.Add(this.tbl_item_lblException, 2, 1);
            this.tableLayoutPanel2.Location = new System.Drawing.Point(0, 2);
            this.tableLayoutPanel2.Margin = new System.Windows.Forms.Padding(2);
            this.tableLayoutPanel2.Name = "tableLayoutPanel2";
            this.tableLayoutPanel2.RowCount = 2;
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 16F));
            this.tableLayoutPanel2.Size = new System.Drawing.Size(570, 67);
            this.tableLayoutPanel2.TabIndex = 11;
            // 
            // lbl_ErrorListTitle
            // 
            this.lbl_ErrorListTitle.AutoSize = true;
            this.lbl_ErrorListTitle.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.tableLayoutPanel2.SetColumnSpan(this.lbl_ErrorListTitle, 3);
            this.lbl_ErrorListTitle.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lbl_ErrorListTitle.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_ErrorListTitle.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.lbl_ErrorListTitle.Location = new System.Drawing.Point(2, 0);
            this.lbl_ErrorListTitle.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lbl_ErrorListTitle.Name = "lbl_ErrorListTitle";
            this.lbl_ErrorListTitle.Size = new System.Drawing.Size(566, 33);
            this.lbl_ErrorListTitle.TabIndex = 0;
            this.lbl_ErrorListTitle.Text = "LISTA DE ERROS";
            this.lbl_ErrorListTitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // tbl_item_lblNumber
            // 
            this.tbl_item_lblNumber.AutoSize = true;
            this.tbl_item_lblNumber.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(250)))), ((int)(((byte)(200)))), ((int)(((byte)(200)))));
            this.tbl_item_lblNumber.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tbl_item_lblNumber.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbl_item_lblNumber.Location = new System.Drawing.Point(2, 33);
            this.tbl_item_lblNumber.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.tbl_item_lblNumber.Name = "tbl_item_lblNumber";
            this.tbl_item_lblNumber.Size = new System.Drawing.Size(53, 34);
            this.tbl_item_lblNumber.TabIndex = 1;
            this.tbl_item_lblNumber.Text = "Hora";
            this.tbl_item_lblNumber.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // tbl_item_lblDescription
            // 
            this.tbl_item_lblDescription.AutoSize = true;
            this.tbl_item_lblDescription.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(250)))), ((int)(((byte)(200)))), ((int)(((byte)(200)))));
            this.tbl_item_lblDescription.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tbl_item_lblDescription.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbl_item_lblDescription.Location = new System.Drawing.Point(59, 33);
            this.tbl_item_lblDescription.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.tbl_item_lblDescription.Name = "tbl_item_lblDescription";
            this.tbl_item_lblDescription.Size = new System.Drawing.Size(252, 34);
            this.tbl_item_lblDescription.TabIndex = 2;
            this.tbl_item_lblDescription.Text = "Descrição";
            this.tbl_item_lblDescription.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // tbl_item_lblException
            // 
            this.tbl_item_lblException.AutoSize = true;
            this.tbl_item_lblException.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(250)))), ((int)(((byte)(200)))), ((int)(((byte)(200)))));
            this.tbl_item_lblException.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tbl_item_lblException.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbl_item_lblException.Location = new System.Drawing.Point(315, 33);
            this.tbl_item_lblException.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.tbl_item_lblException.Name = "tbl_item_lblException";
            this.tbl_item_lblException.Size = new System.Drawing.Size(253, 34);
            this.tbl_item_lblException.TabIndex = 3;
            this.tbl_item_lblException.Text = "Exceção";
            this.tbl_item_lblException.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(250)))), ((int)(((byte)(250)))), ((int)(((byte)(250)))));
            this.CancelButton = this.btn_Exit;
            this.ClientSize = new System.Drawing.Size(588, 612);
            this.Controls.Add(this.pnl_ErrorListBackground);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.stts_StripMenuStatus);
            this.Controls.Add(this.mnu_TopMenu);
            this.Controls.Add(this.tableLayoutPanel1);
            this.Controls.Add(this.tbl_ImportPDF);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.mnu_TopMenu;
            this.Margin = new System.Windows.Forms.Padding(2);
            this.MinimumSize = new System.Drawing.Size(604, 651);
            this.Name = "frmMain";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "PDFConverter";
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.img_PDF)).EndInit();
            this.mnu_TopMenu.ResumeLayout(false);
            this.mnu_TopMenu.PerformLayout();
            this.tbl_ImportPDF.ResumeLayout(false);
            this.tbl_ImportPDF.PerformLayout();
            this.stts_StripMenuStatus.ResumeLayout(false);
            this.stts_StripMenuStatus.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.pnl_ErrorListBackground.ResumeLayout(false);
            this.pnl_ErrorListDataBackground.ResumeLayout(false);
            this.tableLayoutPanel2.ResumeLayout(false);
            this.tableLayoutPanel2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        public System.Windows.Forms.Label lbl_TitlePDFConverter;
        public System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        public System.Windows.Forms.PictureBox img_PDF;
        public System.Windows.Forms.Label lbl_SubtitlePDFConverter;
        public System.Windows.Forms.FolderBrowserDialog folderbd_PDFFolder;
        public System.Windows.Forms.MenuStrip mnu_TopMenu;
        public System.Windows.Forms.ToolStripMenuItem mnu_item_Convertion;
        public System.Windows.Forms.ToolStripMenuItem mnu_item_About;
        public System.Windows.Forms.ToolStripMenuItem mnu_item_Exit;
        public System.Windows.Forms.Label lbl_PathPDF;
        public System.Windows.Forms.TableLayoutPanel tbl_ImportPDF;
        public System.Windows.Forms.TextBox txt_PathImport;
        public System.Windows.Forms.ToolStripStatusLabel stts_lbl_LabelProgress;
        public System.Windows.Forms.ToolStripProgressBar stts_prg_ConversionStatus;
        public System.Windows.Forms.ToolStripStatusLabel stts_lbl_LabelSep2;
        public System.Windows.Forms.ToolStripStatusLabel stts_lbl_ConversionStatus;
        public System.Windows.Forms.StatusStrip stts_StripMenuStatus;
        public System.Windows.Forms.Label lbl_PathImport;
        public System.Windows.Forms.Button btn_Convert;
        public System.Windows.Forms.TextBox txt_PathExport;
        public System.Windows.Forms.Label lbl_PathExport;
        public System.Windows.Forms.ToolStripMenuItem mnu_item_Convert;
        public System.Windows.Forms.ToolStripMenuItem mnu_item_ChoosePath;
        public System.Windows.Forms.ToolStripMenuItem mnu_item_ChoosePathImport;
        public System.Windows.Forms.ToolStripMenuItem mnu_item_ChoosePathExport;
        public System.Windows.Forms.Button btn_OpenPathImport;
        public System.Windows.Forms.Button btn_ChoosePathImport;
        public System.Windows.Forms.Panel panel1;
        public System.Windows.Forms.Button btn_Exit;
        public System.Windows.Forms.ToolStripStatusLabel stts_lbl_LabelStatus;
        public System.Windows.Forms.CheckBox chk_useExportPath;
        public System.Windows.Forms.Button btn_OpenPathExport;
        public System.Windows.Forms.Button btn_ChoosePathExport;
        public System.Windows.Forms.Panel pnl_ErrorListBackground;
        public System.Windows.Forms.TableLayoutPanel tableLayoutPanel2;
        public System.Windows.Forms.Label lbl_ErrorListTitle;
        public System.Windows.Forms.Label tbl_item_lblNumber;
        public System.Windows.Forms.Label tbl_item_lblDescription;
        public System.Windows.Forms.Label tbl_item_lblException;
		public System.Windows.Forms.Panel pnl_ErrorListDataBackground;
		public System.Windows.Forms.TableLayoutPanel tbl_ErrorList;
		public System.Windows.Forms.ToolStripStatusLabel stts_lbl_LastConversionTime;
		public System.Windows.Forms.ToolStripStatusLabel stts_lbl_LabelSep1;
		public System.Windows.Forms.ToolStripStatusLabel stts_lbl_LabelLastConversionTime;
		public System.Windows.Forms.ToolStripMenuItem mnu_item_Open;
		public System.Windows.Forms.ToolStripMenuItem mnu_item_OpenPathImport;
		public System.Windows.Forms.ToolStripMenuItem mnu_item_OpenPathExport;
		public System.Windows.Forms.ToolStripMenuItem mnu_item_OpenTerminalFile;
		public System.Windows.Forms.ToolStripSeparator mnu_item_ItemSeparator2;
		public System.Windows.Forms.ToolStripSeparator mnu_item_ItemSeparator1;
		private System.Windows.Forms.Label lbl_UserName;
		public System.Windows.Forms.ToolStripStatusLabel stts_lbl_ConversionProgress;
        public System.Windows.Forms.Button btn_PararConversao;
    }
}

