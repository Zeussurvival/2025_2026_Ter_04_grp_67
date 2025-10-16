import pygame
import os
main_dir = os.path.split(os.path.abspath(__file__))[0]
print(main_dir)
img_dir = os.path.join(main_dir,"Tiles") 

class TILE():
    def __init__(self,obj,image,rotate):
        self.obj_on = obj
        print(img_dir,image)
        self.image = pygame.image.load(os.path.join(img_dir, image)).convert_alpha()
        self.image = pygame.transform.rotate(self.image,rotate)
    def draw_self(self):
        pass
class Grass(TILE):
    def __init__(self, obj,collision,sound_on,image,rotate):
        super().__init__(obj,os.path.join(img_dir, f"Grass/{image}"),rotate)
        self.collision = collision
        self.sound_on = sound_on
class Road(TILE):
    def __init__(self, obj, collision,sound_on,image,rotate):
        super().__init__(obj,os.path.join(img_dir, f"Road/{image}"),rotate)
        self.collision = collision
        self.sound_on = sound_on



def chunk_loader(chunk):
    chunk_loaded = chunk
    for a in len(chunk[0]):
        for b in len(chunk[0]):
            pos = a,b
            inte = chunk[pos]
pygame.quit()