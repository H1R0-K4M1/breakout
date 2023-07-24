from math import tan

class Objeto(object):
    """
    Objeto geométrico do do jogo
    """
    def __init__(self, cor, pos, vel, tag):
        self.cor = cor
        self.x = pos[0]
        self.y = pos[1]
        self.vx = vel[0]
        self.vy = vel[1]
        self.tag = tag
        self.id = -1

    def move(self, canvas):
        """
        Muda a posição do círculo
        """
        self.x += self.vx
        self.y += self.vy

    def desenhar(self, canvas):
        """
        Desenha a imagem do círculo na tela
        """
        #A ser implementada pela classe filha
        pass
