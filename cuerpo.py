import random
class Cuerpo():
    def __init__(self):
        self.cuerpo_s = []

    def iniciar_cuerpo(self):
        self.cuerpo_s = [[0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]]
    
    def recorrer_sudoku(self):
        for filas in self.cuerpo_s:
            print(filas)
    
    #def posiciones(self): 
        #self.posy = random.randrange(0,9,1)
        #self.posx = random.randrange(0,9,1)

    def colocandonumeros(self):
        for i in range(1,5):
            self.posy = random.randrange(0,9,1)
            self.posx = random.randrange(0,9,1)
            self.numerorandom = random.randrange(1,10,1)
            self.cuerpo_s[self.posy][self.posx] = self.numerorandom



