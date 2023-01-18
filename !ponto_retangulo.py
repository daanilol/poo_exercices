class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostra_x_y(self):
        return self.x, self.y

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro_do_retangulo(self):
        centro = (self.largura + self.altura) / 2
