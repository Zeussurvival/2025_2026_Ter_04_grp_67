import pygame
import os
import time
import numpy as np
import C_Items as I
import C_Humanoid as H
import C_Tiles as T
import json
import random
# import math
pygame.init()
pygame.font.init()
FONT_None = pygame.font.SysFont("timesnewroman", 30)
FONT_combat = pygame.font.SysFont("haettenschweiler", 30)
FONT_death = pygame.font.SysFont("timesnewroman", 80)
S_WIDTH,S_HEIGHT = 1200, 720
# print(pygame.font.get_fonts())
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

if S_WIDTH > S_HEIGHT:
    coeff = S_HEIGHT
else:
    coeff = S_WIDTH

GLOBAL_X_SIZE = round(coeff / 125)
GLOBAL_Y_SIZE = round(coeff / 125)
main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Image")
Humanoid_dir = os.path.join(img_dir,"Humanoid")
print(img_dir)

class Imagee():
    def __init__(self,name):
        self.real_img = pygame.image.load(os.path.join(Humanoid_dir, name)).convert_alpha()
        self.img = self.real_img
        self.rect = self.img.get_rect()
    def draw_self(self,pos):
        real_pos = pos[0] - self.rect[2] / 2, pos[1] - self.rect[3] / 2
        screen.blit(self.img,real_pos)
# self, damage, range, position, name, lore, cooldown,image
Couteau_depart = I.KNIFE(15, 3, 1, "Couteau de cuisine", "Avant on l'utilisait pour couper la viande, maintenant pour couper du zombard",1,"Couteau_de_cuisine.png")
pomme = I.Eatable("Une pomme","récolté depuis un arbre",None,"Apple.png",15,10,10)
Inventaire = [Couteau_depart,pomme,Couteau_depart,Couteau_depart,None,    None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,]

Img_Humain = Imagee("Player.png")
Human1 = H.Humain(3,3,2,"Humain","Bob",Img_Humain.real_img,0.8,Inventaire,25,100,100,FONT_death)
#           x, y, speed, typee, name, image, size, inventaire, inv_max, pv, endurance

zombie_last_search = time.time()
wander_cooldown = 1
Img_Zombie = Imagee("Zombie.png")
# x, y, speed, typee, name, image, size, pv, damage, range, detection_range, wander_cooldown):
Zombie1 = H.Zombie(3,3,1+random.random(),"Zombie","Zomb1",Img_Zombie.real_img,0.8,random.randint(25,50),random.randint(10,20),0.5,random.randint(3,int(GLOBAL_X_SIZE*0.75)),wander_cooldown)
Zombie_liste = [Zombie1] 
for i in range(0,5):
    Zombie_liste.append(H.Zombie(random.randint(5,10),random.randint(5,10),1+random.random(),"Zombie","Zomb"+str(i),Img_Zombie.real_img,random.random()/2 +0.5,random.randint(25,50),random.randint(10,20),0.5,random.randint(3,int(GLOBAL_X_SIZE*0.75)),wander_cooldown))


# with open("Items.json","r") as f:
#     Items = json.loads(f.read())
# print(Items)
Deagle = I.GUN(10,7,100,(5,5),"Deagle","gun","tah Fortnite prime",3,None)
Pompe = I.GUN(25,6,10,(7,5),"Spas 12","gun","Boom -200 headshot",3,None)
List_objet_sol = [Deagle,Pompe]
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
    T.Tree(None,"Grass_1.png","Tree_1_bottom.png",0),T.Tree(None,"Grass_1.png","Tree_1.png",0),T.Tree(None,"Grass_1.png","Tree_1_top.png",0),T.Tree(None,"Grass_1.png","Tree_1_leaves_1.png",0),\
            ]

# def tiles_in_screen(Human_pos,screen_size,global_sizes):
#     abc = screen_size[0]/(2*16*global_sizes[0])
#     defg = screen_size[1]/(2*16*global_sizes[0])
#     return [(Human_pos[0]-abc,Human_pos[1]-defg),(Human_pos[0]+abc,Human_pos[1]+defg)]

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













last_sprint = time.time()

clicked = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((40,0,150))

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    

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
                list_loaded_tiles[Map_tiles[i,b]].draw_self(screen,(b-Human1.pos[0]+S_WIDTH/(tuty),i-Human1.pos[1]+S_HEIGHT/(tuty)),(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))

    for zombie in Zombie_liste:
        zombie.draw_self(screen,Human1.pos,(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))
        zombie.do_itself(Human1.pos,dt,Human1,screen,Map_collision)

    Human1.draw_himself_center(screen,(S_WIDTH,S_HEIGHT),(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))

    if mouse_click == (True,False,False) and not clicked:
        Zombie_liste = Human1.use_hand(Zombie_liste,Human1)
        clicked = True
    if clicked and mouse_click == (False,False,False):
        clicked = False
    if keys[pygame.K_LSHIFT] and time.time()-last_sprint > 1:
        last_sprint = time.time()
        Human1.sprinting()
    if keys[pygame.K_r]:
        Deagle.reload()
    if keys[pygame.K_h]:
        if Human1.alive == False:
            Human1.revive()
    if keys[pygame.K_1] or keys[pygame.K_2] or keys[pygame.K_3] or keys[pygame.K_4] or keys[pygame.K_5]:
        Human1.change_held_item(keys)
    
    # Human1.inventaire[0].draw_self(screen)
    Deagle.update()
    Human1.do_everything(screen,FONT_None,dt,keys)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()