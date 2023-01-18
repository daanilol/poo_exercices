class Square:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def retorna_valor_lado(self):
        return self.tamanho_lado

    def mudar_valor_lado(self, lado):
        self.tamanho_lado = lado

    def calcular_area(self):
        return self.tamanho_lado * self.tamanho_lado
