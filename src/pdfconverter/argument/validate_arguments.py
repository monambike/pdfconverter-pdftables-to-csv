import os.path

from pdfconverter import conversion
from pdfconverter import util
from pdfconverter.__variables__ import Var
from pdfconverter.conversion.string_format import StringFormat
from pdfconverter.output_info import errors


# region Classes

class ValidateArguments:
    """Classe que realiza algumas validações de argumentos."""

    # region Constructors

    def __init__(self) -> None:
        pass

    # endregion

    # region Public Methods

    def validate_all(self) -> None:
        self.import_path()
        self.export_path()
        self.page_number()
        self.make_mapping_columns_file()
        self.make_conversion_details_file()
        self.make_info_file()

    # region Main

    @staticmethod
    def import_path() -> None:
        try:
            conversion_start: str = ""

            if Var.Arguments.parser_main.ImportPath is None:
                errors.add_error(
                    error_description = (
                        "É necessário colocar um valor para o caminho de importação, '"
                        "--ImportPath <caminho_de_exportação>'."
                    ),
                    stop_application = True
                )
            elif os.path.exists(Var.Arguments.parser_main.ImportPath):
                if os.path.isfile(Var.Arguments.parser_main.ImportPath):
                    if util.file_has_pdf_extension(Var.Arguments.parser_main.ImportPath):
                        Var.Arguments.path_import = Var.Arguments.parser_main.ImportPath

                        Var.ConversionInfo.folder_path_import = os.path.dirname(Var.Arguments.parser_main.ImportPath)

                        conversion_start = "single"
                    else:
                        errors.add_error(
                            error_description = "O arquivo informado precisa ter a extensão '.pdf'.",
                            stop_application = True
                        )
                elif os.path.isdir(Var.Arguments.parser_main.ImportPath):
                    Var.Arguments.path_import =\
                        Var.ConversionInfo.folder_path_import =\
                        Var.Arguments.parser_main.ImportPath

                    conversion_start = "multiple"
                else:
                    errors.add_error(
                        error_description = (
                            "O arquivo informado no argumento de importação, precisa ser u"
                            "ma pasta ou um arquivo PDF."
                        ),
                        stop_application = True
                    )
            else:
                errors.add_error_invalid_argument(
                    argument_name = "ImportPath",
                    argument_value = Var.Arguments.parser_main.ImportPath
                )

            Var.ConversionInfo.conversion_type = getattr(
                conversion,
                conversion_start[0:] + "_file_conversion"
            )
        except Exception as exception:
            errors.add_error_method_unknown_exception(error_exception = exception)

    @staticmethod
    def export_path() -> None:
        try:
            export_path: str = ""

            if Var.Arguments.parser_main.ExportPath is None:
                export_path = Var.ConversionInfo.folder_path_export

                errors.add_error(
                    error_description = (
                        "Não foi informado um caminho de exportação. Utilizando '{ExportPathValue}'."
                        .format(ExportPathValue = Var.Arguments.path_import)
                    ),
                    stop_application = False
                )
            elif os.path.isdir(Var.Arguments.parser_main.ExportPath):
                export_path = Var.Arguments.parser_main.ExportPath
            else:
                errors.add_error(
                    error_description = (
                        "A pasta de exportação '{ExportPathValue}' informada não exist"
                        "e."
                        .format(ExportPathValue = Var.Arguments.path_export)
                    ),
                    stop_application = True
                )

            Var.Arguments.path_export =\
                Var.ConversionInfo.folder_path_export =\
                export_path
        except Exception as exception:
            errors.add_error_method_unknown_exception(error_exception = exception)

    @staticmethod
    def page_number() -> None:
        try:
            if Var.Arguments.parser_main.PageNumber is None:
                Var.ConversionInfo.page_numbers_to_read = "all"

                errors.add_error(
                    error_description = (
                        "Não foi informado um número de página. Utilizando '{ReadPagesValue}'."
                        .format(ReadPagesValue = Var.ConversionInfo.page_numbers_to_read)
                    ),
                    stop_application = False
                )
            elif StringFormat(Var.Arguments.parser_main.PageNumber).is_page_number():
                Var.ConversionInfo.page_numbers_to_read = Var.Arguments.parser_main.PageNumber
            else:
                errors.add_error(
                    error_description = (
                        "O valor '{PageNumberValue}' não é um valor válido para --Page"
                        "Number."
                        .format(PageNumberValue = Var.Arguments.parser_main.PageNumber)
                    ),
                    stop_application = True
                )
        except Exception as exception:
            errors.add_error_method_unknown_exception(error_exception = exception)

    # endregion

    # region Bool Settings

    def make_mapping_columns_file(self) -> None:
        self.__validate_bool_config(config_name = "MakeMappingColumnsFile")

    def make_conversion_details_file(self) -> None:
        self.__validate_bool_config(config_name = "MakeConversionDetailsFile")

    def make_info_file(self) -> None:
        self.__validate_bool_config(config_name = "MakeInfoFile")

    # endregion

    # endregion

    # region Private Methods

    @staticmethod
    def __validate_bool_config(config_name: str) -> None:
        try:
            parser_main_argument: str = getattr(
                Var.Arguments.parser_main,
                config_name
            )

            if parser_main_argument is None or parser_main_argument == "False":
                argument_value = False
            elif parser_main_argument == "True":
                argument_value = True
            else:
                errors.add_error_invalid_argument(
                    "--" + config_name,
                    parser_main_argument,
                )
                return

            setattr(
                Var.Arguments.parser_main,
                config_name,
                argument_value
            )
        except Exception as exception:
            errors.add_error_method_unknown_exception(error_exception = exception)

    # endregion

# endregion
