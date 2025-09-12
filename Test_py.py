import pygame
import random
import math
pygame.init()
S_WIDTH,S_HEIGHT = 1280, 720

screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

class Walls():
    def __init__(self,x,y,l,L):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,l,L)
    def rect(self):
        return self.rect
Wall1 = Walls(S_WIDTH - 180, 20,160,60)
Wall_liste = [Wall1]


class Humanoid():
    def __init__(self,x,y,l,L,speed,type,name):
        self.pos = pygame.math.Vector2(x,y)
        self.len = (l,L)
        self.vect = pygame.math.Vector2(0,0)
        self.rect = pygame.Rect(x,y,l,L)
        self.type = type
        self.name = name
        self.speed = speed
        self.image = False
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

Human1 = Humanoid(500,500,80,80,300,"Humain","Bob")
Zombie1 = Humanoid(500,500,80,80,300,"Zombie","Zomb1")
Zombie_liste = [Zombie1] 

clicked = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    Human1.moove(keys,dt)

    screen.fill("purple")
    pygame.draw.rect(screen,(0,25,100),Humanoid.Rect(Human1))
    for obj in Wall_liste:
        pygame.draw.rect(screen,"white",Walls.rect(Wall1))
    if pygame.Rect.collidepoint(Walls.rect(Wall1),mouse_pos[0],mouse_pos[1]) and mouse_click == (True,False,False) and not clicked:
        clicked = True
        name = "Zombie" + str(len(Zombie_liste) + 1)
        Zombie_liste.append(Humanoid(random.randint(0,S_WIDTH),random.randint(0,S_HEIGHT),80,80,300,"Zombie", name))
    if clicked and mouse_click == (False,False,False):
        clicked = False
    for zombie in Zombie_liste:
        pygame.draw.rect(screen,"red",Humanoid.Rect(zombie),0,10)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    print(dt)

pygame.quit()