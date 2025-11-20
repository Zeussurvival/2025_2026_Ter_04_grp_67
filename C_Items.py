import pygame
import time
import os
main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Image")
item_dir = os.path.join(img_dir,"Items") 
class Item():
    def __init__(self,name,lore,position,image):
        if position is tuple:
            self.state = "ground"
        else:
            self.state = "inventory"
            
        if image != None:
            self.image = pygame.image.load(os.path.join(item_dir,image)).convert_alpha()
        else:
            self.image = None
        self.position = position
        self.name = name
        self.lore = lore

    def print(self):
        print(self.name,self.type,self.lore,self.position)
    
    def draw_self(self,screen):
        if self.image:
            screen.blit(self.image,(500,600))
            pass

class KNIFE(Item):
    def __init__(self, damage, range, position, name, lore, cooldown,image):
        super().__init__(name,lore,position,image)
        self.type = "knife"
        self.damage = damage
        self.range = range
        self.cooldown = cooldown
        self.time_last_throw = 0
        self.attacking = False
    
    def use_self(self,endurance,zombie_list,Human):
        if endurance > 3:
            return self.attack(zombie_list,Human)

    def attack(self,zombie_list,Human):
        if time.time() - self.time_last_throw > self.cooldown:
            self.attacking = True
            self.time_last_throw = time.time()
            # print("Could hit")
            new_list = zombie_list
            print(zombie_list)
            for z in range(len(zombie_list)-1):
                vect = Human.pos - zombie_list[z].pos
                if vect.length() < self.range + Human.size/2:
                    print("2")
                    print(zombie_list[z].pv)
                    state = zombie_list[z].take_damage(self.damage)
                    if state == "dead":
                        print("es bien mort")
                        new_list.pop(z)
                    pass
                print(type(vect))
                print(vect.length())

            return self.attacking,zombie_list
        else:
            print("Ya un truc mais non")
            return False,zombie_list
    def update(self):
        if time.time() - self.time_reload > self.cooldown and self.reloading:
            self.attacking = False

class GUN(Item):
    def __init__(self, damage, chargeur, range, position, name, typee, lore, cooldown,image):
        super().__init__(name,lore,position,image)
        self.type = typee
        self.damage = damage
        self.balle_actu = chargeur
        self.chargeur = chargeur
        self.reloading = False
        self.time_last_shoot = 0
        self.time_reload = 0
        self.range = range
        self.cooldown = cooldown

    def use_self(self,endurance):
        if endurance > 0.2:
            return self.attack()

    def attack(self,zombie_list,Human):
        if self.balle_actu > 0 and not self.reloading and time.time() - self.time_last_shoot > self.cooldown:
            self.balle_actu -= 1
            self.reloading = False
            self.time_last_shoot = time.time()
            # print("Shoot well")
            return True,zombie_list
        else:
            # print("Ya un truc mais non")
            return False,zombie_list
    def reload(self):
        self.reloading = True
        self.time_reload = time.time()
    def update(self):
        if time.time() - self.time_reload > 2 and self.reloading:
            self.reloading = False
            self.balle_actu = self.chargeur
    def print_balle(self):
        print(self.balle_actu)

# pistolet1 = GUN(10,6,50,(0,10),"Old Jhon's gun","gun","Jhon avait 10 de killstreak",2)
# pistolet1.print()
# pistolet1.print_balle()




class Eatable(Item):
    def __init__(self, name, lore, position, image, hunger, endurance, heal):
        super().__init__(name,lore,position,image)
        self.hunger = hunger
        self.endurance = endurance
        self.heal = heal

    def use_self(self,endurance,zombie_list,Human):
        return self.eat(),zombie_list
    
    def eat(self):
        print("pas implemente")