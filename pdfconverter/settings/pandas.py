import pandas


# region Public Methods


def set_settings(
    max_column_width: int = 0,
    expand_frame_representation: bool = False,
    encoding: str = "UTF-8-sig",
    multicolumn: bool = False
) -> None:
    """
    Método que define as configurações da biblioteca Pandas.

    Args:
        max_column_width:
        expand_frame_representation:
        encoding:
        multicolumn:
    """

    # Configuração que evita com que dados sejam  quebrados  no
    # arquivo exportado
    pandas.options.display.max_colwidth = max_column_width
    # Configuração que evita com que os dados acabem sendo que-
    # brados na saída do terminal
    pandas.options.display.expand_frame_repr = expand_frame_representation
    # Configuração que define  o  padrão  de  codificação  para
    # UTF-8 com BOM
    pandas.options.display.encoding = encoding
    # Configuração que faz com que caso exista um ";"  ele  não
    # passe os dados pra outra célula
    pandas.options.display.latex.multicolumn = multicolumn


# endregion
