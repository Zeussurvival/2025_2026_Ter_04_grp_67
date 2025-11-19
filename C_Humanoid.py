import pygame
import time
class Humanoid():
    def __init__(self, x, y, speed, type, name, image, inventaire, inv_max, pv, endurance):
        self.pos = pygame.math.Vector2(x,y)
        self.vect = pygame.math.Vector2(0,0)
        self.type = type
        self.name = name
        self.speed = speed
        self.image = image
        self.inventaire = inventaire
        self.inv_max = inv_max
        self.pv = pv - 25
        self.pv_max = pv
        self.endurance = 50
        self.endurance_max = endurance
        self.endurance_per_sec = 1.7
        self.endurance_last_used = time.time()
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

    # def hitbox(self,)
    def draw_center(self,screen,screen_sizes,global_sizes):
        screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0]*0.8,16*global_sizes[1] *0.8)), (screen_sizes[0]/2 -8*0.8*global_sizes[0],screen_sizes[1]/2 -8*global_sizes[1]*0.8))

    # def draw_self(self,screen,pos,global_sizes):
    #     screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0]*0.8,16*global_sizes[1] *0.8))  ,(pos[0]*16*global_sizes[0]- 8*global_sizes[0]*0.8,pos[1]*16*global_sizes[1]- 8*global_sizes[0]*0.8))


    def print_inventaire(self):
        for item in self.inventaire:
            print(item.name)
        pass

    def draw_hp_endurance(self,screen,FONT_None):
        pv_color = (50,255,0)
        endurance_color = (25,10,255)
        pv_percent = self.pv / self.pv_max
        endurance_percent = self.endurance / self.endurance_max
        W,H = screen.get_size()
        AB = 200
        BC = 40
        pygame.draw.rect(screen, (255, 255, 255), (W-AB-20, H-BC-20, AB, BC), width=5)
        pygame.draw.rect(screen, (0, 0, 0), (W-AB-20 + 7, H-BC-20 + 7, AB - 14, BC - 14))
        pygame.draw.rect(screen, pv_color, (W-AB-13, H-BC-13, (AB - 14) * pv_percent, BC - 14))
        pv_text = FONT_None.render(f"{self.pv}/{self.pv_max}",True,(255,255,255))
        pv_text_rect = pv_text.get_rect(center=(W-AB/2 - 20,H-BC/2 - 20))
        screen.blit(pv_text,pv_text_rect)

        pygame.draw.rect(screen, (255, 255, 255), (W-AB-20, H-2*(BC+20), AB, BC), width=5)
        pygame.draw.rect(screen, (0, 0, 0), (W-AB-20 + 7, H-2*(BC+20) + 7, AB - 14, BC - 14))
        pygame.draw.rect(screen, endurance_color, (W-AB-13, H-2*(BC+20)+7, (AB - 14) * endurance_percent, BC - 14))
        endurance_text = FONT_None.render(f"{round(self.endurance)}/{self.endurance_max}",True,(255,255,255))
        endurance_text_rect = endurance_text.get_rect(center=(W- AB/2 - 20,H- 2* BC- 20))
        screen.blit(endurance_text,endurance_text_rect)
        pass

    def endurance_regen(self,dt):

        if self.endurance < self.endurance_max:
            diff = time.time() - self.endurance_last_used
            diff = abs(diff)
            if diff > 3:
                self.endurance += 5 * dt
            if 3>diff > 1:
                self.endurance += self.endurance_per_sec ** diff * dt
        else:
            self.endurance = self.endurance_max

        


    def do_everything(self,screen,FONT_None,dt):
        self.draw_hp_endurance(screen,FONT_None)
        self.endurance_regen(dt)
        pass


    def attack(self):
        if self.inventaire[0].type == "gun" or "knife":
            self.endurance_last_used = time.time()
            response = self.inventaire[0].attack()
            if response:
                self.endurance -= 5

class Humain(Humanoid):
    def __init__(self, x, y, speed, type, name, image, inventaire, inv_max, pv, endurance):
        super().__init__(x, y, speed, type, name, image, inventaire, inv_max, pv, endurance)

class Zombie(Humanoid):
    def __init__(self, x, y, speed, type, name, image, inventaire, inv_max, pv, endurance):
        super().__init__(x, y, speed, type, name, image, inventaire, inv_max, pv, endurance)