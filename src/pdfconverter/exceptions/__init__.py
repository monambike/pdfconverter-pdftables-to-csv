class PathIsNotDirectory(Exception):
    def __init__(
        self,
        message: str = "O caminho não representa um diretório válido.",
        invalid_directory_path: str = ""
    ):
        self.message = message
        self.invalid_directory_path = invalid_directory_path
