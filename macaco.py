class Monkey:
    def __init__(self, nome):
        self.nome = nome 
        self.estomago = []

    def comer(self, alimento):
        self.estomago.append(alimento)

    def ver_estomago(self):
        return self.estomago

    def digerir(self):
        self.estomago.remove()

    def canibal(self, monkey):
        monkey_meat = 'carne_de_macaco'
        for i in monkey.estomago:
            self.estomago.append(i)
        self.estomago.append(monkey_meat)


m1 = Monkey('donk')
m1.comer('banana')
m1.comer('maca')
m1.comer('pera')
print("Macaco 1: {}".format(m1.ver_estomago()))

m2 = Monkey('kong')
m2.comer('abacaxi')
m2.comer('cebola')
m2.comer('pizza')
print("Macaco 2: {}\n".format(m2.ver_estomago()))

m2.canibal(m1)

print("Macaco 2: {}\n".format(m2.ver_estomago()))
