import pygame
import time
import Items as I
import Humanoid as H
import json
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

with open("Items.json","r") as f:
    Items = json.loads(f.read())
print(Items)
Human1 = H.Humanoid(500,500,80,80,300,"Humain","Bob",pygame.image.load(r"C:\\Users\\gunnarsson1\\Documents\\GitHub\\2025_2026_Ter_04_grp_67\\Image\\Player.png"))
Zombie1 = H.Humanoid(500,500,80,80,300,"Zombie","Zomb1",None)
Zombie_liste = [Zombie1] 


Deagle = I.Weapon("pistolet",10,7,100)
Pompe = I.Weapon("pistolet",25,6,10)
# name = "Zombie" + str(len(Zombie_liste) + 1)
# Zombie_liste.append(H.Humanoid(random.randint(0,S_WIDTH),random.randint(0,S_HEIGHT),80,80,300,"Zombie", name))
# if pygame.Rect.collidepoint(Walls.rect(Wall1),mouse_pos[0],mouse_pos[1]) and mouse_click == (True,False,False) and not clicked:
#     clicked = True

clicked = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    

    Human1.moove(keys,dt)
    screen.blit(screen,Human1.pos,Human1.Rect())
    for obj in Wall_liste:
        pygame.draw.rect(screen,"white",Walls.rect(Wall1))
    for zombie in Zombie_liste:
        pygame.draw.rect(screen,"red",zombie.Rect(),0,10)
    
    if mouse_click == (True,False,False) and not clicked:
        Deagle.shoot()
        clicked = True
    if clicked and mouse_click == (False,False,False):
        clicked = False
    if keys[pygame.K_r]:
        Deagle.reload()
    Deagle.print()
    Deagle.update()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    # print(dt)

pygame.quit()