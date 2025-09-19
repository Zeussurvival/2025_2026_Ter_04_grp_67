import pygame
import os
import time
import Items as I
import Humanoid as H
import Walls as W
import json
import random
import math
pygame.init()
S_WIDTH,S_HEIGHT = 1280, 720

screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Image")
print(img_dir)

class Imagee():
    def __init__(self,name):
        self.real_img = pygame.image.load(os.path.join(img_dir, name)).convert_alpha()
        self.real_img = pygame.transform.scale(self.real_img,(64,64))
        self.img = self.real_img
        self.rect = self.img.get_rect()
        # self.rotation = 0  et  https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
    def draw_self(self,pos):
        real_pos = pos[0] - self.rect[2] / 2, pos[1] - self.rect[3] / 2
        print(pos)
        screen.blit(self.img,real_pos)
    def print_rect(self):
        print(self.rect)


Img_Humain = Imagee("Player.png")
Wall1 = W.Walls(S_WIDTH - 180, 20,160,60)
Wall_liste = [Wall1]


with open("Items.json","r") as f:
    Items = json.loads(f.read())
print(Items)

Human1 = H.Humanoid(S_WIDTH/2,S_HEIGHT/2,80,80,300,"Humain","Bob",Img_Humain)
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
    
    for obj in Wall_liste:
        pygame.draw.rect(screen,"white",W.Walls.rect(Wall1))
    # for zombie in Zombie_liste:
    #     pygame.draw.rect(screen,"red",zombie.Rect(),0,10)
    
    Human1.moove(keys,dt)
    Img_Humain.draw_self(Human1.pos)
    if mouse_click == (True,False,False) and not clicked:
        Deagle.shoot()
        clicked = True
    if clicked and mouse_click == (False,False,False):
        clicked = False
    if keys[pygame.K_r]:
        Deagle.reload()
    
    Deagle.update()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    # print(dt)

pygame.quit()