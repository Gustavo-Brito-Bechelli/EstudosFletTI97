class Cliente:

    def __init__(self, login: str, senha: str):
        self.__id_cliente = 1
        self.__id_contato = 1
        self.__login: str = login
        self.__senha: str = senha

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
