import importlib
import os
from glob import glob

from pdfconverter.__variables__ import Var
from pdfconverter import output_info
from pdfconverter.output_info import errors


# region Public Methods


def single_file_conversion() -> None:
    # Como a modalidade de conversão será individual, informa que apenas um PDF será convertido
    Var.ConversionInfo.quantity_files_import = 1

    # Inicia a conversão
    __conversion_start(Var.Arguments.path_import)


def multiple_file_conversion() -> None:
    reference_path_all_pdf_files = (Var.ConversionInfo.folder_path_import + "\\*.pdf")

    Var.ConversionInfo.quantity_files_import = len(glob(reference_path_all_pdf_files))

    for PDF in glob(reference_path_all_pdf_files):
        __conversion_start(PDF)
    else:
        if Var.CurrentConvertedFileInfo.index_pdf <= 0:
            errors.add_error(
                error_description = (
                    "Não há arquivos PDF para serem convertidos."
                ),
                stop_application = True
            )


# endregion

# region Private Methods


def __conversion_start(file_path_pdf: str) -> None:
    Var.CurrentConvertedFileInfo.file_path_pdf = file_path_pdf

    Var.CurrentConvertedFileInfo.file_full_name_pdf = os.path.basename(file_path_pdf)

    Var.CurrentConvertedFileInfo.file_name_pdf = Var.CurrentConvertedFileInfo.file_full_name_pdf[:-4]

    output_info.make_file(directory_path = Var.Main.FOLDER_PATH_PROJECT)

    for Var.CurrentConvertedFileInfo.current_file_reading_library in Var.ConversionInCodeSettings.READING_LIBRARIES:
        # Procura pelos métodos de leitura selecionados de acordo com as bibliotecas selecionadas
        for Var.CurrentConvertedFileInfo.current_file_reading_type in getattr(
            Var.ConversionInCodeSettings,
            (
                str(Var.CurrentConvertedFileInfo.current_file_reading_library).upper()
                + "_READING_TYPES"
            )
        ):
            # Procura pelos tipos de arquivos de saída selecionados de acordo com o método de leitura selecionado
            for Var.CurrentConvertedFileInfo.current_file_export_type in getattr(
                Var.ConversionInCodeSettings,
                (
                    str(Var.CurrentConvertedFileInfo.current_file_reading_library).upper()
                    + "_OUTPUT_TYPES"
                )
            ):
                if Var.CurrentConvertedFileInfo.current_file_export_type == "withoutformatting":
                    # O módulo atual, na verdade, será procurado no retorno dado pela busca da biblioteca vigente, ou
                    # seja, o módulo realmente não tem como ser instanciado ou achado no momento, por isso o erro foi
                    # silenciado.
                    # noinspection PyUnresolvedReferences
                    importlib.import_module(
                        name = (
                            "pdfconverter.conversion.{Library}"
                            .format(Library = Var.CurrentConvertedFileInfo.current_file_reading_library)
                        )
                    ).make_file(
                        Var.CurrentConvertedFileInfo.file_path_pdf,
                        Var.CurrentConvertedFileInfo.current_file_reading_type
                    )

                print("FormattingType: " + Var.CurrentConvertedFileInfo.current_file_export_type)


    output_info.make_file(directory_path = Var.Main.FOLDER_PATH_PROJECT)
# endregion
