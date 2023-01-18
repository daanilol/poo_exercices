class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.calc = (self.fome + self.saude) / 2
        self.humor = self.calc

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, fome_nivel):
        if fome_nivel in range(0, 10):
            self.fome = fome_nivel
        else:
            print("A fome tem que estar entre 0 e 10.")

    def alterar_saude(self, nivel_saude):
        if nivel_saude in range(0, 10):
            self.saude = nivel_saude
        else:
            print("A saúde tem que estar entre 0 e 10.")

    def alterar_idade(self, nova_idade):
        if nova_idade in range(0, 100):
            self.idade = nova_idade

    def calculo_humor(self):
        if self.humor <= 5:
            return ":("
        elif self.humor > 5 and self.humor <= 10:
            return ":D"
        elif self.humor >= 5 and self.humor <= 6:
            return ":|"

tamagushi = Tamagushi('GOD', 9, 0, 1)
print("Nome: {}\nFome: {}\nSaude: {}\nIdade: {}\nHumor: {}".format(tamagushi.nome, tamagushi.fome, tamagushi.saude, tamagushi.idade, tamagushi.calculo_humor()))
tamagushi.calculo_humor()