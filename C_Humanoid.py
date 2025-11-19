import pygame
import time
class Humanoid():
    def __init__(self, x, y, speed, typee, name, image,pv):
        self.pos = pygame.math.Vector2(x,y)
        self.vect = pygame.math.Vector2(0,0)
        self.type = typee
        self.name = name
        self.speed = speed
        self.image = image
        self.pv = pv
        self.pv_max = pv


    # def hitbox(self,)
    def draw_center(self,screen,screen_sizes,global_sizes):
        screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0]*0.8,16*global_sizes[1] *0.8)), (screen_sizes[0]/2 -8*0.8*global_sizes[0],screen_sizes[1]/2 -8*global_sizes[1]*0.8))

    # def draw_self(self,screen,pos,global_sizes):
    #     screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0]*0.8,16*global_sizes[1] *0.8))  ,(pos[0]*16*global_sizes[0]- 8*global_sizes[0]*0.8,pos[1]*16*global_sizes[1]- 8*global_sizes[0]*0.8))




class Humain(Humanoid):
    def __init__(self, x, y, speed, typee, name, image, inventaire, inv_max, pv, endurance):
        super().__init__(x, y, speed, typee, name, image,pv)
        self.inventaire = inventaire
        self.inv_max = inv_max
        self.pv = pv - 25
        self.endurance = 99
        self.endurance_max = endurance
        self.endurance_per_sec = 1.7
        self.endurance_last_used = time.time()
        self.is_sprinting = False
        self.held_item_indice = 0
        self.held_item = self.inventaire[0]
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
        offset_x = 10
        offset_y = 10
        width = 6
        pygame.draw.rect(screen, (255, 255, 255), (W-AB-offset_x, H-BC-offset_y, AB, BC), width=width)
        pygame.draw.rect(screen, (0, 0, 0), (W-AB-offset_x + width, H-BC-offset_y + width, AB - 2*width, BC - 2*width))
        pygame.draw.rect(screen, pv_color, (W-AB-offset_x+width, H-BC-offset_y+width, (AB - 2*width) * pv_percent, BC - 2*width))
        pv_text = FONT_None.render(f"{self.pv}/{self.pv_max}",True,(255,255,255))
        pv_text_rect = pv_text.get_rect(center=(W-AB/2 - offset_x,H-BC/2 - offset_y))
        screen.blit(pv_text,pv_text_rect)

        pygame.draw.rect(screen, (255, 255, 255), (W-AB-offset_x, H-2*(BC+offset_y), AB, BC), width=width)
        pygame.draw.rect(screen, (0, 0, 0), (W-AB-offset_x + width, H-2*(BC+offset_y) + width, AB - 2*width, BC - 2*width))
        pygame.draw.rect(screen, endurance_color, (W-AB-offset_x + width, H-2*(BC+offset_y)+width, (AB - 2*width) * endurance_percent, BC - 2*width))
        endurance_text = FONT_None.render(f"{round(self.endurance)}/{self.endurance_max}",True,(255,255,255))
        endurance_text_rect = endurance_text.get_rect(center=(W- AB/2 - offset_x,H- BC*1.5- 2*offset_y))
        screen.blit(endurance_text,endurance_text_rect)
        pass

    def endurance_regen(self,dt):
        if self.endurance < self.endurance_max:
            if self.is_sprinting == False:
                diff = time.time() - self.endurance_last_used
                diff = abs(diff)
                if diff > 3:
                    self.endurance += 5 * dt
                if 3>diff > 1:
                    self.endurance += self.endurance_per_sec ** diff * dt * 1.1
            if self.is_sprinting:
                if self.endurance - 5*dt >0:
                    self.endurance -= 5*dt
                else:
                    self.endurance = 0
                    self.sprinting()
        elif self.endurance >= self.endurance_max:
            if self.is_sprinting:
                self.endurance = 99
            else:
                self.endurance = self.endurance_max

    def sprinting(self):
        if self.is_sprinting == True:
            self.is_sprinting = False
            self.speed -= 2
            self.endurance_last_used = time.time()
        elif self.is_sprinting == False and self.endurance > 10:
            self.speed += 2
            self.is_sprinting = True

    def draw_hotbar(self,screen):
        lenght_square = 64
        width = 6
        true_lenght = lenght_square + 2*width
        offset = 15 
        y_offset = offset + 10
        number_shown = 5
        first_x = screen.get_size()[0]/2 - 2*(offset+true_lenght) - lenght_square/2
        y = screen.get_size()[1] -lenght_square - y_offset
        for i in range(0,number_shown):
            pygame.draw.rect(screen,(200,200,200),(first_x+(lenght_square+width+offset)*i,y,true_lenght,true_lenght),width)
            if i < len(self.inventaire):
                screen.blit(pygame.transform.scale(self.inventaire[i].image,(lenght_square,lenght_square)),(first_x+width+(lenght_square+width+offset)*i,y+width))
        pass


    def do_everything(self,screen,FONT_None,dt):
        self.draw_hp_endurance(screen,FONT_None)
        self.endurance_regen(dt)
        self.draw_hotbar(screen)
        pass


    def use_hand(self):
        if self.held_item != None:
            response = self.held_item.use_self(self.endurance)
            if response:
                self.endurance_last_used = time.time()
                self.endurance -= 3
        else:
            print(None)
        pass

    def attack(self):
        if self.inventaire[0].type == "gun" or "knife" and self.endurance>3:
            self.endurance_last_used = time.time()
            response = self.inventaire[0].attack()
            print(response)
            if response:
                self.endurance -= 3
class Zombie(Humanoid):
    def __init__(self, x, y, speed, typee, name, image, pv):
        super().__init__(x, y, speed, typee, name, image, pv)