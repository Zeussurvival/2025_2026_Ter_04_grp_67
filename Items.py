import time
class Item():
    def __init__(self,name,type,lore,damage):
        self.name = name
        self.type = type
        self.lore = lore
        if type == "weapon":
            self.damage = damage
    def print(self):
        print(self.name,self.type,self.lore)

class Weapon():
    def __init__(self,type,damage,chargeur,range):
        self.type = type
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
    def print(self):
        print(self.balle_actu)