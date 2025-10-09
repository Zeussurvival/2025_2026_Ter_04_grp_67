import numpy as np
import pygame
import random
pygame.init()
# liste0= []
# liste_tot = []
# for i in range(16):
#     liste0 = []
#     for b in range(16):
#         liste0.append(random.randint(0,4))
#     liste_tot.append(liste0)
# print(liste_tot)

# liste_tot = [[3, 1, 2, 0, 2, 2, 1, 2, 3, 0, 3, 2, 3, 3, 0, 0], [3, 2, 2, 3, 3, 3, 2, 0, 0, 4, 4, 1, 1, 3, 3, 0], [1, 4, 2, 0, 1, 2, 4, 2, 1, 4, 1, 3, 2, 3, 1, 0], [4, 1, 1, 1, 4, 0, 0, 3, 0, 0, 3, 4, 0, 1, 3, 0], [4, 2, 4, 1, 3, 4, 4, 2, 4, 4, 0, 3, 2, 4, 0, 1], [2, 1, 1, 1, 1, 1, 0, 4, 3, 4, 3, 4, 0, 4, 2, 2], [4, 2, 3, 2, 4, 3, 1, 1, 3, 2, 2, 0, 4, 0, 1, 4], [0, 1, 4, 4, 0, 3, 3, 0, 2, 2, 2, 1, 3, 1, 1, 3], [4, 0, 1, 1, 4, 3, 0, 2, 3, 0, 1, 4, 0, 3, 4, 2], [4, 3, 2, 2, 3, 0, 4, 0, 2, 3, 4, 1, 4, 1, 1, 2], [4, 0, 4, 0, 0, 0, 3, 2, 0, 0, 4, 0, 4, 2, 3, 0], [4, 3, 0, 0, 2, 4, 1, 4, 1, 4, 3, 1, 0, 0, 0, 1], [0, 0, 0, 2, 0, 0, 2, 4, 3, 0, 0, 0, 3, 0, 0, 3], [3, 1, 3, 2, 0, 2, 4, 3, 3, 0, 0, 4, 3, 2, 2, 1], [2, 2, 4, 2, 4, 2, 3, 1, 1, 3, 4, 0, 0, 3, 0, 3], [3, 0, 0, 0, 2, 0, 3, 1, 3, 4, 1, 3, 0, 4, 1, 3]]
# a = np.array(liste_tot)
# print(a)
# b = a[1:9,4:12]
# print(b)

# https://youtu.be/ZB7BZMhfPgk?si=r_5U_WEBpwlqMCz5&t=3517


# c = np.arange(25).reshape(5,5)
# print(c)
# red = c[:,1::2]
# yellow = c[4,:]
# blue = c[1::2,:3:2]
# print(blue)


# c = np.arange(25).reshape(5,5)
# print(c)
# for a in range(len(c)):
#     for b in range(len(c[a])):
#         print(c[a,b])


Chunk1 = np.array([[0,0,1,0],
                [0,0,1,0],
                [0,0,1,0],
                [0,1,1,1]])

# print("AAAAAAAAAAAA")
# for i in range(len(Chunk1)):
#     for b in range(len(Chunk1[i])):
#         print("AAA",i,b)
#         if Chunk1[i,b] %2 == 0:
#             # print("AAAAAAAAA",i,b)
#             print(i*16,b*16)
#             # screen.blit(list_loaded_tiles[0].image,(b*16,i*16))

#         if Chunk1[i,b] %2 == 1:
#             # print("BBBBBBBBBBBBBB",i,b)
#             print(i*16,b*16)



screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")

    print("AAAAAAAAAAAAA")
    for i in range(len(Chunk1)):
        for b in range(len(Chunk1[i])):
            print("BBB",Chunk1[i])
            print("AAA",i,b)
            if Chunk1[i,b] == 0:
                print(Chunk1[i,b])
                # print("AAAAAAAAA",i,b)
                print(i*16,b*16)
                pygame.draw.rect(screen,"green",(b*16,i*16,16,16))

            if Chunk1[i,b] == 1:
                print("Non",Chunk1[i,b])
                # print("BBBBBBBBBBBBBB",i,b)
                print(i*16,b*16)
                pygame.draw.rect(screen,"red",(b*16,i*16,16,16))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()