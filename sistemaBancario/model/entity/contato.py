class Contato:

    def __init__(self, telefone: str, email: str):
        self.__id_contato = 1
        self.__telefone: str = telefone
        self.__email: str = email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, novoTelefone: str) -> None:
        self.__telefone = novoTelefone

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, novoEmail: str) -> None:
        self.__email = novoEmail


# função para mudar o telefone
