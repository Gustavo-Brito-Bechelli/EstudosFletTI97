class Conta:

    def __init__(self, id_conta: int, id_cliente: int, saldo: float, ):
        self.__id_cliente: int = id_cliente
        self.__id_conta: int = id_conta
        self.__saldo = saldo
        
    @property
    def id_cliente(self) -> int:
        return self.__id_cliente

    @property
    def id_conta(self) -> int:
        return self.__id_conta

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, novoSaldo: float) -> None:
        self.__saldo = novoSaldo


# função para sacar e depositar
