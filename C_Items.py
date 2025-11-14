import time
class Item():
    def __init__(self,name,type,lore,position):
        if position is tuple:
            self.state = "ground"
        else:
            self.state = "inventory"
            
        self.position = position
        self.name = name
        self.type = type
        self.lore = lore

    def print(self):
        print(self.name,self.type,self.lore,self.position)

class Weapon(Item):
    def __init__(self, damage, chargeur, range, position, name, type, lore):
        super().__init__(name,type,lore,position)
        self.damage = damage
        self.balle_actu = chargeur
        self.chargeur = chargeur
        self.reloading = False
        self.time_last_shoot = 0
        self.time_reload = 0
        self.range = range
    def shoot(self):
        if self.balle_actu > 0 and not self.reloading and time.time() - self.time_last_shoot > 0.1:
            self.balle_actu -= 1
            self.reloading = False
            self.time_last_shoot = time.time()
    def reload(self):
        self.reloading = True
        self.time_reload = time.time()
    def update(self):
        if time.time() - self.time_reload > 2 and self.reloading:
            self.reloading = False
            self.balle_actu = self.chargeur
    def print_balle(self):
        print(self.balle_actu)

class pistolet(Weapon):
    def __init__(self, damage, chargeur, range, position, name, type, lore):
        super().__init__(damage, chargeur, range, position ,name, type, lore)

pistolet1 = pistolet(10,6,50,(0,10),"Old Jhon's gun","gun","Jhon avait 10 de killstreak")
pistolet1.print()
pistolet1.print_balle()