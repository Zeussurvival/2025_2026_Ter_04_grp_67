import pygame
class Walls():
    def __init__(self,x,y,l,L):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,l,L)
    def rect(self):
        return self.rect