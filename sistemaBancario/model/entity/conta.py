class Conta:

    def __init__(self, saldo: float):
        self.__id_cliente = 1
        self.__id = 1
        self.__saldo = saldo

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, novoSaldo: float) -> None:
        self.__saldo = novoSaldo

    def sacar(self, valor: float) -> bool:
        """
        esse metodo vai decrementar valores da variavel saldo
        :param valor: float
        :return: bool
        """
        if valor >= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor: float) -> bool:
        """
        esse metodo vai adicionar valores na variavel saldo
        :param valor: float
        :return: bool
        """
        self.saldo += valor
        return True
