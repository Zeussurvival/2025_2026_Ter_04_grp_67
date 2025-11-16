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
S_WIDTH,S_HEIGHT = 720, 1000

screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

GLOBAL_X_SIZE = round(S_WIDTH / 200)
GLOBAL_Y_SIZE = round(S_WIDTH / 200)

main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Image")
print(img_dir)

class Imagee():
    def __init__(self,name):
        self.real_img = pygame.image.load(os.path.join(img_dir, name)).convert_alpha()
        # self.real_img = pygame.transform.scale(self.real_img,(16,16))
        
        self.img = self.real_img
        self.rect = self.img.get_rect()
    def draw_self(self,pos):
        real_pos = pos[0] - self.rect[2] / 2, pos[1] - self.rect[3] / 2
        screen.blit(self.img,real_pos)


Img_Humain = Imagee("Player.png")
Wall1 = W.Walls(S_WIDTH - 180, 20,160,60)
Wall_liste = [Wall1]



Human1 = H.Humain(0,0,5,"Humain","Bob",Img_Humain.real_img)
Zombie1 = H.Zombie(10,10,3,"Zombie","Zomb1",None)
Zombie_liste = [Zombie1] 

with open("Items.json","r") as f:
    Items = json.loads(f.read())
# print(Items)
Deagle = I.Weapon(10,7,100,(5,5),"Deagle","gun","tah Fortnite prime")
Pompe = I.Weapon(25,6,10,(7,5),"Spas 12","gun","Boom -200 headshot")
# name = "Zombie" + str(len(Zombie_liste) + 1)
# Zombie_liste.append(H.Humanoid(random.randint(0,S_WIDTH),random.randint(0,S_HEIGHT),80,80,300,"Zombie", name))
# if pygame.Rect.collidepoint(Walls.rect(Wall1),mouse_pos[0],mouse_pos[1]) and mouse_click == (True,False,False) and not clicked:
#     clicked = True

Map_tiles = np.array([[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13,13, 4, 7,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13,13, 0, 2,13,13,13,18,13,13,13,13,13,13,13,13],
                   [13,13, 0, 2,13,13,13,17,13,13,13,13,13,13,13,13],
                   [13, 4, 8, 2,13,13,13,16,13,13,13,13,13,13,13,13],
                   [13, 0,14,11, 3, 3,13,15,13,13,13,13,13,13,13,13],
                   [13, 0,14,14,13,12,13,13,13,13,13,13,13,13,13,13],
                   [13, 0,14,14,13,12,13,13,13,13,13,13,13,13,13,13],
                   [13, 0,14,14,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13, 0,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
                   [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13]])


Map_collision = np.zeros(Map_tiles.shape)
Map_collision[5,7] = 1 
print(Map_collision)

list_loaded_tiles = [T.Road(None,"Road_0.png",0),T.Road(None,"Road_0.png",90),T.Road(None,"Road_0.png",180),T.Road(None,"Road_0.png",270),\
    T.Road(None,"Road_coin_1.png",0),T.Road(None,"Road_coin_1.png",90),T.Road(None,"Road_coin_1.png",180),T.Road(None,"Road_coin_1.png",270),\
    T.Road(None,"Road_anticoin_1.png",0),T.Road(None,"Road_anticoin_1.png",90),T.Road(None,"Road_anticoin_1.png",180),T.Road(None,"Road_anticoin_1.png",270),\
    T.Grass(None,"Grass_0.png",0),\
    T.Grass(None,"Grass_01.png",0),\
    T.Road(None,"Road_empty_1.png",0),\
    T.Tree(None,"Tree_1_bottom.png",0),T.Tree(None,"Tree_1.png",0),T.Tree(None,"Tree_1_top.png",0),T.Tree(None,"Tree_1_leaves_1.png",0),\
            ]

# def tiles_in_screen(Human_pos,screen_size,global_sizes):
#     abc = screen_size[0]/(2*16*global_sizes[0])
#     defg = screen_size[1]/(2*16*global_sizes[0])
#     return [(Human_pos[0]-abc,Human_pos[1]-defg),(Human_pos[0]+abc,Human_pos[1]+defg)]
    
# def new_chunk(matrice,pos_list):

#     pos1 = verify_pos1(((pos_list[0][0]-1),pos_list[0][1]-1))
#     pos2 = verify_pos2(((pos_list[1][0]+1),pos_list[1][1]+1))

#     return matrice[plus_or_0_round(pos1[1]):plus_or_0_round(pos2[1]),plus_or_0_round(pos1[0]):plus_or_0_round(pos2[0])]

# def plus_or_0_round(n):
#     if n <= 0:
#         return 0
#     else:
#         return round(n)

# def verify_pos1(pos1):
#     pos1 = list(pos1)
#     while pos1[0] -pos1[1] > 15:
#         pos1[1] = pos1[1] -1
#     return tuple(pos1)

# def verify_pos2(pos2):
#     pos2 = list(pos2)
#     while pos2[1] -pos2[0] > 10:
#         pos2[1] =  pos2[1] -1
#     return tuple(pos2)















clicked = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((40,0,150))

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    for obj in Wall_liste:
        pygame.draw.rect(screen,"white",W.Walls.rect(Wall1))
    # for zombie in Zombie_liste:
    #     pygame.draw.rect(screen,"red",zombie.Rect(),0,10)
    # print(tiles_in_screen(Human1.pos,(S_WIDTH,S_HEIGHT),(GLOBAL_X_SIZE,GLOBAL_Y_SIZE)))
    # pos_list = tiles_in_screen(Human1.pos,(S_WIDTH,S_HEIGHT),(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))
    # chunk_shown = new_chunk(matrice=Map_tiles, pos_list=pos_list)
    # print(pos_list)
    for i in range(len(Map_tiles)):
        for b in range(len(Map_tiles[i])):
                # pygame.draw.rect(screen,"green",(b*16,i*16,16,16))
                # screen.blit(list_loaded_tiles[Map_tiles[i,b]].image,(b*16*GLOBAL_ZOOM,i*16*GLOBAL_ZOOM))
                tuty = 2*16*GLOBAL_X_SIZE
                list_loaded_tiles[Map_tiles[i,b]].draw_self(screen,(b-Human1.pos[0]+S_WIDTH/(16*2*GLOBAL_X_SIZE),i-Human1.pos[1]+S_HEIGHT/(16*2*GLOBAL_X_SIZE)),(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))


    Human1.moove(keys,dt,(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))
    # Human1.draw_self(screen,Human1.pos,(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))
    Human1.draw_center(screen,(S_WIDTH,S_HEIGHT),(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))

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