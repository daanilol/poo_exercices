class Tv:
    def __init__(self, canal: 0, volume):
        self.ligada = False
        self.canal = canal
        self.volume = volume
 
    def aumentar_volume(self):
        if self.volume in range(0, 100):
            self.volume += 1
        else:
            print("O limite é 100.")

    def diminuir_volume(self):
        if self.volume in range(0 + 1, 100):
            self.volume -= 1
        else:
            print("O limite é 0.")

    def mudar_canal(self, canal):
        self.canal = canal
