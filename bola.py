class Ball:
    def __init__(self, cor, raio, material):
        self. cor = cor
        self.raio = raio
        self.material = material

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_circunferencia(self):
        circunferencia = 2 * 3.14 * self.raio
        return circunferencia
