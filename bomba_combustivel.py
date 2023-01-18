class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.total_bomba = 1000
        self.valorCombustivel = valorCombustivel
    
    def abastecerPorValor(self, valorAbastecer):
        abastecidoPorValor =  valorAbastecer / self.valorCombustivel
        return abastecidoPorValor

    def abastecerPorLitro(self, abastecerLitro):
        abastecidoPorLitro = abastecerLitro * self.valorCombustivel
        return abastecidoPorLitro

    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel

    def alterarQuantidadeCombustivel(self, qtdCombustivel):
        self.total_bomba = qtdCombustivel
