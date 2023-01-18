class People:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = float(peso)
        self.altura = float(altura)

    def envelhecer(self, anos):
        self.idade += anos
        return self.idade

    def engordar(self, kg_mais):
        self.peso += kg_mais
        return self.peso

    def emagrecer(self, kg_menos):
        self.peso -= kg_menos
        return self.peso
    
    def crescer(self):
        if self.idade < 21:
            self.altura += (self.idade * 0.05)
        return self.altura
