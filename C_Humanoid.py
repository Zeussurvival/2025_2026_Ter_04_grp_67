import pygame
import time
import random
class Humanoid():
    def __init__(self, x, y, speed, typee, name, image, size, pv):
        self.pos = pygame.math.Vector2(x,y)
        self.vect = pygame.math.Vector2(0,0)
        self.type = typee
        self.name = name
        self.speed = speed
        self.image = image
        self.size = size
        self.pv = pv
        self.pv_max = pv


    # def hitbox(self,)
    def draw_center(self,screen,screen_sizes,global_sizes):
        screen.blit(pygame.transform.scale(self.image,(16*global_sizes[0]*0.8,16*global_sizes[1] *0.8)), (screen_sizes[0]/2 -8*0.8*global_sizes[0],screen_sizes[1]/2 -8*global_sizes[1]*0.8))

    def draw_self(self,screen,Human_pos,global_sizes):
        coeff = 16*global_sizes[0]
        size = coeff*self.size
        x_away_from_human = Human_pos[0] - self.pos[0]
        y_away_from_human = Human_pos[1] - self.pos[1]
        W,H = screen.get_size()
        screen.blit(pygame.transform.scale(self.image,(size,size))  ,(round(W/2 - x_away_from_human*coeff- size/2,2), round( H/2 - y_away_from_human*coeff- size/2,2)))




class Humain(Humanoid):
    def __init__(self, x, y, speed, typee, name, image, size, inventaire, inv_max, pv, endurance,font_death):
        super().__init__(x, y, speed, typee, name, image, size, pv)
        self.inventaire = inventaire
        self.inv_max = inv_max
        self.pv = 1
        self.endurance = 99
        self.endurance_max = endurance
        self.endurance_per_sec = 1.7
        self.endurance_last_used = time.time()
        self.is_sprinting = False
        self.sprint_boost = 1
        self.held_item_indice = 0
        self.held_item = self.inventaire[0]
        self.alive = True
        self.detectable = True
        self.font_death = font_death

    def moove(self,keys,dt,global_sizes):
        if self.can_moove():
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
            self.pos[0],self.pos[1] = round(self.pos[0],2),round(self.pos[1],2)
            self.vect = pygame.math.Vector2(0,0)

    def draw_himself_center(self,screen,screen_sizes,global_sizes):
        if self.detectable:
            self.draw_center(screen,screen_sizes,global_sizes)

    def can_moove(self):
        if self.detectable == False and self.alive == False:
            return False
        else:
            return True

    def print_inventaire(self):
        for item in self.inventaire:
            print(item.name)
        pass

    def revive(self):
        self.alive = True
        self.detectable = True
        self.pv = self.pv_max

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
            self.speed -= self.sprint_boost
            self.endurance_last_used = time.time()
        elif self.is_sprinting == False and self.endurance > 10:
            self.speed += self.sprint_boost
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
            if self.inventaire[i] != None:
                screen.blit(pygame.transform.scale(self.inventaire[i].image,(lenght_square,lenght_square)),(first_x+width+(lenght_square+width+offset)*i,y+width))
        
        pygame.draw.rect(screen,"white",(first_x+(lenght_square+width+offset)*self.held_item_indice  -2 ,y - 2,true_lenght + 4,true_lenght + 4 ),width+ 2)


    def do_everything(self,screen,FONT_None,dt):
        if self.detectable:
            self.endurance_regen(dt)
        self.draw_hp_endurance(screen,FONT_None)
        self.draw_hotbar(screen)
        if self.alive == False:
            self.death_mesage(screen)


    def use_hand(self,zombie_list,Human):
        if self.held_item != None:
            response,zombie_list = self.held_item.use_self(self.endurance,zombie_list,Human)
            if response:
                self.endurance_last_used = time.time()
                self.endurance -= 3 # self.held_item.endurance_used a mettre mais flm la il est 1h41

        else:
            print(None) 
        return zombie_list


    def attack(self):
        if self.inventaire[0].type == "gun" or "knife" and self.endurance>3:
            self.endurance_last_used = time.time()
            response = self.inventaire[0].attack()
            print(response)
            if response:
                self.endurance -= 3


    def change_held_item(self,keys):
        if keys[pygame.K_1]:
            self.held_item_indice = 0
            self.held_item = self.inventaire[0]
        if keys[pygame.K_2]:
            self.held_item_indice = 1
            self.held_item = self.inventaire[1]
        if keys[pygame.K_3]:
            self.held_item_indice = 2
            self.held_item = self.inventaire[2]
        if keys[pygame.K_4]:
            self.held_item_indice = 3
            self.held_item = self.inventaire[3]
        if keys[pygame.K_5]:
            self.held_item_indice = 4
            self.held_item = self.inventaire[4]
        pass

    def death_mesage(self,screen):
        texte = "VOUS ÊTES MORT"
        largeur, hauteur = screen.get_size()
        couleur_texte = (150, 0, 0)  # rouge sombre
        text_surface = self.font_death.render(texte, True, couleur_texte)
        text_rect = text_surface.get_rect(center=(largeur//2, hauteur//2))

        # --- Rectangle semi-transparent ---
        largeur_box = text_rect.width + 80
        hauteur_box = text_rect.height + 40
        box_surface = pygame.Surface((largeur_box, hauteur_box), pygame.SRCALPHA)

        # Couleur : gris foncé transparent
        box_surface.fill((30, 30, 30, 180))  # RGBA -> 180 = transparence

        # Position de la box (centrée)
        box_rect = box_surface.get_rect(center=(largeur//2, hauteur//2))
        screen.blit(box_surface, box_rect)
        screen.blit(text_surface, text_rect)

    def take_damage(self,damage,screen):
        self.pv -= damage
        if self.pv <= 0:
            self.pv = 0
            print("Vous êtes mort")
            self.alive = False
            self.detectable = False
            self.death_mesage(screen)


class Zombie(Humanoid):
    def __init__(self, x, y, speed, typee, name, image, size, pv, damage, range, detection_range, wander_cooldown):
        super().__init__(x, y, speed, typee, name, image, size, pv)
        self.state = "wander"
        self.damage = damage
        self.range = range
        self.detection_range = detection_range
        self.time_since_last_wander_search = time.time()
        self.wander_cd = wander_cooldown
        self.pos_to_go = pygame.math.Vector2(x+0.1,y+0.1)
        self.attack_cd = 1
        self.last_attack = time.time()
        # self.time_since_last_check_pos = time.time()
        # self.check_cd = 0.01
    def search_human(self,Human_pos,dt,Human,screen):
        if Human.detectable:
            vect = Human_pos - self.pos
            if vect.length() <= self.detection_range:
                self.state = "angry"
                self.angry(Human_pos,dt,Human,screen)
            else:
                self.state = "wander"
                self.pos_to_go = pygame.math.Vector2(self.pos[0]+(random.random()-0.5)*4+random.randint(1,10)*0.1, self.pos[1]+(random.random()-0.5)*4 + random.randint(1,10)*0.1)
        else:
            self.pos_to_go = pygame.math.Vector2(self.pos[0]+(random.random()-0.5)*4+random.randint(1,10)*0.1, self.pos[1]+(random.random()-0.5)*4 + random.randint(1,10)*0.1)
    
    def do_itself(self,Human_pos,dt,Human,screen):
        if Human.detectable:
            if self.state == "angry":
                self.angry(Human_pos,dt,Human,screen)
            if self.state == "wander":
                if time.time() - self.time_since_last_wander_search > self.wander_cd:
                    self.time_since_last_wander_search = time.time()
                    self.search_human(Human_pos,dt,Human,screen,)
                self.wandering(dt)
        else:
            self.state == "wander"
            if time.time() - self.time_since_last_wander_search > self.wander_cd:
                self.time_since_last_wander_search = time.time()
                self.search_human(Human_pos,dt,Human,screen)
            self.wandering(dt)

    def angry(self,Human_pos,dt,Human,screen,):
        vector = self.pos-Human_pos
        if time.time() - self.last_attack > self.attack_cd:
            if vector.length() < self.range + self.size/2:
                self.last_attack = time.time()
                self.attack(Human,screen,)
            elif vector.length() > self.detection_range:
                self.state = "wander"
            else:
                vector = vector.normalize() * self.speed *dt
                if vector.length() < 0.5:
                    self.pos -= vector # met += au lieu du -= c hillarant

    def attack(self,Human,screen):
        print(self.damage)
        Human.take_damage(self.damage,screen)

    def wandering(self,dt):
        vector = self.pos - self.pos_to_go
        vector1 = vector.normalize() * self.speed * dt
        if vector.length() > 0.5:
            self.pos -= vector1

    def take_damage(self,damage):
        self.pv -= damage
        if self.pv <= 0:
            self.pv = 0
            self.state = "dead"
            return self.state
        else:
            return "alive"