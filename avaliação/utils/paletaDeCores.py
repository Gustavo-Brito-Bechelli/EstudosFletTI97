class CoresAplicacao:

    def __init__(self):
        self.__corPrimaria: str = '#EDA113'
        self.__corHover: str = '#F7B945'
        self.__corPreta: str = '#000000'
        self.__corBranca: str = '#FFFFF'

    @property
    def corPrimaria(self) -> str:
        return self.__corPrimaria

    @property
    def corHover(self) -> str:
        return self.__corHover

    def corBranca(self) -> str:
        return self.__corBranca

    def corPreta(self) -> str:
        return self.__corPreta
