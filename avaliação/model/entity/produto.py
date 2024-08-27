from datetime import date


class Produto:

    def __init__(self, nome: str, descricao: str, preco: float, data: date, quant: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__data = data
        self.__quant = quant

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self.__nome = novoNome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, novaDescricao: str) -> None:
        self.__descricao = novaDescricao

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, novoPreco: float) -> None:
        self.__preco = novoPreco

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, novaData: date) -> None:
        self.__data = novaData

    @property
    def quant(self) -> int:
        return self.__quant

    @quant.setter
    def quant(self, novoQuant: int) -> None:
        self.__quant = novoQuant
