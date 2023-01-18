class Rectangle:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.perimetro = 0
        self.area = 0
    def mudar_valor_dos_lados(self, largura, altura):
        self.largura = largura
        self.altura = altura
 
    def retorna_valor_altura_largura(self):
        print((self.largura, self.altura))


    def perimetro_retangulo(self):
        self.perimetro = 2 * (self.largura + self.altura)


    def area_retangulo(self):
        self.area =  self.altura * self.largura
