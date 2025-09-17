import pygame
class Humanoid():
    def __init__(self,x,y,l,L,speed,type,name,image):
        self.pos = pygame.math.Vector2(x,y)
        self.len = (l,L)
        self.vect = pygame.math.Vector2(0,0)
        self.rect = pygame.Rect(x,y,l,L)
        self.type = type
        self.name = name
        self.speed = speed
        self.image = image
    def moove(self,keys,dt):
        max_sp = pygame.math.Vector2(self.speed * dt,0).length()
        if keys[pygame.K_z]:
            self.vect[1] -= self.speed * dt
        if keys[pygame.K_s]:
            self.vect[1] += self.speed * dt
        if keys[pygame.K_q]:
            self.vect[0] -= self.speed * dt
        if keys[pygame.K_d]:
            self.vect[0] += self.speed * dt
        if self.vect.length() > 1:
            self.vect = self.vect.normalize()
        self.pos += self.vect * max_sp
        self.vect = pygame.math.Vector2(0,0)
    def Rect(self):
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.len[0],self.len[1])
        return self.rect
    def Name(self):
        return self.name