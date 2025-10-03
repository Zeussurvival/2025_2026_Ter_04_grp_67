class TILE():
    def __init__(self,pos,obj):
        self.pos = pos
        self.obj = obj
        pass
class Grass(TILE):
    def __init__(self, pos, obj,collision,sound_on,image):
        super().__init__(pos, obj)
        self.collision = collision
        self.sound_on = sound_on
        self.image = image
    def draw_self(self):
        pass

tiles_dico = {0:"",
              1:"",
              2:"",
              3:"",
              4:"",
              5:"",
              6:"",
              7:"",
              8:"",
              9:"",
              10:"",
              11:"",
              12:"",
              13:"",
              14:"",
              15:"",
              16:"",
              17:"",
              18:"",
              19:"",
              20:"",
              21:"",
              22:"",}


def chunk_loader(chunk):
    chunk_loaded = chunk
    for a in len(chunk[0]):
        for b in len(chunk[0]):
            pos = a,b
            inte = chunk[pos]
            chunk_loaded[pos] = tiles_dico[inte]