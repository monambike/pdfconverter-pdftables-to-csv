from os import path

from pdfconverter import util
from pdfconverter.__variables__ import Var
from pdfconverter.exceptions import PathIsNotDirectory
from pdfconverter.output_info import conversion
from pdfconverter.output_info import errors


# region Public Methods


def make_file(directory_path: str = Var.Main.FOLDER_PATH_INFO_FILES):
    if not path.isdir(directory_path):
        raise PathIsNotDirectory(invalid_directory_path = directory_path)
    try:
        with open(
            file = (
                directory_path
                + "\\output_info.json"
            ),
            mode = "w",
            encoding = "UTF-8"
        ) as text_file:
            text_file.write(
                util.convert_dictionary_to_json(
                    {
                        "Conversão": Var.OutputInfo.dictionary_conversion_info,
                        "Errors": Var.OutputInfo.dictionary_errors
                    }
                )
            )
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


# endregion
