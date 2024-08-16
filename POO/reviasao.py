from abc import ABC, abstractmethod
from datetime import date


class TestePoo1(ABC):   # classe abstrata nao pode mais ser instanciada

    def __init__(self, nome: str = 'Carlos') -> None:
        self.__nome = nome
        self.__oculto = None
        self.__cont = 0

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self.nome = novoNome

    def contar(self) -> int:
        """
        O metodo contar soma mais 1 valor em cada uma de suas chamadas e retorna o valor somado
        :return: int
        """

        self.__cont += 1
        return self.__cont

    @abstractmethod
    def calcularIdade(self):
        pass


class Poo2(TestePoo1):
    def __init__(self, nome, salario: float, ano_nascimento: int) -> None:
        super().__init__(nome)
        self.__salario: float = salario
        self.__ano_nascimento = ano_nascimento

    def calcularIdade(self) -> int:
        anoAtual = date.today().year
        idade = anoAtual - self.__ano_nascimento
        return idade

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, novoSalario: float) -> None:
        self.salario = novoSalario


if __name__ == '__main__':

    t1 = TestePoo1('jhoana')
    tp2 = Poo2('amanda', 2300.71, 2005)

    print(t1.nome)
    print(t1.contar())

    print(tp2.salario)
    print(tp2.nome)
    print(tp2.contar())
