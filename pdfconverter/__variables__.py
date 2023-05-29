import os
import pathlib

from pandas.core.frame import DataFrame


# region Classes

class Var:

    # region Constructors

    def __init__(self) -> None:
        pass

    # endregion

    # region Fields

    class Main:
        FOLDER_PATH_PROJECT: str = str(pathlib.Path(__file__).parent.absolute())
        """Usa o Script atual para pegar o caminho da pasta do projeto."""

        FOLDER_NAME_EXPORT: str = "resultados"

        FOLDER_PATH_INFO_FILES: str = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    class Arguments:
        # region Parser
        
        parser_editable_main = None
        """
        Variável que vai ser responsável por  armazenar  o  objeto  que
        representará o parser.
        É possível configurar completamente um setup de argumentos  com
        ele.
        """
        parser_main = None
        """
        Variável que representa o objeto do parser com  os  valores  já
        interpretados, sejam eles recebidos  diretamente  da  linha  de
        comando (pegos pelo  de  "sys.argv"  no  terminal)  ou  passado
        através do método em "parse_args()".
        """

        # endregion

        # region Args

        # region Main

        path_import: str = ""
        """
        Caminho de importação fornecido como argumento pelo usuário.\n
        (str)
        """
        path_export: str = ""
        """
        Caminho de importação fornecido como argumento pelo usuário.
        (str, optional, default = [Same from ImportPath])
        """
        page_numbers: str = ""
        """
        Número  de  página  (ou  intervalo  de  páginas)  que  irá  ser
        utilizado como base para realizar a conversão.\n
        (str, optional, default = "all")
        """

        # endregion

        # region Column Mapping

        mapping_lote: str = ""
        """
        Variável que armazena o valor para encontrar o lote no  arquivo
        CSV quando feito o mapeamento.
        """
        mapping_ordem: str = ""
        """
        Variável que armazena o valor para encontrar a ordem no arquivo
        CSV quando feito o mapeamento.
        """
        mapping_codigo: str = ""
        """
        Variável que armazena  o  valor  para  encontrar  o  código  no
        arquivo CSV quando feito o mapeamento.
        """
        mapping_produto: str = ""
        """
        Variável que armazena o  valor  para  encontrar  o  produto  no
        arquivo CSV quando feito o mapeamento.
        """
        mapping_unidade: str = ""
        """
        Variável que armazena o  valor  para  encontrar  a  unidade  no
        arquivo CSV quando feito o mapeamento.    
        """
        mapping_quantidade: str = ""
        """
        Variável que armazena o valor para encontrar  a  quantidade  no
        arquivo CSV quando feito o mapeamento.
        """
        mapping_valor_medio: str = ""
        """
        Variável que armazena o valor para encontrar o valor  médio  no
        arquivo CSV quando feito o mapeamento.
        """

        # endregion

        # region Settings

        folder_path_output_info: str = ""
        """
        Configuração utilizada  para  definir  o  caminho  na  onde  os
        arquivos de saída com informações relevantes serão gerados.
        """
        make_mapping_columns_file: bool = False
        """
        Configuração que caso habilitada faz com que seja  realizado  o
        mapeamento de  colunas  e  gerado  o  arquivo  com  as  colunas
        mapeadas.
        """
        make_conversion_details_file: bool = False
        """
        Configuração que caso habilitada, faz com  que  seja  gerada  o
        arquivo contendo detalhes da conversão.
        """
        make_output_info_file: bool = False
        """
        Configuração que caso habilitada, faz cm que o arquivo contendo
        algumas informações à respeito da conversão  seja  gerado,  bem
        como número de arquivos que foram pegos  para  a  conversão,  e
        número de arquivos que serão exportados.
        """

        # endregion

        # endregion

    class CurrentConvertedFileInfo:
        index_pdf: int = 0

        file_name_pdf: str = ""
        file_full_name_pdf: str = ""
        file_path_pdf: str = ""
        
        current_file_reading_library: str = ""
        current_file_reading_type: str = ""
        current_file_export_type: str = ""

        list_dataframe: list[DataFrame] = None

    class ConversionInfo:

        conversion_type: classmethod = None

        folder_path_import: str = ""
        folder_path_export: str = ""

        page_numbers_to_read: str = ""
        
        folder_name_export: str = ""

        quantity_files_import: int = 0
        
        quantity_files_export: int = 0

    class ColumnMapping:
        MAPPING_LOTE: list[str] = [
            '--Lote',
            'lote'
        ]
        """Lote."""
        MAPPING_ORDEM: list[str] = [
            '--Ordem',
            'ordem',
            'item',
            'nº item'
        ]
        """Ordem (Sequencial)."""
        MAPPING_CODIGO: list[str] = [
            '--Codigo',
            'codigo',
            'código',
            'cód',
            'cod. produto'
        ]
        """Código."""
        MAPPING_DESCRICAO: list[str] = [
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
        MAPPING_UNIDADE: list[str] = [
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
        MAPPING_QUANTIDADE: list[str] = [
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
        MAPPING_VALORMEDIO: list[str] = [
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

    class ConversionInCodeSettings:
        #  Suportadas: tabula, camelot
        READING_LIBRARIES: tuple = (
            "tabula",
            "camelot"
        )

        # Suportadas: lattice, stream
        TABULA_READING_TYPES: tuple = (
            "lattice",
            "stream"
        )

        # Suportadas: "withoutformatting", "tablewithblankcells", "main", "fullclear"
        TABULA_OUTPUT_TYPES: tuple = (
            "withoutformatting",
            "tablewithblankcells",
            "main",
            "fullclear"
        )

        # Suportadas: withoutformatting, main
        CAMELOT_OUTPUT_TYPES: tuple = (
            "withoutformatting",
            "main"
        )
        # Suportadas: lattice
        CAMELOT_READING_TYPES: tuple = ("lattice",)

    class OutputInfo:
        dictionary_prior_info: dict = {}

        dictionary_conversion_info: dict = {}

        index_error: int = 0
        dictionary_errors: dict = {}

    # endregion

# endregion
