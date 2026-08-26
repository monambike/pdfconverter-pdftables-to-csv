import json
import os.path
import re
from datetime import datetime

from pdfconverter.__variables__ import Var


# region Public Methods


def file_has_pdf_extension(file_path: str) -> bool:
    return True if(os.path.isfile(file_path) and (str(file_path[-4:]).lower() == ".pdf")) else False


def justify_text(
    text: str,
    char_quantity: int
) -> str:
    return "\n".join(
        re.findall(
            pattern = '.{1,%i}' % int(char_quantity),
            string = str(text)
        )
    )


def convert_dictionary_to_json(dictionary: dict) -> str:
    return json.dumps(
        obj = dictionary,
        indent = 4,
        ensure_ascii = False
    )


def convert_dictionary_to_json_utf8(dictionary: dict) -> bytes:
    return json.dumps(
        obj = dictionary,
        indent = 4,
        ensure_ascii = False
    ).encode("UTF-8")


def get_current_file_path_export() -> str:
    return (
        Var.ConversionInfo.folder_path_export
        + "\\" + Var.CurrentConvertedFileInfo.current_file_reading_library
        + "\\" + Var.CurrentConvertedFileInfo.current_file_reading_type
        + "\\" + Var.CurrentConvertedFileInfo.current_file_export_type
        + "\\" + Var.CurrentConvertedFileInfo.file_name_pdf + ".txt"
    )


def get_current_date_and_time():
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    # return datetime.today().strftime("%Y%m%d_%H%M%S")


# endregion
