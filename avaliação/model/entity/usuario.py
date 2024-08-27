class Usuario:

    def __init__(self, login: str, senha: str):
        self.__login = login
        self.__senha = senha

    @property
    def login(self) -> str:
        return self.__login

    @property
    def senha(self) -> str:
        return self.__senha
