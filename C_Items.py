import time
class Item():
    def __init__(self,name,lore,position):
        if position is tuple:
            self.state = "ground"
        else:
            self.state = "inventory"
            
        self.position = position
        self.name = name
        self.lore = lore

    def print(self):
        print(self.name,self.type,self.lore,self.position)

class KNIFE(Item):
    def __init__(self, damage, range, position, name, lore, cooldown):
        super().__init__(name,lore,position)
        self.type = "knife"
        self.damage = damage
        self.range = range
        self.cooldown = cooldown
        self.time_last_throw = 0
        self.attacking = False
    def attack(self):
        if time.time() - self.time_last_throw > self.cooldown:
            self.attacking = True
            self.time_last_throw = time.time()
            print("Could hit")
        else:
            print("Ya un truc mais non")
    def update(self):
        if time.time() - self.time_reload > self.cooldown and self.reloading:
            self.attacking = False

class GUN(Item):
    def __init__(self, damage, chargeur, range, position, name, typee, lore, cooldown):
        super().__init__(name,lore,position)
        self.type = typee
        self.damage = damage
        self.balle_actu = chargeur
        self.chargeur = chargeur
        self.reloading = False
        self.time_last_shoot = 0
        self.time_reload = 0
        self.range = range
        self.cooldown = cooldown
    def attack(self):
        if self.balle_actu > 0 and not self.reloading and time.time() - self.time_last_shoot > self.cooldown:
            self.balle_actu -= 1
            self.reloading = False
            self.time_last_shoot = time.time()
            print("Shoot well")
        else:
            print("Ya un truc mais non")
    def reload(self):
        self.reloading = True
        self.time_reload = time.time()
    def update(self):
        if time.time() - self.time_reload > 2 and self.reloading:
            self.reloading = False
            self.balle_actu = self.chargeur
    def print_balle(self):
        print(self.balle_actu)

pistolet1 = GUN(10,6,50,(0,10),"Old Jhon's gun","gun","Jhon avait 10 de killstreak",2)
pistolet1.print()
pistolet1.print_balle()