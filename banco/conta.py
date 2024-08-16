class Contato:

    def __init__(self, tel, email):
        self.tel = tel
        self.email = email


class Cliente:

    def __init__(self, nome, cpf, contato: Contato):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato


class Conta:

    def __init__(self, cliente: Cliente, agencia, nConta, saldo):
        self.cliente = cliente
        self.agencia = agencia
        self.nConta = nConta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


if __name__ == '__main__':

    contato1 = Contato('1112345343', 'carlos.edu@hotmail.com.br')
    cliente1 = Cliente('Ana', '123.444.532-90', contato1)
    cc = Conta(cliente1, '34344', 490, 1200)

    