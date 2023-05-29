import inspect
from os import path

from pdfconverter import program
from pdfconverter import util
from pdfconverter.__variables__ import Var
from pdfconverter.exceptions import PathIsNotDirectory


# region Public Methods


def make_file(directory_path: str = Var.Main.FOLDER_PATH_INFO_FILES) -> None:
    if not path.isdir(directory_path):
        raise PathIsNotDirectory(invalid_directory_path = directory_path)
    with open(
        file = (
            Var.Main.FOLDER_PATH_INFO_FILES
            + "\\" + "output_info_errors.json"
        ),
        mode = "w",
        encoding = "UTF-8"
    ) as text_file:
        text_file.write(
            util.convert_dictionary_to_json(Var.OutputInfo.dictionary_errors)
        )


def add_error(
    error_description: str,
    stop_application: bool,
    error_exception: Exception = None
) -> None:
    Var.OutputInfo.dictionary_errors.update(
        {
            Var.OutputInfo.index_error: {
                "Description": error_description,
                "Exception": str(error_exception),
                "Time": str(util.get_current_date_and_time())
            }
        }
    )
    Var.OutputInfo.index_error += 1

    if stop_application:
        program.finish()


def add_error_method_unknown_exception(
    error_exception: Exception
) -> None:
    add_error(
        error_description = (
            "Ocorreu um erro desconhecido no método '{FunctionName}' em '{FunctionPath}'."
            .format(
                FunctionName = inspect.getouterframes(inspect.currentframe())[1].function,
                FunctionPath = inspect.getouterframes(inspect.currentframe())[1].filename
            )
        ),
        error_exception = error_exception,
        stop_application = True
    )


def add_error_invalid_argument(
    argument_name: str,
    argument_value: str
) -> None:
    add_error(
        error_description = (
            "O valor {ArgumentValue} não é um valor válido para {ArgumentName}."
            .format(
                ArgumentValue = argument_value,
                ArgumentName = argument_name
            )
        ),
        stop_application = True
    )


# endregion
