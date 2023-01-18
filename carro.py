class Car:
    def __init__(self, kmLitro):
        self.ltsTanque = 0
        self.kmLitro = kmLitro

    def adicionarGasolina(self, ltsGasolina):
        self.ltsTanque += ltsGasolina

    def obterGasolina(self):
        return self.ltsTanque

    def andar(self, km):
        self.ltsTanque -= km / self.kmLitro


c = Car(14)
c.adicionarGasolina(1)
print(c.obterGasolina())
c.andar(14)
print(c.obterGasolina())
