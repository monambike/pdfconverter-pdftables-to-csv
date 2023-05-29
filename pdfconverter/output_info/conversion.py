from os import path

from pdfconverter import util
from pdfconverter.__variables__ import Var
from pdfconverter.exceptions import PathIsNotDirectory
from pdfconverter.output_info import errors


# region Public Methods


def update_and_make_file() -> None:
    update()
    make_file()


def make_file(directory_path: str = Var.Main.FOLDER_PATH_INFO_FILES) -> None:
    if not path.isdir(directory_path):
        raise PathIsNotDirectory(invalid_directory_path = directory_path)
    try:
        with open(
            file = (
                Var.Main.FOLDER_PATH_INFO_FILES
                + "\\" + "output_info_conversion.json"
            ),
            mode = "w",
            encoding = "UTF-8"
        ) as text_file:
            text_file.write(
                util.convert_dictionary_to_json(
                    Var.OutputInfo.dictionary_conversion_info
                )
            )
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


def update() -> None:
    try:
        Var.OutputInfo.dictionary_conversion_info = {
            "ResultsFolder": {
                "Name": Var.ConversionInfo.folder_name_export,
                "Path": Var.ConversionInfo.folder_path_export
            },
            "QuantityOfFilesTo": {
                "Import": Var.ConversionInfo.quantity_files_import,
                "Export": Var.ConversionInfo.quantity_files_export
            }
        }
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


# endregion
