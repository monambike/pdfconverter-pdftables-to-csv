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

    parser_Main = None
    """Variável que vai ser responsável por criar o parser."""
    parser_ArgsMain = None
    """
    Variável que vai ser responsável por fazer  a  manipulação  dos
    argumentos dados.
    """

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

    filename_PDF = ""
    """
    Nome do arquivo PDF que vai ser convertido  (sem a extensão).
    """
    folderpath_Script = ""
    """
    Caminho atual para a raiz do projeto (os outros caminhos vão se
    basear nele).
    """
    path_Import = ""
    """
    Caminho da pasta de importação onde os  arquivos  PDF  vão  ser
    alocados.
    """
    path_Export = ""
    """
    Caminho da pasta onde os arquivos exportação vão ser alocados.
    """
    filepath_TerminalFile = ""
    """Caminho para o arquivo do terminal."""
    filepath_ExportTxt = ""
    """
    Caminho do arquivo de texto que vai ser gerado pelo PDF que vai
    ser convertido.
    """
    file_TerminalFile = ""
    """Variável que armazena o arquivo de saída do Terminal."""
    readPDFPages = "all"
    """Páginas que vão ser lidas para realizar a conversão."""

    
    rootPath = "\\resultados"
    """
    Caminhos que indicam a localização das pastas raíz que irão ser
    geradas futuramente.
    """
    list_readingPaths = [
        "\\lattice",
        "\\stream"
    ]
    """
    Caminhos que indicam a localização das pastas  dos  métodos  de
    leitura que vão ser geradas  futuramente  dentro  da  pasta  de
    exportação.
    """
    list_formattingPaths = [
        "\\main",
        "\\fullClear",
        "\\tableWithBlankCells",
        "\\withoutFormatting"
    ]
    """
    Caminhos que indicam a localização das pastas  dos  métodos  de
    formatação que vão ser geradas futuramente  dentro  das  pastas
    de métodos de leitura, que estão dentro da pasta de exportação.
    """

    tableWithBlankCells_OutputTxt = ""
    main_OutputTxt = ""
    fullclear_OutputTxt = ""

class ivar:
    """
    ---
    ---
    ---
    
    ## Index Variables (ivar)
    ---
    ---
    Variáveis relacionadas à indexação que realizam  iterações  nos
    loops.
    
    ---
    ---
    ---
    """

    DataFrame = 0
    """Índice do 'For' que manipula o Data Frame."""
    PdfFile = 0
    """Índice do 'For' que manipula os arquivos PDF."""

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
    
    list_columnFieldsToChange = []
    """
    Variável que vai segurar e possuir todos os argumentos
    que o usuário quer que altere nas colunas.
    """

    lote = [
        '--Lote',
        'lote'
    ]
    """Lote."""
    ordem = [
        '--Ordem',
        'ordem',
        'item',
        'nº item'
    ]
    """Ordem (Sequencial)."""
    codigo = [
        '--Codigo',
        'codigo',
        'código',
        'cód',
        'cod. produto',
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
        'especificações técnicas'
    ]
    """Descrição."""
    unidade = [
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
    quantidade = [
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
    valormedio = [
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

    StoredColumns = []
    """Todos as recomendações de colunas agrupadas."""
    StoredColumns.extend((
        lote,
        ordem,
        codigo,
        descricao,
        unidade,
        quantidade,
        valormedio
    )) 

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