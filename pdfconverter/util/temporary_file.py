import tempfile

from pdfconverter import util


# region Fields

temp_file: _TemporaryFileWrapper = None
"""Variável que armazena o objeto do arquivo temporário."""

# endregion


# region Classes


class TemporaryFile:
    def __init__(
        self,
        file_prefix: str,
        file_suffix: str = "",
        delete_file_after_close: bool = True
    ) -> None:
        global temp_file
        temp_file = tempfile.NamedTemporaryFile(
            mode = "w+",
            prefix = (
                "PDFConverter"
                + "_"
                + file_prefix
                + "_"
                + util.get_current_date_and_time()
            ),
            suffix = (file_suffix + "_.tmp"),
            delete = delete_file_after_close
        )

    # region Public Methods

    @staticmethod
    def write(string: str) -> None:
        temp_file.write(string)

    @staticmethod
    def read_all_lines() -> None:
        temp_file.seek(0, 0)

        return temp_file.readlines()

    @staticmethod
    def close() -> None:
        temp_file.close()

    # endregion


# endregion
