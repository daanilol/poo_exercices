class Conta:
    def __init__(self, numero_da_conta, nome_correntista, saldo = 0):
        self.numero_da_conta = numero_da_conta
        self.nome_correntista = nome_correntista
        self.saldo = float(saldo)

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor
