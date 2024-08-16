class Cliente:

    def __init__(self, id_cliente: int, id_contato: int, login: str, senha: str):
        self.__id_cliente: int = id_cliente
        self.__id_contato: int = id_contato
        self.__login: str = login
        self.__senha: str = senha

    @property
    def id_cliente(self) -> int:
        return self.__id_cliente

    @property
    def id_contato(self) -> int:
        return self.__id_contato

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, novoLogin: str) -> None:
        self.__login = novoLogin

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, novaSenha: str) -> None:
        self.__senha = novaSenha

# função para logar
