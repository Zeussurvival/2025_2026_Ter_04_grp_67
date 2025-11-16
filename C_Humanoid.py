import pygame
class Humanoid():
    def __init__(self,x,y,speed,type,name,image):
        self.pos = pygame.math.Vector2(x,y)
        self.vect = pygame.math.Vector2(0,0)
        self.type = type
        self.name = name
        self.speed = speed
        self.image = image
    def moove(self,keys,dt,global_sizes):
        if keys[pygame.K_z]:
            self.vect[1] -= self.speed * dt
        if keys[pygame.K_s]:
            self.vect[1] += self.speed * dt
        if keys[pygame.K_q]:
            self.vect[0] -= self.speed * dt
        if keys[pygame.K_d]:
            self.vect[0] += self.speed * dt
        if self.vect.length() / (self.speed *dt + 10 **-10) > 1:
            self.vect = self.vect.normalize() * self.speed *dt
        self.pos += self.vect
        if self.pos[0] - 0.4 < 0:
            self.pos[0] = 0.4 
        if self.pos[1] -0.4 < 0:
            self.pos[1] = 0.4 
        self.vect = pygame.math.Vector2(0,0)
        print(self.pos)

    # def hitbox(self,)
    def draw_center(self,screen,screen_sizes,global_sizes):
        screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0]*0.8,16*global_sizes[1] *0.8)), (screen_sizes[0]/2 -8*0.8*global_sizes[0],screen_sizes[1]/2 -8*global_sizes[1]*0.8))



    def draw_self(self,screen,pos,global_sizes):
        screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0]*0.8,16*global_sizes[1] *0.8))  ,(pos[0]*16*global_sizes[0]- 8*global_sizes[0]*0.8,pos[1]*16*global_sizes[1]- 8*global_sizes[0]*0.8))


class Humain(Humanoid):
    def __init__(self, x, y, speed, type, name, image):
        super().__init__(x, y, speed, type, name, image)

class Zombie(Humanoid):
    def __init__(self, x, y, speed, type, name, image):
        super().__init__(x, y, speed, type, name, image)