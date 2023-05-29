"""
---
---
---

## Package: pdfconverter
---
---
### Module Name: __variables__
---
### path: "pdfconverter\\\\\\\\__variables__.py
---
---
Módulo  que  comporta  classes  com  variáveis  utilizadas   no
projeto.

---
---
---
"""


#region VARIABLES

#region MANAGEMENT

class mvar:
    """
    ---
    ---
    ---
    
    ## Management Variables (mvar)
    ---
    ---
    Classe  que   possui   variável   que   são   relacionadas   ao
    gerenciamento de ações do projeto.
    
    ---
    ---
    ---
    """

    ConversionStart = ""
    """
    Variável que segura a função que vai ser executada  no  arquivo
    principal em  __main__.  A  função  que  vai  ser  executada  é
    atribuida  no  momento  em  que  o  argumento  de  caminho   de
    importação é validado.
    
    Atualmente o  arquivo  de  importção  está  sendo  validado  na
    função   "__ValidateImportPath()"   presente   no   pacote   de
    argumentos "argument"
    """

#endregion

#region GENERAL

class avar:
    """
    ---
    ---
    ---
    
    ## Argument Variables (avar)
    ---
    ---
    Classe que possui  variáveis  relacionadas  à  alguma  ação  ou
    função relacionada à argumentos.
    
    ---
    ---
    ---
    """

    # [>] Todos os argumentos que são  relacionados  à  alterar  as
    # colunas padrão dentro de uma array.
    patternColumnArgs = [
        "Lote",
        "Ordem",
        "Codigo",
        "Produto",
        "Unidade",
        "Quantidade",
        "ValorMedio"
    ]

    #region PARSER
    parser_Main = None
    """Variável que vai ser responsável por criar o parser."""
    parser_ArgsMain = None
    """
    Variável que vai ser responsável por fazer  a  manipulação  dos
    argumentos dados.
    """
    #endregion

    #region USER ARGS
    # [!] path_Import
    path_ImportArg = ""
    """
    Caminho de importação com o valor fornecido pelo usuário.
    """
    path_ExportArg = ""
    """
    Caminho de exportação  com  o  valor  fornecido  pelo  usuário.
    Atualmente esse valor apenas pode ser uma referência de pasta
    """
    readPDFPagesArg = "all"
    """Páginas que vão ser lidas para realizar a conversão."""
    #endregion

    #region ARGS DEFAULT VALUES
    argName = ""
    """Nome do argumento."""
    defaultValue = None
    """Valor que vem por padrão no argumento."""
    nargsValue = '?'
    """
    Variável  que  define  o  número  de  valores  suportado   pelo
    argumento, além de poder definir um  número  que  representa  a
    quantidade em si, também é possível definir:
    - '+' == 1 ou mais;
    - '*' == 0 ou mais;
    - '?' == 0 or 1.
    """
    contentType = str
    """Tipo de valor do argumento."""
    #endregion

class cvar:
    """
    ---
    ---
    ---
    
    ## Conversion Variables (cvar)
    ---
    ---
    Variáveis relacionadas à conversão.
    
    ---
    ---
    ---
    """
    
    list_DataFrames = []
    """
    Variável que vai conter a lista de DataFrames de um determinado
    arquivo PDF baseado  em  um  método  de  leitura,  podendo  ser
    lattice ou stream.
    """

class fvar:
    """
    ---
    ---
    ---
    
    ## File Variables (fvar)
    ---
    ---
    Variáveis  relacionadas  à  arquivos  como  nome  de  arquivos,
    caminhos de importação e exportção, pasta do Script, número  de
    páginas de arquivos PDF e estrutura de pastas.
    
    ---
    ---
    ---
    """

    #region PROJECT

    #region GENERAL
    folderpath_Script = ""
    """
    Caminho do arquivo de script que está sendo executado.
    """
    #endregion

    #region TERMINAL FILE
    file_TerminalFile = ""
    """Variável que armazena o arquivo de saída do terminal em si."""
    filepath_TerminalFile = ""
    """Caminho para o arquivo do terminal."""
    #endregion

    #endregion

    #region CONVERSION RUNTIME

    #region GENERAL
    # [!] path_FolderImport
    folderpath_Import = ""
    """
    Caminho da pasta de importação onde os  arquivos  PDF  vão  ser
    alocados.
    """
    folderpath_Export = ""
    """
    Caminho da pasta de exportação onde os arquivos  de  saída  vão
    ser alocados.
    """
    folderpath_Result = ""
    #endregion

    #region PDF INFO
    filename_PDF = ""
    """
    Nome do arquivo PDF que vai ser convertido  (sem a extensão).
    """
    counter_PdfFile = 0
    """
    Contador do 'For' que manipula a conversão  dos  arquivos  PDF.
    Conta os arquivos PDFs convertidos.
    """
    #endregion

    #region CONVERSION FILE GENERATION INFO
    # [!] filepath_ExportTxt
    filepath_WithoutFormatting = ""
    """
    Caminho do arquivo de texto que vai ser gerado pelo PDF que vai
    ser convertido.
    """
    counter_DataFrame = 0
    """
    Contador do 'For' que manipula o DataFrame que vai ser  passado
    para o arquivo sem formatação.
    """
    #endregion

    #region FORMATTING TYPES FILE PATH
    # [!] tableWithBlankCells_OutputTxt
    filepath_TableWithBlankCells = ""
    """"""
    # [!] main_OutputTxt
    filepath_Main = ""
    """"""
    # [!] fullclear_OutputTxt
    filepath_FullClear = ""
    """"""
    #endregion

    #endregion

    #region FOLDER STRUCTURE
    # [i] rootPath
    foldername_Results = "resultados"
    """
    Caminhos que indicam a localização das pastas raíz que irão ser
    geradas futuramente.
    """
    # [i] list_readingPaths
    list_ReadingPaths = [
        "lattice",
        "stream"
    ]
    """
    Caminhos que indicam a localização das pastas  dos  métodos  de
    leitura que vão ser geradas  futuramente  dentro  da  pasta  de
    exportação.
    """
    # [!] list_formattingPaths
    list_FormattingPaths = [
        "main",
        "fullClear",
        "tableWithBlankCells",
        "withoutFormatting"
    ]
    """
    Caminhos que indicam a localização das pastas  dos  métodos  de
    formatação que vão ser geradas futuramente  dentro  das  pastas
    de métodos de leitura, que estão dentro da pasta de exportação.
    """
    #endregion

class pvar:
    """
    ---
    ---
    ---
    
    ## Pattern Variables (pvar)
    ---
    ---
    Variáveis relacionadas à padronização de colunas.
    
    ---
    ---
    ---
    """
    
    # [!] list_columnFieldsToChange
    list_UserGivenColumnToChange = []
    """
    Variável que vai segurar e possuir todos os argumentos
    que o usuário quer que altere nas colunas.
    """

    #region COLUMN MAPPING

    #region SORTED BY COLUMN
    lote =\
        [
        '--Lote',
        'lote'
        ]
    """Lote."""
    ordem =\
        [
        '--Ordem',
        'ordem',
        'item',
        'nº item'
        ]
    """Ordem (Sequencial)."""
    codigo =\
        [
        '--Codigo',
        'codigo',
        'código',
        'cód',
        'cod. produto'
        ]
    """Código."""
    descricao = [
        '--Produto',
        'produto',
        'descricao',
        'descriçao',
        'descricão',
        'descrição',
        'descrição do item',
        'descrição do produto',
        'descrição do material',
        'descrição dos materiais',
        'descrição dos medicamentos',
        'descrição do material/serviço',
        'especificações dos medicamentos',
        'objeto',
        'medicamento',
        'objeto/medicamento',
        'produto - especificação',
        'especificações técnicas']
    """Descrição."""
    unidade =\
        [
        '--Unidade',
        'unidade',
        'un',
        'und',
        'unid',
        'unid.',
        'emb',
        'u/m',
        'apresentação',
        'especificação'
        ]
    """Unidade."""
    quantidade =\
        [
        '--Quantidade',
        'quantidade',
        'qtd',
        'qte',
        'qtd.',
        'qde.',
        'qtde',
        'qntd',
        'qntd.',
        'quant.'
        ]
    """Quantidade."""
    valormedio =\
        [
        '--ValorMedio',
        'valormedio',
        'prev. custo unit. (r$)',
        'valor unit',
        'v. unit',
        'val. unitário',
        'valor unitário',
        'valor médio',
        'valor médio unitário r$',
        'estimado unitário'
        ]
    """Valor Médio."""
    #endregion

    #region ALL
    StoredColumns = []
    """Todas as recomendações de colunas agrupadas."""
    StoredColumns.extend((
        lote,
        ordem,
        codigo,
        descricao,
        unidade,
        quantidade,
        valormedio
    ))
    #endregion

    #endregion

class vvar:
    """
    ---
    ---
    ---
    
    ## Visual Variables (vvar)
    ---
    ---
    Variáveis relacionadas ao visual da aplicação.
    
    ---
    ---
    ---
    """

    GiantLine = (
        "_________________________________________"
        "_________________________________________"
        "_________________________________________"
        "_________________________________________"
        "_________________________________________"
        "_________________________________________"
        "_________________________________________"
        "_________________________________________"
        "_________________________________________"
        "_________________________________"
    )
    """
    Linha gigante que vai ficar disposta  em  alguns  lugares  como
    divisão no terminal.

    Existem 402 linhas.
    """
    BlankSpaces = (
        "                                         "
        "                                         "
        "                                         "
        "                                         "
        "    "
    )
    """
    Variável que contém um espaço gigante usado em alguns layouts.
    
    Existem 168 espaços.
    """

#endregion

#endregion