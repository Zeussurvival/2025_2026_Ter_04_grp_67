import pygame
import os
main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Tiles") 

class TILE():
    def __init__(self,image,rotate):
        self.image = pygame.image.load(os.path.join(img_dir, image)).convert_alpha()
        self.image = pygame.transform.rotate(self.image,rotate)
        self.image = pygame.transform.scale(self.image,(16,16))
    def draw_self(self,screen,pos,global_sizes):
        screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0],16*global_sizes[1]))  ,(pos[0]*16*global_sizes[0],pos[1]*16*global_sizes[1]))
        # screen.blit(list_loaded_tiles[Chunk1[i,b]].image,(b*16*GLOBAL_ZOOM,i*16*GLOBAL_ZOOM))
class Tree(TILE):
    def __init__(self,collision,sound_on,image,rotate):
        super().__init__(os.path.join(img_dir, f"Tree/{image}"),rotate)
        self.collision = collision
        self.sound_on = sound_on
class Grass(TILE):
    def __init__(self,collision,sound_on,image,rotate):
        super().__init__(os.path.join(img_dir, f"Grass/{image}"),rotate)
        self.collision = collision
        self.sound_on = sound_on
class Road(TILE):
    def __init__(self, collision,sound_on,image,rotate):
        super().__init__(os.path.join(img_dir, f"Road/{image}"),rotate)
        self.collision = collision
        self.sound_on = sound_on



def chunk_loader(chunk):
    chunk_loaded = chunk
    for a in len(chunk[0]):
        for b in len(chunk[0]):
            pos = a,b
            inte = chunk[pos]
pygame.quit()