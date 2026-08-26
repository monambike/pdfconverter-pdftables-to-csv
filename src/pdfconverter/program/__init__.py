import sys

from pdfconverter import output_info
from pdfconverter.output_info import errors


# region Public Methods


def finish() -> None:
    try:
        output_info.make_file()

        sys.exit()
    except Exception as exception:
        errors.add_error_method_unknown_exception(error_exception = exception)


# endregion
