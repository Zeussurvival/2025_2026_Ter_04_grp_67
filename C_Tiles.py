import pygame
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Tiles") 

class TILE():
    def __init__(self,obj,image):
        self.obj_on = obj
        self.image = pygame.image.load(os.path.join(img_dir, image)).convert_alpha()
    def draw_self(self):

        pass
class Grass(TILE):
    def __init__(self, obj,collision,sound_on,image):
        super().__init__(obj,os.path.join(img_dir, f"Herbe/{image}"))
        self.collision = collision
        self.sound_on = sound_on
class Road(TILE):
    def __init__(self, obj, collision,sound_on,image):
        super().__init__(obj,image)
        self.collision = collision
        self.sound_on = sound_on
list_loaded_tiles = [Grass(None,None,None,"Grass.png")]


def chunk_loader(chunk):
    chunk_loaded = chunk
    for a in len(chunk[0]):
        for b in len(chunk[0]):
            pos = a,b
            inte = chunk[pos]
            chunk_loaded[pos] = list_loaded_tiles[inte]