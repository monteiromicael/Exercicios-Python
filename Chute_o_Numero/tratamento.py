import random

class Tratamento:
    def __init__(self, palpite, aleatorio):
        self.palpite = 0
        self.aleatorio = 0
    

    def maior(self):
        if self.palpite > self.aleatorio:
            print('Chute mais Baixo!')

    def menor(self):
        if self.palpite < self.aleatorio:
            print('Chute mais Alto!')
    
    def igual(self):
        if self.palpite == self.aleatorio:
            print('Parabens você acertou!')
        
