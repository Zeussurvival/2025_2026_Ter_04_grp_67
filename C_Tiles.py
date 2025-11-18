import pygame
import os
main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Tiles") 
bg_image_dir = os.path.join(main_dir,"Tiles/Background_images") 
class TILE():
    def __init__(self,image,rotate,background_image):
        self.image = pygame.image.load(os.path.join(img_dir, image)).convert_alpha()
        self.image = pygame.transform.rotate(self.image,rotate)
        self.image = pygame.transform.scale(self.image,(16,16))
        if background_image != None:
            print(background_image)
            self.background_image = pygame.image.load(os.path.join(bg_image_dir, background_image)).convert_alpha()
            print(self.background_image)
        else:
            self.background_image = None
        print(self.image)
    def draw_self(self,screen,pos,global_sizes):
        if isinstance(self.background_image, pygame.Surface):
            screen.blit(pygame.transform.scale(self.background_image,(16*global_sizes[0],16*global_sizes[1])) ,(pos[0]*16*global_sizes[0],pos[1]*16*global_sizes[1]))
        screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0],16*global_sizes[1]))  ,(pos[0]*16*global_sizes[0],pos[1]*16*global_sizes[1]))

        # screen.blit(list_loaded_tiles[Chunk1[i,b]].image,(b*16*GLOBAL_ZOOM,i*16*GLOBAL_ZOOM))
class Tree(TILE):
    def __init__(self,sound_on,background_image,image,rotate):
        super().__init__(os.path.join(img_dir, f"Tree/{image}"),rotate,background_image)
        self.sound_on = sound_on
class Grass(TILE):
    def __init__(self,sound_on,image,rotate):
        super().__init__(os.path.join(img_dir, f"Grass/{image}"),rotate,None)
        self.sound_on = sound_on
class Road(TILE):
    def __init__(self,sound_on,image,rotate):
        super().__init__(os.path.join(img_dir, f"Road/{image}"),rotate,None)
        self.sound_on = sound_on



def chunk_loader(chunk):
    chunk_loaded = chunk
    for a in len(chunk[0]):
        for b in len(chunk[0]):
            pos = a,b
            inte = chunk[pos]
pygame.quit()