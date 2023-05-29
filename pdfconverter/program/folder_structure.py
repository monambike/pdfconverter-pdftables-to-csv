import os.path
import pathlib

from pdfconverter.__variables__ import Var


# region Public Methods


def create() -> None:
    index_folder: int = 0
    folder_path: str = (
        Var.ConversionInfo.folder_path_export
        + "\\" + Var.Main.FOLDER_NAME_EXPORT
    )
    folder_name: str = ""
    while os.path.isdir(folder_path):
        index_folder += 1

        folder_name = Var.Main.FOLDER_NAME_EXPORT + " (" + str(index_folder) + ")"

        folder_path = (
            Var.ConversionInfo.folder_path_export
            + "\\" + folder_name
        )
    Var.ConversionInfo.folder_name_export = folder_name
    Var.ConversionInfo.folder_path_export = folder_path

    pathlib.Path(Var.ConversionInfo.folder_path_export).mkdir()
    for library in Var.ConversionInCodeSettings.READING_LIBRARIES:
        pathlib.Path(
            Var.ConversionInfo.folder_path_export
            + "\\" + library
        ).mkdir()
        for reading_type in getattr(Var.ConversionInCodeSettings, str(library).upper() + "_READING_TYPES"):
            pathlib.Path(
                Var.ConversionInfo.folder_path_export
                + "\\" + library
                + "\\" + reading_type
            ).mkdir()
            for output_type in getattr(Var.ConversionInCodeSettings, str(library).upper() + "_OUTPUT_TYPES"):
                pathlib.Path(
                    Var.ConversionInfo.folder_path_export
                    + "\\" + library
                    + "\\" + reading_type
                    + "\\" + output_type
                ).mkdir()


# endregion
