class CoresAplicacao:

    def __init__(self) -> None:
        self.__corPrimaria: str = '#1b9b85'
        self.__corSecundaria: str = '#136f5f'
        self.__corHover: str = '#263238'
        self.__corDefault: str = '#1b9b85'
        self.__corBranca: str = 'ffffff'

    @property
    def corPrimaria(self) -> str:
        """
        constante para retornar a cor primaria
        :return: str
        """
        return self.__corPrimaria

    @property
    def corSecundaria(self) -> str:
        """
        constante para retornar a cor secundaria
        :return: str
        """
        return self.__corSecundaria

    @property
    def corHover(self) -> str:
        """
        constante para retornar a cor quando o mouse esta em cima do botao
        :return: str
        """
        return self.__corHover

    @property
    def corDefault(self) ->str:
        """
        constante para retornar a cor padrao do botao
        :return: str
        """
        return self.__corDefault

    @property
    def corBranca(self) -> str:
        """
        constante para retornar a cor branca
        :return: str
        """
        return self.__corBranca
