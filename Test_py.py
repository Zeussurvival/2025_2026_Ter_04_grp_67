import pygame
import os
import time
import numpy as np
import C_Items as I
import C_Humanoid as H
import C_Walls as W
import C_Tiles as T
import json
# import random
# import math
pygame.init()
S_WIDTH,S_HEIGHT = 1280, 720

screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
CONVERSION_CARRE_PIXEL = 16
CONVERSION_PIXEL_CARRE = 1/16


main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Image")
print(img_dir)

class Imagee():
    def __init__(self,name):
        self.real_img = pygame.image.load(os.path.join(img_dir, name)).convert_alpha()
        self.real_img = pygame.transform.scale(self.real_img,(16,16))
        
        self.img = self.real_img
        self.rect = self.img.get_rect()
    def draw_self(self,pos):
        real_pos = pos[0] - self.rect[2] / 2, pos[1] - self.rect[3] / 2
        screen.blit(self.img,real_pos)


Img_Humain = Imagee("Player.png")
Wall1 = W.Walls(S_WIDTH - 180, 20,160,60)
Wall_liste = [Wall1]



Human1 = H.Humain(0,0,30,"Humain","Bob",Img_Humain.real_img)
Zombie1 = H.Zombie(10,10,3,"Zombie","Zomb1",None)
Zombie_liste = [Zombie1] 

with open("Items.json","r") as f:
    Items = json.loads(f.read())
print(Items)
Deagle = I.Weapon(10,7,100)
Pompe = I.Weapon(25,6,10)
# name = "Zombie" + str(len(Zombie_liste) + 1)
# Zombie_liste.append(H.Humanoid(random.randint(0,S_WIDTH),random.randint(0,S_HEIGHT),80,80,300,"Zombie", name))
# if pygame.Rect.collidepoint(Walls.rect(Wall1),mouse_pos[0],mouse_pos[1]) and mouse_click == (True,False,False) and not clicked:
#     clicked = True
Chunk1 = np.array([[0,0,3,2,0],
                [0,0,1,2,0],
                [0,0,1,2,0],
                [0,3,4,2,0]])

list_loaded_tiles = [T.Grass(None,None,None,"Grass_2.png",0),T.Road(None,None,None,"Road_0.png",0),T.Road(None,None,None,"Road_0.png",-180),T.Road(None,None,None,"Road_coin_1.png",0),T.Road(None,None,None,"Road_4.png",0)]











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

    for i in range(len(Chunk1)):
        for b in range(len(Chunk1[i])):
                # pygame.draw.rect(screen,"green",(b*16,i*16,16,16))
                screen.blit(list_loaded_tiles[Chunk1[i,b]].image,(b*16,i*16))


    Human1.moove(keys,dt)
    screen.blit(Human1.image,Human1.pos)
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

pygame.quit()