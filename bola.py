from objeto import Objeto
from constantes import *

class Bola(Objeto):
    """
    Objeto bola do jogo
    """
    def __init__(self, raio, cor, pos, vel):
        self.r = raio
        self.bateu = False 
        super().__init__(cor, pos, vel, 'bola')

    def update(self, jogo):
        """
        Muda a variável bola
        """
        #Primeiro nós movemos a bola
        self.move(jogo.canvas)

        #Depois verificamos por colisões com as extremidades
        self.chocouBorda(jogo)

        #E por fim vemos se há choques com os retângulos
        for r in jogo.r.copy():
            col, pos = self.colideRect(r)
            if col:
                jogo.r.remove(r)
                self.x -= self.vx
                self.y -= self.vy
                #if pos == 0 or pos == 1:
                self.vy = -self.vy
                #else:
                #    self.vx = -self.vx
                break

        if self.colideRect(jogo.player)[0] and not self.bateu:
            self.vy = -self.vy
            self.bateu = True

        if self.y <= jogo.player.y - 2*self.r:
            self.bateu = False

    def colideRect(self, rect):
        """
        Detecta se há colisão ou não com um retângulo
        """
        if (self.x < rect.x + rect.b and self.x + self.r > rect.x and self.y < rect.y + rect.h and self.y + self.r > rect.y):
            #Distância entre o centro do retângulo e o centro da circunferência
            deltax = self.x + self.r/2 - rect.x - rect.b/2
            deltay = self.y + self.r/2 - rect.y - rect.h/2

            if -rect.b/2 < deltax < rect.b/2 and deltay < -rect.h/2:
                #CIMA
                return True, 0
            elif -rect.b/2< deltax < rect.b/2 and deltay >= rect.h/2:
                #BAIXO
                return True, 1
            elif -self.r/2-rect.h/2< deltay < rect.h/2 + self.r/2 and deltax < -rect.b/2 - self.r/2:
                #DIREITA
                return True, 2
            else:
                #ESQUERDA
                return True, 3

        else:
            return False, 5
    
    def chocouBorda(self, jogo):
        """
        Verifica se a bola chocou-se contra uma das bordas
        """
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx
        elif self.x + self.r > CANVAS_L:
            self.x = CANVAS_L - self.r
            self.vx = -self.vx

        if self.y < 0:
            self.vy = -self.vy
    
    def desenhar(self, canvas):
        """
        Desenha a imagem do círculo na tela
        """
        self.id = canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, fill = self.cor,outline = 'white')
